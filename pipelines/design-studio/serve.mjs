#!/usr/bin/env node
/* ============================================================
   serve.mjs — local re-host of the "omelette" design runtime.

   Node stdlib only (no npm install, no node_modules). Serves the design-studio
   directory, accepts the omelette write-bridge, and renders a parent shell that
   iframes the design canvas with an edit-mode toggle + zoom readout.

   Routes:
     GET  /                      -> index.html (parent shell)
     POST /__omelette/write      -> { path, content } written to disk (sandboxed)
     GET  /solo?board=&w=&h=&ed=  -> one artboard at production size (export source)
     GET  /*                     -> static file under design-studio/

   Run:  node design-studio/serve.mjs        (PORT env overrides; default 5180)
   ============================================================ */
import http from 'node:http';
import { promises as fs, createReadStream } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const PORT = process.env.PORT ? Number(process.env.PORT) : 5180;

const EDITIONS = {
  covers: 'design/No One Did It - Covers.html',
  dossier: 'design/No One Did It - Dossier Edition.html',
};

const MIME = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.mjs': 'text/javascript; charset=utf-8',
  '.jsx': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.svg': 'image/svg+xml',
  '.woff2': 'font/woff2', '.woff': 'font/woff', '.ttf': 'font/ttf',
  '.map': 'application/json; charset=utf-8', '.ico': 'image/x-icon', '.txt': 'text/plain; charset=utf-8',
};

// Resolve a URL path to a real path inside ROOT, or null if it escapes.
function safeJoin(urlPath) {
  let decoded;
  try { decoded = decodeURIComponent(urlPath); } catch { return null; }
  const full = path.normalize(path.join(ROOT, decoded));
  return full === ROOT || full.startsWith(ROOT + path.sep) ? full : null;
}

async function readBody(req) {
  const chunks = [];
  for await (const c of req) chunks.push(c);
  return Buffer.concat(chunks).toString('utf8');
}

async function serveFile(res, file) {
  let stat;
  try { stat = await fs.stat(file); } catch { res.writeHead(404).end('not found'); return; }
  if (stat.isDirectory()) { res.writeHead(403).end('forbidden'); return; }
  const ext = path.extname(file).toLowerCase();
  const headers = { 'Content-Type': MIME[ext] || 'application/octet-stream' };
  // Sidecar JSON, HTML, and the editable design source (.jsx) must reflect the
  // latest on every reload; vendored libs/fonts stay cacheable.
  if (ext === '.json' || ext === '.html' || ext === '.jsx' || ext === '.css') headers['Cache-Control'] = 'no-store';
  res.writeHead(200, headers);
  createReadStream(file).pipe(res);
}

const server = http.createServer(async (req, res) => {
  try {
    const u = new URL(req.url, `http://localhost:${PORT}`);

    // ── omelette write bridge ──────────────────────────────────────────────
    if (req.method === 'POST' && u.pathname === '/__omelette/write') {
      const body = JSON.parse((await readBody(req)) || '{}');
      const target = safeJoin(body.path || '');
      if (!target) { res.writeHead(400).end('bad path'); return; }
      await fs.mkdir(path.dirname(target), { recursive: true });
      await fs.writeFile(target, String(body.content ?? ''), 'utf8');
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ ok: true, path: body.path }));
      return;
    }

    // ── solo artboard (export source) ──────────────────────────────────────
    if (u.pathname === '/solo') {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
      res.end(soloPage(u.searchParams));
      return;
    }

    // ── parent shell ───────────────────────────────────────────────────────
    if (u.pathname === '/' || u.pathname === '/index.html') {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
      res.end(shellPage());
      return;
    }

    // ── static ─────────────────────────────────────────────────────────────
    const file = safeJoin(u.pathname);
    if (!file) { res.writeHead(403).end('forbidden'); return; }
    await serveFile(res, file);
  } catch (e) {
    res.writeHead(500).end('server error: ' + e.message);
  }
});

server.listen(PORT, () => {
  console.log(`design-studio  →  http://localhost:${PORT}/`);
  console.log(`  editions: covers (illustrated/cartoon) · dossier`);
  console.log(`  root: ${ROOT}`);
});

// ─────────────────────────────────────────────────────────────────────────────
// Parent shell — iframes the canvas, drives the edit-mode handshake + zoom readout
// ─────────────────────────────────────────────────────────────────────────────
function shellPage() {
  const covers = '/' + EDITIONS.covers;
  const dossier = '/' + EDITIONS.dossier;
  return `<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8" />
<title>No One Did It — Design Studio</title>
<style>
  :root { color-scheme: dark; }
  html,body { margin:0; height:100%; background:#1b1a17; font:13px/1.4 -apple-system,system-ui,sans-serif; color:#e7e0d0; }
  body { display:flex; flex-direction:column; }
  .bar { display:flex; align-items:center; gap:14px; padding:8px 14px; background:#26241f; border-bottom:1px solid #000; }
  .bar b { letter-spacing:.04em; color:#cdbfa3; }
  .seg { display:inline-flex; border:1px solid #4a4031; border-radius:6px; overflow:hidden; }
  .seg button { background:transparent; color:#cdbfa3; border:0; padding:5px 12px; cursor:pointer; font:inherit; }
  .seg button.on { background:#c96442; color:#fff; }
  label.edit { display:inline-flex; align-items:center; gap:6px; cursor:pointer; user-select:none; }
  .zoom { margin-left:auto; font-variant-numeric:tabular-nums; color:#aaa292; }
  .hint { color:#7d7565; }
  iframe { flex:1; width:100%; border:0; background:#2b2a27; }
</style></head>
<body>
  <div class="bar">
    <b>NO ONE DID IT · Design Studio</b>
    <span class="seg" id="ed">
      <button data-src="${covers}" class="on">Illustrated / Cartoon</button>
      <button data-src="${dossier}">Dossier</button>
    </span>
    <label class="edit"><input type="checkbox" id="edit" checked /> Edit mode</label>
    <span class="hint">double-click a filled image-slot to re-crop · scroll/pinch to zoom · drag to pan</span>
    <span class="zoom" id="zoom">100%</span>
  </div>
  <iframe id="f" src="${covers}"></iframe>
<script>
  var f = document.getElementById('f');
  var editBox = document.getElementById('edit');
  var zoom = document.getElementById('zoom');

  function send(type){ try { f.contentWindow.postMessage({ type: type }, '*'); } catch(e){} }
  function syncEdit(){ send(editBox.checked ? '__activate_edit_mode' : '__deactivate_edit_mode'); }

  // The canvas/panel announce themselves and stream zoom ticks to the parent.
  window.addEventListener('message', function (e) {
    var m = e.data || {};
    if (m.type === '__edit_mode_available' || m.type === '__dc_present') syncEdit();
    else if (m.type === '__dc_zoom' && typeof m.scale === 'number') zoom.textContent = Math.round(m.scale * 100) + '%';
  });

  editBox.addEventListener('change', syncEdit);
  document.getElementById('ed').addEventListener('click', function (e) {
    var b = e.target.closest('button[data-src]'); if (!b) return;
    [].forEach.call(this.children, function (c){ c.classList.toggle('on', c === b); });
    f.src = b.getAttribute('data-src');
  });
  f.addEventListener('load', syncEdit);
</script>
</body></html>`;
}

// ─────────────────────────────────────────────────────────────────────────────
// Solo page — renders exactly ONE artboard component at production size, reusing
// the persisted sidecars. Used by export.mjs as the headless-Chrome screenshot
// source. board ids match the DCArtboard ids in the entry HTMLs.
// ─────────────────────────────────────────────────────────────────────────────
function soloPage(params) {
  const ed = params.get('ed') === 'dossier' ? 'dossier' : 'covers';
  const board = (params.get('board') || '').replace(/[^a-zA-Z0-9_-]/g, '');
  // The Dossier paper tone defaults to "Newsprint" in the studio (it adds a
  // `news` class to <html>); mirror that here so exports match what's on screen.
  // Override with &paper=manila for the warmer default ground.
  const news = ed === 'dossier' && params.get('paper') !== 'manila';
  // Artboard logical size. Authored at 600x925; a `bh` override lets the cover
  // use a 1.6:1 logical box (600x960) so the flex layouts REFLOW to fill it
  // rather than being non-uniformly stretched. One uniform scale is derived
  // from the target width, so nothing is distorted.
  const BASE_W = Math.max(1, Math.min(4000, Number(params.get('bw')) || 600));
  const BASE_H = Math.max(1, Math.min(6000, Number(params.get('bh')) || 925));
  const w = Math.max(1, Math.min(6000, Number(params.get('w')) || 1600));
  const scale = w / BASE_W;
  const h = Math.round(BASE_H * scale);
  // Reuse the real design CSS + components; SVG filters are duplicated here so a
  // solo page is self-contained (the entry HTMLs define them inline).
  const filters = ed === 'dossier' ? DOSSIER_FILTERS : COVERS_FILTERS;
  const cssHref = ed === 'dossier' ? '/design/dossier.css' : '/design/covers.css';
  const compScripts = (ed === 'dossier'
    ? ['design-canvas.jsx', 'tweaks-panel.jsx', 'dossier-front.jsx', 'dossier-back.jsx', 'dossier-chapters.jsx']
    : ['design-canvas.jsx', 'covers.jsx', 'cartoon.jsx', 'cartoon-art.jsx']
  ).map(s => `<script type="text/babel" src="/design/${s}"><\/script>`).join('\n');

  return `<!DOCTYPE html>
<html lang="en"${news ? ' class="news"' : ''}><head><meta charset="UTF-8" />
<link rel="stylesheet" href="/vendor/fonts.css" />
<link rel="stylesheet" href="${cssHref}" />
<base href="/design/" />
<style>
  html,body{ margin:0; background:#fff; }
  /* The export viewport is exactly w x h; the artboard scales to fill it. */
  #stage{ width:${w}px; height:${h}px; overflow:hidden; background:#fff; }
  #scaler{ width:${BASE_W}px; height:${BASE_H}px; transform-origin:top left; transform:scale(${scale.toFixed(6)}); }
  #solo > *{ width:${BASE_W}px !important; height:${BASE_H}px !important; }
</style></head>
<body>
${filters}
<div id="stage"><div id="scaler"><div id="solo"></div></div></div>
<script src="/vendor/react.development.js"><\/script>
<script src="/vendor/react-dom.development.js"><\/script>
<script src="/vendor/babel.min.js"><\/script>
<script src="/omelette-shim.js"><\/script>
<script src="/design/image-slot.js"><\/script>
${compScripts}
<script type="text/babel" data-presets="react">
  // Map board id -> a rendered element, mirroring the entry HTML's <App/> wiring.
  const C = window.Covers || {}, D = window.Dossier || {};
  function pickCovers(id){
    switch(id){
      case 'ill-front': return <C.IllustratedFront/>;
      case 'ill-bleed': return <C.IllustratedFrontBleed/>;
      case 'ill-back':  return <C.IllustratedBack/>;
      case 'f-list':    return <C.FrontStruckList/>;
      case 'f-chair':   return <C.FrontEmptyChair/>;
      case 'f-verdict': return <C.FrontVerdict/>;
      case 'cart-1':    return <C.CartoonCourt/>;
      case 'back':      return <C.BackCover/>;
      default:
        if (id && id.indexOf('ill-ch-')===0 && C.ART_CHAPTERS){
          const c = C.ART_CHAPTERS.find(x => 'ill-ch-'+x.n === id); if (c) return <C.IllustratedChapter c={c}/>;
        }
        return null;
    }
  }
  function pickDossier(id){
    switch(id){
      case 'f-case': return <D.FrontCaseFile/>;
      case 'f-def':  return <D.FrontDefendant/>;
      case 'f-wall': return <D.FrontEvidenceWall/>;
      case 'wrap-1': return <D.Wraparound/>;
      case 'wrap-print-1': return <D.WraparoundPrint/>;
      case 'b-sum':  return <D.BackSummary/>;
      case 'b-inv':  return <D.BackInventory/>;
      case 'b-find': return <D.BackFindings/>;
      case 'cast':   return <D.CastCard/>;
      case 'style':  return <D.StyleStrip/>;
      default:
        if (id && id.indexOf('part-')===0 && D.PARTS){ const p = D.PARTS.find(x => 'part-'+x.n === id); if (p) return <D.PartCover p={p}/>; }
        if (id && id.indexOf('ch-')===0 && D.CHAPTERS){ const c = D.CHAPTERS.find(x => 'ch-'+x.n === id); if (c) return <D.ChapterCard c={c}/>; }
        return null;
    }
  }
  const el = ${ed === 'dossier' ? 'pickDossier' : 'pickCovers'}(${JSON.stringify(board)});
  const root = ReactDOM.createRoot(document.getElementById('solo'));
  root.render(el || <div style={{padding:20,font:'16px sans-serif'}}>unknown board: ${board}</div>);
  // Signal readiness for the headless screenshotter once fonts + images settle.
  Promise.all([document.fonts ? document.fonts.ready : Promise.resolve()])
    .then(() => requestAnimationFrame(() => requestAnimationFrame(() => { window.__SOLO_READY = true; })));
<\/script>
</body></html>`;
}

const COVERS_FILTERS = `<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <filter id="scratch" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.016 0.022" numOctaves="3" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/></filter>
  <filter id="scratch2" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.011 0.014" numOctaves="3" seed="13" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="7" xChannelSelector="R" yChannelSelector="G"/></filter>
</defs></svg>`;

const DOSSIER_FILTERS = `<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <filter id="d-rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.016 0.022" numOctaves="3" seed="5" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="4" xChannelSelector="R" yChannelSelector="G"/></filter>
  <filter id="d-rough2" x="-8%" y="-8%" width="116%" height="116%"><feTurbulence type="fractalNoise" baseFrequency="0.011 0.015" numOctaves="3" seed="11" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="R" yChannelSelector="G"/></filter>
  <filter id="d-grunge"><feTurbulence type="fractalNoise" baseFrequency="0.16" numOctaves="2" seed="7" result="n"/><feColorMatrix in="n" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 -0.7 1.06" result="m"/><feComposite in="SourceGraphic" in2="m" operator="in"/></filter>
</defs></svg>`;
