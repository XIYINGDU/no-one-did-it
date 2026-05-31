"""Tests for the source-ledger validator.

Runs the validator against the live ledger; HARD failures fail the test.
Warnings are allowed (orphan anchors during incremental rollout).
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = PROJECT_ROOT / "scripts" / "validate_source_ledger.py"


def test_validator_script_exists() -> None:
    assert VALIDATOR.exists(), f"validator missing at {VALIDATOR}"


def test_schema_exists() -> None:
    schema = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / "schema" / "research-card.schema.json"
    assert schema.exists(), f"schema missing at {schema}"


def test_validator_passes_no_network() -> None:
    """No-network run: schema, slug uniqueness, cross-references, grade discipline."""
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), "--quiet"],
        capture_output=True,
        text=True,
        cwd=str(PROJECT_ROOT),
    )
    assert result.returncode == 0, (
        f"validator returned {result.returncode}\n"
        f"stdout:\n{result.stdout}\n"
        f"stderr:\n{result.stderr}"
    )


def test_cards_directory_present() -> None:
    cards_dir = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / "cards"
    assert cards_dir.exists(), f"cards directory missing at {cards_dir}"


def test_sidecars_directory_present() -> None:
    sidecars_dir = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / "sidecars"
    assert sidecars_dir.exists(), f"sidecars directory missing at {sidecars_dir}"
