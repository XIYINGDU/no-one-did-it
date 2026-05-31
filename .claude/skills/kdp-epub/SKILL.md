---
name: kdp-epub
description: >-
  Build and validate a KDP-ready reflowable EPUB 3 of *No One Did It* from the v5
  source of truth, conforming to the Amazon Kindle Publishing Guidelines. Use when
  the user wants to compile, build, export, or validate the Kindle / EPUB / KDP
  edition of the book. Governed by rule 16-kdp-epub. Produces dist/no-one-did-it.epub.
---

# /kdp-epub — Build the Kindle/KDP EPUB

Produce the Amazon KDP edition as a **reflowable EPUB 3**, compiled from the v5
canonical text and validated to the gates in `.claude/rules/16-kdp-epub.md`.
The EPUB is a **derived artifact** — fix text in `book/chapters-v5/`, never in the EPUB.

## When to use

- "compile the epub", "build the Kindle edition", "export for KDP", "validate the ebook".
- After any v5 text change that should reach the Kindle edition (rebuild from source).

## Prerequisites (the build script enforces all of these — fail-loud)

1. **Source clean.** `dist/manuscript-v6.md` is current (re-run
   `pipelines/epub/assemble_v6_manuscript.py` if v6 chapters changed) and contains **no raw
   `[CITE:]` markers and no `[EVIDENCE NEEDED]`**. Resolve cites to endnotes first
   (Stephen / the source-ledger pipeline). *Current state: 3 `[CITE:]` markers remain
   (ch08 ×1, ch12 ×2) — these block a non-draft build until resolved.*
2. **Metadata filled.** `book/design/epub/metadata.yml` has no `TODO` tokens (author,
   publisher, identifier). Generate a stable identifier once:
   `python3 -c 'import uuid;print("urn:uuid:"+str(uuid.uuid4()))'`.
3. **Cover present and conforming.** `book/design/epub/cover.jpg` = **2560×1600 JPEG, 1.6:1,
   sRGB, title + author composited** (rule 16). *Current state: the design delivery has
   no title-composited ≥1600px cover — a conforming cover must be produced first. Use
   `--draft` to build a coverless proof in the meantime.*

## Tooling (all present on this machine)

`pandoc 3.9` (build) · `epubcheck v5.3.0` (gate 1) · `Kindle Previewer 3` CLI +
app (gate 2) · `sips` (cover dimension check) · `java`.

## Procedure

### 1. Assemble + clean the source
```bash
python3 pipelines/epub/assemble_v6_manuscript.py    # refresh the manuscript from v6
# (the build script also runs this automatically when the cache is stale)
grep -rn '\[CITE:' dist/manuscript-v6.md  # must be empty before a real build
```
Resolve any `[CITE:]` to endnotes via the source-ledger cards (Stephen locks the
anchor, then the cite becomes a numbered note). Do **not** hand-delete cites.

### 2. Prepare cover + metadata
- Drop the conforming cover at `book/design/epub/cover.jpg` (or pass `--draft` to skip).
- Fill `book/design/epub/metadata.yml` (author / publisher / identifier).

### 3. Build
```bash
python3 pipelines/epub/build_kdp_epub.py            # full, gated build  -> dist/no-one-did-it.epub
python3 pipelines/epub/build_kdp_epub.py --draft    # coverless text proof for review
```
What the build does: guards source + metadata + cover; folds the back-of-book
`# Notes` definitions into **pandoc popup footnotes** (`epub:type="noteref"/"footnote"`)
while keeping the Selected Bibliography; runs `pandoc --to epub3 --split-level=1 --toc`
with `kdp.css`, the metadata, and the cover.

### 4. Validate (both hard gates must pass before upload)
```bash
python3 pipelines/epub/validate_kdp_epub.py dist/no-one-did-it.epub
```
- **Gate 1 — epubcheck:** zero fatals/errors (triage warnings).
- **Gate 2 — Kindle Previewer 3:** converts to KFX/KPF cleanly. *Authoritative Kindle
  gate — a file can pass epubcheck and still break on a Paperwhite.* If the CLI isn't on
  PATH, open `dist/no-one-did-it.epub` in the Kindle Previewer 3 app and run the convert.
- **Structure checks:** cover declared, footnote popups present, no leaked `[CITE:]`/`[^N]`.

### 5. Pre-flight checklist (manual, in Kindle Previewer)
- [ ] Cover renders crisp; title + author legible at thumbnail size.
- [ ] TOC navigates to every chapter + the Bibliography; no page numbers in TOC.
- [ ] A footnote tap opens a **pop-up** (not a jump to the back); back-link returns.
- [ ] A part-divider image displays with alt text; single-column everywhere.
- [ ] Reader font-size changes reflow cleanly (no fixed-px overflow).
- [ ] Epigraphs (incl. CJK/Greek/Arabic/Sanskrit) render; no tofu boxes.
- [ ] No raw `[CITE:]`, `[^N]`, or `## beat-name` text anywhere.

### 6. Upload
Upload `dist/no-one-did-it.epub` to KDP as the manuscript; upload the 2560×1600 JPEG
as the marketing cover separately. KDP assigns the ASIN.

## Guardrails

- The `scan-kdp-epub-css.py` hook warns at edit time if `book/design/epub/*.css` introduces
  KDP-unsupported constructs (`position:`, fixed `pt`/`px` type/margins, `height` on
  text, forced black/white backgrounds).
- Never produce `.mobi` (dead format). Never edit the `.epub` as the master.
- Reflowable only: the fixed-layout dossier interiors do not survive reflow — a
  separate fixed-layout edition would be a different pipeline.

## Troubleshooting

| Symptom | Cause / fix |
|---|---|
| `FAIL: N unresolved [CITE:]` | resolve cites to endnotes in v5, re-assemble, rebuild |
| `FAIL: metadata.yml ... TODO` | fill author/publisher/identifier in `book/design/epub/metadata.yml` |
| `FAIL: cover ... non-conforming` | export a 2560×1600 sRGB JPEG (1.6:1) with title+author, or `--draft` |
| epubcheck errors on fonts | embed only OTF/TTF, or drop embedded fonts and let Kindle use reader font |
| notes render inline, not popup | confirm `epub:type` markup survived; check pandoc version ≥3.0 |
| pandoc: `--split-level` unknown | pandoc < 3.0; upgrade (this repo expects 3.9) |
