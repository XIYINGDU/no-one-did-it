"""Unit tests for the KDP EPUB toolkit (rule 16-kdp-epub):
build guards + the destructive Notes-fold preprocess, the validate structure
checks, and the CSS scanner hook. These paths gate a published book and perform
destructive text transformation, so they are covered here per the cc-suite audit.
"""
from __future__ import annotations

import importlib.util
import io
import sys
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "pipelines" / "epub"))

import build_kdp_epub as bk  # type: ignore[import-not-found]  # noqa: E402
import validate_kdp_epub as vk  # type: ignore[import-not-found]  # noqa: E402


def _load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


HOOK = _load(ROOT / ".claude" / "hooks" / "scan-kdp-epub-css.py")


# --------------------------------------------------------------------------- #
# build_kdp_epub.guard_source — raw markers must never ship
# --------------------------------------------------------------------------- #
def test_guard_source_blocks_cite():
    with pytest.raises(SystemExit):
        bk.guard_source("a sentence with a [CITE: some-slug] marker")


def test_guard_source_blocks_evidence_needed():
    with pytest.raises(SystemExit):
        bk.guard_source("a sentence [EVIDENCE NEEDED: find the source]")


def test_guard_source_passes_clean():
    bk.guard_source("clean prose with a resolved [^1] footnote ref")  # no raise


# --------------------------------------------------------------------------- #
# build_kdp_epub.guard_metadata — unfilled TODO blocks the build
# --------------------------------------------------------------------------- #
def test_guard_metadata_blocks_todo(tmp_path, monkeypatch):
    p = tmp_path / "metadata.yml"
    p.write_text("creator: TODO-AUTHOR-NAME\n", encoding="utf-8")
    monkeypatch.setattr(bk, "METADATA", p)
    with pytest.raises(SystemExit):
        bk.guard_metadata()


def test_guard_metadata_passes_when_filled(tmp_path, monkeypatch):
    p = tmp_path / "metadata.yml"
    p.write_text("creator: Jane Doe\npublisher: An Imprint\n", encoding="utf-8")
    monkeypatch.setattr(bk, "METADATA", p)
    bk.guard_metadata()  # no raise


def test_guard_metadata_ignores_todo_in_comments(tmp_path, monkeypatch):
    # The guard checks parsed VALUES, so a comment documenting the placeholder
    # token must not trip it once the actual fields are filled.
    p = tmp_path / "metadata.yml"
    p.write_text(
        "# Fields marked TODO must be filled before shipping.\n"
        'creator: "Jane Doe"\npublisher: "An Imprint"\n',
        encoding="utf-8")
    monkeypatch.setattr(bk, "METADATA", p)
    bk.guard_metadata()  # no raise


def test_guard_metadata_rejects_malformed_yaml(tmp_path, monkeypatch):
    p = tmp_path / "metadata.yml"
    p.write_text("creator: this: is: not: valid: yaml\n", encoding="utf-8")
    monkeypatch.setattr(bk, "METADATA", p)
    with pytest.raises(SystemExit):
        bk.guard_metadata()


# --------------------------------------------------------------------------- #
# build_kdp_epub.guard_cover — fail-loud in non-draft, lenient in --draft
# --------------------------------------------------------------------------- #
def test_guard_cover_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(bk, "COVER", tmp_path / "nope.jpg")
    with pytest.raises(SystemExit):
        bk.guard_cover(draft=False)
    assert bk.guard_cover(draft=True) is False


def test_guard_cover_unverifiable_fails_loud(tmp_path, monkeypatch):
    fake = tmp_path / "cover.jpg"
    fake.write_text("not a real image", encoding="utf-8")  # sips can't read dimensions
    monkeypatch.setattr(bk, "COVER", fake)
    with pytest.raises(SystemExit):
        bk.guard_cover(draft=False)
    assert bk.guard_cover(draft=True) is True


# --------------------------------------------------------------------------- #
# build_kdp_epub.preprocess — fold Notes into footnotes without truncation
# --------------------------------------------------------------------------- #
NOTES_DOC = """# Chapter 1

A claim [^1] and another [^2].

# Notes

## Chapter 1 — Title

[^1]: First note.
[^2]: Second note, first line.
    a continuation line of the second note.

# Selected Bibliography

Author, A. *Title*. Publisher, 2026.
"""


def test_preprocess_drops_notes_heading_keeps_defs_and_bibliography():
    out = bk.preprocess(NOTES_DOC)
    assert "# Notes" not in out
    assert "## Chapter 1 — Title" not in out  # the empty Notes subheading is removed
    assert "[^1]: First note." in out
    assert "[^2]: Second note, first line." in out
    assert "# Selected Bibliography" in out
    assert "# Chapter 1\n" in out  # the actual chapter body survives


def test_preprocess_keeps_indented_continuation_lines():
    out = bk.preprocess(NOTES_DOC)
    assert "a continuation line of the second note." in out


def test_preprocess_noop_without_notes_section():
    doc = "# Chapter 1\n\nNo notes here.\n"
    assert bk.preprocess(doc) == doc


# --------------------------------------------------------------------------- #
# build_kdp_epub.append_back_cover — optional final-page image
# --------------------------------------------------------------------------- #
def test_append_back_cover_when_present(tmp_path, monkeypatch):
    bc = tmp_path / "back-cover.jpg"
    bc.write_bytes(b"\xff\xd8\xff\xe0")  # jpeg magic, contents irrelevant
    monkeypatch.setattr(bk, "BACK_COVER", bc)
    out = bk.append_back_cover("the body")
    assert "::: {.backcover}" in out
    assert str(bc) in out
    assert out.startswith("the body")


def test_append_back_cover_absent_is_noop(tmp_path, monkeypatch):
    monkeypatch.setattr(bk, "BACK_COVER", tmp_path / "nope.jpg")
    assert bk.append_back_cover("the body") == "the body"


# --------------------------------------------------------------------------- #
# scan-kdp-epub-css hook — flags KDP-unsupported CSS, no false positives
# --------------------------------------------------------------------------- #
def test_hook_flags_each_violation_class():
    css = ".a{position:absolute} .b{font-size:12px} .c{background:#000} .d{height:40px}"
    names = {name for _, name, _, _ in HOOK.scan(css)}
    assert {"position", "fixed-unit", "bw-background", "text-height"} <= names


def test_hook_height_percentage_not_flagged():
    # regression: the lookahead bug flagged `height: 100%` (with a space)
    assert HOOK.scan(".x{height:100%}") == []
    assert HOOK.scan(".x{height: 100%}") == []


def test_hook_font_shorthand_flagged():
    assert any(n == "fixed-unit" for _, n, _, _ in HOOK.scan(".x{font:12px/1.4 serif}"))


def test_hook_clean_css_passes():
    css = ".x{margin:1em 6%; max-width:100%; height:auto; font-size:1.2em; width:80%}"
    assert HOOK.scan(css) == []


def test_hook_ignores_commented_violations():
    assert HOOK.scan("/* position:absolute and font-size:12px are bad */ .x{margin:0}") == []


# --------------------------------------------------------------------------- #
# validate_kdp_epub.gate_structure — popup + leak detection on a crafted EPUB
# --------------------------------------------------------------------------- #
def _epub(xhtml: str, opf: str = '<package><manifest>'
          '<item properties="cover-image" href="c.jpg"/></manifest></package>') -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0"?><container><rootfiles>'
                   '<rootfile full-path="content.opf"/></rootfiles></container>')
        z.writestr("content.opf", opf)
        z.writestr("ch1.xhtml", xhtml)
    return buf.getvalue()


def _structure(epub_bytes: bytes, tmp_path) -> dict:
    p = tmp_path / "book.epub"
    p.write_bytes(epub_bytes)
    vk.RESULTS.clear()
    vk.gate_structure(p)
    return {g: s for g, s, _ in vk.RESULTS}


def test_validate_footnotes_popup_shape_passes(tmp_path):
    # popup shape: epub:type noteref + footnote markup on both sides
    both = '<a epub:type="noteref" href="#n1">1</a><aside epub:type="footnote" id="n1">x</aside>'
    assert _structure(_epub(both), tmp_path)["footnotes"] == "PASS"


def test_validate_footnotes_popup_one_sided_warns(tmp_path):
    one_side = '<a epub:type="noteref" href="#n1">1</a>'
    assert _structure(_epub(one_side), tmp_path)["footnotes"] == "WARN"


def test_validate_footnotes_back_matter_shape_passes(tmp_path):
    # flip-to-back shape: cross-file href to a back-matter anchor id cK-M
    backmatter = '<a href="ch017.xhtml#c1-1"><sup>1</sup></a><span id="c1-1">x</span>'
    assert _structure(_epub(backmatter), tmp_path)["footnotes"] == "PASS"


def test_validate_detects_named_slug_leak(tmp_path):
    leaked = '<p>a leaked marker [^doj-capitol-breach-removal-2025] in the body</p>'
    assert _structure(_epub(leaked), tmp_path)["no leaked markers"] == "FAIL"


def test_validate_clean_body_no_leak(tmp_path):
    clean = '<a epub:type="noteref" href="#n1">1</a><aside epub:type="footnote" id="n1">x</aside>'
    assert _structure(_epub(clean), tmp_path)["no leaked markers"] == "PASS"


def test_validate_detects_inline_style(tmp_path):
    styled = '<p style="color: red">text</p>'
    assert _structure(_epub(styled), tmp_path)["no inline styles"] == "FAIL"


def test_validate_detects_inline_style_on_col(tmp_path):
    # pandoc's pre-Lua-filter behaviour: width on table column
    styled = '<table><colgroup><col style="width: 25%"/></colgroup></table>'
    assert _structure(_epub(styled), tmp_path)["no inline styles"] == "FAIL"


def test_validate_clean_body_no_inline_styles(tmp_path):
    clean = '<p>text</p><table><colgroup><col/></colgroup></table>'
    assert _structure(_epub(clean), tmp_path)["no inline styles"] == "PASS"


def test_validate_opf_via_container_not_decoy(tmp_path):
    # a decoy .opf appears first in the zip; the real one is named in container.xml
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("decoy.opf", "<package>DECOY — no cover</package>")
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0"?><container><rootfiles>'
                   '<rootfile full-path="real.opf"/></rootfiles></container>')
        z.writestr("real.opf", '<package><item properties="cover-image" href="c.jpg"/></package>')
        z.writestr("ch.xhtml",
                   '<a epub:type="noteref" href="#n1">1</a><aside epub:type="footnote" id="n1">x</aside>')
    p = tmp_path / "b.epub"
    p.write_bytes(buf.getvalue())
    vk.RESULTS.clear()
    vk.gate_structure(p)
    r = {g: s for g, s, _ in vk.RESULTS}
    assert r["cover"] == "PASS"  # read real.opf (has cover), not the first-in-zip decoy


# --------------------------------------------------------------------------- #
# validate_kdp_epub.main — verdict aggregation (skip / warn / allow-skips)
# --------------------------------------------------------------------------- #
def _patch_gates(monkeypatch, epubcheck, kp, structure_status=None):
    monkeypatch.setattr(vk, "gate_epubcheck", lambda e: vk.record("epubcheck", epubcheck, ""))
    monkeypatch.setattr(vk, "gate_kindle_previewer", lambda e: vk.record("Kindle Previewer", kp, ""))
    if structure_status:
        monkeypatch.setattr(vk, "gate_structure", lambda e: vk.record("cover", structure_status, ""))
    else:
        monkeypatch.setattr(vk, "gate_structure", lambda e: None)


def test_main_required_skip_blocks(tmp_path, monkeypatch):
    epub = tmp_path / "b.epub"
    epub.write_bytes(_epub("<p>x</p>"))
    _patch_gates(monkeypatch, "SKIP", "SKIP")
    monkeypatch.setattr(sys, "argv", ["validate", str(epub)])
    vk.RESULTS.clear()
    assert vk.main() == 1  # skipped required gates are not shippable


def test_main_allow_skips_is_advisory_not_blocking(tmp_path, monkeypatch):
    epub = tmp_path / "b.epub"
    epub.write_bytes(_epub("<p>x</p>"))
    _patch_gates(monkeypatch, "SKIP", "PASS")
    monkeypatch.setattr(sys, "argv", ["validate", str(epub), "--allow-skips"])
    vk.RESULTS.clear()
    assert vk.main() == 0  # advisory pass, but (by design) not a shipping certification


def test_main_warn_passes_with_warnings(tmp_path, monkeypatch):
    epub = tmp_path / "b.epub"
    epub.write_bytes(_epub("<p>x</p>"))
    _patch_gates(monkeypatch, "PASS", "PASS", structure_status="WARN")
    monkeypatch.setattr(sys, "argv", ["validate", str(epub)])
    vk.RESULTS.clear()
    assert vk.main() == 0


def test_main_fail_blocks(tmp_path, monkeypatch):
    epub = tmp_path / "b.epub"
    epub.write_bytes(_epub("<p>x</p>"))
    _patch_gates(monkeypatch, "FAIL", "PASS")
    monkeypatch.setattr(sys, "argv", ["validate", str(epub)])
    vk.RESULTS.clear()
    assert vk.main() == 1
