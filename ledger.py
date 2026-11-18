#!/usr/bin/env python3
"""The ledger bake: the DisputeDesk event log, compiled to ledger.json.

Free public RPCs stopped serving eth_getLogs over the desk's whole span
from a browser once the deploy block aged past their archive windows
(learned 2026-11-19), so the runners compile the history in chunks and
the page renders it, reading only the pool and the freshest blocks live.
Incremental: resumes from the last baked block. Pure stdlib."""
import datetime, json, os, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DESK = "0x83fcaef2230ec6f36d84717c2222817431e9b377"
DEPLOY = 26390450
TOPICS = ["0x2ccda2b0f41493e529ce24832575361c696cfafefc1093ba0c880020d8aae390",
          "0xc4ce7d81d6c338c2b46c3584df723c252fd308a182cb205c46174d313230c9b6",
          "0x7131877e206047c444d7b8741dadc0ece14cd90ceeee2649bad37c89cc2d9334"]
RPCS = ["https://rpc.flashbots.net", "https://ethereum-rpc.publicnode.com"]
CHUNK = 1900  # under every provider's 2000-block range cap
CONFIRM = 5   # stay behind the head so a reorg cannot bake a phantom log


def call(method, params):
    last = None
    for attempt in range(4):
        for url in RPCS:
            try:
                req = urllib.request.Request(
                    url, data=json.dumps({"jsonrpc": "2.0", "id": 1,
                                          "method": method, "params": params}).encode(),
                    headers={"Content-Type": "application/json",
                             "User-Agent": "openinterest-press/1.0"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    j = json.load(r)
                if "error" in j:
                    raise RuntimeError(j["error"]["message"])
                return j["result"]
            except Exception as e:
                last = e
        time.sleep(2 * (attempt + 1))  # providers rate-limit bursts
    raise last


def main():
    path = os.path.join(HERE, "ledger.json")
    old = {"toBlock": DEPLOY - 1, "logs": []}
    if os.path.exists(path):
        old = json.load(open(path))
    head = int(call("eth_blockNumber", []), 16) - CONFIRM
    frm, logs = old["toBlock"] + 1, list(old["logs"])
    while frm <= head:
        to = min(frm + CHUNK - 1, head)
        logs.extend(call("eth_getLogs", [{"address": DESK, "fromBlock": hex(frm),
                                          "toBlock": hex(to), "topics": [TOPICS]}]))
        frm = to + 1
        time.sleep(1)
    seen, dedup = set(), []
    for l in logs:
        k = (l.get("transactionHash"), l.get("logIndex"))
        if k not in seen:
            seen.add(k)
            dedup.append(l)
    dedup.sort(key=lambda l: (int(l["blockNumber"], 16), int(l["logIndex"], 16)))
    out = {"desk": DESK, "fromBlock": DEPLOY, "toBlock": head,
           "bakedAt": datetime.datetime.now(datetime.timezone.utc
                                            ).isoformat(timespec="seconds"),
           "logs": dedup}
    json.dump(out, open(path, "w"), indent=1)
    open(path, "a").write("\n")
    print(f"ledger baked: {len(dedup)} logs through block {head}")


if __name__ == "__main__":
    main()
