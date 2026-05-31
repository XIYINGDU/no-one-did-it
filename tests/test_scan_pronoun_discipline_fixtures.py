"""Pytest harness for scan-pronoun-discipline.py against the fixture suite.

Asserts that every bad/*.md fixture trips its expected rule-14 finding
and every good/*.md fixture produces zero findings.
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK_PATH = ROOT / ".claude" / "hooks" / "scan-pronoun-discipline.py"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "pronoun-discipline"


def _load_hook_module():
    spec = importlib.util.spec_from_file_location("scan_pronoun_discipline", HOOK_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SCAN = _load_hook_module().scan


BAD_FIXTURES = (
    ("bad/meta-this-chapter.md", "meta-frame:this-chapter"),
    ("bad/meta-the-book.md", "meta-frame:the-book"),
    ("bad/meta-the-reader.md", "meta-frame:the-reader"),
    ("bad/you-will.md", "you:address"),
    ("bad/for-you.md", "you:for-you"),
    ("bad/you-should.md", "modal:you-should"),
    ("bad/people-tend.md", "evasive:people-tend-to"),
)

GOOD_FIXTURES = (
    "good/we-pattern.md",
    "good/we-argue.md",
    "good/we-notice.md",
    "good/imperative.md",
    "good/for-us.md",
    "good/specific-group.md",
    "good/cited-quote-with-you.md",
    "good/heading-the-book.md",
)


class TestScanPronounDisciplineFixtures(unittest.TestCase):
    def _read(self, rel: str) -> str:
        path = FIXTURE_DIR / rel
        self.assertTrue(path.exists(), f"missing fixture: {rel}")
        return path.read_text(encoding="utf-8")

    def test_bad_fixtures_trip_expected_pattern(self) -> None:
        for rel, expected in BAD_FIXTURES:
            with self.subTest(fixture=rel):
                text = self._read(rel)
                findings = SCAN(text)
                self.assertGreater(
                    len(findings), 0,
                    f"{rel} produced no findings; expected at least one '{expected}'",
                )
                names = {name for _, name, _, _ in findings}
                self.assertIn(
                    expected, names,
                    f"{rel} did not trip the expected '{expected}' pattern; got {names}",
                )

    def test_good_fixtures_produce_no_findings(self) -> None:
        for rel in GOOD_FIXTURES:
            with self.subTest(fixture=rel):
                text = self._read(rel)
                findings = SCAN(text)
                self.assertEqual(
                    findings, [],
                    f"{rel} produced findings but is a 'good' (mitigated) fixture: {findings}",
                )


if __name__ == "__main__":
    unittest.main()
