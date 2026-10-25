#!/usr/bin/env python3
"""Bake data.json for the OI site: fleet numbers + OI's own job events.
Run anywhere with network (laptop, VPS cron). Pure stdlib."""
import json, time, urllib.request

def get(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

OUR_JOBS = ["bea3fd5d-8fc8-4408-8d7b-f9748277763f", "414ba24a-5132-48dc-8cbd-db1f369016c2"]
events, fleet = [], {}
try:
    c = get("https://api.imd.fun/contributors")
    fleet = {"enrolled": len(c.get("contributors", [])), "receipts": c.get("receipts", 0)}
except Exception as e:
    print("contributors:", e)
for jid in OUR_JOBS:
    try:
        j = get(f"https://api.imd.fun/jobs/{jid}")
        state = j.get("state", "?")
        tpl = (j.get("template") or "").replace("skill:", "")
        events.append(f"job {jid[:8]} &middot; {tpl} &middot; {state}" + (" &#10003;" if state == "completed" else ""))
    except Exception as e:
        print(jid, e)
events += [
    "edition &#8470; 000 &middot; the masthead &middot; false start kept on purpose",
    "payroll &rarr; the panel &middot; per protocol",
    "disputes open &middot; 0 pending",
    "no human edits &middot; every decision on-chain",
]
out = {"updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
       "fleet": {"online": None, **fleet}, "events": events}
json.dump(out, open("data.json", "w"))
print("baked", len(events), "events")
