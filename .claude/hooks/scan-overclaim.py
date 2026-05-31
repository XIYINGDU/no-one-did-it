#!/usr/bin/env python3
"""PostToolUse warn-mode hook: scan book prose for over-claim verbs that lack
explicit citation or hedging.

Triggered on writes/edits to ``book/evidence/case-files/``, ``book/chapters-v*/``,
``process/review-memos/``, and ``book/proposals/``. Implements
``.claude/rules/05-overclaim-language.md``.

The hook is **warn-only**. It never returns ``permissionDecision: deny`` —
the chapter-promotion gate in ``check-agent-frontmatter.py`` is the only
deny path in the project (per the Phase 3 architecture decision).

Heuristic, not strict: the scanner errs on the side of warning. False
positives are cheap (a one-line note in additionalContext); false negatives
let real overclaim ship.
"""

import json
import re
import sys
from pathlib import Path


SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/.*\.md$"
)

# Banned verbs / phrases that signal possible over-claim. Each entry is
# (regex, short-name, suggested-treatment).
PATTERNS: tuple[tuple[re.Pattern[str], str, str], ...] = (
    (re.compile(r"\b(knew|knew about|was aware that|were aware that)\b", re.IGNORECASE),
     "knew",
     "cite the source proving knowledge or rewrite to qualify"),
    (re.compile(r"\b(deliberately|intentionally|on purpose)\b", re.IGNORECASE),
     "deliberately",
     "cite a source documenting intent (admission, jury finding, recorded statement)"),
    (re.compile(r"\b(guilty|is guilty of|was guilty of)\b", re.IGNORECASE),
     "guilty",
     "cite the court of conviction + date, or replace with 'was charged with' / 'was accused of'"),
    (re.compile(r"\b(lied|lied about)\b", re.IGNORECASE),
     "lied",
     "cite the documented falsehood + contemporaneous knowledge of falsity; otherwise 'misstated'"),
    (re.compile(r"\b(proves|definitively shows|definitively proves)\b", re.IGNORECASE),
     "proves",
     "use 'supports' / 'indicates' / 'is consistent with' unless citing a final adjudication"),
    (re.compile(r"\b(must have|would have) (known|been|seen|read|done)\b", re.IGNORECASE),
     "must-have",
     "forbidden for mental-state attribution; use only documented facts"),
    (re.compile(r"\b(clearly|obviously|undeniably)\b", re.IGNORECASE),
     "clearly",
     "forbidden as evidence-replacement adverb; cite the source that makes it clear"),
)

# Hedging / attribution patterns that, if present in the same line, neutralize
# the warning. A line that contains both an over-claim verb AND a hedge is
# not flagged (the author is doing the right thing). Plain (non-verbose)
# regex — VERBOSE mode would silently strip the spaces inside these patterns.
HEDGE_PATTERNS = (
    r"\[CITE:[^\]]+\]",
    r"\[EVIDENCE NEEDED:[^\]]+\]",
    r"\[HEDGE:[^\]]+\]",
    # Markdown footnote references — actual citation form in v6 prose
    r"\[<sup>\d+</sup>\]",
    r"\[\^\d+\]",
    r"according to \w",
    r"reported (?:that|by)",
    r"per the ",
    r"court records show",
    r"as documented in",
    r"(?:as of|on) \d{4}",
    r"the (?:DPA|DOJ|FAA|SEC|FTC|GAO|FBI|OHCHR|ICC|UN|EPA|HHS|OIG|SSCI|HHRC|HREOC|CARB|NHTSA|NTSB|MOD|FCO|HSE|FCA|PRA|EBA|FATF)(?:[^.;\n]{0,250}?)?\s+(?:says|admits|charges|found|reported|documented|concluded|established)",
    r"(?:per|according to) the [A-Z][A-Za-z\s'-]+? (?:report|review|inquiry|investigation|opinion|judgment|ruling|finding|memorandum|order)",
    # Procedural-stage phrasings that ARE the rule-05 required citation form
    # — "pleaded guilty" / "found guilty" / "guilty plea" / "was convicted"
    # explicitly cite the procedural stage (rule 05 says to replace bare
    # "guilty" with "was charged with" or cite the conviction; these forms
    # already do that).
    r"pleaded guilty",
    r"plead(?:ed)? (?:guilty|nolo)",
    r"(?:was|were|been) (?:found|convicted) guilty",
    r"guilty plea",
    r"jury found",
    r"court convicted",
    # Generic court-attribution: "the Court of Appeal held", "the trial court
    # found", "the District Court ruled", "X J held that" — these are the
    # proper citation form for claims grounded in a ruling.
    r"(?:the )?(?:Court|court of \w+|District Court|Supreme Court|trial court|appellate court|tribunal) (?:held|found|ruled|noted|wrote|determined)",
    r"\w+ J(?:\.|udge|ustice)? (?:held|found|ruled|wrote|noted|determined)",
    # Documentary-record framing — "the documentary record establishes X",
    # "the documentary record shows X" — rule-05's required source-attribution form.
    r"the documentary record (?:establishes|shows|documents)",
    # Methodology / instrument framings — when the text instructs the
    # reader to apply the diagnostic ("ask, in writing, …", "the diagnostic
    # is question N"), the trigger verb is part of the framework's
    # template, not an assertion.
    r"ask,? in writing",
    r"question \d+",
    r"the diagnostic is",
    r"the question carries",
)
HEDGE_RE = re.compile("|".join(HEDGE_PATTERNS), re.IGNORECASE)

# Footnote-definition lines (Markdown `[^N]: ...`) are citation-only
# prose, not the chapter's narrative voice; their content typically
# references court cases, statutes, and plea agreements that legitimately
# use rule-05's verbs.
FOOTNOTE_DEF_RE = re.compile(r"^\s*\[\^[^\]]+\]:\s")

# Diagnostic questions like "Who knew or should have known?" or
# "*Question four: who knew or should have known?*" are the framework's
# question-form, not assertions about who knew. Match both italicised
# and plain forms.
DIAGNOSTIC_QUESTION_RE = re.compile(
    # italicised: *(Question N: )?Who knew...?*
    r"\*(?:question \w+:\s*)?(?:who|what|when|where|why|how)\b[^*]{1,150}\?\*"
    # plain at line/sentence boundary: "Who knew or should have known?"
    # "Question four: who knew or should have known?" etc. Matches the
    # canonical 8 question forms regardless of italics.
    r"|(?:^|[.!?]\s|\n)(?:question \w+:\s+)?"
    r"(?:who|what)\s+(?:was|had|knew|could|controlled|bore|would|benefited)\b"
    r"[^.!?\n]{0,140}\?",
    re.IGNORECASE | re.MULTILINE,
)

# Quote markers — content inside double-quoted strings is exempt because it
# may be a verbatim quotation that legitimately uses the verb.
QUOTED_RE = re.compile(r'"[^"\n]+"')


def _strip_quotes_and_codeblocks(text: str) -> str:
    """Return a copy of `text` with quoted-text and fenced code-block content
    blanked out. Over-claim verbs inside quotations are exempt (per rule 06,
    verbatim quotes may use any verb the source uses)."""
    # Blank fenced code blocks
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)
    # Blank double-quoted spans
    text = QUOTED_RE.sub(lambda m: " " * len(m.group(0)), text)
    return text


# Structural surfaces that aren't the chapter's own reader-facing prose
# and therefore shouldn't trigger overclaim warnings:
#   - YAML frontmatter (between the first `---` and second `---`)
#   - Markdown headings (`# ` through `###### `)
#   - Block-quote lines (`> ...`) — verbatim quotation; rule 06 governs
#   - Table rows (`| ... |`) — visual summary cells, attribution lives
#     in adjacent prose or parenthetical citation
HEADING_RE = re.compile(r"^\s*#{1,6}\s")
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")

# Negation: a match is cleared if 'not ' or 'never ' appears within 40 chars
# before the trigger verb on the same line. Handles framework
# meta-discussion ("the diagnostic does not declare anyone guilty",
# "never deliberately", "is not guilty of") common in this book.
NEGATION_RE = re.compile(r"\b(?:not|never|no)\b", re.IGNORECASE)


def _frontmatter_end_line(text: str) -> int:
    """Return the 1-indexed line number AFTER the closing `---` of YAML
    frontmatter, or 0 if no frontmatter is present."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i + 2  # line after the closing ---, 1-indexed
    return 0


def _is_skippable_structural(line: str) -> bool:
    """True if the line is structural (heading, block-quote, table row)
    rather than the chapter's reader-facing prose."""
    s = line.lstrip()
    if not s:
        return False
    if HEADING_RE.match(line):
        return True
    if s.startswith(">"):
        return True
    if TABLE_ROW_RE.match(line):
        return True
    return False


def _is_negated_match(line: str, match_start: int) -> bool:
    """True if 'not' / 'never' / 'no' appears within 40 chars before the
    trigger verb on the same line."""
    window_start = max(0, match_start - 40)
    window = line[window_start:match_start]
    return bool(NEGATION_RE.search(window))


def scan(text: str) -> list[tuple[int, str, str, str]]:
    """Return findings: list of (line_number, verb-name, line-snippet, treatment)."""
    findings: list[tuple[int, str, str, str]] = []
    sanitized = _strip_quotes_and_codeblocks(text)
    fm_end = _frontmatter_end_line(text)
    orig_lines = text.splitlines()
    for lineno, line in enumerate(sanitized.splitlines(), start=1):
        # 1. skip YAML frontmatter
        if fm_end and lineno < fm_end:
            continue
        # 2. skip structural surfaces (heading, block-quote, table row)
        if _is_skippable_structural(line):
            continue
        # 3. skip footnote definitions (`[^N]: ...`) — citation-only prose
        if FOOTNOTE_DEF_RE.match(line):
            continue
        # 4. existing hedge-pattern exemption
        if HEDGE_RE.search(line):
            continue
        # 5. pattern check, with negation + diagnostic-question guards per match
        for pattern, name, treatment in PATTERNS:
            m = pattern.search(line)
            if not m:
                continue
            if _is_negated_match(line, m.start()):
                continue
            # Skip if the match sits inside an italicized diagnostic question
            # like "*Who knew or should have known?*" — the question is the
            # framework template, not an assertion.
            if _match_in_diagnostic_question(line, m.start(), m.end()):
                continue
            orig_line = orig_lines[lineno - 1] if lineno <= len(orig_lines) else ""
            snippet = orig_line.strip()[:120]
            findings.append((lineno, name, snippet, treatment))
    return findings


def _match_in_diagnostic_question(line: str, match_start: int, match_end: int) -> bool:
    """True if the trigger-verb match falls inside an italicised diagnostic
    question span on the same line."""
    for q in DIAGNOSTIC_QUESTION_RE.finditer(line):
        if q.start() <= match_start and match_end <= q.end():
            return True
    return False


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

    # Resolve to project-relative; only scan files inside book/
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
        _emit(f"Warn mode: scan-overclaim passed for {rel}.")
        return

    lines = [f"Warn mode: scan-overclaim flagged {len(findings)} possible over-claim(s) in {rel}:"]
    for lineno, name, snippet, treatment in findings[:10]:
        lines.append(f"  L{lineno} [{name}] {snippet}")
        lines.append(f"     → {treatment}")
    if len(findings) > 10:
        lines.append(f"  ... and {len(findings) - 10} more.")
    _emit(" ".join(lines))


if __name__ == "__main__":
    main()
