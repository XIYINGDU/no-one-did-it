#!/usr/bin/env python3
"""PostToolUse warn-mode hook: scan book prose for rule-14 violations.

Implements ``.claude/rules/14-authorial-stance.md``: refuse meta-frame
language ("this chapter", "the book", "the reader", "readers", "the
author", etc.), refuse author-voice "you", refuse modal-prescriptive
forms ("you should", "we must remember"), refuse evasive-collective
forms ("people tend to", "many readers will").

Triggered on writes/edits to ``book/evidence/case-files/``, ``book/chapters-v*/``,
``process/review-memos/``, and ``book/proposals/``.

The hook is **warn-only**. The chapter-promotion gate in
``check-agent-frontmatter.py`` remains the only deny path.

Exemptions
----------
- Inside fenced code blocks (``` ... ```)
- Inside verbatim double-quoted spans ("..." and Unicode curly-quote spans)
- Inside Markdown blockquotes (lines beginning with `>`)
- Inside frontmatter (between leading `---` and the next `---`)
- Inside intra-crew sections (e.g. lines under `## Findings for xaiolai`
  or similar `## Annotations` / `## Notes for ...` headers that signal
  crew-internal metadata not reader-facing)
- Headings (lines starting with `#`) are partially exempted: "the book"
  is permitted in headings like "About the Book" but flagged in prose.
"""

import json
import re
import sys
from pathlib import Path


# Scope: scan reader-facing prose only. Briefs (*-brief.md) are architecture
# artifacts that legitimately discuss "the chapter" / "the reader" / "the book"
# as the OBJECT of architectural design; they are not reader-facing and are
# exempted from rule 14 (which governs author voice in reader-facing prose).
SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/(?!.*-brief\.md$).*\.md$"
)

# Patterns that flag rule-14 violations.

META_FRAME_PATTERNS = (
    (re.compile(r"\bthis chapter\b", re.IGNORECASE), "meta-frame:this-chapter",
     "drop 'this chapter' — refer to structure ('we', 'now', 'earlier') not to the object"),
    (re.compile(r"\bthe chapter('s|s)?\b", re.IGNORECASE), "meta-frame:the-chapter",
     "drop 'the chapter' — let the prose carry the point without naming the container"),
    (re.compile(r"\bthe book\b", re.IGNORECASE), "meta-frame:the-book",
     "drop 'the book' — name 'we' (co-investigator) or 'the pattern' (diagnostic)"),
    (re.compile(r"\bthe reader(?:'s|s)?\b", re.IGNORECASE), "meta-frame:the-reader",
     "drop 'the reader' — use 'we' (co-investigator stance)"),
    (re.compile(r"\breaders\b", re.IGNORECASE), "meta-frame:readers",
     "drop 'readers' — use 'we' or name the specific group ('citizens reading news of...')"),
    (re.compile(r"\bthis section\b", re.IGNORECASE), "meta-frame:this-section",
     "drop 'this section' — just do the work the section does"),
    (re.compile(r"\bthis passage\b", re.IGNORECASE), "meta-frame:this-passage",
     "drop 'this passage' — let the passage speak"),
    (re.compile(r"\bthis paragraph\b", re.IGNORECASE), "meta-frame:this-paragraph",
     "drop 'this paragraph' — let the paragraph speak"),
    (re.compile(r"\bthe author(?:'s|s)?\b", re.IGNORECASE), "meta-frame:the-author",
     "drop 'the author' — use 'I' for authorial position-taking or 'we' for collective"),
    (re.compile(r"\bin this (chapter|section|book)\b", re.IGNORECASE),
     "meta-frame:in-this-x",
     "drop 'in this chapter/section/book' — use 'earlier' / 'now' / 'we saw' instead"),
    (re.compile(r"\bearlier in (?:this )?(chapter|book|section)\b", re.IGNORECASE),
     "meta-frame:earlier-in-x",
     "use 'we saw earlier' (drop the container reference)"),
)

# Author-voice "you" patterns. Permitted only inside cited quotes (handled
# by the strip-quotes pass below).
YOU_PATTERNS = (
    (re.compile(
        r"\byou (?:will|may|might|should|must|need|ought|can|are|have|do|don'?t|"
        r"won'?t|can'?t|haven'?t|tend|find|see|notice|feel|know|think)\b",
        re.IGNORECASE), "you:address",
     "reframe 'you ...' to 'we ...' or imperative ('Ask in writing')"),
    (re.compile(r"\byour\b", re.IGNORECASE), "you:your",
     "reframe 'your X' to 'our X' or drop possessive"),
    (re.compile(r"\byourself\b", re.IGNORECASE), "you:yourself",
     "reframe 'yourself' to 'ourselves'"),
    (re.compile(r"\bfor you\b", re.IGNORECASE), "you:for-you",
     "reframe 'for you' to 'for us'"),
    (re.compile(r"\bto you\b", re.IGNORECASE), "you:to-you",
     "reframe 'to you' to 'to us'"),
    (re.compile(r"\bif you (?:are|find|see|have|encounter|meet|notice|feel|sign|read)\b",
                re.IGNORECASE), "you:if-you",
     "reframe 'if you X' to 'if we X' (or 'those of us who' + imperative)"),
)

MODAL_PRESCRIPTIVE_PATTERNS = (
    (re.compile(r"\byou (?:should|must|ought|need to)\b", re.IGNORECASE),
     "modal:you-should",
     "reframe to imperative ('Ask in writing', not 'you should ask')"),
    (re.compile(r"\bwe (?:should|must) (?:remember|never|always|note)\b",
                re.IGNORECASE), "modal:we-should-remember",
     "reframe to imperative; moralizing-cadence is forbidden even in 'we' form"),
)

EVASIVE_COLLECTIVE_PATTERNS = (
    (re.compile(
        r"\b(?:people|anyone|many readers|most readers|one) "
        r"(?:tend|tends|may|might|will|should|finds?|sees?|notes?|"
        r"assumes?|believes?|thinks?)\b", re.IGNORECASE),
     "evasive:people-tend-to",
     "name the specific group ('citizens reading news of...') or use 'we'"),
)

ALL_PATTERNS = (
    META_FRAME_PATTERNS + YOU_PATTERNS
    + MODAL_PRESCRIPTIVE_PATTERNS + EVASIVE_COLLECTIVE_PATTERNS
)

# Exempt sections — once we enter one, we don't scan until we exit.
INTRA_CREW_SECTION_RE = re.compile(
    r"^##\s+(Findings for xaiolai|Annotations(?:\s+and\s+handoff)?|Notes for crew|"
    r"Crew notes|Handoff\s*$)",
    re.IGNORECASE | re.MULTILINE,
)

# Headers that legitimately name "the book" / "the chapter" (front-matter,
# table-of-contents). We skip lines starting with `#`.
HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)

# Quote / code-block strippers (same pattern as scan-overclaim).
QUOTED_RE = re.compile(r'"[^"\n]+"|“[^”\n]+”')


def _strip_exempt_regions(text: str) -> str:
    """Blank out fenced code blocks, frontmatter, intra-crew sections,
    blockquotes, double-quoted spans, and Markdown headings so that
    pattern matches inside them are not flagged. Preserves line structure
    so line numbers in findings remain accurate."""
    # 1. Fenced code blocks
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"),
                  text, flags=re.DOTALL)
    # 2. Frontmatter (between leading `---` and the next `---`)
    if text.startswith("---\n"):
        fm_close = text.find("\n---", 4)
        if fm_close >= 0:
            fm_end = fm_close + 4
            text = ("\n" * text[:fm_end].count("\n")) + text[fm_end:]
    # 3. Intra-crew sections (## Findings for ..., etc.) — blank from
    #    the header through end of file or until next H1/H2 of the same level.
    section_match = INTRA_CREW_SECTION_RE.search(text)
    if section_match:
        before = text[:section_match.start()]
        after = text[section_match.start():]
        # Take the intra-crew section to the next H2/H1 boundary (rare in
        # these chapters since intra-crew sections sit at chapter end)
        next_h_match = re.search(r"\n##?\s+(?!Findings for|Annotations|Notes for|Crew notes|Handoff)",
                                 after[1:])
        if next_h_match:
            crew_end = 1 + next_h_match.start()
            text = before + ("\n" * after[:crew_end].count("\n")) + after[crew_end:]
        else:
            text = before + ("\n" * after.count("\n"))
    # 3b. Trailing bare-schema crew block: many chapters end with a `---`
    #     separator followed by an Owner: / Task: / Inputs: / ... / Handoff:
    #     schema block (the project's default artifact-output schema). This
    #     is intra-crew metadata per rule 14 edge case 12; exempt the whole
    #     trailing block. Pattern: a `---` line followed within a few lines
    #     by an `Owner:` line, then take to end of file.
    schema_match = re.search(
        r"^---\s*$.*?^(?:Owner|Task):", text, re.MULTILINE | re.DOTALL,
    )
    if schema_match:
        text = text[:schema_match.start()] + ("\n" * text[schema_match.start():].count("\n"))
    # 3c. Whole-document review-memo exemption: review-memos are
    #     intrinsically meta-frame — Nancy / Laura / Stephen review "the
    #     book" / "the chapter" by definition. When a document opens with
    #     the project's default Owner: / Task: / Inputs: / ... / Handoff:
    #     schema header at the top (within the first ~30 non-blank lines),
    #     treat the whole document as intra-crew per rule 14 edge case 12.
    #     This is distinct from 3b (trailing schema block) — here the
    #     schema IS the document, not an appendix.
    head = text[:3000]  # first ~30-60 lines
    if re.search(r"^Owner:\s", head, re.MULTILINE) and \
       re.search(r"^Task:\s", head, re.MULTILINE):
        # Whole-doc exemption — blank everything but preserve newlines so
        # line numbers in any other concurrent reporting stay accurate.
        text = "\n" * text.count("\n")
    # 4. Blockquotes: lines starting with `>`
    text = re.sub(r"^>.*$", "", text, flags=re.MULTILINE)
    # 5. Markdown headings: blank the heading content but preserve the line
    text = re.sub(r"^#{1,6}\s+[^\n]*$", "", text, flags=re.MULTILINE)
    # 6. Double-quoted spans (cited verbatim quotes per rule 06)
    text = QUOTED_RE.sub(lambda m: " " * len(m.group(0)), text)
    return text


def scan(text: str) -> list[tuple[int, str, str, str]]:
    """Return findings: (line_number, pattern-name, snippet, fix-hint)."""
    findings: list[tuple[int, str, str, str]] = []
    sanitized = _strip_exempt_regions(text)
    original_lines = text.splitlines()
    for lineno, line in enumerate(sanitized.splitlines(), start=1):
        if not line.strip():
            continue
        for pattern, name, fix in ALL_PATTERNS:
            if pattern.search(line):
                orig_line = (original_lines[lineno - 1]
                             if lineno <= len(original_lines) else "")
                snippet = orig_line.strip()[:120]
                findings.append((lineno, name, snippet, fix))
    return findings


def _extract_path(tool_input: dict) -> str:
    for key in ("file_path", "path"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def _emit(context: str) -> None:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        }
    }))


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    inp = data.get("tool_input") or {}
    raw_path = _extract_path(inp)
    if not raw_path:
        sys.exit(0)

    path = Path(raw_path)
    if not path.is_absolute():
        path = Path(data.get("cwd") or ".") / path
    if not path.exists():
        sys.exit(0)

    project_root = Path(__file__).resolve().parents[2]
    try:
        rel = path.resolve().relative_to(project_root).as_posix()
    except ValueError:
        sys.exit(0)
    if not SCOPE_RE.match(rel):
        sys.exit(0)

    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        sys.exit(0)

    findings = scan(text)
    if not findings:
        _emit(f"Warn mode: scan-pronoun-discipline passed for {rel}.")
        return

    lines = [
        f"Warn mode: scan-pronoun-discipline flagged {len(findings)} rule-14 violation(s) in {rel}:"
    ]
    for lineno, name, snippet, fix in findings[:10]:
        lines.append(f"  L{lineno} [{name}] {snippet}")
        lines.append(f"     → {fix}")
    if len(findings) > 10:
        lines.append(f"  ... and {len(findings) - 10} more.")
    _emit(" ".join(lines))


if __name__ == "__main__":
    main()
