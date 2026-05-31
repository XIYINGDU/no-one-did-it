#!/usr/bin/env python3
"""Build the KDP-ready reflowable EPUB 3 from the v6 source of truth.

Governed by .claude/rules/16-kdp-epub.md. The EPUB is a DERIVED artifact: this
script regenerates it from dist/manuscript-v6.md (assembled by
pipelines/epub/assemble_v6_manuscript.py from book/spine-v6.yml: front matter +
part dividers + book/chapters-v6/ + back matter). It is fail-loud — it refuses
to build on unresolved citation markers, unfilled metadata, or a non-conforming
cover.

Pipeline:
  1. guard: no raw [CITE:] / [EVIDENCE NEEDED] in the source
  2. guard: metadata.yml has no TODO tokens
  3. guard: cover exists and meets KDP spec (>=1000px longest side, ~1.6:1, JPEG)
     -- bypass with --draft to produce a coverless proof for review
  4. preprocess: fold the back-of-book "# Notes" defs into pandoc popup footnotes
     (keep the [^N]: lines, drop the empty Notes headings); keep the Bibliography
  5. pandoc -> EPUB 3 (single column, toc, split per chapter)

Run from anywhere:
    python3 pipelines/epub/build_kdp_epub.py            # full build (requires conforming cover)
    python3 pipelines/epub/build_kdp_epub.py --draft    # coverless text proof
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "dist" / "manuscript-v6.md"
METADATA = ROOT / "book" / "design" / "epub" / "metadata.yml"
CSS = ROOT / "book" / "design" / "epub" / "kdp.css"
COVER = ROOT / "book" / "design" / "epub" / "cover.jpg"
BACK_COVER = ROOT / "book" / "design" / "epub" / "back-cover.jpg"
OUT = ROOT / "dist" / "no-one-did-it.epub"

CITE_RE = re.compile(r"\[CITE:")
EVIDENCE_RE = re.compile(r"\[EVIDENCE NEEDED")
FN_DEF_RE = re.compile(r"^\[\^[^\]]+\]:\s")


def die(msg: str) -> "None":
    print(f"FAIL: {msg}", file=sys.stderr)
    raise SystemExit(1)


def guard_source(text: str) -> None:
    cites = [i + 1 for i, ln in enumerate(text.splitlines()) if CITE_RE.search(ln)]
    if cites:
        die(f"{len(cites)} unresolved [CITE:] marker(s) in the manuscript "
            f"(lines {cites[:8]}{'...' if len(cites) > 8 else ''}). "
            f"Resolve to endnotes before building (rule 16: raw cite markers must not ship).")
    ev = [i + 1 for i, ln in enumerate(text.splitlines()) if EVIDENCE_RE.search(ln)]
    if ev:
        die(f"{len(ev)} [EVIDENCE NEEDED] placeholder(s) in the manuscript (lines {ev[:8]}).")


def guard_metadata() -> None:
    if not METADATA.exists():
        die(f"missing metadata file: {METADATA}")
    raw = METADATA.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError as e:
        die(f"metadata.yml is not valid YAML: {e}")
    # Check parsed string VALUES only, so the template's own comments may mention
    # placeholder tokens ("TODO") freely without tripping the guard.
    placeholders: list[str] = []

    def walk(node: object, path: str) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}.{k}" if path else str(k))
        elif isinstance(node, list):
            for idx, v in enumerate(node):
                walk(v, f"{path}[{idx}]")
        elif isinstance(node, str) and "TODO" in node:
            placeholders.append(path)

    walk(data, "")
    if placeholders:
        die(f"metadata.yml still has unfilled placeholder(s): {placeholders}. "
            f"Fill author / publisher / identifier before building.")


def guard_cover(draft: bool) -> bool:
    """Return True if a conforming cover is present. In --draft, warn and continue."""
    if not COVER.exists():
        msg = (f"cover not found at {COVER}. A KDP cover is 2560x1600 px (height x width; "
               f"portrait, 1.6:1), title+author composited, JPEG, sRGB (rule 16).")
        if draft:
            print(f"WARN (--draft): {msg} Building without a cover.")
            return False
        die(msg + " Use --draft to build a coverless proof.")
    # dimensions via sips (macOS)
    try:
        out = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(COVER)],
                             capture_output=True, text=True, check=True).stdout
        w = int(re.search(r"pixelWidth:\s*(\d+)", out).group(1))
        h = int(re.search(r"pixelHeight:\s*(\d+)", out).group(1))
    except Exception as e:  # noqa: BLE001
        msg = f"could not verify cover dimensions ({e})"
        if draft:
            print(f"WARN (--draft): {msg}; building anyway.")
            return True
        die(f"{msg}. A shippable cover must be dimension-verifiable (2560x1600 px, "
            f"height x width, portrait 1.6:1, JPEG). Use --draft to bypass.")
    longest = max(w, h)
    ratio = h / w if w else 0
    problems = []
    if longest < 1000:
        problems.append(f"longest side {longest}px < 1000px minimum (ideal 2560)")
    if not (1.45 <= ratio <= 1.75):
        problems.append(f"aspect h/w={ratio:.2f} outside ~1.6:1 (KDP adds white bars / distorts)")
    if COVER.suffix.lower() not in (".jpg", ".jpeg"):
        problems.append(f"format {COVER.suffix} — KDP prefers JPEG")
    if problems:
        detail = "; ".join(problems)
        if draft:
            print(f"WARN (--draft): cover {w}x{h} non-conforming: {detail}")
            return True
        die(f"cover {w}x{h} non-conforming: {detail}. Use --draft to bypass.")
    print(f"OK: cover {w}x{h} (h/w={ratio:.2f}) meets KDP spec.")
    return True


def preprocess(text: str) -> str:
    """Fold the back-of-book Notes into pandoc popup footnotes.

    Keep the [^N]: definition lines (pandoc consumes them into popups at the refs),
    drop the now-empty '# Notes' / '## Chapter N' headings, keep the Bibliography.
    """
    notes_idx = text.find("\n# Notes")
    biblio_idx = text.find("\n# Selected Bibliography")
    if notes_idx == -1:
        return text  # no separate Notes section; pandoc handles inline defs as-is
    chapters = text[:notes_idx].rstrip()
    if biblio_idx != -1 and biblio_idx > notes_idx:
        notes_region = text[notes_idx:biblio_idx]
        biblio = text[biblio_idx:].strip()
    else:
        notes_region = text[notes_idx:]
        biblio = ""
    # Keep each [^N]: definition plus any indented continuation lines, so multi-line
    # notes are not silently truncated; a flush-left heading/prose line ends a def run.
    defs: list[str] = []
    in_def = False
    for ln in notes_region.splitlines():
        if FN_DEF_RE.match(ln):
            in_def = True
            defs.append(ln)
        elif in_def and (ln.startswith((" ", "\t")) or not ln.strip()):
            defs.append(ln)
        else:
            in_def = False
    parts = [chapters, "\n".join(defs)]
    if biblio:
        parts.append(biblio)
    return "\n\n".join(p for p in parts if p) + "\n"


def append_back_cover(text: str) -> str:
    """Append the Dossier back cover as a final full-page image, if present.

    The reflowable EPUB carries the front cover via --epub-cover-image; the back
    cover is a normal embedded image on the last page (page-break-before via the
    .backcover rule in kdp.css). It is optional — absent file is a no-op.
    """
    if not BACK_COVER.exists():
        return text
    alt = ("Back cover, Dossier edition: the responsibility-laundering blurb "
           "(Power keeps the control. It gives away the blame.), the "
           "scales-of-justice emblem, and the ISBN barcode.")
    return text.rstrip() + f"\n\n::: {{.backcover}}\n![{alt}]({BACK_COVER})\n:::\n"


def ensure_fresh_manuscript() -> None:
    """Re-run pipelines/epub/assemble_v6_manuscript.py if the manuscript is
    older than any source it depends on, or simply missing. Without this
    guard, edits to back-matter (e.g. note-from-the-author.md) silently
    fail to appear in the EPUB because pandoc reads a stale manuscript.

    Sources checked: spine-v6.yml, every chapter under book/chapters-v6/,
    and every front/back-matter md the spine references."""
    assembler = HERE / "assemble_v6_manuscript.py"
    spine_path = ROOT / "book" / "spine-v6.yml"

    def newest_source_mtime() -> float:
        latest = spine_path.stat().st_mtime
        for chapter in (ROOT / "book" / "chapters-v6").glob("*.md"):
            latest = max(latest, chapter.stat().st_mtime)
        try:
            spine = yaml.safe_load(spine_path.read_text(encoding="utf-8"))
        except Exception:
            return latest
        for section in ("front_matter", "back_matter"):
            for entry in spine.get(section, []) or []:
                fp = ROOT / entry.get("file", "")
                if fp.exists():
                    latest = max(latest, fp.stat().st_mtime)
        return latest

    needs_rebuild = (not MANUSCRIPT.exists()
                     or MANUSCRIPT.stat().st_mtime < newest_source_mtime())
    if needs_rebuild:
        print("INFO: manuscript stale or missing; re-running assemble_v6_manuscript.py …")
        result = subprocess.run([sys.executable, str(assembler)], cwd=str(ROOT))
        if result.returncode != 0:
            die(f"assemble_v6_manuscript.py failed (exit {result.returncode})")
        if not MANUSCRIPT.exists():
            die(f"assembler ran but {MANUSCRIPT} still missing")


def build(draft: bool, out: Path) -> None:
    ensure_fresh_manuscript()
    text = MANUSCRIPT.read_text(encoding="utf-8")
    guard_source(text)
    guard_metadata()
    have_cover = guard_cover(draft)

    processed = append_back_cover(preprocess(text))
    out.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tf:
        tf.write(processed)
        tmp = Path(tf.name)

    cmd = [
        "pandoc", str(tmp),
        "--from", "markdown",
        "--to", "epub3",
        "--metadata-file", str(METADATA),
        "--css", str(CSS),
        "--lua-filter", str(HERE / "mark_chapter_openers.lua"),
        "--lua-filter", str(HERE / "strip_inline_styles.lua"),
        "--toc", "--toc-depth=1",
        "--split-level=1",
        "--standalone",
        # Allow chapter-source ![](book/evidence/diagrams/proofs/…) repo-relative
        # paths to resolve against the project root; pandoc looks in this dir
        # in addition to the temp-file location for embedded resources.
        "--resource-path", str(ROOT),
        "-o", str(out),
    ]
    if have_cover and COVER.exists():
        cmd += ["--epub-cover-image", str(COVER)]

    print("RUN: " + " ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        die("pandoc not found on PATH (brew install pandoc).")
    except subprocess.CalledProcessError as e:
        die(f"pandoc failed (exit {e.returncode}).")
    finally:
        tmp.unlink(missing_ok=True)

    size_mb = out.stat().st_size / (1024 * 1024)
    print(f"\nOK: built {out} ({size_mb:.2f} MB)"
          + ("  [DRAFT — no/again cover]" if draft else ""))
    print("NEXT: validate with  python3 pipelines/epub/validate_kdp_epub.py")


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the KDP reflowable EPUB 3 from v5.")
    ap.add_argument("--draft", action="store_true",
                    help="bypass the cover gate to produce a coverless text proof")
    ap.add_argument("--out", type=Path, default=OUT, help=f"output path (default {OUT})")
    args = ap.parse_args()
    build(args.draft, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
