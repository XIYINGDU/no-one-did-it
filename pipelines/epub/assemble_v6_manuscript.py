#!/usr/bin/env python3
"""Assemble dist/manuscript-v6.md from the declared spine.

v6 is the canonical source of truth. Unlike the v4/v5 assemblers (which simply
concatenated chapters + back-matter), this one is *spine-driven*: it reads
book/spine-v6.yml and emits the full EPUB reading order —

    front matter -> part dividers + chapters -> back matter

— so the reading order lives in one declared manifest, not implicit in the
script. The back cover is appended later by pipelines/epub/build_kdp_epub.py
(append_back_cover), and the front cover + title page + contents are produced by
pandoc at build time; the spine documents those for completeness.

Run from the project root:
    python3 pipelines/epub/assemble_v6_manuscript.py
"""
from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SPINE = ROOT / "book" / "spine-v6.yml"

CHAPTER_REF_RE = re.compile(r"\n+## References\b.*$", re.DOTALL)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# A trailing intra-crew handoff block: a thematic-break `---` followed by lines
# that begin with a crew metadata key. Never reader-facing; strip before ship.
CREW_KEYS = (
    "Owner", "Purpose", "Task", "Handoff", "Evidence grade", "Assumptions",
    "Open questions", "Risks", "Inputs reviewed", "Inputs", "Output",
)
CREW_TRAILER_RE = re.compile(
    r"\n-{3,}\s*\n+(?:" + "|".join(re.escape(k) for k in CREW_KEYS) + r")\b.*$",
    re.DOTALL,
)


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 4)
        if end >= 0:
            text = text[end + 4:].lstrip("\n")
    return text


def strip_crew_trailer(text: str) -> str:
    return CREW_TRAILER_RE.sub("", text)


def body_is_empty(text: str) -> bool:
    """A front-matter file counts as empty (-> skipped) when, after removing
    the YAML front-matter and any HTML comments, only whitespace remains."""
    stripped = HTML_COMMENT_RE.sub("", strip_frontmatter(text))
    return not stripped.strip()


def read_doc(path: Path, *, is_chapter: bool = False) -> str:
    text = path.read_text(encoding="utf-8")
    text = strip_frontmatter(text)
    if is_chapter:
        text = CHAPTER_REF_RE.sub("", text)
    else:
        text = strip_crew_trailer(text)
    return text.rstrip() + "\n"


def part_divider(part: dict) -> str:
    pid = part["id"]
    title = part["title"]
    tagline = part.get("tagline")
    img = (ROOT / part["divider_image"]).resolve()
    alt = f"Part {pid}: {title}"
    chunks = [f"# Part {pid} — {title} {{.part-heading}}\n"]
    if tagline:
        chunks.append(f"::: {{.part-tagline}}\n{tagline}\n:::\n")
    chunks.append(f"::: {{.divider}}\n![{alt}]({img})\n:::\n")
    return "\n".join(chunks)


def normalize_chapter(entry) -> str:
    """Accept either a bare slug string (legacy) or an object with `slug:`
    (+ optional per-chapter metadata). Returns the slug."""
    if isinstance(entry, str):
        return entry
    return entry["slug"]


def main() -> int:
    spine = yaml.safe_load(SPINE.read_text(encoding="utf-8"))
    chapters_dir = ROOT / spine["canonical_text"]
    out = ROOT / spine["manuscript_out"]

    chunks: list[str] = []
    skipped: list[str] = []
    n_chapters = 0

    # 1. front matter
    for entry in spine.get("front_matter", []):
        path = ROOT / entry["file"]
        if not path.exists():
            if entry.get("optional"):
                skipped.append(entry["file"] + " (missing)")
                continue
            raise SystemExit(f"FAIL: front-matter file not found: {entry['file']}")
        if entry.get("optional") and body_is_empty(path.read_text(encoding="utf-8")):
            skipped.append(entry["file"] + " (empty/placeholder)")
            continue
        chunks.append(read_doc(path))

    # 2. parts -> divider + chapters
    for part in spine.get("parts", []):
        chunks.append(part_divider(part))
        for entry in part["chapters"]:
            slug = normalize_chapter(entry)
            cpath = chapters_dir / f"{slug}.md"
            if not cpath.exists():
                raise SystemExit(f"FAIL: chapter not found: {cpath}")
            chunks.append(read_doc(cpath, is_chapter=True))
            n_chapters += 1

    # 3. back matter
    for entry in spine.get("back_matter", []):
        path = ROOT / entry["file"]
        if not path.exists():
            raise SystemExit(f"FAIL: back-matter file not found: {entry['file']}")
        chunks.append(read_doc(path))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(chunks), encoding="utf-8")

    n_parts = len(spine.get("parts", []))
    print(f"assembled {out.relative_to(ROOT)} "
          f"({n_parts} parts, {n_chapters} chapters, {out.stat().st_size} bytes)")
    if skipped:
        print("  skipped optional front matter: " + ", ".join(skipped))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
