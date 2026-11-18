/* The corrections ledger: history compiled from the DisputeDesk event log
   by the newsroom's runners (ledger.json); the pool balance and the
   freshest blocks read live over public RPC. No database. No human edits. */
(function () {
  var DESK = "0x83fcaef2230ec6f36d84717c2222817431e9b377";
  var RPCS = ["https://ethereum-rpc.publicnode.com", "https://rpc.flashbots.net"];
  var T_FILED = "0x2ccda2b0f41493e529ce24832575361c696cfafefc1093ba0c880020d8aae390";
  var T_SETTLED = "0xc4ce7d81d6c338c2b46c3584df723c252fd308a182cb205c46174d313230c9b6";
  var T_CORRECTION = "0x7131877e206047c444d7b8741dadc0ece14cd90ceeee2649bad37c89cc2d9334";
  var box = document.getElementById("ledger");

  function rpc(i, method, params) {
    return fetch(RPCS[i], {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: method, params: params }),
    }).then(function (r) { return r.json(); }).then(function (j) {
      if (j.error) throw new Error(j.error.message);
      return j.result;
    }).catch(function (e) {
      if (i + 1 < RPCS.length) return rpc(i + 1, method, params);
      throw e;
    });
  }
  var sh = function (h) { return h.slice(2, 10); };

  // the pool, live from the contract: poolBalance()
  var pool = document.getElementById("pool");
  if (pool) {
    rpc(0, "eth_call", [{ to: DESK, data: "0x96365d44" }, "latest"])
      .then(function (r) {
        var v = Number(BigInt(r)) / 1e18;
        pool.textContent = v.toLocaleString("en-US", { maximumFractionDigits: 2 }) + " IMD";
      })
      .catch(function () { pool.textContent = "see the contract"; });
  }

  if (!box) return;

  // history from the baked log, freshness from a live read of the blocks
  // past it (public RPCs cap browser getLogs ranges, so the page cannot
  // read the whole span itself)
  var baked = fetch("ledger.json", { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error("no ledger"); return r.json(); });

  baked.then(function (led) {
    var fresh = rpc(0, "eth_getLogs", [{
      address: DESK, fromBlock: "0x" + (led.toBlock + 1).toString(16),
      toBlock: "latest", topics: [[T_FILED, T_SETTLED, T_CORRECTION]] }])
      .catch(function () { return []; });
    return fresh.then(function (live) {
      var seen = {}, logs = [];
      led.logs.concat(live).forEach(function (l) {
        var k = l.transactionHash + ":" + l.logIndex;
        if (!seen[k]) { seen[k] = 1; logs.push(l); }
      });
      return logs;
    });
  }).then(function (logs) {
    var filed = 0, open = 0, verdicts = { "0x01": "upheld", "0x02": "rejected", "0x03": "failed" };
    var corrections = [], settled = [];
    logs.forEach(function (l) {
      if (l.topics[0] === T_FILED) { filed++; open++; }
      if (l.topics[0] === T_SETTLED) {
        open--;
        var status = "0x0" + parseInt(l.data.slice(2, 66), 16);
        settled.push({ id: sh(l.topics[1]), verdict: verdicts[status] || "settled" });
      }
      if (l.topics[0] === T_CORRECTION)
        corrections.push({ edition: sh(l.topics[1]), claim: sh(l.topics[2]), id: sh(l.topics[3]) });
    });
    if (filed === 0) {
      box.innerHTML = '<div class="ledger-empty"><b>&#10003; no corrections</b>' +
        "no challenges filed &middot; every verdict prints here, either way</div>";
      return;
    }
    var html = '<div class="ledger-row" style="border-top:none;padding-top:0">' +
      filed + " challenge" + (filed === 1 ? "" : "s") + " filed &middot; " +
      open + " open &middot; " + corrections.length + " correction" +
      (corrections.length === 1 ? "" : "s") + "</div>";
    corrections.forEach(function (c) {
      html += '<div class="ledger-row"><b>correction</b> &middot; edition ' + c.edition +
        "&hellip; &middot; claim " + c.claim + "&hellip; &middot; verdict " + c.id + "&hellip;</div>";
    });
    settled.forEach(function (s) {
      if (s.verdict !== "upheld")
        html += '<div class="ledger-row">challenge ' + s.id + "&hellip; &middot; " + s.verdict + "</div>";
    });
    box.innerHTML = html;
  })
  .catch(function () {
    box.innerHTML = '<div class="ledger-empty">the event log could not be read just now &middot; ' +
      'the record itself is on chain, unchanged</div>';
  });
})();
