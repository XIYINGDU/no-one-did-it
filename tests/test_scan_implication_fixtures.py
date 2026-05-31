"""Pytest harness for scan-implication.py against the fixture suite.

Asserts that every bad/*.md fixture trips at least one finding of its
declared expected_finding pattern, and every good/*.md fixture produces
zero findings. This is the regression guard against scanner drift —
adding a new pattern requires adding fixtures here first.
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK_PATH = ROOT / ".claude" / "hooks" / "scan-implication.py"
FIXTURE_DIR = ROOT / "tests" / "fixtures" / "implication-audit"


def _load_hook_module():
    spec = importlib.util.spec_from_file_location("scan_implication", HOOK_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


SCAN = _load_hook_module().scan


# (fixture relative path, expected finding name) for bad fixtures.
BAD_FIXTURES = (
    ("bad/anonymous-chain.md",         "anonymous-chain"),
    ("bad/chain-ladder.md",            "chain-ladder"),
    ("bad/decision-benefit.md",        "decision-benefit-juxtaposition"),
    ("bad/sympathetic-cold.md",        "sympathetic-then-cold"),
    ("bad/causation-adjacency.md",     "causation-by-adjacency"),
)

GOOD_FIXTURES = (
    "good/anonymous-chain.md",
    "good/chain-ladder.md",
    "good/decision-benefit.md",
    "good/sympathetic-cold.md",
    "good/causation-adjacency.md",
)


class TestScanImplicationFixtures(unittest.TestCase):
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
