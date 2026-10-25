// Open Interest — live chrome (clock, fleet pulse, ticker from baked data)
(async function () {
  const $ = (s) => document.querySelector(s);
  let data = { fleet: { online: null, enrolled: null }, events: [], updated: null };
  try { data = await (await fetch("/data.json?x=" + Date.now())).json(); } catch (e) {
    try { data = await (await fetch("data.json?x=" + Date.now())).json(); } catch (e2) {}
  }
  // ticker from baked OI events
  const tin = $(".ticker-in");
  if (tin && data.events && data.events.length) {
    const spans = data.events.map((t) => `<span>${t}</span>`).join("");
    tin.innerHTML = spans + spans;
  }
  // live fleet pulse: the one CORS-open endpoint, else baked numbers
  let online = data.fleet.online;
  try {
    const r = await fetch("https://api.imd.fun/steps/hourly");
    if (r.ok) { const d = await r.json(); if (d && d.online) online = d.online; }
  } catch (e) {}
  // ticking meta line
  let synced = 0;
  const meta = $("#livemeta");
  function render() {
    if (!meta) return;
    const o = online ? Number(online).toLocaleString("en-US") : "—";
    meta.innerHTML = `<span class="dot"></span>swarm ${o} online &middot; synced ${synced === 0 ? "just now" : synced + "s ago"}<span class="blink">&#9646;</span>`;
  }
  render();
  setInterval(() => { synced++; if (synced > 9 + Math.random() * 4) synced = 0; render(); }, 1000);
})();

document.addEventListener('click', function (e) {
  const el = e.target.closest('[data-soon]');
  if (!el) return;
  e.preventDefault();
  const old = document.querySelector('.oi-toast');
  if (old) old.remove();
  const t = document.createElement('div');
  t.className = 'oi-toast';
  t.innerHTML = 'coming soon &middot; ' + el.getAttribute('data-soon');
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3500);
});
