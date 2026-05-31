#!/usr/bin/env python3
"""Overlay continuous page numbers + running heads on a concatenated print
interior PDF for No One Did It (KDP paperback).

Spine kinds:
  - title, front, toc   : no number, no header
  - part                : no number, no header (divider plate)
  - chapter             : number every page, running header on every page
                          (chapter num + chapter title)
  - back                : number every page, running header on every page

Numbering starts at "1" on the first chapter page (which follows Part I's
divider) and runs continuously through chapters and back matter.

Usage:
  python3 print-pdf-finalize.py \
    --input  dist/no-one-did-it-interior-unnumbered.pdf \
    --output dist/no-one-did-it-interior.pdf \
    --spine  dist/print-sections/_spine.json
"""

from __future__ import annotations

import argparse
import io
import json
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
PRINT_DIR = ROOT / "pipelines" / "print"

PAGE_W, PAGE_H = 6 * inch, 9 * inch


def register_font():
    """Register a TTF for the overlay (page numbers + running headers).
    reportlab can't read woff2 and PDF base fonts aren't embedded — KDP
    needs every font embedded. Try system TTFs first, then fall back."""
    candidates = [
        ("/System/Library/Fonts/Supplemental/Georgia Italic.ttf", "GeorgiaItalic"),
        ("/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf", "TimesItalic"),
        ("/Library/Fonts/EBGaramond-Italic.ttf", "EBGaramondItalic"),
        ("/System/Library/Fonts/Supplemental/Georgia.ttf", "Georgia"),
    ]
    for path, name in candidates:
        if Path(path).exists():
            try:
                pdfmetrics.registerFont(TTFont(name, path))
                return name
            except Exception:
                continue
    print("  ⚠ no system TTF found; falling back to Times-Italic (unembedded — KDP may reject)")
    return "Times-Italic"


def build_overlay_document(total_pages, page_numbers, headers, font_name):
    """Build ONE multi-page PDF with all overlays — one page per source page,
    blank when no overlay needed. Reportlab embeds each font ONCE for the
    whole document; pypdf can then merge per-page from this single source,
    avoiding the per-page font subset duplication that occurs when each
    overlay is its own PDF (previous design created ~864 redundant font
    subsets for a 432-page numbered run)."""
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(PAGE_W, PAGE_H))

    for i in range(total_pages):
        num = page_numbers.get(i)
        hdr = headers.get(i)

        if hdr:
            c.setFont(font_name, 9)
            c.setFillColorRGB(0.47, 0.47, 0.47)
            c.drawCentredString(PAGE_W / 2, PAGE_H - 0.45 * inch, hdr)

        if num is not None:
            c.setFont(font_name, 9)
            c.setFillColorRGB(0.27, 0.27, 0.27)
            c.drawCentredString(PAGE_W / 2, 0.4 * inch, str(num))

        c.showPage()

    c.save()
    return buf.getvalue()


def compute_section_page_counts(input_pdf, spine):
    """For each spine entry, compute (start, end) in the concatenated PDF
    by reading its section PDF's own page count."""
    sections_dir = input_pdf.parent / "print-sections"
    result = []
    cursor = 0
    for entry in spine:
        section_path = sections_dir / entry["pdf"]
        with section_path.open("rb") as f:
            r = PdfReader(f)
            n = len(r.pages)
        result.append((entry, cursor, cursor + n - 1))
        cursor += n
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--spine", required=True)
    args = p.parse_args()

    input_pdf = Path(args.input)
    output_pdf = Path(args.output)
    spine = json.loads(Path(args.spine).read_text())

    sections = compute_section_page_counts(input_pdf, spine)

    page_numbers = {}
    headers = {}
    n = 0
    for entry, start, end in sections:
        kind = entry["kind"]
        header_text = entry.get("header") or ""
        if kind in ("title", "front", "toc", "part"):
            # No number, no header on these (front matter + part dividers)
            continue
        if kind == "chapter":
            # Trade-paperback convention: chapter page 1 carries the folio
            # but suppresses the running header (the chapter title is right
            # there on the opening page; a header repeating it is redundant).
            # Subsequent chapter pages get folio AND running header.
            for p_idx in range(start, end + 1):
                n += 1
                page_numbers[p_idx] = n
                if header_text and p_idx > start:
                    headers[p_idx] = header_text
        elif kind == "back":
            for p_idx in range(start, end + 1):
                n += 1
                page_numbers[p_idx] = n
                if header_text:
                    headers[p_idx] = header_text

    font_name = register_font()
    total_pages = sections[-1][2] + 1 if sections else 0
    print(f"  Font for overlays: {font_name}")
    print(f"  Total pages: {total_pages}")
    print(f"  Numbered: {len(page_numbers)} pages")
    print(f"  Running header on: {len(headers)} pages")

    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()

    # Build ONE multi-page overlay PDF; reportlab embeds Georgia-Italic and
    # Helvetica once for the whole document instead of once per overlay.
    overlay_bytes = build_overlay_document(total_pages, page_numbers, headers, font_name)
    overlay_pdf = PdfReader(io.BytesIO(overlay_bytes))

    for i, page in enumerate(reader.pages):
        if i < len(overlay_pdf.pages) and (i in page_numbers or i in headers):
            page.merge_page(overlay_pdf.pages[i])
        writer.add_page(page)

    # ── PDF outline / bookmarks ────────────────────────────────────────
    FRONT_LABELS = {
        "title":     "Title page",
        "copyright": "Copyright",
        "dedication": "Dedication",
        "book-epigraph": "Epigraph",
        "preface": "Preface",
        "note-on-cases": "A Note on Cases",
        "toc": "Contents",
    }
    print(f"  Building PDF outline ({len(sections)} entries)…")
    front_parent = None
    body_parent = None
    back_parent = None
    last_group = None
    for entry, start, _end in sections:
        kind = entry["kind"]
        slug = entry.get("slug")
        if kind == "title":
            label = "Title page"
        elif kind in ("front", "toc"):
            label = FRONT_LABELS.get(slug) or (slug.replace("-", " ").title() if slug else kind.title())
        elif kind == "part":
            label = f"Part {slug.split('-')[-1].upper() if slug else ''}"
        else:
            label = entry.get("header") or (slug.replace("-", " ").title() if slug else kind.title())

        if kind in ("title", "front", "toc") and last_group != "front":
            front_parent = writer.add_outline_item("Front matter", start, parent=None)
            last_group = "front"
        elif kind in ("part", "chapter") and last_group != "body":
            body_parent = writer.add_outline_item("Chapters", start, parent=None)
            last_group = "body"
        elif kind == "back" and last_group != "back":
            back_parent = writer.add_outline_item("Back matter", start, parent=None)
            last_group = "back"

        parent = (
            front_parent if kind in ("title", "front", "toc")
            else body_parent if kind in ("part", "chapter")
            else back_parent
        )
        writer.add_outline_item(label, start, parent=parent)

    # Tell viewers to open with the bookmarks sidebar visible. We belt-
    # and-brace this with three settings:
    #   - /PageMode /UseOutlines : the canonical "open with outline panel" flag
    #   - /PageLayout /SinglePage : explicit page layout for single-page view
    #   - DocumentInformation /Title set so viewers see a non-empty doc name
    # Some viewers (especially macOS Preview) sometimes ignore /PageMode
    # alone; layering these together makes the intent unambiguous.
    from pypdf.generic import TextStringObject
    writer._root_object[NameObject("/PageMode")] = NameObject("/UseOutlines")
    writer._root_object[NameObject("/PageLayout")] = NameObject("/SinglePage")
    try:
        i18n = json.loads((PRINT_DIR / "i18n" / "en.json").read_text())
    except Exception:
        i18n = {}
    writer.add_metadata({
        "/Title": i18n.get("title", "No One Did It"),
        "/Author": i18n.get("author", "Li Xiaolai"),
        "/Subject": i18n.get("subtitle", ""),
        "/Producer": "print-pdf-finalize.py (pypdf + reportlab + qpdf)",
    })

    # Write intermediate numbered PDF, then qpdf lossless compress.
    # gs is avoided because it substitutes Type 3 web fonts with Times.
    intermediate = output_pdf.with_suffix(".numbered.pdf")
    with intermediate.open("wb") as f:
        writer.write(f)

    import shutil
    import subprocess
    qpdf = shutil.which("qpdf")
    if qpdf:
        print(f"  Compressing with qpdf (lossless; preserves fonts)…")
        subprocess.run([
            qpdf,
            "--linearize",
            "--object-streams=generate",
            "--compress-streams=y",
            "--remove-unreferenced-resources=yes",
            str(intermediate),
            str(output_pdf),
        ], check=True)
        intermediate.unlink()
    else:
        print(f"  ⚠ qpdf not found; skipping compression")
        intermediate.rename(output_pdf)

    size_mb = output_pdf.stat().st_size / 1024 / 1024
    print(f"  ✓ Final PDF → {output_pdf}  ({size_mb:.2f} MB)")

    write_timestamped_snapshot(output_pdf)
    return 0


def write_timestamped_snapshot(canonical):
    """`<stem>-v<VERSION>-<YYYYMMDD>-<HHMMSS>.<ext>` sibling. Mirrors EPUB build."""
    import datetime
    import json
    import shutil

    i18n_path = PRINT_DIR / "i18n" / "en.json"
    try:
        version = json.loads(i18n_path.read_text()).get("version")
    except Exception:
        version = None

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    version_tag = f"-v{version}" if version else ""
    snapshot = canonical.with_name(f"{canonical.stem}{version_tag}-{stamp}{canonical.suffix}")
    shutil.copyfile(canonical, snapshot)
    print(f"  Snapshot   → {snapshot.name}")
    return snapshot


if __name__ == "__main__":
    sys.exit(main())
