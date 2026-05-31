// font-css.mjs — generate @font-face CSS for the embedded fonts. Reads
// fonts/manifest.json and emits one @font-face block per (family, weight,
// style, subset) combination.
//
// `pathPrefix` is the relative path from the consuming HTML page to the
// fonts/ directory.

import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const MANIFEST_PATH = resolve(__dirname, 'fonts', 'manifest.json');

let CACHED;
function loadManifest() {
  if (!CACHED) CACHED = JSON.parse(readFileSync(MANIFEST_PATH, 'utf8'));
  return CACHED;
}

export function fontFaceCss(pathPrefix) {
  const records = loadManifest();
  return records.map((r) => {
    const lines = [
      `@font-face {`,
      `  font-family: '${r.family}';`,
      `  font-style: ${r.style};`,
      `  font-weight: ${r.weight};`,
      `  font-display: swap;`,
      `  src: url('${pathPrefix}${r.filename}') format('woff2');`,
    ];
    if (r.unicodeRange) lines.push(`  unicode-range: ${r.unicodeRange};`);
    lines.push(`}`);
    return lines.join('\n  ');
  }).join('\n  ');
}

export function fontManifest() { return loadManifest(); }
