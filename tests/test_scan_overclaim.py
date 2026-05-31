"""Tests for `.claude/hooks/scan-overclaim.py` — warn-mode scanner that
flags over-claim verbs without citation/hedging in `book/` prose.

Implements regression coverage for `.claude/rules/05-overclaim-language.md`.
The hook is warn-only; these tests assert it never emits `permissionDecision`.
"""

import importlib.util
import json
from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / ".claude" / "hooks" / "scan-overclaim.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("scan_overclaim", HOOK)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestScanFunction(unittest.TestCase):
    """Unit tests against `scan()` directly — fast, no subprocess."""

    def setUp(self) -> None:
        self.mod = _load_module()

    def test_clean_prose_returns_no_findings(self) -> None:
        text = "This is a clean paragraph about a case file. It contains no banned verbs.\n"
        self.assertEqual(self.mod.scan(text), [])

    def test_knew_without_hedge_is_flagged(self) -> None:
        text = "The CEO knew about the safety issue.\n"
        findings = self.mod.scan(text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0][1], "knew")

    def test_knew_with_citation_marker_is_not_flagged(self) -> None:
        text = "The CEO knew about the safety issue [CITE: DPA §III.A].\n"
        self.assertEqual(self.mod.scan(text), [])

    def test_knew_with_hedge_pattern_is_not_flagged(self) -> None:
        text = "According to the Seattle Times, the CEO knew about the safety issue.\n"
        self.assertEqual(self.mod.scan(text), [])

    def test_knew_inside_double_quotes_is_exempt(self) -> None:
        text = 'The witness said "the CEO knew" but provided no documentation.\n'
        self.assertEqual(self.mod.scan(text), [])

    def test_must_have_known_is_flagged(self) -> None:
        text = "The board must have known about the irregularities.\n"
        findings = self.mod.scan(text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0][1], "must-have")

    def test_clearly_is_flagged(self) -> None:
        text = "The executive clearly directed the cover-up.\n"
        findings = self.mod.scan(text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0][1], "clearly")

    def test_guilty_without_court_citation_is_flagged(self) -> None:
        text = "He is guilty of fraud.\n"
        findings = self.mod.scan(text)
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0][1], "guilty")

    def test_guilty_with_court_citation_is_not_flagged(self) -> None:
        text = "He is guilty of fraud, as the Southern District of New York found in 2023 [CITE: SDNY 23-cr-001].\n"
        self.assertEqual(self.mod.scan(text), [])

    def test_code_fence_content_is_exempt(self) -> None:
        text = "Here is a quote:\n```\nThe CEO knew about it.\n```\nClean line.\n"
        self.assertEqual(self.mod.scan(text), [])

    def test_multiple_lines_returns_one_finding_per_line(self) -> None:
        text = (
            "Line 1: The CEO knew about it.\n"
            "Line 2: This is clean.\n"
            "Line 3: He clearly did it.\n"
        )
        findings = self.mod.scan(text)
        self.assertEqual(len(findings), 2)
        self.assertEqual({f[1] for f in findings}, {"knew", "clearly"})


class TestHookIntegration(unittest.TestCase):
    """Subprocess test of the hook end-to-end."""

    def _run(self, fixture_text: str, rel_path: str) -> subprocess.CompletedProcess[str]:
        fixture = ROOT / rel_path
        fixture.parent.mkdir(parents=True, exist_ok=True)
        fixture.write_text(fixture_text, encoding="utf-8")
        try:
            payload = {
                "hook_event_name": "PostToolUse",
                "cwd": str(ROOT),
                "tool_input": {"file_path": str(fixture)},
            }
            return subprocess.run(
                ["python3", str(HOOK)],
                input=json.dumps(payload),
                capture_output=True,
                text=True,
                check=False,
            )
        finally:
            fixture.unlink(missing_ok=True)

    def test_clean_book_chapter_passes(self) -> None:
        text = (
            "---\nstatus: draft\n---\n\n"
            "This chapter discusses the case [CITE: source].\n"
        )
        proc = self._run(text, "book/chapters-v6/_tmp_clean.md")
        self.assertEqual(proc.returncode, 0)
        self.assertNotIn("permissionDecision", proc.stdout)
        out = json.loads(proc.stdout)
        self.assertIn("scan-overclaim passed", out["hookSpecificOutput"]["additionalContext"])

    def test_book_chapter_with_overclaim_warns_without_deny(self) -> None:
        text = (
            "---\nstatus: draft\n---\n\n"
            "The CEO knew about the issue. He clearly directed it. The board "
            "must have known by then.\n"
        )
        proc = self._run(text, "book/chapters-v6/_tmp_overclaim.md")
        self.assertEqual(proc.returncode, 0)
        # MUST be warn-only — the scan-overclaim hook never denies.
        self.assertNotIn("permissionDecision", proc.stdout)
        out = json.loads(proc.stdout)
        ctx = out["hookSpecificOutput"]["additionalContext"]
        self.assertIn("scan-overclaim flagged", ctx)
        self.assertIn("knew", ctx)
        self.assertIn("clearly", ctx)
        self.assertIn("must-have", ctx)

    def test_file_outside_book_scope_is_skipped(self) -> None:
        text = "The CEO knew about it. Should be ignored.\n"
        fixture = ROOT / ".claude" / "docs" / "_tmp_overclaim_doc.md"
        fixture.write_text(text, encoding="utf-8")
        try:
            payload = {
                "hook_event_name": "PostToolUse",
                "cwd": str(ROOT),
                "tool_input": {"file_path": str(fixture)},
            }
            proc = subprocess.run(
                ["python3", str(HOOK)],
                input=json.dumps(payload),
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0)
            # No output → silently skipped (file is outside book/ scope)
            self.assertEqual(proc.stdout.strip(), "")
        finally:
            fixture.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
