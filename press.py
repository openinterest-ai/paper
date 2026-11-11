#!/usr/bin/env python3
"""The press: a completed edition job becomes the day's paper, mechanically.

  python3 press.py              find today's completed, schedule-opened edition
                                job and publish it (no-op if none, or already in)
  python3 press.py --job ID     publish that job (testing; schedule not required)
  python3 press.py --job ID --dry   fetch and grade only; write nothing

It fetches the job's answer verbatim (publish.py does the fetching and the
mechanical grading), refuses on a failed grade, writes the raw record, adds
one manifest entry and reruns build_pages.py. It never edits the answer: the
press can refuse, it cannot write. Commit and push belong to the workflow
that calls it (.github/workflows/press.yml). Pure stdlib."""
import datetime, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
import build_pages
import publish

API = "https://api.imd.fun"
WALLET = "0xbe80e5979313cf8aff2b8e54e615fe3ecd8358f5"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "openinterest-press/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def manifest():
    return json.load(open("editions.json"))


def published_job_ids(man):
    return {jid for e in man["entries"] for _, jid in e["jobs"]}


def discover(man):
    """Today's publishable job: completed, schedule-opened, paid by the
    newsroom wallet, not yet in the manifest. The public list carries no
    payer, so candidates are narrowed by state, freshness and the paper's
    name in the objective before any detail is fetched (the API rate-limits
    a greedy crawl), and the detail check remains authoritative."""
    import time
    done = published_job_ids(man)
    fresh = (datetime.datetime.now(datetime.timezone.utc)
             - datetime.timedelta(hours=36)).isoformat()
    recent = get(f"{API}/jobs").get("jobs", [])
    for j in recent:
        if (j["id"] in done or j.get("state") != "completed"
                or (j.get("createdAt") or "") < fresh
                or "open interest" not in (j.get("objective") or "").lower()):
            continue
        time.sleep(1)
        try:
            full = get(f"{API}/jobs/{j['id']}")
        except Exception as e:
            print(f"  ({j['id'][:8]}: {e}; skipping)")
            continue
        if ((full.get("paidBy") or "").lower() == WALLET
                and full.get("createdBy") == "schedule"):
            return full
    return None


def fetch_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "openinterest-press/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode()


def fetch_answer_from_delivery(job_id):
    """The edition's verbatim text, from the job's delivery repository at its
    pinned commit (the API result names both). Preference order: the canonical
    output path the schedule's brief demands (artifacts/edition.txt), else the
    winner that selection.txt names. Returns (answer, winner_node or None)."""
    res = get(f"{API}/jobs/{job_id}/result")
    d = res.get("delivery") or {}
    if d.get("mode") != "repository" or not d.get("repoUrl") or not d.get("commit"):
        sys.exit("no repository delivery on the result; the press cannot fetch the answer")
    base = (d["repoUrl"].replace("https://github.com/", "https://raw.githubusercontent.com/")
            .removesuffix(".git") + "/" + d["commit"])
    try:
        return fetch_text(f"{base}/artifacts/edition.txt").strip(), None
    except Exception:
        pass
    sel = fetch_text(f"{base}/selection.txt")
    m = re.search(r"WINNER:\s*(\S+)", sel)
    if not m:
        sys.exit("selection.txt names no WINNER; the press refuses to guess")
    path = m.group(1).strip()
    letter_m = re.search(r"draft[s]?/([a-z])\.md|draft[_-]([a-z])", path)
    winner = None
    if letter_m:
        winner = "draft_" + (letter_m.group(1) or letter_m.group(2))
    return fetch_text(f"{base}/{path}").strip(), winner


def credits(job, winner_node):
    """Mechanical credit line from the job's nodes. The numbers are seat
    tokenIds, as on every rehearsal. The winning draft comes from the
    selection's own record; if it cannot be read, all drafts are credited
    (honest degradation, never a guess)."""
    token = {n["key"]: str((n.get("seat") or {}).get("tokenId") or "?")
             for n in job.get("nodes", [])}
    drafts = sorted(k for k in token if k.startswith("draft"))
    select = next((k for k in token if "select" in k), None)
    attack = next((k for k in token if "attack" in k or "verif" in k), None)
    if winner_node and winner_node in token:
        drafted = "drafted #" + token[winner_node]
    elif drafts:
        drafted = "drafted in competition " + " ".join("#" + token[d] for d in drafts)
    else:
        drafted = "drafted #?"
    parts = [drafted]
    if select:
        parts.append("selected #" + token[select])
    if attack:
        parts.append("verified #" + token[attack])
    return " · ".join(parts), len(job.get("nodes", []))


def date_fields(ans, fallback):
    m = re.search(r"\b(\d{1,2}) (January|February|March|April|May|June|July|August"
                  r"|September|October|November|December),? (\d{4})", ans)
    if m:
        d = datetime.date(int(m.group(3)),
                          ["January", "February", "March", "April", "May", "June", "July",
                           "August", "September", "October", "November", "December"
                           ].index(m.group(2)) + 1, int(m.group(1)))
    else:
        d = fallback
    monday = d - datetime.timedelta(days=d.weekday())
    fmt = lambda x: f"{x.strftime('%A').lower()} {x.day} {x.strftime('%B %Y').lower()}"
    return fmt(d), d.strftime("%b").lower(), f"week of {monday.day} {monday.strftime('%B %Y').lower()}"


def main():
    args = sys.argv[1:]
    dry = "--dry" in args
    job_id = args[args.index("--job") + 1] if "--job" in args else None

    man = manifest()
    if job_id:
        if job_id in published_job_ids(man):
            sys.exit(f"job {job_id[:8]} is already in the manifest")
        job = get(f"{API}/jobs/{job_id}")
        if job.get("state") != "completed":
            sys.exit(f"job {job_id[:8]} is {job.get('state')}, not completed")
    else:
        job = discover(man)
        if not job:
            print("nothing to publish: no new completed schedule-opened job")
            return
    job_id = job["id"]

    ans, winner_node = fetch_answer_from_delivery(job_id)
    verdict, checks, meta = publish.grade(ans)
    print(f"job {job_id[:8]} | {meta['words']} words | {meta['urls']} URLs | grade {verdict}")
    for name, p, d in checks:
        print(f"  [{'ok' if p else 'XX'}] {name}" + (f" — {d}" if d else ""))
    if verdict != "PASS":
        sys.exit("grade FAIL: the press refuses; nothing written, the site keeps "
                 "the previous edition. The answer was not edited.")

    agents, n_agents = credits(job, winner_node)

    nums = [int(m.group(1)) for e in man["entries"]
            if (m := re.search(r"edition № (\d+)", e["label"]))]
    n = (max(nums) + 1) if nums else 1
    created = (job.get("createdAt") or "")[:10]
    fallback = (datetime.date.fromisoformat(created) if created
                else datetime.date.today())
    date, month, week = date_fields(ans, fallback)

    raw_path = f"editions/raw/{n:03d}/edition.txt"
    page_path = f"editions/{n:03d}.html"
    import hashlib
    sha = hashlib.sha256(ans.encode()).hexdigest()
    from_schedule = job.get("createdBy") == "schedule"
    entry = {
        "label": f"edition № {n:03d}",
        "kind": "edition",
        "date": date, "month": month, "week": week,
        "lead_tag": f"the lead · {agents}",
        "agents": agents + (" · opened by the schedule" if from_schedule else ""),
        "agents_count": n_agents,
        "newsroom": agents,
        "jobs": [[f"job {job_id[:8]}", job_id]],
        "job_page": f"engine/job-{job_id[:8]}.html",
        "raw": raw_path,
        "raw_sha16": sha[:16],
        "page": page_path,
    }
    if from_schedule:
        entry["provenance_note"] = "opened by the schedule, not by hands"

    if dry:
        print("(dry run) entry would be:")
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        return

    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    open(raw_path, "w").write(ans + "\n")
    man["entries"].insert(0, entry)
    json.dump(man, open("editions.json", "w"), indent=2, ensure_ascii=False)
    open("editions.json", "a").write("\n")
    build_pages.main()
    print(f"published {entry['label']}: raw {raw_path} (sha256 {sha[:16]}…), "
          f"page {page_path}, front page rebuilt")


if __name__ == "__main__":
    main()
