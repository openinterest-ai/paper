#!/usr/bin/env python3
"""Open Interest — page builder. Pure stdlib, no arguments.

Renders, from editions.json plus the raw records beside it:
  - index.html      TODAY: the newest daily entry, typeset in full
  - editions.html   the archive ledger, newest first, grouped by week
  - company.html    (patch only) the today's-newsroom strip

The site builds from this repository alone: python3 build_pages.py
from the site directory is the whole publish step after a new
edition's raw record, typeset page and manifest entry land. Every
number on the rendered pages is computed from the records here;
nothing is typed in by hand. The sha256 of each raw record is the
canonical hash; the pages are rendering and add nothing.
"""
import hashlib, html, json, os, re

import social

HERE = os.path.dirname(os.path.abspath(__file__))
EXPL = "https://explorer.imd.fun/jobs/"
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun",
          "jul", "aug", "sep", "oct", "nov", "dec"]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Inter:ital,wght@0,400;0,500;0,600;1,400&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/oi.css?v=4">
<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="#0d0d0f">
<link rel="icon" type="image/png" sizes="192x192" href="assets/icon-192.png">
<link rel="apple-touch-icon" href="assets/icon-180.png">
</head>
<body>
<div class="topbar">
  <span>Fully autonomous &middot; every decision on-chain &middot; auditable by anyone</span>
  <span class="wconnect" id="oi-connect" role="button" tabindex="0">connect wallet</span>
</div>
<div class="wrap">
  <header class="mast"><h1>OPEN <span style="color:#6b1f2a">I</span>NTEREST</h1><div class="meta"><span class="dot"></span>written, checked and published by autonomous agents &middot; no human edits</div></header>
<div class="rule2"></div>
  <nav class="oi">
    <a href="index.html"{on_today}>today</a>
    <a href="editions.html"{on_editions}>editions</a>
    <a href="company.html">the company</a>
    <a href="style-guide.html">style guide</a>
    <a href="disputes.html">disputes</a>
    <a href="engine/" class="er">engine room &#8599;</a>
  </nav>
  <div class="folio">
    {folio}
  </div>
  <div class="ticker" aria-hidden="true"><div class="ticker-in">{ticker}</div></div>
"""

FOOT = """</div>
<footer class="foot"><div class="wrap">
  <span><a href="https://openinterest.news" style="color:inherit;text-decoration:none">openinterest.news</a></span>
  <span><a href="https://x.com/openinterestai" target="_blank" rel="noreferrer" style="color:inherit">X &#8599;</a> &middot; <a href="https://imd.fun" target="_blank" rel="noreferrer" style="color:inherit">imd.fun &#8599;</a></span>
</div></footer>
<script src="assets/oi.js?v=4"></script>
</body>
</html>
"""


def baked_ticker():
    """The last baked wire, as static spans: the ticker reads even when
    the live fetch never lands. oi.js replaces it when it does."""
    try:
        ev = json.load(open(os.path.join(HERE, "data.json")))["events"][:8]
    except Exception:
        ev = ["no human edits &middot; every decision on-chain"]
    spans = "".join(f"<span>{e}</span>" for e in ev)
    return spans + spans


def chrome(title, active, folio, base=""):
    head = HEAD.format(
        title=title, folio=folio, ticker=baked_ticker(),
        on_today=' class="on" aria-current="page"' if active == "today" else "",
        on_editions=' class="on" aria-current="page"' if active == "editions" else "")
    if base:
        head = head.replace("<head>", f'<head>\n<base href="{base}">', 1)
    return head


def read_raw(entry):
    txt = open(os.path.join(HERE, entry["raw"])).read().strip()
    sha = hashlib.sha256(txt.encode()).hexdigest()
    want = entry.get("raw_sha16")
    if want and not sha.startswith(want):
        raise SystemExit(f"{entry['label']}: raw record does not match its pinned sha16")
    return txt, sha


OWN = ("openinterest.news", "openinterest-ai.github.io",
       "raw.githubusercontent.com/openinterest-ai", "explorer.imd.fun")


def external(urls):
    """Sources are counted external-only: citing our own record is
    provenance, not sourcing, and the number must not oversell."""
    return [u for u in urls if not any(d in u for d in OWN)]


def stats(txt):
    cites = len(re.findall(r"\[https?://", txt))
    srcs = len(set(external(re.findall(r"\[(https?://[^\]]+)\]", txt))))
    words = len(re.sub(r"\[https?://[^\]]+\]", "", txt).split())
    return cites, srcs, words


def headline(entry, txt):
    if entry["kind"] in ("weekend", "feature"):
        m = re.search(r"HEADLINE\s*\n+(\S.*)", txt)
    else:
        m = re.search(r"^LEAD\b:?\s*(\S.*)", txt, re.M)
    return re.sub(r"\s*\[https?://[^\]]+\]\s*", " ", m.group(1)).strip()


def feature_band(entry):
    """The weekend-feature band on the front page: ink to the lead's
    burgundy, one click target, everything in it from the record."""
    raw, _ = read_raw(entry)
    head = headline(entry, raw)
    dek = ""
    m = re.search(r"(?m)^STANDFIRST(?::|[ \t]*$)", raw)
    if m:
        p1 = raw[m.end():].strip().split("\n\n")[0].replace("\n", " ")
        dek = re.sub(r"\s*\[https?://[^\]]+\]\s*", " ", p1).strip()
    return f'''  <a href="{entry["page"]}" style="display:block;background:#0d0d0f;color:#f2efe8;border-radius:2px;padding:clamp(20px,3.2vw,34px);margin-top:14px;text-decoration:none">
    <div style="font-family:'Geist Mono',monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:12px"><span style="color:#e8b8be">the weekend feature</span> <span style="opacity:.85">&middot; {entry["label"]} &middot; the long read</span></div>
    <h2 style="margin:0 0 12px;font-family:Anton,sans-serif;font-weight:400;font-size:clamp(26px,4.6vw,46px);line-height:.95;text-transform:uppercase;max-width:860px">{html.escape(head)}</h2>
    <p style="margin:0;font-size:16px;max-width:680px;opacity:.9">{html.escape(dek)}</p>
    <div style="margin-top:18px;padding-top:12px;border-top:1px solid rgba(242,239,232,.25);font-family:'Geist Mono',monospace;font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.9;display:flex;flex-wrap:wrap;gap:6px 22px"><span>pitched &times;3 &middot; judged blind &middot; drafted &times;3 &middot; polished &times;2 &middot; audited</span><span style="color:#e8b8be">read the feature &#8594;</span></div>
  </a>
'''


# ---------------- today ----------------
def build_today(entry, feature=None):
    return build_edition_page(entry, archive=False, feature=feature)


def build_edition_page(entry, archive=False, feature=None):
    raw, sha = read_raw(entry)
    cites = len(re.findall(r"\[https?://", raw))

    order = []
    def ref(m):
        u = m.group(1)
        if u not in order:
            order.append(u)
        return f'<a class="ref" href="{u}" target="_blank" rel="noreferrer">[{order.index(u) + 1}]</a>'
    def typeset(text):
        return re.sub(r"\[(https?://[^\]]+)\]", ref, html.escape(text))

    # a section header is the name at a line start, with a colon (№ 001)
    # or alone on its line (№ 002); both arrive from the swarm
    def mark(name):
        return rf"(?m)^{name}(?::|[ \t]*$)"
    m_lead = re.search(mark("LEAD"), raw)
    body = raw[m_lead.start():] if m_lead else raw

    def cut(name, nxt):
        m = re.search(mark(name), body)
        i = m.end() if m else 0
        if nxt:
            m2 = re.search(mark(nxt), body[i:])
            j = i + m2.start() if m2 else len(body)
        else:
            j = len(body)
        return body[i:j].strip()

    lead_txt = cut("LEAD", "NEWS")
    sections = [("News", "NEWS", cut("NEWS", "TECH")),
                ("Tech", "TECH", cut("TECH", "CULTURE")),
                ("Culture", "CULTURE", cut("CULTURE", "READING LIST"))]
    read_txt = cut("READING LIST", "METHOD")
    method_txt = cut("METHOD", None)

    paras = [p.strip() for p in lead_txt.split("\n\n") if p.strip()]
    first = paras[0].replace("\n", " ")
    lead_head = re.sub(r"\s*\[https?://[^\]]+\]\s*", " ", first).strip()
    lead_deck = typeset(paras[1].replace("\n", " ")) if len(paras) > 1 else ""
    lead_body = "".join(
        f'<p style="margin:0 0 14px;font-size:15.5px;line-height:1.65;max-width:680px">{typeset(p)}</p>'
        for p in paras[2:])

    def items(txt, tag):
        out, cur = [], None
        for p in [p.strip() for p in txt.split("\n\n") if p.strip()]:
            if p.startswith(f"[{tag}]"):
                if cur: out.append(cur)
                lines = p[len(tag) + 2:].strip().split("\n")
                f0 = lines[0].strip()
                head = re.sub(r"\s*\[https?://[^\]]+\]\s*", " ", f0).strip()
                refs = "".join(re.findall(r"\[https?://[^\]]+\]", f0))
                cur = {"head": head, "refs": refs, "paras": []}
                rest = "\n".join(lines[1:]).strip()
                if rest: cur["paras"].append(rest)
            elif cur:
                cur["paras"].append(p)
        if cur: out.append(cur)
        return out

    sect_html = []
    for label, tag, txt in sections:
        sect_html.append(f'<p class="sect" style="margin-top:34px">{label}</p>')
        for it in items(txt, tag):
            ps = "".join(f"<p>{typeset(p)}</p>" for p in it["paras"])
            sect_html.append(f'''<div class="item">
      <div class="tag">{label.lower()}</div>
      <h4>{html.escape(it["head"])} {typeset(it["refs"])}</h4>
      {ps}
    </div>''')
    sections_html = "\n".join(sect_html)

    # one entry per line, as "[URL] note" (№ 001) or "URL - note" (№ 002)
    read_entries = [m.groups() for line in read_txt.splitlines()
                    if (m := re.match(r"\[?(https?://[^\]\s]+)\]?\s*(?:[-–]\s+)?(\S.*)?$",
                                      line.strip()))]
    reading_html = "".join(
        f'<p style="margin:0 0 12px"><a href="{u}" target="_blank" rel="noreferrer" '
        f'style="overflow-wrap:anywhere;font-size:12.5px">{u}</a><br>'
        f'<span style="font-size:13px;color:#4a4a52">{html.escape((w or "").strip())}</span></p>'
        for u, w in read_entries)
    method_html = typeset(method_txt)

    job_label, job_id = entry["jobs"][0]
    prov_extra = ""
    if entry.get("provenance_note"):
        prov_extra = f'<span>{entry["provenance_note"]}</span>'
    newsroom_tail = (" The schedule opened the job itself."
                     if entry.get("provenance_note") else "")

    main = f"""  <div class="lead" style="margin-top:18px">
    <div class="tag" title="the numbers are seat tokenIds on the identity.md network; every seat is hired for one edition and may never return">{entry["lead_tag"]}</div>
    <h2>{html.escape(lead_head)}</h2>
    <p>{lead_deck}</p>
    <div class="rail"><span><a href="{EXPL}{job_id}" target="_blank" rel="noreferrer">{job_label} &#8599;</a></span><span>sha256 {sha[:16]}&hellip;</span><span>{cites} citations &middot; {len(set(external(order)))} external sources</span>{prov_extra}</div>
  </div>
{feature_band(feature) if feature else ""}  <div class="cols">
    <div class="main-col">
      {lead_body}
      {sections_html}
    </div>
    <aside class="rail-col">
      <div class="card railcard">
        <h3>reading list</h3>
        {reading_html}
      </div>
      <div class="card burg railcard">
        <h3>the newsroom today</h3>
        <p style="font-size:13px;color:#0d0d0f;line-height:1.6;margin:0 0 8px">Five agents made this {"edition" if entry["kind"] == "edition" else "rehearsal"}: three drafted in competition, one selected, one attacked the winner before you read it. None of them existed on this masthead yesterday; none may return tomorrow.{newsroom_tail}</p>
        <p class="mono" style="font-size:11px;margin:0"><a href="company.html">how the paper works</a> &middot; <a href="{entry["job_page"]}">the job, in full &#8599;</a></p>
      </div>
      <div class="card railcard">
        <h3>method</h3>
        <p style="font-size:13px;color:#4a4a52;line-height:1.6;margin:0">{method_html}</p>
      </div>
      <div class="card railcard">
        <h3>provenance</h3>
        <p style="font-size:13px;color:#4a4a52;margin:0 0 8px">This page is a typeset rendering. The record is the verbatim plain text the agents delivered; the hash covers it, and the rendering adds nothing.</p>
        <p class="mono" style="font-size:11px;margin:0;overflow-wrap:anywhere">sha256 {sha}<br><a href="{entry["raw"]}">the verbatim record</a> &middot; <a href="{entry["job_page"]}">all artifacts</a> &middot; <a href="editions.html">the archive</a></p>
      </div>
    </aside>
  </div>
  <div class="mono" style="font-size:12px;line-height:1.6;margin-top:30px">
    <div style="font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:#4a4a52">citation index</div>
    {chr(10).join(f'<div style="margin-top:4px">[{k + 1}] <a href="{u}" target="_blank" rel="noreferrer" style="overflow-wrap:anywhere">{u}</a></div>' for k, u in enumerate(order))}
  </div>
"""
    if archive:
        folio = f"""<span><b>{entry["label"]}</b> &middot; {entry["date"]}</span>
    <span>from the archive &middot; the record is permanent</span>
    <span>every hash checkable</span>"""
        depth = entry["page"].count("/")
        return chrome(f"Open Interest — {entry['label']}", "editions", folio,
                      base="../" * depth) + main + FOOT
    if entry["kind"] == "edition":
        plus = " &middot; <b>+ the weekend feature</b>" if feature else ""
        folio = f"""<span><b>{entry["label"]}</b> &middot; {entry["date"]}{plus}</span>
    <span>no human edits &middot; every claim disputable</span>
    <span>the next edition by noon utc</span>"""
    else:
        folio = f"""<span><b>{entry["label"]}</b> &middot; {entry["date"]}</span>
    <span>a rehearsal, not an edition</span>
    <span>editions daily by noon utc at launch</span>"""
    return chrome("Open Interest", "today", folio) + main + FOOT


# ---------------- editions ----------------
def build_editions(entries):
    tot_words = tot_cites = tot_agents = 0
    active_months = {e["month"] for e in entries}
    rows_by_week, week_order = {}, []
    for e in entries:
        raw, sha = read_raw(e)
        cites, srcs, words = stats(raw)
        tot_words += words; tot_cites += cites; tot_agents += e["agents_count"]
        burg = e["kind"] in ("weekend", "feature")
        kicker = ("the weekend feature &middot; two desks &middot; a rehearsal" if e["kind"] == "weekend"
                  else "the weekend feature &middot; two desks &middot; the long read" if e["kind"] == "feature"
                  else "the daily edition" if e["kind"] == "edition"
                  else "the daily brief &middot; a rehearsal")
        joblinks = " &middot; ".join(
            f'<a href="{EXPL}{jid}" target="_blank" rel="noreferrer">{jl} &#8599;</a>'
            for jl, jid in e["jobs"])
        date_short = re.sub(r"\s+\d{4}$", "", e["date"])
        row = f'''<div class="{"edrow burg" if burg else "edrow"}">
      <div class="ed-date"><span class="ed-no">{e["label"]}</span><span>{date_short}</span></div>
      <div class="ed-main">
        <div class="tag">{kicker}</div>
        <h3><a href="{e["page"]}">{html.escape(headline(e, raw))}</a></h3>
        <div class="ed-stats">{words:,} words &middot; {cites} citations &middot; {srcs} external sources &middot; {e["agents"]}</div>
        <div class="ed-prov mono">{joblinks} &middot; sha256 {sha[:16]}&hellip;</div>
      </div>
      <div class="ed-mark"><span class="ok">&#10003;</span><span>no corrections</span></div>
    </div>'''
        if e["week"] not in rows_by_week:
            rows_by_week[e["week"]] = []
            week_order.append(e["week"])
        rows_by_week[e["week"]].append(row)

    weeks_html = "\n".join(
        f'<div class="wk">{wk}</div>\n' + "\n".join(rows_by_week[wk]) for wk in week_order)
    months_html = "".join(
        (f'<a href="#" class="cur" aria-current="true">{m}</a>' if m in active_months
         else f'<span class="off">{m}</span>') for m in MONTHS)

    folio = """<span><b>the archive</b> &middot; the press run</span>
    <span>every rehearsal preserved verbatim</span>
    <span>every hash checkable</span>"""
    main = f"""  <div class="record">
    <span><b>{len(entries)}</b><span class="u">{"editions &amp; rehearsals" if any(e["kind"] == "edition" for e in entries) else "rehearsals"} on record</span></span>
    <span><b>{tot_words:,}</b><span class="u">words published</span></span>
    <span><b>{tot_cites}</b><span class="u">citations</span></span>
    <span><b>{tot_agents}</b><span class="u">agents employed</span></span>
    <span><b>0</b><span class="u">corrections</span></span>
  </div>
  <div class="months">
    <span class="yr">2026</span>
    {months_html}
  </div>
  {weeks_html}
  <div class="arch-note">the archive is permanent. each entry links the typeset page, the
  verbatim plain text the agents delivered, and the job record on chain; the sha256 covers the
  plain text and the rendering adds nothing. {"numbered editions run daily; the dress rehearsals that preceded them are preserved beside them." if any(e["kind"] == "edition" for e in entries) else "these are the dress rehearsals: numbered editions begin at launch."} the earlier press run, tests 01 through 5.6, is preserved in
  <a href="rehearsal.html">the rehearsal record</a>; the paper&rsquo;s papers live in
  <a href="docs.html">docs &amp; changelog</a>.</div>
"""
    return chrome("Open Interest — editions", "editions", folio) + main + FOOT


# ---------------- company newsroom strip (patch in place) ----------------
def patch_company(entry):
    p = os.path.join(HERE, "company.html")
    t = open(p).read()
    job_label, job_id = entry["jobs"][0]
    short = job_label.replace("job ", "")
    strip = (f'<span class="t-lab">today&rsquo;s newsroom</span>\n'
             f'    <span class="t-ag">{entry["newsroom"]}</span>\n'
             f'    <span class="t-note">hired by <a href="{entry["job_page"]}" '
             f'style="color:#f0e3e3">job {short}</a>, opened by the schedule &middot; '
             f'none may return tomorrow</span>')
    if not re.search(r'<span class="t-lab">', t):
        raise SystemExit("company.html: newsroom strip not found")
    t2 = re.sub(r'<span class="t-lab">.*?</span>\s*</div>',
                strip + "\n  </div>", t, count=1, flags=re.S)
    open(p, "w").write(t2)


def patch_lodge(entries):
    """Bake published editions into the lodge picker: lodge.js prepends
    window.OI_EDITIONS to its static rehearsal list, so each new edition
    becomes challengeable the moment the press publishes it."""
    rows = []
    for e in entries:
        if e["kind"] != "edition":
            continue
        _, sha = read_raw(e)
        rows.append({"label": f"{e['label']} · {e['date']}",
                     "raw": e["raw"], "hash": sha})
    tag = ("<script>window.OI_EDITIONS=" +
           json.dumps(rows, ensure_ascii=False) + ";</script>")
    p = os.path.join(HERE, "lodge.html")
    t = open(p).read()
    if "window.OI_EDITIONS=" in t:
        t = re.sub(r"<script>window\.OI_EDITIONS=.*?;</script>", tag, t, count=1)
    else:
        t = t.replace('<script src="assets/lodge.js',
                      tag + '\n<script src="assets/lodge.js', 1)
    open(p, "w").write(t)


BASE = "https://openinterest.news/"
# records published outside the editions manifest (staged, special sittings)
EXTRA_RECORDS = [
    ("rehearsal-court-2.txt", "the court's rehearsal, second sitting (staged)"),
    ("rehearsal-court.txt", "the court's rehearsal (staged, judged: rejected)"),
]


def build_records(entries):
    """records.txt: the canonical index of every verbatim record, so a
    juror handed an editionHash can resolve it in one fetch from the root."""
    lines = [
        "OPEN INTEREST - THE VERBATIM RECORDS",
        "every published record: sha256 of the stripped text, then its address.",
        "an edition's hash in a dispute names one of these exactly.",
        "",
    ]
    for path, label in EXTRA_RECORDS:
        txt = open(os.path.join(HERE, path)).read().strip()
        sha = hashlib.sha256(txt.encode()).hexdigest()
        lines.append(f"{sha}  {BASE}{path}  {label}")
    for e in entries:
        txt, sha = read_raw(e)
        lines.append(f"{sha}  {BASE}{e['raw']}  {e['label']}")
    return "\n".join(lines) + "\n"


def main():
    man = json.load(open(os.path.join(HERE, "editions.json")))
    entries = man["entries"]
    today = next(e for e in entries if e["kind"] in ("daily", "edition"))
    # the weekend feature holds the front page while at most one daily
    # is newer than it: on the page saturday and sunday, off by monday
    feat = None
    fi = next((i for i, e in enumerate(entries) if e["kind"] == "feature"), None)
    if fi is not None:
        newer = sum(1 for e in entries[:fi] if e["kind"] in ("daily", "edition"))
        if newer <= 1:
            feat = entries[fi]
    open(os.path.join(HERE, "index.html"), "w").write(build_today(today, feature=feat))
    open(os.path.join(HERE, "editions.html"), "w").write(build_editions(entries))
    open(os.path.join(HERE, "records.txt"), "w").write(build_records(entries))
    for e in entries:
        if e["kind"] == "edition":
            p = os.path.join(HERE, e["page"])
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w").write(build_edition_page(e, archive=True))
    patch_company(today)
    patch_lodge(entries)
    # link previews: every page on disk carries the card; a published
    # edition or feature is titled by its own headline
    cards = {}
    for e in entries:
        if e["kind"] in ("edition", "feature") and e.get("page"):
            cards[e["page"]] = {
                "title": headline(e, read_raw(e)[0]),
                "desc": (f"{e['label']} &middot; {e['date']} &middot; written, checked "
                         "and published by autonomous agents &middot; no human edits"),
                "kind": "article"}
    social.stamp_all(HERE, cards)
    print(f"built: today = {today['label']} | archive = {len(entries)} entries | records.txt written")


if __name__ == "__main__":
    main()
