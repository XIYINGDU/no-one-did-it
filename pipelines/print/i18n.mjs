// i18n.mjs — load print/i18n/en.json (the book's strings file).
// Single config loader so build scripts read title, subtitle, ISBN,
// publisher, headings from a single JSON file.

import { readFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const REQUIRED_TOP = ['lang', 'title', 'subtitle', 'author', 'headings'];
const REQUIRED_HEADINGS = ['contents', 'chapter_n'];

function validateI18n(i18n, path) {
  for (const k of REQUIRED_TOP) {
    if (i18n[k] === undefined) {
      throw new Error(`i18n schema error in ${path}: missing required top-level key '${k}'`);
    }
  }
  for (const k of REQUIRED_HEADINGS) {
    if (i18n.headings[k] === undefined) {
      throw new Error(`i18n schema error in ${path}: missing required headings.${k}`);
    }
  }
}

function loadI18n() {
  const path = resolve(__dirname, 'i18n', 'en.json');
  let i18n;
  try {
    i18n = JSON.parse(readFileSync(path, 'utf8'));
  } catch (e) {
    throw new Error(`i18n parse error in ${path}: ${e.message}`);
  }
  validateI18n(i18n, path);
  return i18n;
}

export const I18N = loadI18n();

export function formatChapter(n) {
  return I18N.headings.chapter_n.replace('%d', String(n));
}

export function formatPart(s) {
  return (I18N.headings.part_n || 'Part %s').replace('%s', String(s));
}
