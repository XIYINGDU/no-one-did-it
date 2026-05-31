#!/usr/bin/env node
/* ============================================================
   export.mjs — render one design-studio artboard to a production asset.

   Drives the solo route (/solo) through headless Chrome, then (for covers/JPEG)
   converts to sRGB JPEG via ImageMagick. Self-contained: reuses a running
   studio server if one answers on the port, else starts a temporary one and
   shuts it down after.

   Examples:
     node design-studio/export.mjs --cover
         # ill-front (Illustrated/Cartoon) at 1600x2560 sRGB JPEG -> book/design/epub/cover.jpg
     node design-studio/export.mjs --board ill-bleed --cover
         # full-bleed layout as the cover instead
     node design-studio/export.mjs --board f-case --ed dossier --cover
         # the Dossier "Case File" front as the cover
     node design-studio/export.mjs --board cart-1 --w 1600 --jpeg
         # any board to out/<board>-WxH.jpg (PNG without --jpeg)

   Flags:
     --cover            shortcut: bh=960 (1.6:1 logical box), w=1600, JPEG,
                        out=book/design/epub/cover.jpg, default board ill-front
     --board <id>       DCArtboard id (see the entry HTMLs / studio labels)
     --ed covers|dossier   which edition the board lives in (default covers)
     --w <px>           target width (default 1600); height follows the box ratio
     --bw <px> --bh <px>   logical artboard box (default 600x925; cover uses 960 h)
     --out <path>       output path (overrides the default)
     --jpeg             convert the PNG to sRGB JPEG
     --port <n>         studio port (default 5180 / $PORT)
     --keep-png         keep the intermediate PNG next to a JPEG output
   ============================================================ */
import http from 'node:http';
import os from 'node:os';
import { spawn, spawnSync } from 'node:child_process';
import { mkdirSync, mkdtempSync, existsSync, statSync, copyFileSync, rmSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.dirname(fileURLToPath(import.meta.url));
const argv = process.argv.slice(2);
const has = (n) => argv.includes('--' + n);
const val = (n, d) => {
  const i = argv.indexOf('--' + n);
  if (i < 0) return d;
  const v = argv[i + 1];
  return v === undefined || v.startsWith('--') ? true : v;
};

const cover = has('cover');
const board = String(val('board', cover ? 'ill-front' : ''));
if (!board) {
  console.error('error: --board <id> is required (or use --cover). See header for examples.');
  process.exit(2);
}
const ed = val('ed', 'covers') === 'dossier' ? 'dossier' : 'covers';
const bw = Number(val('bw', 600));
const bh = Number(val('bh', cover ? 960 : 925));
const w = Number(val('w', 1600));
const h = Math.round((bh * w) / bw);
const port = Number(val('port', process.env.PORT || 5180));
const toJpeg = cover || has('jpeg');

const stem = `${board}-${w}x${h}`;
const pngTmp = path.join(ROOT, 'out', `${stem}.png`);
let finalOut;
const outArg = val('out', null);
if (typeof outArg === 'string') finalOut = path.resolve(process.cwd(), outArg);
else if (cover) finalOut = path.resolve(ROOT, '..', '..', 'book', 'design', 'epub', 'cover.jpg');
else finalOut = path.join(ROOT, 'out', `${stem}.${toJpeg ? 'jpg' : 'png'}`);

const CHROME = process.env.CHROME
  || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

function probe() {
  return new Promise((res) => {
    const r = http.get({ host: 'localhost', port, path: '/', timeout: 1000 }, (x) => { x.resume(); res(true); });
    r.on('error', () => res(false));
    r.on('timeout', () => { r.destroy(); res(false); });
  });
}
async function waitUp(ms) {
  const t = Date.now();
  while (Date.now() - t < ms) { if (await probe()) return true; await new Promise((r) => setTimeout(r, 200)); }
  return false;
}

function run(cmd, args) {
  const r = spawnSync(cmd, args, { stdio: 'inherit' });
  if (r.error) throw r.error;
  if (r.status !== 0) throw new Error(`${path.basename(cmd)} exited ${r.status}`);
}

// Chrome's --headless=new writes the --screenshot file but does NOT reliably
// self-exit, so we don't block on its exit: spawn it, wait until the output
// file appears and its size is stable (write finished), then kill it.
function screenshot(args, outFile, timeoutMs = 40000) {
  return new Promise((resolve, reject) => {
    const ch = spawn(CHROME, args, { stdio: 'ignore' });
    let settled = false;
    const finish = (err) => {
      if (settled) return; settled = true;
      clearInterval(iv);
      try { ch.kill('SIGKILL'); } catch {}
      err ? reject(err) : resolve();
    };
    ch.on('error', finish);
    const t0 = Date.now();
    let last = -1, stable = 0;
    const iv = setInterval(() => {
      let sz = -1; try { sz = statSync(outFile).size; } catch {}
      if (sz > 0 && sz === last) stable++; else stable = 0;
      last = sz;
      if (sz > 0 && stable >= 3) finish();                       // unchanged ~0.9s -> done
      else if (Date.now() - t0 > timeoutMs) finish(new Error('screenshot timed out'));
    }, 300);
  });
}

async function main() {
  mkdirSync(path.dirname(pngTmp), { recursive: true });
  mkdirSync(path.dirname(finalOut), { recursive: true });

  // Reuse a running studio, else start a temporary one.
  let child = null;
  if (!(await probe())) {
    console.log(`starting a temporary studio on :${port} …`);
    child = spawn(process.execPath, [path.join(ROOT, 'serve.mjs')],
      { env: { ...process.env, PORT: String(port) }, stdio: 'ignore', detached: false });
    if (!(await waitUp(8000))) { try { child.kill(); } catch {} throw new Error(`studio did not start on :${port}`); }
  } else {
    console.log(`reusing studio already running on :${port}`);
  }

  // A fresh, throwaway Chrome profile per run — avoids SingletonLock collisions
  // when the studio is open or another export is mid-flight.
  const profile = mkdtempSync(path.join(os.tmpdir(), 'noid-chrome-'));
  try {
    const url = `http://localhost:${port}/solo?board=${encodeURIComponent(board)}`
      + `&ed=${ed}&w=${w}&bw=${bw}&bh=${bh}`;
    if (!existsSync(CHROME)) throw new Error(`Chrome not found at ${CHROME} (set $CHROME)`);
    console.log(`rendering ${ed}/${board} @ ${w}x${h} …`);
    rmSync(pngTmp, { force: true });   // clear any stale capture so the poller sees the fresh write
    await screenshot([
      '--headless=new', '--disable-gpu', '--hide-scrollbars',
      '--force-device-scale-factor=1', `--window-size=${w},${h}`,
      `--user-data-dir=${profile}`,
      '--virtual-time-budget=15000', `--screenshot=${pngTmp}`, url,
    ], pngTmp);
    if (!existsSync(pngTmp)) throw new Error('screenshot was not produced');

    if (toJpeg) {
      // rule 16: JPEG, sRGB. -strip drops metadata; q92 keeps the painting clean.
      run('magick', [pngTmp, '-colorspace', 'sRGB', '-strip', '-quality', '92', finalOut]);
      if (!has('keep-png')) rmSync(pngTmp, { force: true });
    } else if (path.resolve(finalOut) !== path.resolve(pngTmp)) {
      copyFileSync(pngTmp, finalOut);
    }
  } finally {
    rmSync(profile, { recursive: true, force: true });
    if (child) { try { child.kill('SIGTERM'); } catch {} }
  }

  // Report final dimensions for a quick sanity check.
  const sips = spawnSync('sips', ['-g', 'pixelWidth', '-g', 'pixelHeight', '-g', 'format', finalOut], { encoding: 'utf8' });
  console.log(`\nOK -> ${finalOut}`);
  if (sips.stdout) console.log(sips.stdout.trim().split('\n').slice(1).map((s) => '  ' + s.trim()).join('\n'));
  if (cover) console.log('NEXT: python3 pipelines/epub/build_kdp_epub.py && python3 pipelines/epub/validate_kdp_epub.py');
}

main().catch((e) => { console.error('FAIL:', e.message); process.exit(1); });
