#!/usr/bin/env python3
"""Audit Markdown emphasis (*em*, **strong**) by judgment, not by budget.

The book uses emphasis as a structural signal, not decoration. Every
instance should pay rent on two questions:

  1. Is it applied LOGICALLY?  — for the right kind of reason (term
     install, status label, source-tag, closed-set member, stress the
     prose can't carry unmarked).
  2. Is it NECESSARY?  — would the unmarked sentence be weaker in the
     way that matters? (Repeated marking of an already-installed term
     and decorative intensifiers fail this test.)

Per-instance classifier categories:

  logical_publication      em: case names, foreign terms, Latin shorthand,
                               institutional abbreviations (publication
                               convention; never structural emphasis)
  logical_table            strong/em: inside a Markdown table row
                               (status labels, header cells)
  logical_install_first    multi-word term emphasized at first mention in
                               the chapter — vocabulary entry
  logical_set_member       short emphasis appearing as part of a cluster
                               of 2+ similar marks within ~10 lines — a
                               closed-set installation (e.g. 5 Post Office
                               roles, 3 AI layers, 4 categories)
  redundant_repeat         same text already emphasized earlier in the
                               chapter — the install has already happened
  decorative_intensifier   common stress word with no diagnostic load
                               (really, very, literally, completely, …)
  pseudo_install           multi-word term emphasized here but the same
                               text appears unmarked earlier in the chapter
                               — the "install" is fake
  review                   uncategorized; needs human judgment

Structural HARD violations (not budget-based; misuse of the tag itself):

  structural_subheader     <strong> at line start in sentence form —
                               this is a sub-heading and should be #### H4
                               (better semantics, audio-survivable)
  structural_overlong      emphasis spanning more than 15 words — paragraph
                               wallpaper; break into prose

Block-quote rule (rule 06 — quote integrity):

  in_quote                 emphasis inside > block-quote — flagged if no
                               "(emphasis added)" / "(emphasis in original)"
                               annotation is present in the chapter

Usage:
  python3 scripts/audit_emphasis.py                 # all 13 chapters
  python3 scripts/audit_emphasis.py --chapter 02    # one chapter
  python3 scripts/audit_emphasis.py --verbose       # show every instance
  python3 scripts/audit_emphasis.py --flagged-only  # only show flagged
  python3 scripts/audit_emphasis.py --include-back-matter

Exit codes:
  0  no structural violations
  1  one or more structural_subheader / structural_overlong findings
  2  script error
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "book" / "chapters-v6"
BACK_MATTER_DIR = ROOT / "book" / "back-matter"

# Only one hard structural limit remains: a single <strong> spanning more
# than this many words is paragraph wallpaper regardless of what it says.
STRONG_WORDS_MAX = 15
# Cluster-detection: emphasis instances within this many lines and of
# comparable length are treated as a closed set.
SET_LINE_WINDOW = 12
SET_LENGTH_TOLERANCE_WORDS = 3

# Decorative intensifiers — almost always unnecessary as italic stress.
# Kept short on purpose: a longer list will catch real diagnostic uses.
DECORATIVE_INTENSIFIERS = {
    "really", "very", "actually", "literally", "truly", "completely",
    "totally", "absolutely", "definitely", "obviously", "incredibly",
    "necessarily", "essentially", "merely", "simply",
}

# A line wrapped in pipes is a Markdown table row.
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
# A line that starts with **TEXT.** is acting as a sub-heading.
LINE_START_STRONG_RE = re.compile(r"^\s*\*\*[^*\n]+?[.:!?]\*\*")

# Markdown emphasis regexes. Asterisk form only (the corpus uses
# asterisks consistently). Inner content may include underscores.
# (?<![\w*]) and (?![\w*]) prevent intra-word matches and stacked markers.
STRONG_RE = re.compile(r"(?<![\w*])\*\*([^*\n]+?)\*\*(?![\w*])")
EM_RE = re.compile(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])")
HTML_STRONG_RE = re.compile(r"<strong[^>]*>(.*?)</strong>", re.DOTALL | re.IGNORECASE)
HTML_EM_RE = re.compile(r"<em[^>]*>(.*?)</em>", re.DOTALL | re.IGNORECASE)

# Exemption heuristics for <em>
CASE_NAME_RE = re.compile(r"\bv\.?\s+\w", re.IGNORECASE)
FOREIGN_DIACRITIC_RE = re.compile(
    # Latin diacritics
    r"[áéíóúàèìòùâêîôûäëïöüçñãõÁÉÍÓÚÀÈÌÒÙÄËÏÖÜ]"
    # Slavic / Eastern European: háček, ogonek, Ł
    r"|[čďěňřšťůžĐšŠČĐŘŇŤŽłŁą]"
    # German sharp s
    r"|[ß]"
    # Common transliteration diacritics
    r"|[ḥṣṭṣẓāīūṛṅṇčḫŝšž]"
)
ABBREVIATION_RE = re.compile(r"^[A-Z][A-Za-z0-9.&\-\s]{0,40}$")
# Single capitalized word ≥ 4 chars likely a proper noun (institutions,
# foreign terms, journal/report short forms, case short forms).
SINGLE_PROPER_NOUN_RE = re.compile(r"^[A-Z][\w\-']{3,}$")
PUBLISHING_LATIN = {
    "ad hoc", "ad hominem", "a priori", "a posteriori", "ex ante", "ex post",
    "mutatis mutandis", "inter alia", "sub silentio", "in re", "sui generis",
    "et al.", "et al", "ibid.", "ibid", "id.", "cf.", "viz.", "supra", "infra",
    "sic", "passim", "coup d'état", "coup d'etat", "in flagrante",
    "prima facie", "per curiam", "in camera", "ex parte", "post hoc",
    "stare decisis", "habeas corpus", "amicus curiae", "qui tam",
    "bordereau",  # canonical foreign term in ch-02 Dreyfus passage
}

QUOTE_EMPH_ANNOTATION_RE = re.compile(
    r"\(emphasis (?:added|in (?:the )?original)\)", re.IGNORECASE
)


@dataclass
class Emphasis:
    kind: str            # "em" or "strong"
    text: str
    line_no: int
    paragraph_no: int
    in_quote: bool
    in_table: bool = False
    is_line_start: bool = False
    # Filled in by classify():
    category: str = ""
    reason: str = ""


def _normalize(text: str) -> str:
    """Lowercase + strip surrounding whitespace and trailing punctuation."""
    return text.strip().rstrip(".,;:!?").lower()


# Connective words that stay lowercase inside a Title Case publication
# name (newspapers, books, reports, commission names, statutes).
# Includes German connectives so long German statute / commission names
# pass the test ("Gesetz zur Aufhebung nationalsozialistischer
# Unrechtsurteile in der Strafrechtspflege").
TITLE_CASE_CONNECTIVES = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in",
    "of", "on", "or", "the", "to", "v", "v.", "vs", "vs.", "with",
    # German
    "zur", "zum", "der", "die", "das", "des", "den", "dem",
    "im", "ins", "von", "vom", "auf", "aus", "bei", "mit", "nach",
    "und", "oder",
}

# "Lex / Loi / Ley <Name>" — civil-law naming convention (Lex Iulia,
# Loi Veil, Ley Orgánica) for laws named for a person or sponsor.
NAMED_STATUTE_PREFIX_RE = re.compile(r"^(Lex|Loi|Ley|Statuto)\b\s+\w", re.IGNORECASE)

# Small foreign-term allowlist (Greek transliterations and similar)
# the corpus actually uses; words too short or too lowercase to match
# the proper-noun heuristic but functionally publication-convention.
FOREIGN_TERM_ALLOWLIST = {
    "pharmakos",  # ancient Greek; ch-01
    "scapegoat",  # the book's central term — install once, keep as
                  # ordinary noun thereafter (handled via repeat check)
}


def _looks_like_publication_title(text: str) -> bool:
    """Heuristic: italicized text that reads as a Title Case publication
    name (book, newspaper, report, commission, statute, broadcast)."""
    t = text.strip()
    if not t:
        return False
    words = t.split()
    # Widened from 12 → 16 to cover long German statute and commission
    # names that span 13+ tokens.
    if len(words) < 2 or len(words) > 16:
        return False
    capped = 0
    for w in words:
        bare = w.strip(",.;:!?()[]'\"")
        if not bare:
            continue
        # Acceptable: starts with uppercase OR is a known lowercase connective
        if bare[:1].isupper() or bare.lower() in TITLE_CASE_CONNECTIVES:
            capped += 1
    # ≥ 75 % of tokens (slightly relaxed from 80 %) are capitalised
    # or accepted connectives — handles German statute names that
    # carry one or two non-connective lowercase modifiers.
    return capped >= max(2, int(0.75 * len(words)))


def _is_exempt_em(text: str) -> bool:
    """Publication-convention italics that aren't structural emphasis."""
    t = text.strip()
    if not t:
        return False
    if CASE_NAME_RE.search(t):
        return True
    if FOREIGN_DIACRITIC_RE.search(t):
        return True
    if t.lower() in PUBLISHING_LATIN:
        return True
    if t.lower() in FOREIGN_TERM_ALLOWLIST:
        return True
    if NAMED_STATUTE_PREFIX_RE.match(t):
        return True
    words = t.split()
    if 1 <= len(words) <= 3 and ABBREVIATION_RE.match(t) and any(c.isupper() for c in t):
        if any(w.isupper() or "." in w for w in words):
            return True
    if _looks_like_publication_title(t):
        return True
    # Single capitalized proper noun: institutional names, foreign terms,
    # case short-forms (Park, Hamilton), report/journal names (Bundesarchiv,
    # Reichsgesetzblatt). Conservative length 4+ to avoid catching stress
    # on common capitalised words like "The" or "And".
    if len(words) == 1 and SINGLE_PROPER_NOUN_RE.match(t):
        return True
    return False


def _strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 4)
    if end < 0:
        return text
    return text[end + 4:].lstrip("\n")


def parse_chapter(path: Path) -> list[Emphasis]:
    """Find every <em> / <strong> in a chapter with line and paragraph
    position. Skips YAML frontmatter and fenced code blocks."""
    text = _strip_frontmatter(path.read_text(encoding="utf-8"))
    lines = text.splitlines()

    findings: list[Emphasis] = []
    in_code = False
    paragraph_no = 0
    seen_first_h1 = False
    blank_after_h1 = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped.startswith("# "):
            seen_first_h1 = True
            paragraph_no = 0
            continue
        if not stripped:
            if seen_first_h1:
                blank_after_h1 = True
            continue
        if seen_first_h1 and (blank_after_h1 or paragraph_no == 0):
            paragraph_no += 1
            blank_after_h1 = False

        in_quote = stripped.startswith(">")
        in_table = bool(TABLE_ROW_RE.match(line))
        line_start_strong = bool(LINE_START_STRONG_RE.match(line))

        scan = re.sub(r"<!--.*?-->", "", line)

        strong_spans = []
        for m in STRONG_RE.finditer(scan):
            strong_spans.append((m.start(), m.end()))
            is_first = len(strong_spans) == 1
            findings.append(Emphasis(
                "strong", m.group(1), i, paragraph_no, in_quote,
                in_table=in_table,
                is_line_start=line_start_strong and is_first,
            ))
        for m in HTML_STRONG_RE.finditer(scan):
            strong_spans.append((m.start(), m.end()))
            findings.append(Emphasis(
                "strong", m.group(1), i, paragraph_no, in_quote, in_table=in_table,
            ))

        masked = list(scan)
        for s, e in strong_spans:
            for j in range(s, e):
                masked[j] = " "
        masked_line = "".join(masked)

        for m in EM_RE.finditer(masked_line):
            findings.append(Emphasis(
                "em", m.group(1), i, paragraph_no, in_quote, in_table=in_table,
            ))
        for m in HTML_EM_RE.finditer(masked_line):
            findings.append(Emphasis(
                "em", m.group(1), i, paragraph_no, in_quote, in_table=in_table,
            ))

    return findings


def classify(
    f: Emphasis,
    chapter_body_lower_no_quotes: str,
    line_offsets: list[int],
    all_findings: list[Emphasis],
) -> None:
    """Decide why each instance was used and whether the prose needs it.
    Writes verdict into f.category and f.reason."""
    text = f.text.strip()
    norm = _normalize(text)
    word_count = len(text.split())

    # Context categories take precedence — they're not "our" prose.
    if f.in_table:
        f.category = "logical_table"
        f.reason = "in-table status label / header"
        return
    if f.in_quote:
        f.category = "in_quote"
        f.reason = "inside > block-quote; chapter must annotate (emphasis added)"
        return

    # Structural rules — misuse of the tag in the chapter's own voice.
    if f.kind == "strong" and f.is_line_start:
        f.category = "structural_subheader"
        f.reason = "line-start sentence form — convert to #### H4 heading"
        return
    if word_count > STRONG_WORDS_MAX and f.kind == "strong":
        f.category = "structural_overlong"
        f.reason = f"{word_count} words — break into prose, not bold"
        return

    # Em publication conventions.
    if f.kind == "em" and _is_exempt_em(text):
        f.category = "logical_publication"
        f.reason = "case name / foreign term / Latin / institutional shorthand"
        return

    # Decorative intensifiers — fail the necessity test.
    if norm in DECORATIVE_INTENSIFIERS:
        f.category = "decorative_intensifier"
        f.reason = f"intensifier '{text}' — unnecessary stress"
        return

    # Redundant repeat: identical text emphasized earlier in this chapter.
    prior = [
        x for x in all_findings
        if x.kind == f.kind
        and x.line_no < f.line_no
        and _normalize(x.text) == norm
        and not x.in_quote
        and not x.in_table
    ]
    if prior:
        first = prior[0]
        f.category = "redundant_repeat"
        f.reason = f"already emphasized at L{first.line_no} — install happened once"
        return

    # Pseudo-install: term appears unmarked earlier in the chapter's own
    # voice (block-quoted previews / epigraphs / tables / headings are
    # excluded — those are previews or labels, not the install moment).
    # Length floor of 5 chars avoids false positives on stop words.
    # Word-boundary match avoids substring false positives like
    # "knowledge" in "acknowledged", "control" in "controlled",
    # "record" in "recorded".
    if len(norm) >= 5:
        if f.line_no > 1 and f.line_no - 1 < len(line_offsets):
            cutoff = line_offsets[f.line_no - 1]
        else:
            cutoff = len(chapter_body_lower_no_quotes)
        prior_text = chapter_body_lower_no_quotes[:cutoff]
        if re.search(r"\b" + re.escape(norm) + r"\b", prior_text):
            f.category = "pseudo_install"
            f.reason = (
                "first emphasis here but term appeared unmarked earlier — "
                "install missed or unnecessary"
            )
            return

    # Closed-set member: 2+ similar-length emphasis marks nearby.
    nearby = [
        x for x in all_findings
        if x is not f
        and x.kind == f.kind
        and not x.in_quote
        and not x.in_table
        and abs(x.line_no - f.line_no) <= SET_LINE_WINDOW
        and abs(len(x.text.split()) - word_count) <= SET_LENGTH_TOLERANCE_WORDS
    ]
    if len(nearby) >= 1:
        f.category = "logical_set_member"
        f.reason = f"part of a cluster of {len(nearby) + 1} similar emphasis marks (closed set)"
        return

    # First-mention of a noun phrase (hyphenated single token like
    # "shadow-corpus" or multi-word like "system/object alibi") = install.
    if (2 <= word_count <= 6) or (word_count == 1 and len(norm) >= 6):
        f.category = "logical_install_first"
        f.reason = "first emphasis of a term — vocabulary install"
        return

    # Single short word, no other signal → human judgment.
    f.category = "review"
    f.reason = "uncategorized — manual judgment needed"


def _build_line_offsets(text: str) -> list[int]:
    """Return [0, start-of-line-2, start-of-line-3, ...] for lookup by
    line number (1-indexed). Caller passes line_no, gets char cutoff."""
    offsets = [0]
    pos = 0
    for ch in text:
        pos += 1
        if ch == "\n":
            offsets.append(pos)
    return offsets


def audit_chapter(path: Path) -> dict:
    """Classify every emphasis instance in the chapter and aggregate."""
    raw = path.read_text(encoding="utf-8")
    body = _strip_frontmatter(raw)
    # Build a chapter-voice-only lowercase corpus for prior-occurrence
    # checks. Block-quoted lines (source quotations, audio-form previews)
    # and Markdown table rows (preview/reference tables) are *not* the
    # chapter's install voice — they're previews or references — so they
    # don't count against pseudo-install detection. Padding with spaces
    # preserves char-offset alignment with body so line_offsets stays valid.
    chapter_voice_lines = []
    for line in body.splitlines():
        stripped = line.lstrip()
        # Headings (# H1 through #### H4) are structural labels, not
        # the chapter's install prose — exclude them too so e.g. the
        # chapter title "Chapter 3 — Who Could Have Stopped It?" does
        # not trigger pseudo_install on an italicized callback.
        is_heading = bool(re.match(r"^#{1,6}\s", stripped))
        if (stripped.startswith(">")
                or TABLE_ROW_RE.match(line)
                or is_heading):
            chapter_voice_lines.append(" " * len(line))
        else:
            chapter_voice_lines.append(line)
    body_voice_lower = "\n".join(chapter_voice_lines).lower()
    line_offsets = _build_line_offsets(body)

    findings = parse_chapter(path)
    for f in findings:
        classify(f, body_voice_lower, line_offsets, findings)

    # Aggregate counts by category, separately for em vs strong.
    counts: dict[str, dict[str, int]] = {"em": {}, "strong": {}}
    for f in findings:
        counts[f.kind][f.category] = counts[f.kind].get(f.category, 0) + 1

    # Flagged categories (need human attention).
    FLAG = {
        "structural_subheader",
        "structural_overlong",
        "redundant_repeat",
        "decorative_intensifier",
        "pseudo_install",
        "review",
    }
    HARD = {"structural_subheader", "structural_overlong"}
    flagged = [f for f in findings if f.category in FLAG]
    hard = [f for f in findings if f.category in HARD]

    # Block-quote integrity: any in-quote emphasis without an
    # "(emphasis added)" / "(emphasis in original)" annotation is SOFT.
    in_quote_emph = [f for f in findings if f.in_quote and not _is_exempt_em(f.text)]
    quote_soft = bool(in_quote_emph) and not QUOTE_EMPH_ANNOTATION_RE.search(raw)

    return {
        "path": path,
        "findings": findings,
        "counts": counts,
        "flagged": flagged,
        "hard": hard,
        "in_quote_emph": in_quote_emph,
        "quote_soft": quote_soft,
    }


def _fmt_counts(by_kind: dict[str, int]) -> str:
    if not by_kind:
        return "0"
    parts = []
    for cat, n in sorted(by_kind.items(), key=lambda kv: -kv[1]):
        short = cat.replace("logical_", "").replace("structural_", "STR-")
        parts.append(f"{n} {short}")
    return ", ".join(parts)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Audit emphasis (em / strong) by judgment, not budget."
    )
    p.add_argument("--chapter", help="single chapter number, e.g. '02'")
    p.add_argument("--verbose", action="store_true",
                   help="list every emphasis instance with classification")
    p.add_argument("--flagged-only", action="store_true",
                   help="only show chapters with flagged instances (and the flags)")
    p.add_argument("--include-back-matter", action="store_true",
                   help="also audit book/back-matter/*.md")
    p.add_argument("--paths", nargs="+", help="explicit file paths to audit")
    args = p.parse_args(argv)

    if args.paths:
        targets = [Path(x) for x in args.paths]
    else:
        glob = f"{args.chapter}-*.md" if args.chapter else "*.md"
        targets = sorted(CHAPTERS_DIR.glob(glob))
        if args.include_back_matter:
            targets += sorted(BACK_MATTER_DIR.glob("*.md"))

    if not targets:
        print("No chapters matched.", file=sys.stderr)
        return 2

    total_hard = 0
    total_flagged = 0
    for ch in targets:
        report = audit_chapter(ch)
        n_hard = len(report["hard"])
        n_flag = len(report["flagged"])
        total_hard += n_hard
        total_flagged += n_flag

        if args.flagged_only and not (n_flag or report["quote_soft"]):
            continue

        status = "FAIL" if n_hard else ("FLAG" if n_flag else "PASS")
        em_summary = _fmt_counts(report["counts"]["em"])
        strong_summary = _fmt_counts(report["counts"]["strong"])
        print(f"[{status}] {ch.name}")
        print(f"        em ({sum(report['counts']['em'].values())}): {em_summary}")
        print(f"    strong ({sum(report['counts']['strong'].values())}): {strong_summary}")
        if report["quote_soft"]:
            print(f"    SOFT: {len(report['in_quote_emph'])} in-quote emphasis without "
                  f"(emphasis added) annotation")
        # Show flagged instances unless verbose mode shows all
        items = report["findings"] if args.verbose else report["flagged"]
        for f in items:
            if f.category in ("logical_publication", "logical_table") and not args.verbose:
                continue
            tag = "<strong>" if f.kind == "strong" else "<em>"
            cat = f.category.upper()
            snippet = f.text[:70] + ("…" if len(f.text) > 70 else "")
            print(f"        L{f.line_no:>4} {tag:9} {cat:24} {f.reason}")
            print(f"             \"{snippet}\"")
        print()

    summary = (
        f"{len(targets)} chapter(s) audited: "
        f"{total_hard} structural, {total_flagged} flagged"
    )
    print(summary)
    return 1 if total_hard else 0


if __name__ == "__main__":
    raise SystemExit(main())
