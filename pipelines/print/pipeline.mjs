// pipeline.mjs — single-command print PDF build.
//
//   1. build-prose.mjs   — markdown → HTML per section
//   2. build-print-pdf.mjs — Playwright PDF render + qpdf concat + Python finalize
//   3. read page count from the final interior PDF
//   4. build-print-cover.py with the measured page count
//
// Each step inherits stdio so output streams live. Any non-zero exit aborts.

import { spawn, execFileSync } from 'node:child_process';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { I18N } from './i18n.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..', '..');
const VENV_PYTHON = resolve(ROOT, '.venv', 'bin', 'python');
const INTERIOR_PDF = resolve(ROOT, 'dist', I18N.pdf_filename);

function run(cmd, args, opts = {}) {
  return new Promise((res, rej) => {
    const child = spawn(cmd, args, { stdio: 'inherit', cwd: __dirname, ...opts });
    child.on('exit', (code) => code === 0 ? res() : rej(new Error(`${cmd} ${args.join(' ')} exited ${code}`)));
    child.on('error', rej);
  });
}

async function step(label, fn) {
  const start = Date.now();
  process.stdout.write(`\n\x1b[1m▸ ${label}\x1b[0m\n`);
  await fn();
  const ms = Date.now() - start;
  process.stdout.write(`  \x1b[2m(${(ms / 1000).toFixed(1)}s)\x1b[0m\n`);
}

async function main() {
  await step('build prose (markdown → HTML)', () => run('node', ['build-prose.mjs']));
  await step('build interior PDF (Playwright + qpdf + finalize)', () => run('node', ['build-print-pdf.mjs']));

  // Read final page count from the interior PDF for cover spine width.
  // FAIL LOUD: a silent fallback here would let the cover build use the
  // hardcoded 446-page default, producing a cover whose spine width does
  // NOT match the actual interior — KDP rejects at upload.
  let pages = null;
  try {
    const info = execFileSync('pdfinfo', [INTERIOR_PDF]).toString();
    const m = info.match(/Pages:\s*(\d+)/);
    if (m) pages = parseInt(m[1], 10);
  } catch (e) {
    console.error(`  ✗ could not read page count from ${INTERIOR_PDF}: ${e.message}`);
    console.error(`    refusing to build cover with stale page-count default; install pdfinfo (poppler) or pass --pages manually.`);
    process.exit(1);
  }
  if (!pages) {
    console.error(`  ✗ pdfinfo returned no Pages: field for ${INTERIOR_PDF}; refusing to build cover.`);
    process.exit(1);
  }

  await step(`build cover PDF (pages=${pages})`, () => {
    return run(VENV_PYTHON, ['build-print-cover.py', '--pages', String(pages)]);
  });

  console.log('\n\x1b[32m✓ print build complete\x1b[0m');
  console.log(`  Interior: dist/${I18N.pdf_filename}`);
  console.log(`  Cover:    dist/${I18N.cover_filename}`);
}

main().catch((e) => {
  console.error(`\n\x1b[31m✗ pipeline failed:\x1b[0m ${e.message}`);
  process.exit(1);
});
