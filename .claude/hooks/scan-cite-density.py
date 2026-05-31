#!/usr/bin/env python3
"""PostToolUse warn-mode hook: scan book prose for verbose inline ``[CITE:]``
markers that violate the rule-13 slug-only invariant.

Implements ``.claude/rules/13-citation-form.md`` Layer-2 discipline: inline
``[CITE:]`` brackets carry only card slugs separated by ``;``. No commas,
no embedded citation metadata, no "see also", no archive notes, no tier-1
corroboration lists. The full citation apparatus lives in the source-ledger
card (Layer 3, compile-generated).

Triggered on writes/edits to ``book/evidence/case-files/``, ``book/chapters-v*/``,
``process/review-memos/``, and ``book/proposals/``. Sibling to scan-overclaim
and scan-implication.

Mode: **warn-only initially.** Block-mode candidate after corpus migration
sweep completes and the existing verbose ``[CITE:]`` brackets are normalized.

Allowed forms:
- ``[CITE: card-slug]``                                          single slug
- ``[CITE: card-slug; another-slug]``                            multi-slug
- ``[CITE: card-slug — pending-stephen-lock]``                   pending marker
- ``[EVIDENCE NEEDED: <description>]``                           legacy gap marker (rule 30)
- ``[HEDGE: <description>]``                                     legacy hedge marker

Disallowed forms (flagged):
- ``[CITE: Author, "Title," Journal vol. issue (year).]``        full citation in bracket
- ``[CITE: Speaker, date, time; reproduced in tier-1 sources.]`` corroboration apparatus
- ``[CITE: ... archived at ...]``                                archive metadata
- Any inline ``[CITE:]`` over 60 characters total (signals embedded apparatus)
"""

import json
import re
import sys
from pathlib import Path


SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/.*\.md$"
)

# Captures [CITE: ...] with non-greedy match up to first ]
CITE_RE = re.compile(r"\[CITE:\s*([^\]]*?)\s*\]")

# Allowed content inside [CITE:] after the leading whitespace:
# - one or more slugs (lowercase-kebab-case-with-digits) separated by ';'
# - optional " — pending-stephen-lock" suffix on a single-slug marker
SLUG_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")

PENDING_SUFFIX_RE = re.compile(
    r"^\s*(?P<slug>[a-z0-9]+(?:[-_][a-z0-9]+)*)\s*[—-]\s*pending-stephen-lock\s*$"
)

MAX_BRACKET_LENGTH = 80  # raised from 60 after Wave-1 migration: court-case + multilateral-instrument slugs (e.g., un-ga-resolution-68-262-territorial-integrity-ukraine-2014-03-27, blackwater-nisour-square-doj-indictment-and-state-dept-record) legitimately exceed 60 chars without embedded metadata; 80 still catches the hidden-metadata pattern (typical embedded text pushes a slug-shaped bracket to 90+ chars)

# Fenced code blocks are exempt
def _strip_codeblocks(text: str) -> str:
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"),
                  text, flags=re.DOTALL)


def _classify(content: str) -> str | None:
    """Return None if the bracket is valid; else a short reason string."""
    raw = content.strip()
    if not raw:
        return "empty"

    # Pending-stephen-lock suffix on a single slug
    if PENDING_SUFFIX_RE.match(content):
        return None

    # One or more semicolon-separated slugs
    parts = [p.strip() for p in raw.split(";")]
    for p in parts:
        if not SLUG_RE.match(p):
            # The most common failure modes:
            if "," in p:
                return "contains comma (full-citation pattern; should be card slug only)"
            if '"' in p or "'" in p:
                return "contains quote characters (looks like in-prose citation)"
            if any(word in p.lower() for word in ("reproduced", "archived", "tier-1",
                                                  "verbatim", "see also", "corroborated",
                                                  "verify", "stephen verify")):
                return "contains citation-apparatus phrasing (move to card)"
            return f"non-slug content: '{p[:40]}'"
    return None


def scan(text: str) -> list[tuple[int, str, str, str]]:
    """Return findings: list of (line_number, snippet, reason, suggested-fix).

    A bracket is flagged when its content fails classification (commas,
    quote marks, citation-apparatus phrasing). The length cap is a fallback
    for single-slug brackets whose content classifies as slug-shaped but is
    suspiciously long — typically a slug with embedded metadata that snuck
    past classify(). Valid multi-slug and pending-lock brackets are exempt
    from the length cap because their length scales legitimately with
    content."""
    findings: list[tuple[int, str, str, str]] = []
    sanitized = _strip_codeblocks(text)
    lines = sanitized.splitlines()
    for lineno, line in enumerate(lines, start=1):
        for match in CITE_RE.finditer(line):
            raw_bracket = match.group(0)
            content = match.group(1)
            classify_violation = _classify(content)
            # Length check applies only to single-slug brackets that
            # passed classification — catches malformed slugs that look
            # slug-like but carry hidden metadata.
            is_single_slug = ";" not in content and "pending-stephen-lock" not in content
            length = len(raw_bracket)
            length_violation = (
                is_single_slug
                and classify_violation is None
                and length > MAX_BRACKET_LENGTH
            )
            if length_violation or classify_violation:
                snippet = raw_bracket.strip()
                if len(snippet) > 120:
                    snippet = snippet[:117] + "..."
                if length_violation:
                    reason = (
                        f"single-slug bracket length {length} chars exceeds "
                        f"{MAX_BRACKET_LENGTH} (suspicious for hidden metadata)"
                    )
                else:
                    reason = classify_violation
                fix = ("replace bracket content with the source-ledger card slug "
                       "(e.g., [CITE: <card-slug>]); move citation apparatus to the card")
                findings.append((lineno, snippet, reason, fix))
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
        _emit(f"Warn mode: scan-cite-density passed for {rel}.")
        return

    lines = [
        f"Warn mode: scan-cite-density flagged {len(findings)} verbose [CITE:] bracket(s) in {rel} (rule 13):"
    ]
    for lineno, snippet, reason, fix in findings[:10]:
        lines.append(f"  L{lineno} [{reason}] {snippet}")
        lines.append(f"     → {fix}")
    if len(findings) > 10:
        lines.append(f"  ... and {len(findings) - 10} more.")
    _emit(" ".join(lines))


if __name__ == "__main__":
    main()
