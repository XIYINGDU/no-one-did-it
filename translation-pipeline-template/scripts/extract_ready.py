#!/usr/bin/env python3
"""Extract clean target-language text from bilingual translation draft.

Reads a bilingual draft (source blocks + translation blocks + notes),
outputs a clean target-language file with frontmatter + body + references.

Usage:
    python3 scripts/extract_ready.py <chapter-slug>
    python3 scripts/extract_ready.py 01-the-altar-moves

The script reads from {{TRANSLATION_DIR}}/chapters/<slug>-draft.md
and writes to {{TRANSLATION_DIR}}/ready/<slug>.md.
"""

import sys
import re
import os

# --- Configurable paths (replaced by init script) ---
TRANSLATION_DIR = "{{TRANSLATION_DIR}}"


def extract_clean(slug: str) -> int:
    draft_path = os.path.join(TRANSLATION_DIR, "chapters", f"{slug}-draft.md")
    ready_path = os.path.join(TRANSLATION_DIR, "ready", f"{slug}.md")

    if not os.path.exists(draft_path):
        print(f"ERROR: draft not found: {draft_path}")
        return 1

    with open(draft_path, "r") as f:
        content = f.read()

    lines = content.split("\n")
    output = []
    in_frontmatter = False
    frontmatter_done = False
    in_source = False
    in_notes = False
    in_translation = False
    in_references = False

    for line in lines:
        # Frontmatter
        if line.strip() == "---" and not frontmatter_done:
            if not in_frontmatter:
                in_frontmatter = True
                output.append(line)
                continue
            else:
                in_frontmatter = False
                frontmatter_done = True
                output.append(line)
                continue

        if in_frontmatter:
            output.append(line)
            continue

        # Chapter title
        if line.strip().startswith("# ") and "章" in line:
            output.append(line)
            output.append("")
            continue

        # Section headings
        if line.strip().startswith("## "):
            in_source = in_translation = in_notes = False
            output.append("")
            output.append(line)
            output.append("")
            continue

        # References section
        if line.strip() == "## References":
            in_references = True
            in_source = in_translation = in_notes = False
            output.append("")
            output.append(line)
            output.append("")
            continue

        # HTML comment in References
        if in_references and line.strip().startswith("<!--"):
            continue

        # Footnote definitions
        if in_references and line.strip().startswith("[^"):
            output.append(line)
            continue

        # Note about references
        if in_references and line.strip().startswith("> 注："):
            output.append("")
            output.append(line)
            break

        # Source blocks
        if line.strip() == "**原文：**":
            in_source, in_translation, in_notes = True, False, False
            continue

        # Translation blocks
        if line.strip() == "**译文：**":
            in_source, in_translation, in_notes = False, True, False
            continue

        # Notes blocks
        if line.strip() == "**翻译笔记：**":
            in_source, in_translation, in_notes = False, False, True
            continue

        # Separator
        if line.strip() == "---" and not in_frontmatter:
            in_source = in_translation = in_notes = False
            continue

        if in_source or in_notes:
            continue

        if in_translation:
            output.append(line)

    # Clean excessive blank lines
    result = "\n".join(output)
    result = re.sub(r"\n{4,}", "\n\n\n", result)
    result = re.sub(r"\n{3,}", "\n\n", result)

    os.makedirs(os.path.dirname(ready_path), exist_ok=True)
    with open(ready_path, "w") as f:
        f.write(result)

    print(f"Done: {draft_path} → {ready_path} ({len(result.split(chr(10)))} lines)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <chapter-slug>")
        sys.exit(1)
    sys.exit(extract_clean(sys.argv[1]))
