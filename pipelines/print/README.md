# Print PDF build — KDP paperback

This directory builds the KDP paperback interior PDF + full-wrap cover PDF for *No One Did It* from the v6 canonical source (`book/chapters-v6/`, `book/front-matter/`, `book/back-matter/`).

The toolchain is borrowed from xiaolai's [The Half Second](https://github.com/xiaolai) print pipeline (Node + Playwright + qpdf + pypdf + reportlab + Pillow), adapted for this book's spine structure (parts + 13 chapters + Chicago endnote apparatus).

## Pipeline

```text
book/chapters-v6/*.md              ┐
book/front-matter/*.md             ├──▶ build-prose.mjs       ──▶ print/out/prose/*/*.html
book/back-matter/*.md              ┘                                       │
                                                                           ▼
book/spine-v6.yml                 ───▶ build-print-pdf.mjs   ──▶ dist/print-sections/*.pdf
                                                       (Playwright Chromium per-section render
                                                        → qpdf --pages concat
                                                        → print-pdf-finalize.py page-number overlay)
                                                                           │
                                                                           ▼
                                                              dist/no-one-did-it-interior.pdf
                                                                           │
                                                                           ▼
book/design/epub/cover.jpg + back-cover.jpg ──▶ build-print-cover.py  ──▶ dist/no-one-did-it-cover.pdf
                                       (Pillow: front + spine + back wrap at 300 DPI with bleed)
```

## Run

```bash
# One-command full build (prose → interior PDF → cover PDF)
node pipeline.mjs

# Or step by step:
node build-prose.mjs                                      # markdown → HTML
node build-print-pdf.mjs                                  # interior PDF
../.venv/bin/python build-print-cover.py                  # cover PDF (uses default page count from interior PDF)
../.venv/bin/python build-print-cover.py --pages 451      # explicit page count override
```

Outputs land in `dist/`:
- `no-one-did-it-interior.pdf` — 6×9 interior, numbered + running heads
- `no-one-did-it-cover.pdf` — full wrap cover with computed spine width

Each canonical file gets a timestamped sibling (`*-v1.0.0-YYYYMMDD-HHMMSS.pdf`) for diff history.

## Prerequisites

System binaries (verified at scope-time):
- Node ≥ 18 (tested 22.22.0)
- Python 3 (tested 3.14.5) in `../.venv/`
- qpdf (tested 12.3.2) — PDF concat + lossless compression
- pdfinfo (poppler 26.04) — page count probes

Node deps (installed via `npm install`):
- `marked`, `marked-footnote`, `marked-gfm-heading-id` — markdown → HTML
- `playwright` — Chromium for HTML → PDF
- `js-yaml` — read `book/spine-v6.yml`

Python deps (in `../.venv/`):
- `pypdf` (overlay, outline)
- `reportlab` (page-number + header rendering)
- `Pillow` (cover composition)
- `PyYAML`

Playwright Chromium browser binary at `~/Library/Caches/ms-playwright/`.

## Trim + paper

| Setting | Value |
|---|---|
| Trim size | 6.0″ × 9.0″ |
| Body type | EB Garamond 11pt / line-height 1.4 |
| Code/mono | JetBrains Mono |
| Margins (recto) | top 0.85″ / outer 0.5″ / bottom 0.75″ / inner 0.625″ |
| Margins (verso) | mirrored |
| Footnotes | page-bottom, per-chapter, via marked-footnote |
| Paper (cover spine calc) | cream by default (current build: 451 pp, spine 1.1275″); override with `--paper white\|premium` |
| Bleed | 0.125″ on all outer edges |

## KDP spec compliance

- ✓ Interior page size 6×9 (432×648 pts), embedded fonts (EB Garamond woff2 loaded via `@font-face`)
- ✓ Cover full wrap (13.355″ × 9.25″) with computed spine + 0.125″ bleed on all edges, 300 DPI native
- ✓ Front matter unnumbered; numbering starts on first chapter and runs through back matter
- ✓ PDF outline (bookmarks) generated for sidebar navigation
- ✓ Reading order: Title → Contents → Copyright → Dedication → Epigraph → Preface → A Note on Cases → Parts/Chapters → Back matter (matches `book/spine-v6.yml`)
- ✓ **Print-specific ISBN** (`978-1-80826-003-2`) substituted into the copyright page; the EPUB ISBN (`978-1-80826-002-5`) stays distinct.
- ✓ **Print-resolution cover assets** at 1800×2775 px (6×9.25″ at 300 DPI — top/bottom bleed baked into the image height; L/R outer-edge bleed added by `build-print-cover.py`'s edge extension).
- ⚠ **Back cover has a designed barcode placeholder** at lower-right (current design-studio output). KDP typically prints its own barcode at that location; the design will be overprinted unless you (a) crop the existing barcode out before assembly, or (b) confirm with KDP that the embedded ISBN-barcode matches their format.
- ⚠ CMYK conversion not applied to cover — KDP accepts RGB (sRGB IEC61966-2.1). For CMYK, apply Ghostscript step.
- ⚠ Bleed marks not added — KDP doesn't require them.

## Cover production procedure (the design-studio path)

The print cover IS NOT built from `book/design/epub/cover.jpg` — that file is the 1600×2560 EPUB cover at 1.6:1 ratio and would distort when squished to a 6×9 print trim. Instead, print covers are exported fresh from the design studio at print resolution:

```bash
# Start the design studio (Node stdlib only — no npm install)
node design-studio/serve.mjs                                         # localhost:5180

# Export print-resolution front + back covers (1800×2775 = 6×9.25″ at 300 DPI)
node design-studio/export.mjs --board ill-bleed --w 1800 --bh 925 --jpeg --out book/design/print-covers/cover-front-print.jpg
node design-studio/export.mjs --board ill-back  --w 1800 --bh 925 --jpeg --out book/design/print-covers/cover-back-print.jpg

# build-print-cover.py defaults to these print assets; --baked-tb-bleed is on by default
node print/pipeline.mjs
```

The design lives in `design-studio/design/cartoon-art.jsx` (court-of-animals illustration); the design-studio README at `design-studio/README.md` explains alternate boards (Dossier edition, full-bleed variants, chapter openers).

## Known limitations to verify against your KDP preview

- **Footnote anchor links inside each chapter section are dead** (point to `#c1-1` etc. which live in the consolidated `book/back-matter/references.md`). Superscripts are visible and correctly numbered in the chapter prose; the references list itself ships as a separate back-matter section that the reader flips to. This is the same arrangement the EPUB uses.
- **Pandoc smart-quote behaviour** converts straight `'` to curly `'` (e.g. *A Reader's Field Guide*). Running headers and TOC entries pick up the curly form.
- **Bibliography may contain author-name duplication** (e.g., "Schwartz, Gary T. Schwartz, Gary T., ...") inherited from the upstream Chicago formatter (`scripts/format_citations_chicago.py` retired May 30). Not introduced by the print pipeline; surface the issue to the back-matter regenerator.

## Spine treatment for parts (RL-specific)

The Half Second has flat chapters; *No One Did It* has 4 parts × 3-4 chapters. The spine adapter (`loadSpine()` in `build-print-pdf.mjs`) inserts a typographic part-divider section between parts. The divider page renders Part roman numeral + part title + tagline (from `book/spine-v6.yml`), is unnumbered and headerless, and counts toward total page count.

## Footnote handling

Chapter prose uses `[^N]` markdown footnote references. `marked-footnote` converts these to `<sup>` links + `<ol class="footnotes">` block at the end of each chapter section. CSS in `build-print-pdf.mjs` styles the footnote section with a hairline divider, 9pt mono labels, and tight line-height. The compiled Chicago endnotes also live as a separate back-matter section (`book/back-matter/references.md`) and ship as page-numbered back matter.

## What was borrowed vs written

| File | Origin |
|---|---|
| `fonts/` (16 woff2 + manifest.json) | Copied verbatim from `the-half-second/build/fonts/` |
| `font-css.mjs` | Verbatim |
| `i18n.mjs` | Adapted (relaxed required-field validation) |
| `i18n/en.json` | Written fresh for RL |
| `build-prose.mjs` | **Pandoc-based** (not marked.js) — RL source uses pandoc fenced divs (`::: {.copyright-page}`), `[^N]:` footnote definitions, and Chicago citation conventions; reusing pandoc + the existing `pipelines/epub/strip_inline_styles.lua` keeps the print build in sync with the EPUB build's conversion contract. Per-chapter trailing `## References` sections are stripped (back-matter `references.md` is canonical). |
| `build-print-pdf.mjs` | Adapted: SPINE built from `book/spine-v6.yml`; part-divider section kind added (typographic Part roman + title + tagline from the spine); chapter cover SVGs removed (typographic chapter starts); Card-index pass removed; reading-guide synthesis removed. Title extraction reads body H1 (correct casing, apostrophes, smart quotes). TOC inserted right after title page (canonical reading order from `spine-v6.yml`). |
| `print-pdf-finalize.py` | Adapted: spine kinds match RL (title/front/toc/part = unnumbered, chapter+back = numbered+header); outline labels adapted to RL slugs |
| `build-print-cover.py` | Adapted: default front/back paths point at `book/design/epub/cover.jpg` and `book/design/epub/back-cover.jpg`; defaults updated |
| `pipeline.mjs` | Adapted: no Apple Books steps, runs cover after measuring interior page count |
