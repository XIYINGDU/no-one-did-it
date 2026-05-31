#!/usr/bin/env python3
"""PostToolUse warn-mode hook: scan book prose for narrative implication
that asserts mental state, motive, knowledge, causation, or chain
responsibility without citation or hedge.

Sibling to ``scan-overclaim.py``. Implements ``.claude/rules/07-implication-burden.md``.

Triggered on writes/edits to ``book/evidence/case-files/``, ``book/chapters-v*/``,
``process/review-memos/``, and ``book/proposals/``.

The hook is **warn-only** at first; the spec allows promotion to block-mode
after a 5-chapter false-positive-rate calibration per rule 09. The chapter-
promotion gate in ``check-agent-frontmatter.py`` remains the only deny path
until that calibration runs.

Heuristics:
- "Adjacent benefit" pattern: a paragraph mentioning a decision or order
  followed within 3 lines by a paragraph naming who profited / acquired /
  received / benefited. Implies intent.
- "Chain ladder" pattern: three or more proper nouns introduced with a
  hierarchical verb (authorized, approved, signed off, ordered, instructed)
  in adjacent sentences. Implies documented chain authorization.
- "Sympathetic-then-cold" cut: a paragraph using sympathetic descriptors
  for an actor immediately followed by an analytical paragraph naming a
  chain that "engineered" / "produced" / "manufactured" the actor's harm.
- "Anonymous chain reference": "someone in the chain", "a higher office",
  "approval came from above", "the decision was made", "instructions came
  down" — implies a real but unnamed authority.
- "Causation by adjacency": two date-stamped events within two lines with
  no causal-link source citation.

False-positive control:
- A flagged passage clears if a hedge / citation pattern appears within the
  same paragraph OR the immediately adjacent paragraph (per rule 07 spec).
- Verbatim quotations are exempt (per rule 06).
- Fenced code blocks are exempt.

Protocol:

- Stdin: JSON envelope from Claude Code with ``tool_input.file_path`` (or
  ``tool_input.path``) naming the just-edited file, and an optional
  ``cwd`` for resolving relative paths.
- Stdout: a single JSON object with ``hookSpecificOutput.additionalContext``
  carrying the warn message. Reports "passed" when no implication pattern
  fires; otherwise lists up to 10 findings (line + pattern + suggested
  treatment).
- Exit codes: 0 always. Block-mode after rule-09 calibration would return
  a permissionDecision="deny" payload; that path is not active yet.
"""

import json
import re
import sys
from pathlib import Path


SCOPE_RE = re.compile(
    r"^(process/review-memos|book/evidence/case-files|book/(chapters-v\d+|proposals))/.*\.md$"
)

# Patterns are scanned at the paragraph level. Each entry is
# (name, paragraph-pair-checker, suggested treatment).

ANONYMOUS_CHAIN_RE = re.compile(
    r"\b(someone in the chain|a higher office|approval came from above|"
    r"instructions came down|the decision was made|orders came from|"
    r"the chain decided|the office signed off|approval was granted|"
    r"someone authorized|someone approved|was authorized by a)\b",
    re.IGNORECASE,
)

HIERARCHICAL_VERB_RE = re.compile(
    r"\b(authorized|approved|signed off|ordered|instructed|directed|sanctioned|"
    r"green[- ]?lit|cleared|countersigned)\b",
    re.IGNORECASE,
)

BENEFIT_LANGUAGE_RE = re.compile(
    r"\b(profited|acquired|received|gained|benefited|enriched|netted|"
    r"walked away with|cashed out|collected|pocketed)\b",
    re.IGNORECASE,
)

DECISION_LANGUAGE_RE = re.compile(
    r"\b(decided|chose|opted|moved to|elected to|agreed to|signed|"
    r"approved|authorized|issued the order|gave the green light)\b",
    re.IGNORECASE,
)

SYMPATHETIC_DESCRIPTOR_RE = re.compile(
    r"\b(young|inexperienced|junior|exhausted|untrained|"
    r"alone|isolated|frightened|new to the job|first day|"
    r"struggling|overwhelmed|in over (?:his|her|their) head)\b",
    re.IGNORECASE,
)

# Engineering verbs tightened to strong-implication only. Generic
# 'produced' / 'set up' / 'designed' / 'arranged' / 'constructed'
# are common in descriptive prose (court 'produced findings', courts
# 'set up' procedures, etc.) and don't on their own carry the
# 'engineered the harm' implication rule 07 targets.
ENGINEERING_VERB_RE = re.compile(
    r"\b(engineered|orchestrated|manufactured|fabricated|architected|"
    r"set the conditions for|stage-managed)\b",
    re.IGNORECASE,
)

DATE_RE = re.compile(
    r"\b("
    r"\d{1,2}\s+(?:January|February|March|April|May|June|July|August|"
    r"September|October|November|December)\s+\d{4}"
    r"|"
    r"(?:January|February|March|April|May|June|July|August|"
    r"September|October|November|December)\s+\d{1,2},?\s+\d{4}"
    r"|"
    r"\d{4}-\d{2}-\d{2}"
    r")\b"
)

PROPER_NOUN_PHRASE_RE = re.compile(
    r"\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2}\b"
)

# Hedge / citation patterns that clear a paragraph.
HEDGE_RE = re.compile(
    r"("
    r"\[CITE:[^\]]+\]"
    r"|\[EVIDENCE NEEDED:[^\]]+\]"
    r"|\[HEDGE:[^\]]+\]"
    # Markdown footnote references — the actual citation form in v6 prose.
    # `[<sup>N</sup>](#cX-N)` (pandoc-rendered) and `[^N]` (raw).
    r"|\[<sup>\d+</sup>\]"
    r"|\[\^\d+\]"
    r"|the record does not (?:establish|show|name|identify)"
    r"|no document in the public record"
    r"|per the (?:inquiry|court|inspector|investigation|ruling|finding)"
    r"|reconstructed this sequence"
    r"|the underlying authorization remains contested"
    r"|the order in which the events appear"
    r"|contemporaneous notes show"
    r"|the connection is not signed"
    r"|whether (?:that|this|the|higher|approval|benefit) (?:was|had|came|motivated)"
    r"|according to \w"
    r"|reported (?:that|by)"
    # Diagnostic / hypothetical frames — discussing what responsibility
    # WOULD look like under the diagnostic, not asserting actual chain.
    r"|would (?:attach|point|be|name|face|run)"
    r"|the diagnostic"
    r"|the eight questions"
    r"|the responsibility chain"
    # Explicit convergence-not-causation frame (rule-07 paradigmatic form)
    r"|convergence (?:at|of) the same"
    r"|the structural fact"
    r"|is a question for (?:evidentiary )?discovery"
    r"|the framing"
    r"|hypothetical"
    # Documentary backing
    r"|the documentary record"
    r"|on the public record"
    r"|on the documentary record"
    r"|in the (?:trial|appellate|court) record"
    r"|the (?:trial|court|inquiry|appellate) (?:opinion|judgment|finding|ruling)"
    r")",
    re.IGNORECASE,
)

QUOTED_RE = re.compile(r'"[^"\n]+"')


def _strip_quotes_and_codeblocks(text: str) -> str:
    """Blank verbatim-quote and fenced-code-block content so implication
    patterns inside them are not flagged. Preserves line structure."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)
    text = QUOTED_RE.sub(lambda m: " " * len(m.group(0)), text)
    return text


# Structural surfaces that aren't the chapter's own reader-facing prose:
#   - YAML frontmatter (between the first `---` and second `---`)
#   - Markdown headings (`# ` through `###### `)
#   - Block-quote lines (`> ...`) — verbatim citation; rule 06 governs
#   - Table rows (`| ... |`) — visual summary; attribution adjacent
HEADING_RE = re.compile(r"^\s*#{1,6}\s")
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
# Markdown footnote definitions like `[^91]: United States v...`
FOOTNOTE_DEF_RE = re.compile(r"^\s*\[\^[^\]]+\]:\s")


def _frontmatter_end_line(text: str) -> int:
    """Return the 1-indexed line number AFTER the closing `---` of YAML
    frontmatter, or 0 if no frontmatter is present."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i + 2  # 1-indexed line after closing ---
    return 0


def _blank_structural_lines(text: str) -> str:
    """Return a copy of `text` where heading / block-quote / table-row /
    footnote-definition lines have their content replaced by dots —
    preserves line length AND paragraph identity (a dot line doesn't
    strip to empty, so it doesn't break paragraph boundaries in
    _split_paragraphs). The implication patterns won't match against a
    row of dots."""
    out_lines = []
    fm_end = _frontmatter_end_line(text)
    for i, line in enumerate(text.splitlines(), start=1):
        if fm_end and i < fm_end:
            out_lines.append("")
            continue
        s = line.lstrip()
        if not s:
            out_lines.append(line)
            continue
        if (HEADING_RE.match(line)
                or s.startswith(">")
                or TABLE_ROW_RE.match(line)
                or FOOTNOTE_DEF_RE.match(line)):
            out_lines.append("." * len(line))
            continue
        out_lines.append(line)
    return "\n".join(out_lines)


def _split_paragraphs(text: str) -> list[tuple[int, str]]:
    """Return list of (starting_line_number, paragraph_text). A paragraph is
    a run of non-blank lines separated by one or more blank lines."""
    paragraphs: list[tuple[int, str]] = []
    current: list[str] = []
    current_start: int | None = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "":
            if current:
                paragraphs.append((current_start or lineno, "\n".join(current)))
                current = []
                current_start = None
        else:
            if current_start is None:
                current_start = lineno
            current.append(line)
    if current:
        paragraphs.append((current_start or 1, "\n".join(current)))
    return paragraphs


def _cleared_by_hedge(*paragraph_texts: str) -> bool:
    """A flag is cleared if any of the provided paragraphs contains a hedge
    or citation pattern (rule 07: same paragraph OR adjacent paragraph)."""
    for txt in paragraph_texts:
        if HEDGE_RE.search(txt):
            return True
    return False


def scan(text: str) -> list[tuple[int, str, str, str]]:
    """Return findings: list of (line_number, pattern-name, snippet, treatment)."""
    sanitized = _strip_quotes_and_codeblocks(text)
    sanitized = _blank_structural_lines(sanitized)
    paragraphs = _split_paragraphs(sanitized)
    findings: list[tuple[int, str, str, str]] = []

    for i, (start, para) in enumerate(paragraphs):
        prev_para = paragraphs[i - 1][1] if i > 0 else ""
        next_para = paragraphs[i + 1][1] if i + 1 < len(paragraphs) else ""
        snippet = para.replace("\n", " ").strip()[:120]

        # 1. Anonymous chain reference
        if ANONYMOUS_CHAIN_RE.search(para):
            if not _cleared_by_hedge(para, prev_para, next_para):
                findings.append((
                    start,
                    "anonymous-chain",
                    snippet,
                    "name the office, or hedge with 'the public record does not identify which office'",
                ))

        # 2. Chain ladder: requires 2+ DISTINCT hierarchical verbs + 3+ proper
        # nouns. Distinct-verb requirement filters out single-actor repetition
        # like "The Court directed... The Court directed..." which isn't a
        # chain — it's one actor issuing multiple instructions.
        hier_verbs = [m.lower() for m in HIERARCHICAL_VERB_RE.findall(para)]
        distinct_hier = len(set(hier_verbs))
        proper_nouns = len(set(PROPER_NOUN_PHRASE_RE.findall(para)))
        if distinct_hier >= 2 and proper_nouns >= 3:
            if not _cleared_by_hedge(para, prev_para, next_para):
                findings.append((
                    start,
                    "chain-ladder",
                    snippet,
                    "cite per-actor authorization, or hedge: 'the chain of authorization is partly documented and partly inferred'",
                ))

        # 3. Adjacent benefit + adjacent decision (this para benefit, prev para decision; or vice versa)
        para_has_decision = bool(DECISION_LANGUAGE_RE.search(para))
        para_has_benefit = bool(BENEFIT_LANGUAGE_RE.search(para))
        prev_has_decision = bool(DECISION_LANGUAGE_RE.search(prev_para))
        prev_has_benefit = bool(BENEFIT_LANGUAGE_RE.search(prev_para))

        if (para_has_decision and prev_has_benefit) or (para_has_benefit and prev_has_decision):
            if not _cleared_by_hedge(para, prev_para, next_para):
                findings.append((
                    start,
                    "decision-benefit-juxtaposition",
                    snippet,
                    "name the benefit-flow source at time of decision, or frame: 'benefit accrued; whether it motivated the decision is not in the record'",
                ))

        # 4. Sympathetic-then-cold cut
        if SYMPATHETIC_DESCRIPTOR_RE.search(prev_para) and ENGINEERING_VERB_RE.search(para):
            if not _cleared_by_hedge(para, prev_para, next_para):
                findings.append((
                    start,
                    "sympathetic-then-cold",
                    snippet,
                    "cite the engineering claim, or revise framing to avoid implying coordinated harm",
                ))

        # 5. Causation by date-adjacency: two date-stamped events in same paragraph, no hedge
        dates_in_para = DATE_RE.findall(para)
        if len(dates_in_para) >= 2 and not _cleared_by_hedge(para):
            # Only flag if a STRONG causal-implying verb is also present.
            # 'triggered' is too ambiguous in technical / mechanical contexts
            # (MCAS triggered nose-down trim) — dropped.
            if re.search(r"\b(in response to|led to|because of|in light of|caused by|as a result of|in retaliation for)\b", para, re.IGNORECASE):
                findings.append((
                    start,
                    "causation-by-adjacency",
                    snippet,
                    "cite the causal link, or use 'these two events appear in the record in this order' framing",
                ))

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
        _emit(f"Warn mode: scan-implication passed for {rel}.")
        return

    lines = [f"Warn mode: scan-implication flagged {len(findings)} possible implication-burden issue(s) in {rel} (rule 07):"]
    for lineno, name, snippet, treatment in findings[:10]:
        lines.append(f"  L{lineno} [{name}] {snippet}")
        lines.append(f"     → {treatment}")
    if len(findings) > 10:
        lines.append(f"  ... and {len(findings) - 10} more.")
    _emit(" ".join(lines))


if __name__ == "__main__":
    main()
