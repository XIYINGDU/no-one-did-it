#!/usr/bin/env python3
"""One-off renumber: convert book-wide [^N] footnote refs to per-chapter
superscript hyperlinks, and convert the back-matter Notes section to a visible
References section with chapter subsections and anchored numbered list items.

After:
  - Chapter prose carries `<sup><a href="#cK-M">M</a></sup>` (raw HTML; K is
    the chapter number, M is the per-chapter index starting at 1).
  - book/back-matter/references.md is `# References` + per-chapter
    `## Chapter N — Title` subsections + ordered list items numbered M with an
    `<a id="cK-M"></a>` anchor immediately before each item's text.

Reader experience: click any superscript in chapter prose -> jumps to the
matching anchor in the back-matter References section. Popup behavior gone
(consistent with print/PDF).

Idempotent: re-running on already-converted source is a no-op (no [^N] in
prose; no [^N]: defs in references.md sections that have already been
converted).

Run from the repo root:
    python3 scripts/renumber_footnotes.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = ROOT / "book" / "chapters-v6"
REFS_FILE = ROOT / "book" / "back-matter" / "references.md"

# Match a footnote ref [^N] with at most one preceding space/tab (not newline -
# do not collapse line breaks). The space gets dropped so the superscript sits
# tight against the preceding word.
REF_PATTERN = re.compile(r"[ \t]?\[\^(\d+)\]")

# Match a footnote definition line `[^N]: text` at start of line.
DEF_PATTERN = re.compile(r"^\[\^(\d+)\]:\s*(.*)$", re.MULTILINE)

# Match a chapter subsection in references.md: `## Chapter N — Title` followed
# by body until the next chapter subsection or end of file.
CHAPTER_SECTION_PATTERN = re.compile(
    r"(## Chapter \d+ — [^\n]+\n+)(.*?)(?=\n## Chapter \d+ — |\Z)",
    re.DOTALL,
)

# Old [^N] -> (chap_num, new_M)
global_map: dict[int, tuple[int, int]] = {}


def main() -> int:
    print("Renumbering chapter prose...")
    total_unique = 0
    total_occurrences = 0
    for cfile in sorted(CHAPTERS_DIR.glob("[0-9]*.md")):
        chap_num = int(cfile.name.split("-")[0])
        text = cfile.read_text(encoding="utf-8")

        # Don't touch the chapter's own ## References section (stripped by
        # the assembler anyway; we don't want to mangle the def list there).
        refs_idx = text.find("\n## References")
        prose = text[:refs_idx] if refs_idx >= 0 else text
        rest = text[refs_idx:] if refs_idx >= 0 else ""

        # Walk prose in order, assign per-chapter indices to first occurrence
        # of each unique [^N].
        seen: dict[int, int] = {}
        next_index = 0
        for m in REF_PATTERN.finditer(prose):
            old_N = int(m.group(1))
            if old_N not in seen:
                next_index += 1
                seen[old_N] = next_index
                if old_N in global_map:
                    print(
                        f"  ERROR: ch-{chap_num:02d}: footnote [^{old_N}] "
                        f"already mapped to {global_map[old_N]}"
                    )
                    return 1
                global_map[old_N] = (chap_num, next_index)

        occurrences = len(REF_PATTERN.findall(prose))
        if next_index == 0:
            print(f"  ch-{chap_num:02d}: no [^N] refs in prose, skipped")
            continue

        # Replace each [^N] (with at-most-one leading space/tab) with
        # <sup><a href="#cK-M">M</a></sup>.
        def replace(m, _chap=chap_num, _seen=seen):
            old_N = int(m.group(1))
            new_M = _seen[old_N]
            return f'<sup><a href="#c{_chap}-{new_M}">{new_M}</a></sup>'

        new_prose = REF_PATTERN.sub(replace, prose)
        cfile.write_text(new_prose + rest, encoding="utf-8")
        print(
            f"  ch-{chap_num:02d}: {next_index} unique refs, "
            f"{occurrences} occurrences -> renumbered"
        )
        total_unique += next_index
        total_occurrences += occurrences

    print(
        f"\nTotal: {total_unique} unique refs "
        f"({total_occurrences} occurrences) across chapter prose.\n"
    )

    print("Restructuring references.md...")
    refs_text = REFS_FILE.read_text(encoding="utf-8")
    # Rename top heading if it's still "# Notes"
    if "# Notes\n" in refs_text:
        refs_text = refs_text.replace("# Notes\n", "# References\n", 1)
        print("  renamed `# Notes` -> `# References`")

    def process_section(match):
        header = match.group(1)
        chap_match = re.search(r"## Chapter (\d+)", header)
        chap_num = int(chap_match.group(1))
        body = match.group(2)

        defs_found = list(DEF_PATTERN.finditer(body))
        if not defs_found:
            # Already converted (no [^N]: lines); return section unchanged.
            return match.group(0)

        items: list[str] = []
        warns = 0
        for i, m in enumerate(defs_found, 1):
            old_N = int(m.group(1))
            def_text = m.group(2).rstrip()
            if old_N not in global_map:
                print(
                    f"  WARN ch-{chap_num:02d}: def [^{old_N}] has no prose "
                    f"ref (orphaned); dropped"
                )
                warns += 1
                continue
            ch, new_M = global_map[old_N]
            if ch != chap_num:
                print(
                    f"  WARN ch-{chap_num:02d}: def [^{old_N}] but prose ref "
                    f"is in ch-{ch:02d}; using ch-{ch:02d} anchor"
                )
                warns += 1
            items.append(
                f'{new_M}. <a id="c{chap_num}-{new_M}"></a>{def_text}'
            )

        suffix = f", {warns} warnings" if warns else ""
        print(f"  ch-{chap_num:02d}: {len(items)} defs renumbered" + suffix)
        return header + "\n".join(items) + "\n\n"

    new_refs = CHAPTER_SECTION_PATTERN.sub(process_section, refs_text)
    REFS_FILE.write_text(new_refs, encoding="utf-8")
    print(f"\n  wrote {REFS_FILE.relative_to(ROOT)}")
    n_chapters = len({c for c, _ in global_map.values()})
    print(
        f"\nDone. Global map: {len(global_map)} refs across {n_chapters} chapters."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
