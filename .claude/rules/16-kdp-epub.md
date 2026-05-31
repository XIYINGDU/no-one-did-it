**The Kindle/KDP edition ships as a reflowable EPUB 3 built from the v6 source of truth, conforming to the Amazon Kindle Publishing Guidelines; it is valid only when epubcheck passes with zero errors AND Kindle Previewer 3 converts it cleanly. The EPUB is a derived artifact — never the canonical source.**

# KDP EPUB Production

**Scope:** binds the production of the Kindle/KDP eBook edition of *No One Did It* — the build inputs under `book/design/epub/`, the build/validate scripts (`pipelines/epub/build_kdp_epub.py`, `pipelines/epub/validate_kdp_epub.py`), and the output EPUB. Constitutional anchor for the `/kdp-epub` skill and the `scan-kdp-epub-css.py` hook. Sibling to rule `13-citation-form.md` (citations/endnotes), rule `12`/`15` (reader experience), and the visual-material ownership in rule `03`.

## Source-of-truth invariant

The EPUB is **compiled from `book/chapters-v6/`** — the v6 canonical text — via a declared spine. `book/spine-v6.yml` is the single manifest of reading order (front matter → part dividers + chapters → back matter); `pipelines/epub/assemble_v6_manuscript.py` reads it and emits `dist/manuscript-v6.md`; `pipelines/epub/build_kdp_epub.py` turns that manuscript into the EPUB (pandoc adds the cover, the metadata-driven title page, and the contents; it appends the back cover). The `.epub` and the assembled `manuscript/*.md` are build outputs: regenerate them, never treat them as the editable master. Any text fix lands in `book/chapters-v6/` (or the front/back-matter source); reordering lands in `book/spine-v6.yml`; then the EPUB is reassembled and rebuilt. The build **must fail loud** if the source still contains unresolved `[CITE:]` markers or `[EVIDENCE NEEDED]` placeholders — raw citation markers must not ship.

## Format

| Requirement | Value |
|---|---|
| Edition type | **Reflowable** EPUB (text-heavy trade nonfiction; reader controls font/size) |
| EPUB version | **EPUB 3** (recommended — converts to Amazon KFX with minimal fidelity loss; EPUB 2 also accepted) |
| Upload format | `.epub` (KDP also accepts KPF/DOCX/HTML/RTF/PDF; we standardize on EPUB 3 from pandoc) |
| MOBI | **Dead.** Not accepted for reflowable (since 2021-08-01) or fixed-layout (since 2025-03-18). Never produce `.mobi`. |
| Layout | **Single column.** Do **not** use CSS `position:` for alignment. |

## Cover (rule 03 visual-material gates still apply)

| Requirement | Value |
|---|---|
| Ideal dimensions | **2,560 × 1,600 px** (height × width) |
| Aspect ratio | **1.6 : 1** (1.6 tall to 1 wide). Off-ratio → KDP adds white bars or distorts. |
| Minimum | never below **1,000 px** on the longest side; always target the ideal |
| Format | **JPEG** (preferred) or TIFF |
| Color profile | **RGB / sRGB** |
| Resolution | ≥ 300 DPI recommended |
| File size | ≤ 50 MB hard cap; a quality 2,560×1,600 JPEG is well under 5 MB |
| Content | **must carry the title and author**; no price/promo text; light backgrounds need a 3–4 px medium-gray border |
| Internal (in-EPUB) cover | declared via EPUB 3 `properties="cover-image"` **and** legacy `<meta name="cover">`; the cover image must fill ≥ 50% of its page; **do not add a separate HTML cover page** alongside it (duplication / conversion failure) |

> **Standing blocker (2026-05-29):** the design-team delivery contains **no title-composited, ≥1,600 px cover**. The cartoon "Animal Court" crop is 840×1,295 and carries no title. A conforming cover (titled, 2,560×1,600, JPEG, sRGB) is a prerequisite for a shippable build. See `dev-docs/design-team-delivery-2026-05-29.md`.

## HTML / CSS subset (reflowable)

Kindle's renderer is not a full browser. Build for the supported subset:

- **Relative units only** for type and spacing: use `em` / `%`, never `pt` or `px` for `font-size`, `width`, `margin`, `padding`, `text-indent`. (`px` is acceptable only on image dimensions.)
- **Body text:** default size (`1em`) and default `line-height`; no forced `font-family`; not primarily bold/italic; left/right margins = `0`; no imposed text color (if grays are used, keep them `#666`–`#999`); no black or white forced background.
- **No `height`** on text elements (only on images). **No `position:`**. No non-breaking spaces between words to fake spacing.
- **Margins:** left/right in `%`, top/bottom in `em`.
- **Headings:** set an explicit `text-align` (`left`/`center`/`right`) to avoid justified word-gaps.
- **Paragraphs:** distinguish by indent **or** spacing, not both; `text-indent` ≤ 4em; no double-spacing.
- **Page breaks:** `page-break-before/after/inside` and `break-before/after/inside` (`avoid`/`auto`/`always`) are supported — break before each chapter/part.
- **Embedded fonts** (if any): **OTF or TTF only** (no Type 1). Default to not embedding body fonts; let Kindle use the reader's font.

## Images

- Supported: **JPEG, PNG, GIF, BMP** (use JPEG for photos, PNG for line art / part dividers).
- High resolution but reasonable file size; **every image needs `alt` text** (accessibility + KDP quality).
- Part-divider art (the design `part0–3.png`) is the only interior art a reflowable build carries; embed as block images with alt text. The fixed-layout dossier interiors do not survive reflow.

## Footnotes / endnotes (aligns with rule 13)

Kindle renders notes as **pop-ups** when marked per EPUB 3:

- Reference: `<sup><a epub:type="noteref" href="…#nX">N</a></sup>`
- Note body: `<aside id="nX" epub:type="footnote">…<a href="…back">↩</a></aside>` (bidirectional link back).
- Requires the namespace `xmlns:epub="http://www.idpf.org/2007/ops"` on `<html>`.
- The book's Chicago endnotes (grouped per chapter) satisfy this: pandoc EPUB 3 emits `epub:type="noteref"`/`footnote` markup from `[^N]` — **verify** the built EPUB carries the `noteref`/`footnote` types so notes pop up rather than render inline.

## Navigation, metadata, accessibility

- **Nav:** an EPUB 3 nav document (`nav epub:type="toc"`) plus an NCX for EPUB 2 readers. TOC entries are **hyperlinked section names, no page numbers**; convert "see page XX" to internal links. Include `landmarks`; a `page-list` is optional (Roman/Arabic numerals only, relative paths).
- **Metadata (OPF `dc:`):** `title` (+ subtitle), `creator` (author), `language` (`en`), `publisher`, `date`, `identifier` (ISBN if assigned, else a stable UUID URN), `description`, `rights`. KDP assigns the ASIN at upload; an ISBN is optional.
- **Accessibility:** declare `dc:language`; logical reading order; `alt` on every image; semantic headings; include EPUB accessibility metadata (`schema:accessibilityFeature`, `accessibilityHazard none`, `accessMode textual`) where the toolchain allows.

## Validation gates (both required; in order)

1. **epubcheck (W3C, ≥ v5.x)** — must report **zero errors** (warnings triaged). Spec conformance.
2. **Kindle Previewer 3** — converts the EPUB to KFX/KF8 and renders on emulated devices; **must convert with no errors**. This is the authoritative Kindle gate: *a file can pass epubcheck and still break on a Paperwhite.* Run via its CLI (`kindlepreviewer <epub> -convert -output …`) or the app.
3. **Manual spot-check** — open the converted output and confirm: cover renders, TOC navigates, a footnote pops up, a part-divider image displays, no raw `[CITE:]`/`[^…]` text leaks into the body.

A build that has not passed gates 1 and 2 is not a candidate for KDP upload.

## Who owns what

- **Build/validate scripts + skill (`/kdp-epub`):** the production step (orchestrator-run). Deterministic; fail-loud on unresolved cites, missing/oversized cover, epubcheck/Previewer errors.
- **Stephen (fact-check):** the source must be cite-clean before build (no pending-lock, no `[EVIDENCE NEEDED]`).
- **Nancy (legal):** the cover and any caption/credit clear rule-03 image-rights before ship.
- **Bonnie (architect):** cover direction + which interior art (part dividers) the reflowable edition carries.
- **`scan-kdp-epub-css.py` hook:** warn-mode at edit time on `book/design/epub/` CSS — flags `position:`, fixed `pt`/`px` type/margins, `height` on text, forced black/white backgrounds.

## Why this rule exists

A book that argues records must be kept honestly cannot ship a malformed edition. KDP silently "fixes" non-conforming files (white bars on off-ratio covers, fallback fonts, inline notes that should pop up), and those silent fixes are exactly the kind of uncontrolled transformation the book diagnoses elsewhere. Pinning the format to EPUB 3 + the validation gates makes the Kindle edition a deliberate artifact rather than whatever KDP's converter happens to produce. The source-of-truth invariant keeps the prose canonical in v6 behind a declared spine, so the edition can be regenerated cleanly every time the text or its order changes.
