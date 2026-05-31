// build-prose.mjs — convert each markdown source file under
// book/{front-matter,chapters-v6,back-matter}/ into a print-ready HTML
// fragment via pandoc. Reuses the same converter the EPUB build uses
// (pipelines/epub/build_kdp_epub.py), so pandoc-specific syntax in the source
// (::: {.copyright-page} fenced divs, [^N] footnotes, smart typography,
// Chicago citation conventions) is handled correctly.
//
// Output: print/out/prose/<group>/<slug>.html — each file an <html><body>
// document containing the converted prose, ready for embedding in the
// section template by build-print-pdf.mjs.

import { spawnSync } from 'node:child_process';
import { readFile, writeFile, readdir, mkdir, rm } from 'node:fs/promises';
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, resolve, basename } from 'node:path';
import { I18N } from './i18n.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..', '..');
const BOOK_DIR = resolve(ROOT, 'book');
const OUT_DIR = resolve(__dirname, 'out', 'prose');
const STRIP_INLINE_STYLES_LUA = resolve(ROOT, 'pipelines', 'epub', 'strip_inline_styles.lua');

const LANG = I18N.lang;

// Group definitions for RL:
//   front-matter: copyright, [dedication], [book-epigraph], preface
//   chapters-v6:  the 13 numbered chapters
//   back-matter:  references, bibliography, note-on-sources-and-method,
//                 cases-at-a-glance, cases-timeline, acronyms-and-institutions,
//                 about-the-author, note-from-the-author, note-on-cases
const GROUPS = [
  { id: 'front-matter', dir: 'front-matter', skip: [] },
  { id: 'chapters-v6',  dir: 'chapters-v6',  skip: [] },
  { id: 'back-matter',  dir: 'back-matter',  skip: ['refs-index'] },
];

// Strip leading NN- prefix (e.g. 01-the-altar-moves.md → the-altar-moves)
function slugify(name) {
  return name.replace(/^\d+-/, '').replace(/\.md$/, '');
}

// Strip YAML frontmatter from a markdown file. Pandoc would handle this
// natively via --metadata-file, but stripping up front keeps the input
// minimal and avoids producing a leading <h1> from the title metadata.
function stripFrontmatter(md) {
  const m = md.match(/^---\r?\n[\s\S]*?\r?\n---\r?\n/);
  if (!m) return md;
  return md.slice(m[0].length);
}

// Strip the per-chapter trailing "## References" section. Each chapter
// markdown carries [^N]: footnote definitions for standalone rendering;
// when concatenated for the published manuscript the assembly script
// strips them in favor of the consolidated `book/back-matter/references.md`.
// For the print build (per-chapter PDF) we use the same back-of-book
// references section, so strip the per-chapter one to avoid an empty
// "References" heading at chapter end and orphan footnote definitions.
function stripChapterReferences(md) {
  // Match the standalone "## References" heading at the end of the chapter,
  // through end of file. The H2 may have any case; following content is
  // typically an HTML comment + [^N]: lines.
  return md.replace(/\n##\s+References\s*\n[\s\S]*$/i, '\n');
}

// Extract the title from frontmatter (if present) for use in the HTML
// <title> element. Handles quoted (title: "X" / title: 'X') and unquoted
// (title: X with apostrophes inside) forms. Falls back to the slug.
function extractTitleFromFrontmatter(md, fallback) {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n/);
  if (!m) return fallback;
  // Try double-quoted, then single-quoted, then unquoted-to-end-of-line.
  let titleMatch = m[1].match(/^title:\s*"([^"]+)"\s*$/m);
  if (!titleMatch) titleMatch = m[1].match(/^title:\s*'((?:[^']|\\')+)'\s*$/m);
  if (!titleMatch) titleMatch = m[1].match(/^title:\s*(.+?)\s*$/m);
  return titleMatch ? titleMatch[1].trim() : fallback;
}

// Extract the title from the first H1 in the body. More reliable than
// frontmatter for back-matter files that don't carry frontmatter.
function extractTitleFromH1(md, fallback) {
  const m = md.match(/^#\s+(.+?)\s*$/m);
  return m ? m[1].trim() : fallback;
}

function escapeXml(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' }[c]));
}

function htmlShell({ title, body }) {
  return `<!doctype html>
<html lang="${LANG}">
<head>
<meta charset="UTF-8">
<title>${escapeXml(title)}</title>
</head>
<body>
${body}
</body>
</html>
`;
}

// Pandoc: markdown → HTML5 fragment. Reuses the same Lua filter the EPUB
// build uses (strip_inline_styles.lua) for consistency. Pandoc's default
// markdown reader includes fenced_divs, footnotes, pipe_tables, and
// raw_html — everything the project's prose uses.
function pandocConvert(mdContent) {
  const args = [
    '--from', 'markdown',
    '--to', 'html5',
    '--no-highlight',
    '--lua-filter', STRIP_INLINE_STYLES_LUA,
    '--wrap=none',
    // Allow chapter-source ![](book/evidence/diagrams/proofs/…) repo-relative
    // paths to resolve against the project root.
    '--resource-path', ROOT,
  ];
  const result = spawnSync('pandoc', args, {
    input: mdContent,
    encoding: 'utf8',
  });
  if (result.status !== 0) {
    throw new Error(`pandoc failed (exit ${result.status}): ${result.stderr}`);
  }
  return absolutizeImagePaths(result.stdout);
}

// Rewrite <img src="rel/path"> → <img src="file:///abs/rel/path">. Pandoc emits
// image paths verbatim in HTML; Playwright loads the section HTML from
// out/sections/, so any non-absolute src 404s. Skips http://, https://,
// data:, and file:// (already absolute).
function absolutizeImagePaths(html) {
  return html.replace(
    /<img\b([^>]*?)\bsrc="([^"]+)"/g,
    (full, attrs, src) => {
      if (/^(https?:|data:|file:)/i.test(src) || src.startsWith('/')) return full;
      const abs = resolve(ROOT, src);
      return `<img${attrs} src="file://${abs}"`;
    }
  );
}

async function ensureCleanDir(d) {
  if (existsSync(d)) await rm(d, { recursive: true, force: true });
  await mkdir(d, { recursive: true });
}

async function processGroup(group) {
  const srcDir = resolve(BOOK_DIR, group.dir);
  const outDir = resolve(OUT_DIR, group.id);
  await mkdir(outDir, { recursive: true });

  if (!existsSync(srcDir)) {
    console.log(`  (skipping ${group.id}: ${srcDir} does not exist)`);
    return [];
  }

  const files = (await readdir(srcDir))
    .filter((f) => f.endsWith('.md'))
    .filter((f) => !group.skip.includes(slugify(f)))
    .sort();

  const records = [];
  for (const file of files) {
    const slug = slugify(file);
    const rawMd = await readFile(resolve(srcDir, file), 'utf8');
    let md = stripFrontmatter(rawMd);
    if (group.id === 'chapters-v6') md = stripChapterReferences(md);
    // Print-edition ISBN substitution: the source copyright.md carries the
    // EPUB ISBN; the print PDF must carry the paperback ISBN. Substitution
    // is contained to this build (the source markdown is unchanged) so the
    // EPUB build continues to ship the EPUB ISBN.
    if (slug === 'copyright' && I18N.isbn && I18N.paperback_isbn && I18N.isbn !== I18N.paperback_isbn) {
      md = md.replace(new RegExp(I18N.isbn.replace(/-/g, '-'), 'g'), I18N.paperback_isbn);
    }
    // Prefer frontmatter title; fall back to H1 in body (for back-matter
    // files with no frontmatter); finally fall back to slug.
    const title = extractTitleFromFrontmatter(rawMd, null)
                  || extractTitleFromH1(md, slug);
    const bodyHtml = pandocConvert(md);
    const out = htmlShell({ title, body: bodyHtml });
    const outPath = join(outDir, `${slug}.html`);
    await writeFile(outPath, out, 'utf8');
    records.push({ group: group.id, slug, title, file });
    console.log(`  + ${group.id}/${slug}`);
  }
  return records;
}

async function main() {
  console.log(`[lang] ${LANG}`);
  console.log(`[converter] pandoc ${spawnSync('pandoc', ['--version']).stdout.toString().split('\n')[0]}`);
  await ensureCleanDir(OUT_DIR);
  const all = [];
  for (const g of GROUPS) {
    console.log(`\n[${g.id}]`);
    all.push(...await processGroup(g));
  }
  await writeFile(join(OUT_DIR, 'index.json'), JSON.stringify(all, null, 2), 'utf8');
  console.log(`\n[done] ${all.length} prose pages → ${OUT_DIR}`);
}

main().catch((e) => { console.error(e); process.exit(1); });
