/* Lodge a dispute: the whole flow runs in the reader's browser against
   the DisputeDesk contract. The page computes the hashes, the reader's
   wallet signs; nothing passes through a server of ours. */
(function () {
  var DESK = "0x83fcaef2230ec6f36d84717c2222817431e9b377";
  var TOKEN = "0xd34a99bc0f67ae1bbd63c660e6d0b0dd03e263b7";
  // sha256 of each verbatim record, matching the record pages' printed hashes
  var EDITIONS = [
    { label: "rehearsal 09 \u00b7 saturday 7 november 2026", raw: "tests/raw/test-09/edition.txt",
      hash: "b113f7d2e678af9c1e3a22bb28299ca9faa617292b9f00adc13d395e15853bcc" },
    { label: "rehearsal 08 \u00b7 saturday 7 november 2026", raw: "tests/raw/test-08/edition.txt",
      hash: "f8a879152182451e8ae47de08be04dcd9dede99b8332b5d46b82dc59caf5a351" },
    { label: "rehearsal 07 \u00b7 weekend \u00b7 saturday 7 november 2026", raw: "tests/raw/test-07/polish/a.md",
      hash: "3b1c7a191eb858fb04e1a3687199e71c81a165696e0e5c249bd5d2692339d429" },
    { label: "rehearsal 06 \u00b7 monday 2 november 2026", raw: "tests/raw/test-06/edition.txt",
      hash: "0886aeb934c40b290088e9831bd4bb52bade83b2dca15f89f284efeff273edb0" },
  ];
  var $ = function (id) { return document.getElementById(id); };
  var sel = $("ed"), ta = $("cl"), ev = $("ev"), evh = $("evh"),
      btn = $("file"), state = $("fstate");
  var record = null, claimHash = null, checkTimer = null;

  EDITIONS.forEach(function (e, i) {
    var o = document.createElement("option");
    o.value = i; o.textContent = e.label; sel.appendChild(o);
  });

  function strip(s) {
    return s.replace(/^[ \t\n\r\v\f]+/, "").replace(/[ \t\n\r\v\f]+$/, "");
  }
  function sha256hex(text) {
    return crypto.subtle.digest("SHA-256", new TextEncoder().encode(text)).then(function (d) {
      return Array.prototype.map.call(new Uint8Array(d), function (b) {
        return b.toString(16).padStart(2, "0");
      }).join("");
    });
  }

  function loadEdition() {
    var e = EDITIONS[sel.value];
    record = null;
    $("edhash").innerHTML = "editionHash (sha256 of the verbatim record)<br>" + e.hash;
    fetch(e.raw).then(function (r) { return r.text(); }).then(function (t) {
      t = strip(t);
      return sha256hex(t).then(function (h) {
        if (h !== e.hash) { $("edhash").innerHTML += "<br>record fetch did not match its hash \u2014 do not file"; return; }
        record = t; checkClaim();
      });
    }).catch(function () {
      $("edhash").innerHTML += "<br>the record could not be fetched just now";
    });
  }

  function checkClaim() {
    clearTimeout(checkTimer);
    checkTimer = setTimeout(function () {
      var q = strip(ta.value);
      claimHash = null;
      var st = $("clstate"), ch = $("clhash");
      if (!q) {
        st.className = "pending";
        st.innerHTML = "&middot; checked against the verbatim record as you type";
        ch.style.display = "none"; ready(); return;
      }
      if (!record) {
        st.className = "pending"; st.textContent = "\u00b7 the record is still loading";
        ready(); return;
      }
      if (record.indexOf(q) === -1) {
        st.className = "bad-badge"; st.textContent = "\u2717 not found in the verbatim record";
        ch.style.display = "none"; ready(); return;
      }
      sha256hex(q).then(function (h) {
        claimHash = h;
        st.className = "ok-badge"; st.textContent = "\u2713 located in the record";
        ch.style.display = "block";
        ch.innerHTML = "claimHash (sha256 of the quoted passage)<br>" + h;
        ready();
      });
    }, 250);
  }

  function uriOk(u) { return /^[A-Za-z][A-Za-z0-9+.-]*:[^\s"\\]+$/.test(u) && u.length <= 500; }
  function evhOk(h) {
    var v = h.replace(/^0x/, "");
    return h === "" || /^[0-9a-fA-F]{64}$/.test(v);
  }
  function ready() {
    var ok = claimHash && uriOk(strip(ev.value)) && evhOk(strip(evh.value));
    btn.disabled = !ok || busy;
  }

  sel.onchange = function () { loadEdition(); };
  ta.oninput = checkClaim;
  ev.oninput = ready; evh.oninput = ready;
  loadEdition();

  /* --- the filing --- */
  var busy = false;
  function say(t) { state.textContent = t; }
  function req(method, params) { return window.ethereum.request({ method: method, params: params }); }
  function call(to, data) { return req("eth_call", [{ to: to, data: data }, "latest"]); }
  function pad32(hex) { return hex.replace(/^0x/, "").padStart(64, "0"); }
  function waitReceipt(tx) {
    return req("eth_getTransactionReceipt", [tx]).then(function (r) {
      if (r) return r;
      return new Promise(function (res) { setTimeout(res, 4000); }).then(function () { return waitReceipt(tx); });
    });
  }
  function encodeChallenge(editionHash, claim, uri, evidenceHash) {
    var u = new TextEncoder().encode(uri), hex = "";
    for (var i = 0; i < u.length; i++) hex += u[i].toString(16).padStart(2, "0");
    hex += "0".repeat((64 - (hex.length % 64)) % 64);
    return "0xd5224ffe" + pad32(editionHash) + pad32(claim) +
      pad32("80") + pad32(evidenceHash) + pad32(u.length.toString(16)) + hex;
  }

  btn.onclick = function () {
    if (busy) return;
    busy = true; btn.disabled = true;
    var e = EDITIONS[sel.value];
    var uri = strip(ev.value);
    var pin = strip(evh.value).replace(/^0x/, "").toLowerCase() || "0".repeat(64);
    var account = null, bond = null;
    (function () {
      if (!window.ethereum) { say("no wallet found in this browser \u2014 the desk needs one to hold your bond"); throw 0; }
      return req("eth_requestAccounts", []);
    })().then(function (accts) {
      account = accts[0];
      return req("eth_chainId", []);
    }).then(function (chain) {
      if (parseInt(chain, 16) !== 1) {
        say("switch the wallet to ethereum mainnet");
        return req("wallet_switchEthereumChain", [{ chainId: "0x1" }]);
      }
    }).then(function () {
      return Promise.all([call(DESK, "0x5c975abb"), call(DESK, "0x64c9ec6f"),
        call(TOKEN, "0xdd62ed3e" + pad32(account) + pad32(DESK))]);
    }).then(function (r) {
      if (BigInt(r[0]) === 1n) { say("the desk is paused for new filings just now"); throw 0; }
      bond = BigInt(r[1]);
      if (BigInt(r[2]) >= bond) return null;
      say("prompt 1 of 2 \u00b7 approve the " + (Number(bond / 10n ** 14n) / 10000) + " IMD bond\u2026");
      return req("eth_sendTransaction", [{ from: account, to: TOKEN,
        data: "0x095ea7b3" + pad32(DESK) + pad32(bond.toString(16)) }]).then(waitReceipt)
        .then(function (rc) { if (BigInt(rc.status) !== 1n) { say("the approval reverted \u2014 nothing filed"); throw 0; } });
    }).then(function () {
      say("final prompt \u00b7 file the challenge\u2026");
      return req("eth_sendTransaction", [{ from: account, to: DESK,
        data: encodeChallenge(e.hash, claimHash, uri, pin) }]).then(waitReceipt);
    }).then(function (rc) {
      if (BigInt(rc.status) !== 1n) { say("the filing reverted \u2014 the bond was not taken"); throw 0; }
      var id = "";
      (rc.logs || []).forEach(function (l) {
        if (l.topics && l.topics[0] === "0x2ccda2b0f41493e529ce24832575361c696cfafefc1093ba0c880020d8aae390")
          id = l.topics[1];
      });
      say("\u2713 filed \u00b7 challenge " + id.slice(0, 10) + "\u2026 \u00b7 the court is convening \u00b7 the verdict prints on the disputes page");
    }).catch(function (err) {
      if (err !== 0) say("declined or failed: " + ((err && err.message) || err));
    }).then(function () { busy = false; ready(); });
  };
})();
