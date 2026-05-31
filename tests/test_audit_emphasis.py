"""Tests for the emphasis auditor (scripts/audit_emphasis.py).

The auditor classifies each <em> / <strong> mark by whether it is
applied logically (right kind of use) and necessarily (the prose can't
carry it unmarked). No numerical budgets — only structural HARDs
(line-start sentence-form bold = should be H4; > 15 words = wallpaper)
and per-instance verdicts for human review.

Coverage:
  - Markdown / HTML emphasis detection
  - Frontmatter, code-fence, heading exclusion
  - Exemption: case names, foreign diacritics (Latin / Slavic / etc.),
    Publishing Latin, Title Case publication names, single proper nouns
  - Structural HARDs: sub-header and overlong
  - Per-instance categories: logical_table, logical_publication,
    logical_install_first, logical_set_member, redundant_repeat,
    decorative_intensifier, pseudo_install, review
  - Block-quote / table-row exclusion from the prior-occurrence corpus
    so chapter previews don't falsely trigger pseudo_install
  - Char-offset alignment between body and body_voice_lower
"""
from __future__ import annotations

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import audit_emphasis as ae  # type: ignore[import-not-found]  # noqa: E402


def _write(tmp: Path, body: str) -> Path:
    """Write a minimal chapter file with frontmatter + H1, return path."""
    text = "---\nstatus: ready\n---\n\n# Test Chapter\n\n" + body
    f = tmp / "ch.md"
    f.write_text(text, encoding="utf-8")
    return f


# ── parsing ────────────────────────────────────────────────────────

def test_detects_em_and_strong() -> None:
    with TemporaryDirectory() as d:
        f = _write(Path(d), "A *plain* paragraph with **strong** marks.\n")
        findings = ae.parse_chapter(f)
        kinds = [x.kind for x in findings]
        assert kinds.count("em") == 1
        assert kinds.count("strong") == 1


def test_strong_matched_before_em() -> None:
    with TemporaryDirectory() as d:
        f = _write(Path(d), "Try **double stars** here.\n")
        findings = ae.parse_chapter(f)
        assert [x.kind for x in findings] == ["strong"]
        assert findings[0].text == "double stars"


def test_intraword_asterisks_skipped() -> None:
    with TemporaryDirectory() as d:
        f = _write(Path(d), "Math like 2*3*4 is not emphasis.\n")
        findings = ae.parse_chapter(f)
        assert findings == []


def test_html_emphasis_matched() -> None:
    with TemporaryDirectory() as d:
        f = _write(Path(d),
                   "Raw <em>html italic</em> and <strong>html bold</strong>.\n")
        findings = ae.parse_chapter(f)
        kinds = [x.kind for x in findings]
        assert kinds.count("em") == 1
        assert kinds.count("strong") == 1


def test_code_fence_skipped() -> None:
    body = (
        "Plain.\n\n"
        "```\n"
        "*not* an emphasis **either**\n"
        "```\n\n"
        "After.\n"
    )
    with TemporaryDirectory() as d:
        findings = ae.parse_chapter(_write(Path(d), body))
        assert findings == []


def test_frontmatter_skipped() -> None:
    raw = (
        "---\n"
        "title: \"*not emphasis* in frontmatter\"\n"
        "---\n\n"
        "# H1\n\n"
        "Real *one*.\n"
    )
    with TemporaryDirectory() as d:
        f = Path(d) / "ch.md"
        f.write_text(raw, encoding="utf-8")
        findings = ae.parse_chapter(f)
        assert [x.text for x in findings] == ["one"]


# ── exemption heuristics ───────────────────────────────────────────

def test_case_name_exempt() -> None:
    assert ae._is_exempt_em("Hamilton v Post Office Ltd")
    assert ae._is_exempt_em("Roe v. Wade")
    assert not ae._is_exempt_em("simple structural emphasis")


def test_foreign_diacritic_exempt_latin() -> None:
    assert ae._is_exempt_em("coup d'état")
    assert ae._is_exempt_em("réseau")
    assert ae._is_exempt_em("naïveté")


def test_foreign_diacritic_exempt_other_scripts() -> None:
    assert ae._is_exempt_em("mašmaššu")     # Akkadian (Slavic-class diacritic š)
    assert ae._is_exempt_em("Spaß")         # German sharp s
    # Polish ł
    assert ae._is_exempt_em("Łódź")


def test_publishing_latin_exempt() -> None:
    assert ae._is_exempt_em("ad hoc")
    assert ae._is_exempt_em("et al.")
    assert ae._is_exempt_em("ibid.")
    assert ae._is_exempt_em("sic")


def test_publication_title_case_exempt() -> None:
    assert ae._is_exempt_em("Bringing Them Home")
    assert ae._is_exempt_em("Seattle Times")
    assert ae._is_exempt_em("Tragedy in Dedham")


def test_single_proper_noun_exempt() -> None:
    # Institutional / German publications / case short forms
    assert ae._is_exempt_em("Reichsgesetzblatt")
    assert ae._is_exempt_em("Bundesarchiv")
    assert ae._is_exempt_em("Park")         # case short form (United States v. Park)
    # Too short to be a proper noun
    assert not ae._is_exempt_em("not")


# ── structural HARDs (the only build failures) ─────────────────────

def test_strong_sub_header_hard_fail() -> None:
    body = "First.\n\n**Section heading.** Then prose continues.\n"
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        assert len(report["hard"]) >= 1
        assert any(f.category == "structural_subheader" for f in report["hard"])


def test_strong_overlong_hard_fail() -> None:
    long = " ".join(["word"] * 20)
    body = f"X.\n\n**{long}**\n"
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        assert any(f.category == "structural_overlong" for f in report["hard"])


# ── classification verdicts ────────────────────────────────────────

def test_table_cell_bold_is_logical() -> None:
    body = (
        "Intro.\n\n"
        "| Stage | Status |\n"
        "|---|---|\n"
        "| Phase 1 | **Succeeded.** |\n"
        "| Phase 2 | **In progress.** |\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        cats = [f.category for f in report["findings"] if f.kind == "strong"]
        assert cats == ["logical_table", "logical_table"]
        assert report["hard"] == []


def test_redundant_repeat_fires() -> None:
    # "novel-term" emphasized twice in the chapter's own voice.
    body = (
        "Intro.\n\n"
        "Para A introduces *novel-term* here.\n\n"
        "Para B uses *novel-term* again.\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        cats = [f.category for f in report["findings"]]
        assert "redundant_repeat" in cats


def test_decorative_intensifier_flagged() -> None:
    body = "Prose.\n\nThe outcome was *really* important.\n"
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        assert any(f.category == "decorative_intensifier" for f in report["findings"])


def test_pseudo_install_fires_when_term_appears_unmarked_earlier() -> None:
    body = (
        "Para A: we will introduce shadow-corpus later.\n\n"
        "Para B: this names **shadow-corpus** as a category.\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        cats = [f.category for f in report["findings"] if f.kind == "strong"]
        assert "pseudo_install" in cats


def test_blockquote_does_not_trigger_pseudo_install() -> None:
    # The same term mentioned inside a > block-quote preview should NOT
    # block the chapter's later first install from being logical.
    body = (
        "> This chapter will install the doctrine of named control.\n\n"
        "Para B installs **named control** here.\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        strong_cats = [f.category for f in report["findings"] if f.kind == "strong"]
        assert "pseudo_install" not in strong_cats


def test_table_row_does_not_trigger_pseudo_install() -> None:
    # A preview table containing the term should not count as prior prose.
    body = (
        "| Category | Note |\n"
        "|---|---|\n"
        "| Named control | summary |\n\n"
        "Para B installs **named control** here.\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        strong_cats = [f.category for f in report["findings"] if f.kind == "strong"]
        assert "pseudo_install" not in strong_cats


def test_heading_does_not_trigger_pseudo_install() -> None:
    # Chapter title containing a question phrase should NOT count as prior prose.
    body = (
        "## Who Could Have Stopped It?\n\n"
        "Prose introducing the chapter.\n\n"
        "Question one: *Who could have stopped it?* — the named question.\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        em_cats = [f.category for f in report["findings"] if f.kind == "em"]
        assert "pseudo_install" not in em_cats


def test_first_install_classified_logically() -> None:
    body = "Intro.\n\nThis paragraph names *novel-term-X* for the first time.\n"
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        cats = [f.category for f in report["findings"]]
        # logical_install_first or logical_set_member — either is acceptable
        assert any(c.startswith("logical_") for c in cats)


def test_in_quote_emphasis_without_annotation_softflag() -> None:
    body = "First.\n\n> The press release *quietly* changed the wording.\n"
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        assert report["quote_soft"] is True


def test_in_quote_emphasis_with_annotation_passes() -> None:
    body = "First.\n\n> Quietly *changed* the wording (emphasis added).\n"
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        assert report["quote_soft"] is False


def test_clean_chapter_passes_with_no_flags() -> None:
    body = (
        "Plain opening paragraph with no emphasis.\n\n"
        "A second paragraph that names *Hamilton v Post Office* once.\n\n"
        "A third paragraph that mentions *ad hoc* in passing.\n"
    )
    with TemporaryDirectory() as d:
        report = ae.audit_chapter(_write(Path(d), body))
        assert report["hard"] == []
        assert report["flagged"] == []
