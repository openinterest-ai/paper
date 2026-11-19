/* The pressroom cache: the service worker behind the installed app.
   Network first, always — the reader sees the freshest edition whenever
   the network answers. Every page and asset that loads is kept, so the
   editions you have read stay readable offline. No tracking, no push,
   no background anything: a cache, nothing else. */
var CACHE = "oi-v2"; // v2: the icon set became the burgundy profile mark
var SHELL = [
  "index.html",
  "editions.html",
  "manifest.webmanifest",
  "assets/oi.css?v=4",
  "assets/oi.js?v=4",
  "assets/icon-192.png",
];

self.addEventListener("install", function (e) {
  e.waitUntil(
    caches.open(CACHE)
      .then(function (c) { return c.addAll(SHELL); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener("activate", function (e) {
  e.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        if (k !== CACHE) return caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET") return;
  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return; // fonts, RPC: untouched
  e.respondWith(
    fetch(req).then(function (res) {
      if (res && res.ok) {
        var copy = res.clone();
        caches.open(CACHE).then(function (c) { c.put(req, copy); });
      }
      return res;
    }).catch(function () {
      return caches.match(req).then(function (hit) {
        if (hit) return hit;
        // offline navigation to a page never visited: front page
        if (req.mode === "navigate") return caches.match("index.html");
        return Response.error();
      });
    })
  );
});
