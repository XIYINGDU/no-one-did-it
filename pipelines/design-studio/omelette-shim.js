/* ============================================================
   omelette-shim.js — local re-host of the design tool's persistence bridge.

   The design package (design-canvas.jsx, image-slot.js, tweaks-panel.jsx) was
   built for a host runtime called "omelette": it READS state via plain
   fetch('./<sidecar>.json') and WRITES via window.omelette.writeFile(path, json).
   Outside that host, window.omelette is absent, so every <image-slot> renders
   read-only (image-slot.js gates editability on `window.omelette.writeFile`).

   This shim restores write persistence by POSTing to serve.mjs, which writes the
   sidecar JSON to disk next to the design files. Reads already work (the server
   serves the sidecars statically). Load this BEFORE the design scripts.
   ============================================================ */
(function () {
  function resolve(path) {
    // Sidecars are referenced relative to the iframe document (e.g.
    // ".image-slots.state.json" from /design/...html -> /design/.image-slots.state.json).
    return new URL(path, document.baseURI).pathname;
  }

  function writeFile(path, content) {
    return fetch('/__omelette/write', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ path: resolve(path), content: String(content) }),
    }).then(function (r) {
      if (!r.ok) throw new Error('omelette write failed: HTTP ' + r.status);
      return r.json().catch(function () { return {}; });
    });
  }

  function readFile(path) {
    return fetch(resolve(path), { cache: 'no-store' })
      .then(function (r) { return r.ok ? r.text() : null; });
  }

  // Object.assign so we don't clobber anything a future host injects first.
  window.omelette = Object.assign(window.omelette || {}, { writeFile: writeFile, readFile: readFile });
})();
