#!/usr/bin/env python3
"""Bake data.json for the OI site: fleet numbers + OI's own job events.
Finds the newsroom's jobs automatically: lists recent network jobs, fetches
detail for ids it hasn't resolved yet, and keeps the ones paid by the
newsroom wallet. Known jobs persist in data.json, so nothing ages out of
the API's recent-jobs window. Pure stdlib; safe to run from cron or CI."""
import json, time, urllib.request

WALLET = "0xbe80e5979313cf8aff2b8e54e615fe3ecd8358f5"
SEED_JOBS = [  # pre-wallet-era jobs, paid before the ops wallet convention
    "bea3fd5d-8fc8-4408-8d7b-f9748277763f",
    "414ba24a-5132-48dc-8cbd-db1f369016c2",
]
TERMINAL = {"completed", "failed", "cancelled"}

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "openinterest-bake/2.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

# previous bake: carry known jobs forward
known = {}
try:
    prev = json.load(open("data.json"))
    known = {j["id"]: j for j in prev.get("jobs", [])}
except Exception:
    pass

fleet = {}
try:
    c = get("https://api.imd.fun/contributors")
    fleet = {"enrolled": len(c.get("contributors", [])), "receipts": c.get("receipts", 0)}
except Exception as e:
    print("contributors:", e)

candidates = list(SEED_JOBS)
try:
    recent = get("https://api.imd.fun/jobs")
    candidates += [j["id"] for j in recent.get("jobs", [])]
except Exception as e:
    print("jobs list:", e)

for jid in candidates:
    prior = known.get(jid)
    if prior and (prior.get("state") in TERMINAL) and prior.get("ours") is not None:
        continue  # resolved and final; nothing to re-fetch
    if not prior and jid not in SEED_JOBS:
        pass  # unknown id from the recent list: resolve it below
    try:
        j = get(f"https://api.imd.fun/jobs/{jid}")
    except Exception as e:
        print(jid, e)
        continue
    ours = jid in SEED_JOBS or (j.get("paidBy") or "").lower() == WALLET
    known[jid] = {
        "id": jid,
        "ours": ours,
        "state": j.get("state", "?"),
        "template": (j.get("template") or "").replace("skill:", ""),
        "createdAt": j.get("createdAt", ""),
    }

ours = sorted((j for j in known.values() if j["ours"]), key=lambda j: j["createdAt"])
events = []
for j in ours:
    tick = " ✓" if j["state"] == "completed" else ""
    events.append(f"job {j['id'][:8]} &middot; {j['template']} &middot; {j['state']}{tick}")
events += [
    "edition &#8470; 000 &middot; the masthead &middot; false start kept on purpose",
    "payroll &rarr; the panel &middot; per protocol",
    "disputes open &middot; 0 pending",
    "no human edits &middot; every decision on-chain",
]

out = {
    "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "fleet": {"online": None, **fleet},
    "jobs": [j for j in known.values() if j["ours"]],
    "events": events,
}
json.dump(out, open("data.json", "w"))
print("baked", len(ours), "of our jobs,", len(events), "events")
