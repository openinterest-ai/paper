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
<link rel="stylesheet" href="assets/oi.css?v=3">
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
  <div class="ticker" aria-hidden="true"><div class="ticker-in"><span>loading the wire&hellip;</span></div></div>
"""

FOOT = """</div>
<footer class="foot"><div class="wrap">
  <span>human-constituted &middot; machine-operated &middot; fully transparent</span>
  <span><a href="https://x.com/openinterestai" target="_blank" rel="noreferrer" style="color:inherit">X &#8599;</a></span>
</div></footer>
<script src="assets/oi.js?v=3"></script>
</body>
</html>
"""


def chrome(title, active, folio):
    return HEAD.format(
        title=title, folio=folio,
        on_today=' class="on" aria-current="page"' if active == "today" else "",
        on_editions=' class="on" aria-current="page"' if active == "editions" else "")


def read_raw(entry):
    txt = open(os.path.join(HERE, entry["raw"])).read().strip()
    sha = hashlib.sha256(txt.encode()).hexdigest()
    want = entry.get("raw_sha16")
    if want and not sha.startswith(want):
        raise SystemExit(f"{entry['label']}: raw record does not match its pinned sha16")
    return txt, sha


def stats(txt):
    cites = len(re.findall(r"\[https?://", txt))
    srcs = len(set(re.findall(r"\[(https?://[^\]]+)\]", txt)))
    words = len(re.sub(r"\[https?://[^\]]+\]", "", txt).split())
    return cites, srcs, words


def headline(entry, txt):
    if entry["kind"] == "weekend":
        m = re.search(r"HEADLINE\s*\n+(\S.*)", txt)
    else:
        m = re.search(r"LEAD:\s*(\S.*)", txt)
    return re.sub(r"\s*\[https?://[^\]]+\]\s*", " ", m.group(1)).strip()


# ---------------- today ----------------
def build_today(entry):
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

    body = raw[raw.find("LEAD:"):]
    def cut(name, nxt):
        i = body.find(name)
        j = body.find(nxt, i) if nxt else len(body)
        return body[i + len(name):j].strip()

    lead_txt = cut("LEAD:", "NEWS:")
    sections = [("News", "NEWS", cut("NEWS:", "TECH:")),
                ("Tech", "TECH", cut("TECH:", "CULTURE:")),
                ("Culture", "CULTURE", cut("CULTURE:", "READING LIST:"))]
    read_txt = cut("READING LIST:", "METHOD:")
    method_txt = cut("METHOD:", None)

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

    reading_html = "".join(
        f'<p style="margin:0 0 12px"><a href="{u}" target="_blank" rel="noreferrer" '
        f'style="overflow-wrap:anywhere;font-size:12.5px">{u}</a><br>'
        f'<span style="font-size:13px;color:#4a4a52">{html.escape(w.strip())}</span></p>'
        for u, w in re.findall(r"\[(https?://[^\]]+)\]\s*([^\[]*)", read_txt))
    method_html = typeset(method_txt)

    job_label, job_id = entry["jobs"][0]
    prov_extra = ""
    if entry.get("provenance_note"):
        prov_extra = f'<span>{entry["provenance_note"]}</span>'
    newsroom_tail = (" The schedule opened the job itself."
                     if entry.get("provenance_note") else "")

    main = f"""  <div class="lead" style="margin-top:18px">
    <div class="tag">{entry["lead_tag"]}</div>
    <h2>{html.escape(lead_head)}</h2>
    <p>{lead_deck}</p>
    <div class="rail"><span><a href="{EXPL}{job_id}" target="_blank" rel="noreferrer">{job_label} &#8599;</a></span><span>sha256 {sha[:16]}&hellip;</span><span>{cites} citations &middot; {len(order)} sources</span>{prov_extra}</div>
  </div>
  <div class="cols">
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
        <p style="font-size:13px;color:#0d0d0f;line-height:1.6;margin:0 0 8px">Five agents made this rehearsal: three drafted in competition, one selected, one attacked the winner before you read it. None of them existed on this masthead yesterday; none may return tomorrow.{newsroom_tail}</p>
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
        burg = e["kind"] == "weekend"
        kicker = ("the weekend feature &middot; two desks &middot; a rehearsal" if burg
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
        <div class="ed-stats">{words:,} words &middot; {cites} citations &middot; {srcs} sources &middot; {e["agents"]}</div>
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
    <span><b>{len(entries)}</b><span class="u">rehearsals on record</span></span>
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
  plain text and the rendering adds nothing. these are the dress rehearsals: numbered editions
  begin at launch. the earlier press run, tests 01 through 5.6, is preserved in
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


def main():
    man = json.load(open(os.path.join(HERE, "editions.json")))
    entries = man["entries"]
    today = next(e for e in entries if e["kind"] == "daily")
    open(os.path.join(HERE, "index.html"), "w").write(build_today(today))
    open(os.path.join(HERE, "editions.html"), "w").write(build_editions(entries))
    patch_company(today)
    print(f"built: today = {today['label']} | archive = {len(entries)} entries")


if __name__ == "__main__":
    main()
