// Open Interest — live chrome (clock, fleet pulse, ticker from baked data)
(async function () {
  const $ = (s) => document.querySelector(s);
  let data = { fleet: { online: null, enrolled: null }, events: [], updated: null };
  try { data = await (await fetch("data.json?x=" + Date.now())).json(); } catch (e) {}
  // ticker from baked OI events
  const tin = $(".ticker-in");
  if (tin && data.events && data.events.length) {
    const spans = data.events.map((t) => `<span>${t}</span>`).join("");
    tin.innerHTML = spans + spans;
  }
  // tap toggles the ticker (hover-pause has no touch equivalent)
  document.addEventListener("click", (e) => {
    const tick = e.target.closest(".ticker");
    if (!tick) return;
    const inner = tick.querySelector(".ticker-in");
    if (inner) inner.style.animationPlayState = inner.style.animationPlayState === "paused" ? "running" : "paused";
  });
  // live fleet pulse: the one CORS-open endpoint, else baked numbers
  let online = data.fleet.online;
  try {
    const r = await fetch("https://api.imd.fun/steps/hourly");
    if (r.ok) { const d = await r.json(); if (d && d.online) online = d.online; }
  } catch (e) {}
  // meta line: the age shown is the real age of the baked data, nothing else
  const meta = $("#livemeta");
  const baked = data.updated ? Date.parse(data.updated) : NaN;
  function render() {
    if (!meta) return;
    const o = online ? Number(online).toLocaleString("en-US") : "—";
    let age = "";
    if (!isNaN(baked)) {
      const s = Math.max(0, Math.floor((Date.now() - baked) / 1000));
      age = " &middot; data " + (s < 90 ? s + "s" : Math.round(s / 60) + "m") + " old";
    }
    meta.innerHTML = `<span class="dot"></span>swarm ${o} online${age}`;
  }
  render();
  if (!isNaN(baked)) setInterval(render, 1000);
})();

document.addEventListener('click', function (e) {
  const el = e.target.closest('[data-soon]');
  if (!el) return;
  e.preventDefault();
  const old = document.querySelector('.oi-toast');
  if (old) old.remove();
  const t = document.createElement('div');
  t.className = 'oi-toast';
  t.setAttribute('role', 'status');
  t.setAttribute('aria-live', 'polite');
  t.innerHTML = 'coming soon &middot; ' + el.getAttribute('data-soon');
  document.body.appendChild(t);
  setTimeout(() => t.remove(), 3500);
});
