"""Tests for ``scripts/check_nlpm_specs.py`` — the static validator for
NLPM test specs under ``.nlpm-test/``."""

from pathlib import Path
import tempfile
import textwrap
import unittest

from scripts.check_nlpm_specs import (
    REQUIRED_LEAD_SPECS,
    check_repo,
    validate_spec,
)


ROOT = Path(__file__).resolve().parents[1]


class TestLiveSpecsAllPass(unittest.TestCase):
    def test_live_repo_has_all_required_lead_specs(self) -> None:
        passed, reports, gaps = check_repo(ROOT / ".nlpm-test", ROOT)
        self.assertTrue(
            passed,
            msg=(
                "Spec coverage / format gaps:\n"
                + "\n".join(f"  - {g}" for g in gaps)
                + "\n"
                + "\n".join(
                    f"  - {r.path}: " + "; ".join(r.issues)
                    for r in reports
                    if r.issues
                )
            ),
        )

    def test_each_lead_spec_references_its_agent(self) -> None:
        for lead in REQUIRED_LEAD_SPECS:
            spec = ROOT / ".nlpm-test" / f"{lead}.spec.md"
            self.assertTrue(spec.exists(), msg=f"missing spec for cell lead: {lead}")
            report = validate_spec(spec, ROOT)
            self.assertTrue(
                report.passed,
                msg=f"spec for {lead} has issues: {report.issues}",
            )


class TestStaticChecker(unittest.TestCase):
    def _make(self, body: str) -> tuple[Path, tempfile.TemporaryDirectory[str]]:
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        spec_dir = root / ".nlpm-test"
        spec_dir.mkdir()
        (root / ".claude" / "agents").mkdir(parents=True)
        (root / ".claude" / "agents" / "real-agent.md").write_text(
            "---\nname: real-agent\n---\nbody\n", encoding="utf-8"
        )
        spec = spec_dir / "real-agent.spec.md"
        spec.write_text(body, encoding="utf-8")
        return root, tmp

    def test_missing_frontmatter_is_flagged(self) -> None:
        root, tmp = self._make("no frontmatter here\n")
        try:
            passed, reports, _gaps = check_repo(root / ".nlpm-test", root)
            self.assertFalse(passed)
            self.assertTrue(
                any("missing frontmatter" in issue for r in reports for issue in r.issues)
            )
        finally:
            tmp.cleanup()

    def test_nonexistent_artifact_path_is_flagged(self) -> None:
        body = textwrap.dedent(
            """\
            ---
            artifact: .claude/agents/ghost-agent.md
            type: agent
            min_score: 90
            ---
            body
            """
        )
        root, tmp = self._make(body)
        try:
            passed, reports, _gaps = check_repo(root / ".nlpm-test", root)
            self.assertFalse(passed)
            self.assertTrue(
                any("does not exist" in issue for r in reports for issue in r.issues)
            )
        finally:
            tmp.cleanup()

    def test_type_mismatch_is_flagged(self) -> None:
        body = textwrap.dedent(
            """\
            ---
            artifact: .claude/agents/real-agent.md
            type: skill
            min_score: 90
            ---
            body
            """
        )
        root, tmp = self._make(body)
        try:
            passed, reports, _gaps = check_repo(root / ".nlpm-test", root)
            self.assertFalse(passed)
            self.assertTrue(
                any("does not match inferred type" in issue for r in reports for issue in r.issues)
            )
        finally:
            tmp.cleanup()

    def test_invalid_min_score_is_flagged(self) -> None:
        body = textwrap.dedent(
            """\
            ---
            artifact: .claude/agents/real-agent.md
            type: agent
            min_score: 200
            ---
            body
            """
        )
        root, tmp = self._make(body)
        try:
            passed, reports, _gaps = check_repo(root / ".nlpm-test", root)
            self.assertFalse(passed)
            self.assertTrue(
                any("must be 0-100" in issue for r in reports for issue in r.issues)
            )
        finally:
            tmp.cleanup()

    def test_coverage_gap_is_flagged(self) -> None:
        body = textwrap.dedent(
            """\
            ---
            artifact: .claude/agents/real-agent.md
            type: agent
            min_score: 90
            ---
            body
            """
        )
        root, tmp = self._make(body)
        try:
            passed, _reports, gaps = check_repo(root / ".nlpm-test", root)
            self.assertFalse(passed)
            # The fake repo has no cell-lead agents, so every required lead is a gap
            self.assertEqual(len(gaps), len(REQUIRED_LEAD_SPECS))
        finally:
            tmp.cleanup()


if __name__ == "__main__":
    unittest.main()
