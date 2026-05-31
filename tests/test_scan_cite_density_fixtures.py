"""Pytest harness for scan-cite-density.py against the fixture suite.

Asserts that every bad/*.md fixture trips a finding, every good/*.md
fixture produces zero findings. Regression guard against rule-13 drift.
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK_PATH = ROOT / ".claude" / "hooks" / "scan-cite-density.py"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "cite-density"


def _load_hook_module():
    spec = importlib.util.spec_from_file_location("scan_cite_density", HOOK_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SCAN = _load_hook_module().scan


BAD_FIXTURES = (
    "bad/full-citation.md",
    "bad/corroboration-list.md",
    "bad/archive-metadata.md",
    "bad/hidden-metadata.md",
)

GOOD_FIXTURES = (
    "good/full-citation.md",
    "good/multi-slug.md",
    "good/pending-lock.md",
)


class TestScanCiteDensityFixtures(unittest.TestCase):
    def _read(self, rel: str) -> str:
        path = FIXTURE_DIR / rel
        self.assertTrue(path.exists(), f"missing fixture: {rel}")
        return path.read_text(encoding="utf-8")

    def test_bad_fixtures_trip_findings(self) -> None:
        for rel in BAD_FIXTURES:
            with self.subTest(fixture=rel):
                text = self._read(rel)
                findings = SCAN(text)
                self.assertGreater(
                    len(findings), 0,
                    f"{rel} produced no findings; expected at least one rule-13 violation",
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
