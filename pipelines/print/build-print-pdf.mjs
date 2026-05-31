// build-print-pdf.mjs — render a 6×9 print-interior PDF for KDP paperback.
// Per-section render route gives true per-chapter running heads.
//
// Pipeline:
//   1. Read book/spine-v6.yml; build a flat SPINE array including
//      synthesized title page, optional dedication/epigraph, preface,
//      note-on-cases (front), TOC (synthesized), part dividers, all 13
//      chapters, and back matter.
//   2. Pass 1: render each section to print/out/sections/<NN>-<slug>.pdf
//      via Playwright page.pdf(). Capture page counts via pdfinfo.
//   3. Pass 2: build TOC from measured page counts; render TOC.
//   4. Concat all section PDFs in spine order with qpdf.
//   5. Post-process: overlay continuous page numbers + running heads
//      via print-pdf-finalize.py (pypdf + reportlab).
//
// Output: dist/no-one-did-it-interior.pdf

import { chromium } from 'playwright';
import yaml from 'js-yaml';
import { readFileSync, writeFileSync, mkdirSync, existsSync, rmSync } from 'node:fs';
import { join, dirname, resolve, relative } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { execFileSync } from 'node:child_process';
import { fontFaceCss } from './font-css.mjs';
import { I18N, formatChapter } from './i18n.mjs';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..', '..');
const BUILD_DIR = __dirname;
const OUT_DIR = resolve(BUILD_DIR, 'out');
const PROSE_DIR = resolve(OUT_DIR, 'prose');
const SECTIONS_DIR_HTML = resolve(OUT_DIR, 'sections');
const DIST_DIR = resolve(ROOT, 'dist');
const SECTIONS_DIR = resolve(DIST_DIR, 'print-sections');
const BOOK_DIR = resolve(ROOT, 'book');
const COVERS_DIR = resolve(BOOK_DIR, 'design', 'covers');

// ─────────────────────────────────────────────────────────────────────────
// Spine construction from book/spine-v6.yml
// ─────────────────────────────────────────────────────────────────────────

function loadSpine() {
  const yamlPath = resolve(BOOK_DIR, 'spine-v6.yml');
  const raw = readFileSync(yamlPath, 'utf8');
  const spineDoc = yaml.load(raw);
  const sections = [];

  // Title page (synthesized; pandoc-style title block)
  sections.push({ kind: 'title', slug: null, header: '' });

  // Front matter from spine-v6.yml
  for (const fm of spineDoc.front_matter || []) {
    const filePath = fm.file;  // e.g. "book/front-matter/preface.md"
    const m = filePath.match(/book\/([^/]+)\/(.+)\.md$/);
    if (!m) continue;
    const groupDir = m[1];     // "front-matter" or "back-matter"
    const slug = m[2].replace(/^\d+-/, '');
    // Map disk group → output prose group dir
    const proseGroup = groupDir; // build-prose writes to same group dir name
    const proseFile = join(PROSE_DIR, proseGroup, slug + '.html');
    if (!existsSync(proseFile)) {
      // Optional entries (dedication, epigraph) skip if file missing
      if (fm.optional) continue;
      throw new Error(`front-matter prose missing: ${proseFile}`);
    }
    // Skip optional files whose body is functionally empty (placeholder content)
    if (fm.optional && isFunctionallyEmpty(proseFile)) continue;
    sections.push({
      kind: 'front',
      slug,
      proseGroup,
      header: '',
    });
  }

  // Parts (each: divider + chapters)
  for (const part of spineDoc.parts || []) {
    // Part divider: transparent-background Dossier plate (book/design/covers/part-{1..4}.png),
    // placed INSET within the page margins (not full-bleed) so a no-bleed 6×9
    // interior never reports "image outside the margins" at KDP.
    const partNum = { I: 1, II: 2, III: 3, IV: 4 }[part.id];
    const partCoverPath = join(BOOK_DIR, 'design', 'covers', `part-${partNum}.png`);
    sections.push({
      kind: 'part',
      slug: `part-${part.id.toLowerCase()}`,
      partId: part.id,
      partTitle: part.title,
      partTagline: part.tagline,
      coverImage: existsSync(partCoverPath) ? partCoverPath : null,
      header: '',
    });
    let chapterNumWithinBook = chapterCountSoFar(spineDoc.parts, part.id);
    for (const entry of part.chapters) {
      chapterNumWithinBook += 1;
      // Spine accepts either a bare slug string (legacy) or an object with
      // `slug:` (+ optional `cover_image:`); pull the slug uniformly.
      const chapterSlug = typeof entry === 'string' ? entry : entry.slug;
      // Chapter file slug strips NN- prefix
      const slug = chapterSlug.replace(/^\d+-/, '');
      const chapterNum = parseInt(chapterSlug.match(/^(\d+)/)[1], 10);
      const proseFile = join(PROSE_DIR, 'chapters-v6', slug + '.html');
      if (!existsSync(proseFile)) {
        throw new Error(`chapter prose missing: ${proseFile}`);
      }
      // Chapter covers were dropped in the cover-removal pass; chapter
      // openers are now typographic (H1 chapter title + drop-cap first
      // paragraph). Part-divider full-bleed plates are still wired above.
      sections.push({
        kind: 'chapter',
        slug,
        chapterNum,
        proseGroup: 'chapters-v6',
        header: `${chapterNum} · ${chapterTitleFromHtml(proseFile)}`,
        coverImage: null,
      });
    }
  }

  // Back matter from spine-v6.yml
  for (const bm of spineDoc.back_matter || []) {
    const filePath = bm.file;
    const m = filePath.match(/book\/([^/]+)\/(.+)\.md$/);
    if (!m) continue;
    const groupDir = m[1];
    const slug = m[2].replace(/^\d+-/, '');
    const proseFile = join(PROSE_DIR, groupDir, slug + '.html');
    if (!existsSync(proseFile)) {
      if (bm.optional) continue;
      throw new Error(`back-matter prose missing: ${proseFile}`);
    }
    if (bm.optional && isFunctionallyEmpty(proseFile)) continue;
    const title = backMatterTitle(slug, proseFile);
    sections.push({
      kind: 'back',
      slug,
      proseGroup: groupDir,
      header: title,
    });
  }

  return sections;
}

function chapterCountSoFar(parts, currentId) {
  let n = 0;
  for (const p of parts) {
    if (p.id === currentId) break;
    n += (p.chapters || []).length;
  }
  return n;
}

// Return true if the prose HTML body contains only an HTML comment or
// whitespace — used to skip optional front-matter placeholders.
function isFunctionallyEmpty(htmlPath) {
  const txt = readFileSync(htmlPath, 'utf8');
  const m = txt.match(/<body[^>]*>([\s\S]*?)<\/body>/);
  if (!m) return true;
  const body = m[1].replace(/<!--[\s\S]*?-->/g, '').replace(/\s+/g, '');
  return body.length === 0;
}

// Extract title by preferring the body <h1> (always carries the reader-
// facing title including curly apostrophes) and only falling back to the
// HTML <title> element.
function chapterTitleFromHtml(htmlPath) {
  const txt = readFileSync(htmlPath, 'utf8');
  // Try H1 first — strip inline tags, decode common entities
  const h1 = txt.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);
  if (h1) {
    const text = h1[1].replace(/<[^>]+>/g, '').trim();
    return text.replace(/^Chapter\s+\d+\s*[—–-]\s*/i, '').trim();
  }
  const t = txt.match(/<title>([^<]+)<\/title>/);
  if (!t) return 'Untitled';
  return t[1].replace(/^Chapter\s+\d+\s*[—–-]\s*/i, '').trim();
}

function backMatterTitle(slug, htmlPath) {
  const txt = readFileSync(htmlPath, 'utf8');
  // Prefer H1 body title (correct casing, apostrophes); fall back to <title>
  const h1 = txt.match(/<h1[^>]*>([\s\S]*?)<\/h1>/);
  if (h1) {
    return h1[1].replace(/<[^>]+>/g, '').trim();
  }
  const t = txt.match(/<title>([^<]+)<\/title>/);
  if (t) return t[1].trim();
  return slug.replace(/-/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());
}

// ─────────────────────────────────────────────────────────────────────────
// HTML body extraction + light transforms
// ─────────────────────────────────────────────────────────────────────────

function extractBody(html) {
  const m = html.match(/<body[^>]*>([\s\S]*)<\/body>/);
  if (!m) throw new Error('no <body> found');
  return m[1];
}

function stripFirstH1(body) {
  return body.replace(/<h1[^>]*>[\s\S]*?<\/h1>\s*/, '');
}

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
                  .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// Print-only: append the URL inline after any external link whose link text
// doesn't already contain the URL. The EPUB carries the same prose through
// its own renderer and keeps links live; the print PDF needs the URL visible
// in text because clickable links are useless on paper.
function injectInlinePrintUrls(html) {
  const RX_ANCHOR = /<a\s+([^>]*?)href\s*=\s*"([^"]+)"([^>]*)>([\s\S]*?)<\/a>/gi;
  return html.replace(RX_ANCHOR, (match, before, href, after, text) => {
    const textPlain = text.replace(/<[^>]+>/g, '');
    let displayUrl = null;
    const httpMatch = href.match(/^https?:\/\/(.+)$/);
    if (httpMatch) {
      const host = httpMatch[1];
      const hostOnly = host.split('/')[0];
      const inText = textPlain.includes(host) || textPlain.includes(hostOnly + '/') || textPlain.includes(href);
      if (!inText) displayUrl = host;
    } else if (href.startsWith('mailto:')) {
      const addr = href.slice(7);
      if (!textPlain.includes(addr)) displayUrl = addr;
    }
    if (!displayUrl) return match;
    const suffix = `<span class="print-url"> (${escapeHtml(displayUrl)})</span>`;
    return `<a ${before}href="${href}"${after}>${text}</a>${suffix}`;
  });
}

// ─────────────────────────────────────────────────────────────────────────
// Print CSS
// ─────────────────────────────────────────────────────────────────────────

function printCss() {
  return `
${fontFaceCss('../../fonts/')}

@page {
  size: 6in 9in;
  margin: 0.85in 0.5in 0.75in 0.625in;
}
@page :left  { margin-left: 0.5in;   margin-right: 0.625in; }
@page :right { margin-left: 0.625in; margin-right: 0.5in; }

* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0;
  font-family: 'EB Garamond', 'Times New Roman', serif;
  font-size: 11pt; line-height: 1.4;
  color: #111; background: white;
}
body {
  text-align: justify;
  hyphens: auto; -webkit-hyphens: auto;
  orphans: 3; widows: 3;
}
/* References + Selected Bibliography: left-align (ragged right). Long
 * citations + URLs justify into rivers and 2-3-word lines on a narrow
 * 6x9 column; ragged right reads cleanly for reference lists. */
.back-references, .back-references p, .back-references li,
.back-bibliography, .back-bibliography p, .back-bibliography li {
  text-align: left;
  hyphens: none; -webkit-hyphens: none;
}

h1, h2, h3, h4 {
  font-family: 'EB Garamond', serif; font-weight: 500;
  page-break-after: avoid; break-after: avoid;
  page-break-inside: avoid; break-inside: avoid;
}
h1 { font-size: 18pt; margin: 0 0 0.8em 0; }
h2 { font-size: 13pt; margin: 2.4em 0 0.4em 0; }
h3 { font-size: 11pt; font-style: italic; font-weight: 500; margin: 1.6em 0 0.3em 0; }
h4 { font-size: 11pt; font-weight: 600; margin: 1.1em 0 0.25em 0; }

p { margin: 0 0 0.5em 0; text-indent: 1.2em; }
p:first-of-type, h1+p, h2+p, h3+p, blockquote+p, ul+p, ol+p, pre+p, hr+p { text-indent: 0; }

blockquote { margin: 1em 1.5em; font-style: italic; font-size: 10.5pt; }
blockquote p { margin-bottom: 0.4em; text-indent: 0; }

/* Figure embeds — chapter diagrams (pre-rotated CCW; reader turns the book
 * clockwise to read). figure-embed div wrapper carries the page-break rule;
 * figcaption uses pandoc's auto-extraction from the image alt text.
 *
 * CRITICAL: max-height on the image is the only thing that stops figures
 * splitting across pages. break-inside: avoid is a hint and is ignored if
 * the content is taller than the page. The 1056×2456 rotated portraits
 * would scale to ~12in tall at max-width 100% on a 4.875in column without
 * this cap. Page content area is ~7.4in (9in trim − 0.85 top − 0.75 bottom);
 * leaving ~0.7in for figcaption + figure margins, image cap is 6.5in. */
.figure-embed, figure {
  text-align: center;
  margin: 1em 0;
  page-break-inside: avoid; break-inside: avoid-page;
}
.figure-embed figure { margin: 0; }
.figure-embed img, figure img {
  max-width: 100%;
  max-height: 6.5in;
  height: auto;
  display: block;
  margin: 0 auto;
}
figcaption {
  font-family: 'EB Garamond', serif;
  font-size: 9.5pt;
  font-style: italic;
  color: #444;
  margin: 0.4em auto 0 auto;
  max-width: 32em;
  text-align: center;
  text-indent: 0;
}
ul, ol { margin: 0.8em 0 0.8em 1.5em; padding: 0; }
li { margin: 0.3em 0; }
li > p { margin-bottom: 0.3em; text-indent: 0; }
hr { border: none; border-top: 1px solid #888; margin: 1.4em auto; width: 25%; }
code, pre, kbd, samp, tt { font-family: 'JetBrains Mono', monospace; font-size: 0.85em; }
pre { white-space: pre-wrap; margin: 1em 0; font-size: 9.5pt; line-height: 1.35; }
em, i { font-style: italic; }
strong, b { font-weight: 600; }

/* Footnotes (marked-footnote output) */
.footnote-ref { font-size: 0.75em; vertical-align: super; }
.footnotes, section.footnotes, [data-footnotes] {
  margin-top: 2em;
  border-top: 1px solid #888;
  padding-top: 0.6em;
  font-size: 9pt;
  line-height: 1.35;
}
.footnotes ol, section.footnotes ol { padding-left: 1.4em; }
.footnotes li, section.footnotes li { margin-bottom: 0.25em; }
.footnotes p, section.footnotes p { text-indent: 0; margin: 0; }

/* Pandoc-style markdown footnotes */
sup a, a.footnote-ref { font-size: 0.75em; vertical-align: super; text-decoration: none; }

/* Tables: vector pt-sized borders so they survive Chromium's pixel snapping */
table {
  border-collapse: collapse;
  margin: 1.2em 1pt 1.2em 0;
  width: calc(100% - 2pt);
  font-size: 10pt;
}
th, td { border: 0.5pt solid #888; padding: 0.25em 0.45em; text-align: left; vertical-align: top; }
th { background: #eee; font-weight: 500; }

.front-matter-page { break-before: page; }

/* ── Full-page cover/divider pages (chapter + part) ─────────────────
 * Image fills the @page content area (inside standard margins). Avoids
 * named @page rules that can leak into subsequent prose pages — a bug
 * we hit when @page :first { margin: 0 } cleared margins on the first
 * page of every rendered section, and named cover-page state stuck on
 * subsequent prose pages. Image-within-margins reads as traditional
 * book art-page convention anyway. */
.part-divider-page img {
  max-width: 100%;
  max-height: 7in;          /* inset within the content area; never full-bleed */
  height: auto;
  display: block;
  margin: 0 auto;
  object-fit: contain;
}

/* ── Copyright page ────────────────────────────────────────────────── */
.copyright-page {
  font-size: 9.5pt;
  line-height: 1.45;
  text-align: left;
  max-width: 26em;
  margin: 1.5in auto 0;
}
.copyright-page p {
  margin: 0 0 0.7em 0;
  text-indent: 0;
}
.copyright-page p:first-of-type {
  font-size: 11pt;
  font-style: italic;
  margin-bottom: 1.5em;
}

/* ── Dedication ────────────────────────────────────────────────────── */
.dedication {
  margin: 3.5in auto 0;
  max-width: 22em;
  text-align: center;
  font-style: italic;
  font-size: 12pt;
  line-height: 1.5;
}
.dedication p { text-indent: 0; margin: 0; }

/* ── Book epigraph ─────────────────────────────────────────────────── */
.book-epigraph {
  margin: 2.5in auto 0;
  max-width: 26em;
  text-align: left;
}
.book-epigraph blockquote {
  margin: 0;
  font-style: italic;
  font-size: 11.5pt;
  line-height: 1.5;
  border: none;
}
.book-epigraph blockquote p { text-indent: 0; margin: 0 0 0.7em 0; }
.book-epigraph blockquote p:last-child {
  font-style: normal;
  font-size: 10pt;
  text-align: right;
  margin-top: 1em;
  color: #555;
}

/* ── Title page ────────────────────────────────────────────────────── */
.title-page {
  text-align: center; padding-top: 1.5in;
}
.title-page h1 { font-size: 30pt; font-weight: 400; letter-spacing: 0.02em; margin: 0 0 0.5em 0; }
.title-page .subtitle { font-size: 14pt; font-style: italic; font-weight: 400; color: #555; margin: 0 0 2em 0; max-width: 24em; margin-left: auto; margin-right: auto; line-height: 1.35; }
.title-page .author { font-size: 16pt; margin-top: 3em; }
.title-page .publisher { font-size: 11pt; margin-top: 5em; color: #555; }

/* ── Part divider ──────────────────────────────────────────────────── */
.part-divider-page {
  break-before: page;
  break-after: page;
  height: 7.4in;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
.part-divider-page .part-roman {
  font-family: 'EB Garamond', serif;
  font-size: 11pt;
  font-style: italic;
  letter-spacing: 0.3em;
  color: #777;
  margin-bottom: 1.5em;
  text-transform: uppercase;
}
.part-divider-page .part-title {
  font-family: 'EB Garamond', serif;
  font-size: 26pt;
  font-weight: 400;
  margin: 0 0 1.2em 0;
}
.part-divider-page .part-tagline {
  font-family: 'EB Garamond', serif;
  font-size: 12pt;
  font-style: italic;
  color: #555;
  max-width: 20em;
  line-height: 1.4;
}

/* ── Chapter start ─────────────────────────────────────────────────── */
.chapter-start { break-before: page; padding-top: 0.8in; }
.chapter-start .chapter-num {
  font-family: 'EB Garamond', serif;
  font-size: 10pt;
  font-style: italic;
  letter-spacing: 0.3em;
  color: #777;
  text-align: center;
  margin: 0 0 1.2em 0;
  text-transform: uppercase;
}
.chapter-start h1.chapter-title {
  font-family: 'EB Garamond', serif;
  font-size: 22pt;
  font-weight: 400;
  text-align: center;
  margin: 0 auto 2em auto;
  max-width: 20em;
  line-height: 1.2;
}
/* Drop cap on the first paragraph of chapter bodies (not back matter). */
.chapter-start:not(.back-matter) > .prose-body > p:first-of-type { text-indent: 0; }
.chapter-start:not(.back-matter) > .prose-body > p:first-of-type::first-letter {
  font-size: 2.6em; float: left; line-height: 0.9;
  margin: 0.05em 0.1em 0 0; font-weight: 500;
}

p, li, blockquote, table { break-inside: avoid-page; }

a, a:link, a:visited { color: inherit; text-decoration: none; }

.print-url {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78em;
  color: #555;
  white-space: nowrap;
}

/* ── Table of contents ─────────────────────────────────────────────── */
.toc-page {
  break-before: page;
  padding-top: 1in;
}
.toc-page h1 {
  font-size: 22pt;
  font-weight: 400;
  text-align: center;
  margin: 0 0 1.5em 0;
}
.toc-list {
  list-style: none;
  margin: 0;
  padding: 0;
}
.toc-list li {
  display: flex;
  align-items: baseline;
  padding: 0.35em 0;
  font-size: 11pt;
  text-indent: 0;
  break-inside: avoid;
}
.toc-list li.toc-section-break { padding-top: 0.9em; }
.toc-list li.toc-part {
  font-style: italic;
  color: #555;
  letter-spacing: 0.05em;
  padding-top: 1.2em;
}
.toc-title { flex: 0 1 auto; white-space: nowrap; overflow: hidden; }
.toc-dots {
  flex: 1 1 auto;
  border-bottom: 0.5pt dotted #999;
  margin: 0 0.5em;
  transform: translateY(-0.35em);
  min-width: 1em;
}
.toc-pn {
  flex: 0 0 auto;
  font-variant-numeric: tabular-nums;
  min-width: 2.5em;
  text-align: right;
}
`;
}

// ─────────────────────────────────────────────────────────────────────────
// Section HTML synthesis (per kind)
// ─────────────────────────────────────────────────────────────────────────

function sectionHtml(entry) {
  let body = '';
  if (entry.kind === 'title') {
    body = `
      <section class="title-page">
        <h1>${escapeHtml(I18N.title)}</h1>
        ${I18N.subtitle ? `<div class="subtitle">${escapeHtml(I18N.subtitle)}</div>` : ''}
        <div class="author">${escapeHtml(I18N.author)}</div>
        ${I18N.publisher ? `<div class="publisher">${escapeHtml(I18N.publisher)}</div>` : ''}
      </section>
    `;
  } else if (entry.kind === 'front') {
    const html = readFileSync(join(PROSE_DIR, entry.proseGroup, entry.slug + '.html'), 'utf8');
    body = `<section class="front-matter-page">${extractBody(html)}</section>`;
  } else if (entry.kind === 'part') {
    if (entry.coverImage) {
      body = `
        <section class="part-divider-page">
          <img src="${pathToFileURL(entry.coverImage).href}" alt="Part ${escapeHtml(entry.partId)}" />
        </section>
      `;
    } else {
      // Fallback: typographic divider (used when print-cover JPG is missing)
      body = `
        <section class="part-divider-page typographic">
          <div class="part-roman">Part ${escapeHtml(entry.partId)}</div>
          <h1 class="part-title">${escapeHtml(entry.partTitle)}</h1>
          ${entry.partTagline ? `<div class="part-tagline">${escapeHtml(entry.partTagline)}</div>` : ''}
        </section>
      `;
    }
  } else if (entry.kind === 'chapter') {
    const proseHtml = readFileSync(join(PROSE_DIR, entry.proseGroup, entry.slug + '.html'), 'utf8');
    const proseBody = stripFirstH1(extractBody(proseHtml));
    // Typographic chapter opener: eyebrow + title + drop-cap prose.
    const chapterTitle = chapterTitleFromHtml(join(PROSE_DIR, entry.proseGroup, entry.slug + '.html'));
    body = `
        <section class="chapter-start">
          <div class="chapter-num">${escapeHtml(formatChapter(entry.chapterNum))}</div>
          <h1 class="chapter-title">${escapeHtml(chapterTitle)}</h1>
          <div class="prose-body">${proseBody}</div>
        </section>
      `;
  } else if (entry.kind === 'back') {
    const html = readFileSync(join(PROSE_DIR, entry.proseGroup, entry.slug + '.html'), 'utf8');
    body = `<section class="chapter-start back-matter back-${entry.slug}">${extractBody(html)}</section>`;
  } else if (entry.kind === 'toc') {
    body = entry.tocBody;
  }

  body = injectInlinePrintUrls(body);

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>${escapeHtml(entry.header || I18N.title)}</title>
<style>${printCss()}</style>
</head>
<body>
${body}
</body>
</html>`;
}

// ─────────────────────────────────────────────────────────────────────────
// TOC construction
// ─────────────────────────────────────────────────────────────────────────

function buildTocEntries(spine, pageCounts) {
  // The TOC's printed page number for each section must match the printed
  // folio the reader will actually see on that page. Front matter, part
  // dividers, and chapter cover pages are all UNNUMBERED — they take up
  // physical pages but consume no printed page numbers. Only chapter prose
  // pages and back-matter pages carry printed folios (continuous from 1).
  //
  // Bug fix: the previous implementation accumulated `pageCounts[i]`
  // (physical pages) regardless of whether those pages were numbered,
  // pushing every TOC entry forward by the count of unnumbered cover/
  // divider pages that came before it. With 13 chapter covers + 4 part
  // dividers, chapter entries were off by ~17 by the back of the book.
  const entries = [];
  let printedPagesSoFar = 0;  // count of pages with a printed folio
  let prevKind = null;
  for (let i = 0; i < spine.length; i++) {
    const entry = spine[i];
    if (entry.kind === 'title' || entry.kind === 'front' || entry.kind === 'toc') {
      continue;
    }
    let title;
    let liClass = '';
    if (entry.kind === 'part') {
      title = `Part ${entry.partId} · ${entry.partTitle}`;
      liClass = 'toc-part';
    } else {
      title = entry.header;
    }
    const isMajor = prevKind && prevKind !== entry.kind && entry.kind !== 'chapter';
    // Each part/chapter/back entry begins at the next printed page (the
    // unnumbered pages that come first — divider, cover — don't advance
    // the printed counter).
    entries.push({
      title,
      page: printedPagesSoFar + 1,
      isMajor,
      liClass,
    });
    // Now accumulate the numbered pages contributed by THIS section.
    let numberedInSection = 0;
    if (entry.kind === 'chapter') {
      // Chapter section = 1 cover (unnumbered) + (N-1) prose (numbered) when a
      // cover image is present; full N pages numbered when the chapter falls
      // back to typographic-only.
      numberedInSection = entry.coverImage ? Math.max(0, pageCounts[i] - 1) : pageCounts[i];
    } else if (entry.kind === 'back') {
      numberedInSection = pageCounts[i];
    }
    // 'part' contributes 0 numbered pages (divider is always unnumbered).
    printedPagesSoFar += numberedInSection;
    prevKind = entry.kind;
  }
  return entries;
}

function tocHtml(entries) {
  const li = (e) => {
    const cls = [e.liClass, e.isMajor ? 'toc-section-break' : ''].filter(Boolean).join(' ');
    return `<li${cls ? ` class="${cls}"` : ''}><span class="toc-title">${escapeHtml(e.title)}</span><span class="toc-dots"></span><span class="toc-pn">${e.page}</span></li>`;
  };
  return `
    <section class="toc-page">
      <h1>${escapeHtml(I18N.headings.contents || 'Contents')}</h1>
      <ul class="toc-list">
        ${entries.map(li).join('\n        ')}
      </ul>
    </section>
  `;
}

// ─────────────────────────────────────────────────────────────────────────
// Per-section render
// ─────────────────────────────────────────────────────────────────────────

async function renderSection(page, entry, idx) {
  const sectionId = `${String(idx).padStart(2, '0')}-${entry.slug || entry.kind}`;
  const pdfPath = join(SECTIONS_DIR, sectionId + '.pdf');

  // Part dividers now render through the default path below — the
  // transparent plate is placed inset within the page margins, not
  // full-bleed, so KDP's no-bleed margin check passes.

  // Default: single HTML → single PDF (title, front matter, part divider,
  // chapter, back matter, toc).
  const htmlPath = join(SECTIONS_DIR_HTML, sectionId + '.html');
  writeFileSync(htmlPath, sectionHtml(entry));
  await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'networkidle' });
  await page.waitForTimeout(400);
  await page.pdf({
    path: pdfPath, width: '6in', height: '9in',
    printBackground: true, preferCSSPageSize: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });
  return pdfPath;
}

// ─────────────────────────────────────────────────────────────────────────
// Main
// ─────────────────────────────────────────────────────────────────────────

async function main() {
  if (!existsSync(DIST_DIR)) mkdirSync(DIST_DIR, { recursive: true });
  if (existsSync(SECTIONS_DIR)) rmSync(SECTIONS_DIR, { recursive: true, force: true });
  mkdirSync(SECTIONS_DIR, { recursive: true });
  mkdirSync(SECTIONS_DIR_HTML, { recursive: true });

  const SPINE = loadSpine();
  console.log(`Building print interior PDF…`);
  console.log(`  Spine: ${SPINE.length} sections (TOC injected after first pass)`);

  console.log(`  Launching Chromium…`);
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: 1200, height: 1800 },
    deviceScaleFactor: 1,
  });
  const page = await ctx.newPage();

  // Pass 1: render every section, collect page counts.
  console.log(`\n  Pass 1: render each section`);
  const sectionPdfs = new Array(SPINE.length);
  const pageCounts = new Array(SPINE.length);
  for (let i = 0; i < SPINE.length; i++) {
    const entry = SPINE[i];
    const sectionId = `${String(i).padStart(2, '0')}-${entry.slug || entry.kind}`;
    process.stdout.write(`    [${i + 1}/${SPINE.length}] ${sectionId}… `);
    const pdfPath = await renderSection(page, entry, i);
    sectionPdfs[i] = pdfPath;
    const info = execFileSync('pdfinfo', [pdfPath]).toString();
    pageCounts[i] = parseInt(info.match(/Pages:\s*(\d+)/)[1], 10);
    console.log(`done (${pageCounts[i]}pp)`);
  }

  // Pass 2: build and render the TOC.
  console.log(`\n  Pass 2: build & render TOC`);
  const tocEntries = buildTocEntries(SPINE, pageCounts);
  const tocEntry = {
    kind: 'toc',
    slug: 'toc',
    header: '',
    tocBody: tocHtml(tocEntries),
  };
  const tocId = '99-toc';
  const tocHtmlPath = join(SECTIONS_DIR_HTML, tocId + '.html');
  const tocPdfPath = join(SECTIONS_DIR, tocId + '.pdf');
  writeFileSync(tocHtmlPath, sectionHtml(tocEntry));
  await page.goto(pathToFileURL(tocHtmlPath).href, { waitUntil: 'networkidle' });
  await page.waitForTimeout(400);
  await page.pdf({
    path: tocPdfPath,
    width: '6in', height: '9in',
    printBackground: true, preferCSSPageSize: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });
  const tocInfo = execFileSync('pdfinfo', [tocPdfPath]).toString();
  const tocPages = parseInt(tocInfo.match(/Pages:\s*(\d+)/)[1], 10);
  console.log(`    TOC rendered: ${tocPages}pp, ${tocEntries.length} entries`);

  await browser.close();

  // Insert TOC right after the title page, before copyright. This matches
  // the canonical reading order in book/spine-v6.yml (cover → title →
  // contents → copyright → dedication → epigraph → preface → ...).
  let insertAt = 0;
  for (let i = 0; i < SPINE.length; i++) {
    if (SPINE[i].kind === 'title') {
      insertAt = i + 1;
      break;
    }
  }
  const concatList = [
    ...sectionPdfs.slice(0, insertAt),
    tocPdfPath,
    ...sectionPdfs.slice(insertAt),
  ];

  // Concatenate with qpdf
  const concatPath = join(DIST_DIR, I18N.pdf_filename.replace(/\.pdf$/, '-unnumbered.pdf'));
  console.log(`\n  Concatenating ${concatList.length} sections with qpdf…`);
  execFileSync('qpdf', ['--empty', '--pages', ...concatList, '--', concatPath]);

  // Build the spine JSON for the Python finalizer
  const spineForPython = [];
  for (let i = 0; i < SPINE.length; i++) {
    if (i === insertAt) {
      spineForPython.push({
        idx: spineForPython.length,
        kind: 'front',  // TOC counts as front matter (unnumbered)
        slug: 'toc',
        header: '',
        pdf: tocId + '.pdf',
      });
    }
    const e = SPINE[i];
    // Preserve 'part' kind for the finalizer; finalizer treats part dividers
    // as unnumbered, headerless pages (like front matter for numbering).
    spineForPython.push({
      idx: spineForPython.length,
      kind: e.kind,
      slug: e.slug || e.kind,
      header: e.header || '',
      pdf: `${String(i).padStart(2, '0')}-${e.slug || e.kind}.pdf`,
    });
  }
  if (insertAt === SPINE.length) {
    spineForPython.push({
      idx: spineForPython.length,
      kind: 'front',
      slug: 'toc',
      header: '',
      pdf: tocId + '.pdf',
    });
  }
  const spineJsonPath = join(SECTIONS_DIR, '_spine.json');
  writeFileSync(spineJsonPath, JSON.stringify(spineForPython, null, 2));

  // Hand off to Python for page-number overlay
  console.log(`  Adding page numbers via pypdf+reportlab…`);
  const finalPath = join(DIST_DIR, I18N.pdf_filename);
  const venvPython = join(ROOT, '.venv', 'bin', 'python');
  execFileSync(venvPython, [
    join(BUILD_DIR, 'print-pdf-finalize.py'),
    '--input', concatPath,
    '--output', finalPath,
    '--spine', spineJsonPath,
  ], { stdio: 'inherit' });

  let pageCount = null;
  try {
    const out = execFileSync('pdfinfo', [finalPath]).toString();
    const m = out.match(/Pages:\s*(\d+)/);
    if (m) pageCount = parseInt(m[1], 10);
  } catch (_) { /* skip */ }

  const stat = (await import('node:fs')).statSync(finalPath);
  console.log(`\n  ✓ PDF: ${finalPath}`);
  console.log(`    Size:  ${(stat.size / 1024 / 1024).toFixed(2)} MB`);
  if (pageCount) console.log(`    Pages: ${pageCount}`);

  rmSync(concatPath);

  console.log(`\nNext: node build-cover.js --pages ${pageCount || '<N>'}  (or run cover build directly)`);
}

main().catch(e => {
  console.error('FAIL:', e);
  process.exit(1);
});
