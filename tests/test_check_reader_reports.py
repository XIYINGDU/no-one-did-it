"""Regression tests for the reader-report gate's override semantics.

Per rule 15-reader-experience-authority.md, a HARD finding blocks v3
promotion until resolved OR until xaiolai records an override. The gate
(scripts/check_reader_reports.py) is the deterministic enforcement, and it
must honour a recorded override — otherwise it contradicts both rule 15 and
its own "record an xaiolai override" remedy message.

These tests pin three properties:
  1. read_verdict distinguishes CLEAN / BLOCKED / OVERRIDE / UNKNOWN.
  2. An override requires BOTH the OVERRIDE token and the xaiolai
     attribution; "override" without attribution stays BLOCKED (no casual
     bypass).
  3. --gate passes when chapters are CLEAN or OVERRIDE, and fails on a
     bare BLOCKED.
"""

from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import check_reader_reports as crr  # type: ignore[import-not-found]


def _report(verdict_line: str) -> str:
    return f"Owner: the-reader\n\n## Verdict\n\n{verdict_line}\n\n## Findings\n"


class TestReadVerdict(unittest.TestCase):
    def _verdict(self, verdict_line: str) -> str:
        with TemporaryDirectory() as d:
            p = Path(d) / "r.md"
            p.write_text(_report(verdict_line), encoding="utf-8")
            return crr.read_verdict(p)

    def test_clean(self) -> None:
        self.assertEqual(self._verdict("CLEAN — no HARD findings."), "CLEAN")

    def test_blocked(self) -> None:
        self.assertEqual(self._verdict("BLOCKED — 1 HARD."), "BLOCKED")

    def test_override_wins_over_blocked(self) -> None:
        line = ("BLOCKED — 1 HARD · OVERRIDE (xaiolai, 2026-05-28): the HARD is "
                "the author's standing item; gate-block overridden.")
        self.assertEqual(self._verdict(line), "OVERRIDE")

    def test_override_accepts_xiaolai_spelling(self) -> None:
        self.assertEqual(
            self._verdict("BLOCKED — 1 HARD · OVERRIDE (xiaolai, 2026-05-28)."),
            "OVERRIDE",
        )

    def test_override_token_without_attribution_stays_blocked(self) -> None:
        # No casual bypass: "override" without the xaiolai attribution must
        # not lift the block.
        self.assertEqual(
            self._verdict("BLOCKED — 1 HARD. We could override this later."),
            "BLOCKED",
        )

    def test_unknown(self) -> None:
        self.assertEqual(self._verdict("pending review"), "UNKNOWN")


class TestGate(unittest.TestCase):
    def _run(self, reports: dict[str, str], gate: bool) -> tuple[int, str]:
        """Build a throwaway project tree and run the gate against it."""
        with TemporaryDirectory() as d:
            root = Path(d)
            (root / "book" / "chapters-v6").mkdir(parents=True)
            (root / "process" / "reader-reports").mkdir(parents=True)
            for slug, verdict_line in reports.items():
                (root / "book" / "chapters-v6" / f"{slug}.md").write_text(
                    "# chapter\n", encoding="utf-8")
                (root / "process" / "reader-reports" / f"{slug}-2026-05-28.md").write_text(
                    _report(verdict_line), encoding="utf-8")
            argv = ["--project-root", str(root)]
            if gate:
                argv.append("--gate")
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = crr.main(argv)
            return rc, buf.getvalue()

    def test_gate_passes_on_clean_and_override(self) -> None:
        rc, out = self._run(
            {
                "01-a": "CLEAN — no HARD findings.",
                "13-z": "BLOCKED — 1 HARD · OVERRIDE (xaiolai, 2026-05-28).",
            },
            gate=True,
        )
        self.assertEqual(rc, 0, out)
        self.assertIn("GATE PASS", out)
        self.assertIn("OVERRIDE (xaiolai):  1", out)
        self.assertIn("retirement", out)

    def test_gate_fails_on_bare_blocked(self) -> None:
        rc, out = self._run(
            {
                "01-a": "CLEAN — no HARD findings.",
                "13-z": "BLOCKED — 1 HARD.",
            },
            gate=True,
        )
        self.assertEqual(rc, 1, out)
        self.assertIn("GATE FAIL", out)


if __name__ == "__main__":
    unittest.main()
