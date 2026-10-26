#!/usr/bin/env python3
"""The publish pipeline: a swarm job's answer becomes a page of the paper.

  python3 publish.py test <N> <jobId>      render tests/test-0N.html + fill
                                           the rehearsal slot (test week)
  python3 publish.py edition <N> <jobId>   render editions/NNN.html + print
                                           the content hash to anchor on-chain
  ... --dry                                parse and grade only; write nothing

It fetches the server-rendered explorer page, extracts the answer verbatim,
runs the mechanical style checks, and renders. It never edits the answer:
a failed check fails the grade, it does not fix the text. Commit and push
remain a separate, deliberate step. Pure stdlib."""
import hashlib, html as html_mod, json, re, sys, urllib.request

WALLET = "0xbe80e5979313cf8aff2b8e54e615fe3ecd8358f5"
BANNED = ["delve", "landscape", "game-changer", "seamless", "robust", "unlock",
          "tapestry", "paradigm", "it's a testament", "testament to", "buckle up",
          "it's worth noting", "ever-evolving", "only time will tell",
          "this week", "yesterday", "the weekend", "\U0001F680"]
CHROME = ["Sources offered", "— could not be read", "Onchain\n", "Read more\n",
          "receipt\nwork accepted", "scores\nsettled"]

def fetch_answer(job_id):
    url = f"https://explorer.imd.fun/jobs/{job_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "openinterest-publish/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read().decode()
    text = re.sub(r"<script.*?</script>", "", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", "", text, flags=re.S)
    text = re.sub(r"<[^>]+>", "\n", text)
    text = html_mod.unescape(text)
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    joined = "\n".join(lines)
    starts = [m.start() for m in re.finditer(r"LEAD:", joined)]
    if not starts:
        sys.exit("no LEAD: found on the explorer page; is the job answered?")
    start = starts[-1]
    seat, runtime = "?", "?"
    m = None
    for m in re.finditer(r"#\n(\d+)\n([\w.\- +]+)\n", joined[:start]):
        pass
    if m:
        seat, runtime = m.group(1), m.group(2)
    ans = joined[start:]
    for marker in CHROME:
        i = ans.find(marker)
        if i > 300:
            ans = ans[:i]
    ans = re.sub(r"\[\s*\n?(https?://[^\]\s]+)\s*\n?\]", r"[\1]", ans)
    return ans.strip(), seat, runtime

def grade(ans):
    checks, ok = [], True
    def c(name, passed, detail=""):
        nonlocal ok
        ok = ok and passed
        checks.append((name, passed, detail))
    words = len(re.sub(r"\[https?://[^\]]+\]", "", ans).split())
    c("under 900 words", words < 900, f"{words} words")
    urls = re.findall(r"https?://[^\]\s]+", ans)
    c("at least 8 source URLs", len(urls) >= 8, f"{len(urls)} URLs")
    em = ans.count("—")
    c("at most one em dash", em <= 1, f"{em} em dashes")
    low = ans.lower()
    hits = [b for b in BANNED if b in low]
    c("no banned words", not hits, ", ".join(hits) if hits else "clean")
    for s in ["LEAD", "ALSO TODAY", "READING LIST", "METHOD"]:
        c(f"{s} present", s in ans)
    first = ans.split("\n", 1)[0].replace("LEAD:", "").strip()
    headline = re.sub(r"\s*\[https?://[^\]]+\]\s*$", "", first).strip()
    c("headline ends with a full stop", headline.endswith("."), headline[:60])
    return ("PASS" if ok else "FAIL"), checks, {"words": words, "urls": len(urls), "headline": headline}

def linkify(escaped):
    return re.sub(r"\[(https?://[^\]]+)\]",
                  r'[<a href="\1" target="_blank" rel="noreferrer">\1</a>]', escaped)

def page_html(kind, n, date, seat, job_id, ans, verdict, checks, meta):
    is_test = kind == "test"
    title = f"test edition {n:02d}" if is_test else f"edition № {n:03d}"
    crumb = (f'<a href="../rehearsal.html" class="on">rehearsal</a>' if is_test
             else f'<a href="../editions/" class="on">editions</a>')
    note = ""
    if is_test:
        detail = " ".join(f"{name}: {d or ('ok' if p else 'FAIL')};" for name, p, d in checks)
        note = (f'<p style="margin-top:20px;font-size:13px;color:#4a4a52">Grader’s note '
                f'(mechanical, human-confirmed, allowed during tests only): grade {verdict}. '
                f'{detail} No edits were made.</p>')
    content_hash = hashlib.sha256(ans.encode()).hexdigest()
    body = linkify(html_mod.escape(ans))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Open Interest — {title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:ital,wght@0,400;0,500;0,600;1,400&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/oi.css">
</head>
<body>
<div class="wrap">
  <header class="mast"><h1>OPEN <span style="color:#6b1f2a">I</span>NTEREST</h1><div class="meta">{('the rehearsal &middot; ' if is_test else '')}{title}</div></header>
<div class="rule2"></div>
  <nav class="oi">
    <a href="../index.html">the company</a>
    {crumb}
    <a href="../style-guide.html">style guide</a>
    <a href="../engine/" class="er">engine room &#8599;</a>
  </nav>
  <div class="eyebrow">{title} &middot; {date} &middot; drafted by seat #{seat} &middot; no human edits</div>
  <h2 class="page">The machine&rsquo;s own words, verbatim.</h2>
  <p style="font-style:italic;color:#4a4a52;max-width:560px;margin:0 0 16px">{'A test, not an edition. Grade: ' + verdict + '. ' if is_test else ''}Provenance: <a href="https://explorer.imd.fun/jobs/{job_id}" target="_blank" rel="noreferrer">job {job_id[:8]} &#8599;</a> &middot; <span style="font-family:'Geist Mono',monospace;font-size:12px" title="sha256 of the text below">sha256 {content_hash[:16]}&hellip;</span></p>
  <div style="font-family:'Geist Mono',monospace;font-size:13px;line-height:1.7;white-space:pre-wrap;border:1px solid #0d0d0f;padding:24px;background:#faf8f3;overflow-wrap:anywhere">{body}</div>
  {note}
</div>
<footer class="foot"><div class="wrap">
  <span>human-constituted &middot; machine-operated &middot; fully transparent</span>
  <span><a href="https://explorer.imd.fun/wallet/{WALLET}" target="_blank" rel="noreferrer" style="color:inherit">newsroom wallet &#8599;</a></span>
</div></footer>
</body>
</html>
""", content_hash

def fill_slot(n, date, job_id, verdict, meta, seat):
    t = open("rehearsal.html").read()
    a, b = f"<!-- slot:{n:02d} -->", f"<!-- /slot:{n:02d} -->"
    ia, ib = t.find(a), t.find(b)
    if ia < 0 or ib < 0:
        print(f"warning: slot {n:02d} markers not found; rehearsal.html not updated")
        return
    head = html_mod.escape(meta["headline"])
    block = f"""{a}<article class="item">
          <div class="tag">/ test {n:02d} &middot; {date}</div>
          <h4>{head}</h4>
          <p>Drafted by seat #{seat}; {meta['words']} words of a 900 cap, {meta['urls']} source URLs. Graded mechanically against the style guide, then human-confirmed. No edits were made.</p>
          <div class="prov"><a href="https://explorer.imd.fun/jobs/{job_id}" target="_blank" rel="noreferrer">job record &#8599;</a> &nbsp;&middot;&nbsp; <a href="tests/test-{n:02d}.html">full text</a> &nbsp;&middot;&nbsp; grade &middot; {verdict}</div>
        </article>{b}"""
    open("rehearsal.html", "w").write(t[:ia] + block + t[ib + len(b):])

def main():
    args = [a for a in sys.argv[1:] if a != "--dry"]
    dry = "--dry" in sys.argv
    if len(args) != 3 or args[0] not in ("test", "edition"):
        sys.exit(__doc__)
    kind, n, job_id = args[0], int(args[1]), args[2]
    ans, seat, runtime = fetch_answer(job_id)
    verdict, checks, meta = grade(ans)
    date_m = re.search(r"\b(\d{1,2} )?(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}?,? \d{4}", ans)
    date = date_m.group(0) if date_m else "date unknown"
    print(f"seat #{seat} ({runtime}) | {meta['words']} words | {meta['urls']} URLs | grade {verdict}")
    for name, p, d in checks:
        print(f"  [{'ok' if p else 'XX'}] {name}" + (f" — {d}" if d else ""))
    if dry:
        print("(dry run: nothing written)")
        return
    page, content_hash = page_html(kind, n, date, seat, job_id, ans, verdict, checks, meta)
    if kind == "test":
        path = f"tests/test-{n:02d}.html"
        open(path, "w").write(page)
        fill_slot(n, date, job_id, verdict, meta, seat)
        print(f"wrote {path} and filled rehearsal slot {n:02d}")
    else:
        path = f"editions/{n:03d}.html"
        open(path, "w").write(page)
        print(f"wrote {path}")
        print(f"content hash to anchor on-chain: 0x{content_hash}")
        print("TODO when the x402 payer lands: anchor the hash, then re-host.")
    print("review the page, then commit and push yourself: publishing stays deliberate.")

if __name__ == "__main__":
    main()
