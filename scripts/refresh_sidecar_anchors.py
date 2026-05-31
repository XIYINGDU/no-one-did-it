#!/usr/bin/env python3
"""Refresh source-ledger sidecars after the rule-13 Chicago citation
migration so that ``anchor_text`` matches what now appears in chapter
prose (the card slug) instead of the pre-migration verbose citation.

Before migration
----------------
The sidecar mapped the verbose in-prose `[CITE: <full citation>]` form
to one or more card_ids:

    - anchor_text: 'Leveson & Turner, "An Investigation of the Therac-25 Accidents," IEEE Computer 26(7) (Jul. 1993).'
      card_ids:
        - leveson-turner-therac-25-ieee-1993
      line_in_chapter: 24
      notes: "Accusation scene; ..."

After migration
---------------
Chapter prose now carries `[CITE: leveson-turner-therac-25-ieee-1993]`.
The sidecar should reflect that: ``anchor_text`` becomes the slug string
(matching the new bracket content), and the original human-readable
citation moves to a new ``description`` field that preserves the semantic
context Stephen and Nancy rely on:

    - anchor_text: leveson-turner-therac-25-ieee-1993
      card_ids:
        - leveson-turner-therac-25-ieee-1993
      description: 'Leveson & Turner, "An Investigation of the Therac-25 Accidents," IEEE Computer 26(7) (Jul. 1993).'
      line_in_chapter: 24
      notes: "Accusation scene; ..."

For multi-card anchors, the new anchor_text uses ``slug-a; slug-b``
(semicolon-separated) — matching the rule-13 multi-slug bracket form.

Idempotency
-----------
If ``anchor_text`` already matches the slug form (the script has already
run, or the sidecar was authored slug-form from the start), the anchor is
left untouched. ``description`` is added only on first refresh when no
description field exists yet.

Comment preservation
--------------------
The leading comment block (everything before the first non-comment,
non-blank line) is captured verbatim and re-emitted as the file header.
PyYAML round-tripping loses inline comments inside the body; that is an
accepted limitation. The sidecar's leading description block carries the
authorial intent; mid-file annotations are rare and recoverable from
git history.

Usage
-----
::

    python3 scripts/refresh_sidecar_anchors.py
        Refresh all sidecars under book/evidence/source-ledger/sidecars/.

    python3 scripts/refresh_sidecar_anchors.py --dry-run
        Report what would change without writing files.

    python3 scripts/refresh_sidecar_anchors.py --file <path>
        Refresh a single sidecar.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ERROR: PyYAML required. Install with: python3 -m pip install PyYAML",
          file=sys.stderr)
    sys.exit(2)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SIDECARS_DIR = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / "sidecars"


@dataclass
class RefreshStats:
    sidecar_path: Path
    total_anchors: int = 0
    anchors_refreshed: int = 0
    anchors_already_slug: int = 0
    anchors_skipped: int = 0
    cards_referenced: int = 0


SLUG_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")


def _looks_like_slug(text: str) -> bool:
    """Return True if the text already looks like a slug or slug-list."""
    if not text:
        return False
    parts = [p.strip() for p in text.split(";")]
    return all(SLUG_RE.match(p) for p in parts if p)


def _split_header_and_body(text: str) -> tuple[str, str]:
    """Return (header_comments, body) split at the first non-comment,
    non-blank YAML line. header_comments ends with a newline."""
    lines = text.splitlines(keepends=True)
    split_at = 0
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        split_at = i
        break
    return "".join(lines[:split_at]), "".join(lines[split_at:])


def refresh_anchors(anchors: list) -> tuple[list, RefreshStats]:
    """Walk the parsed anchors list, refreshing each entry's anchor_text
    to the slug form while preserving the original in a description field."""
    stats = RefreshStats(sidecar_path=Path())
    new_anchors: list = []
    for entry in anchors:
        if not isinstance(entry, dict):
            new_anchors.append(entry)
            stats.anchors_skipped += 1
            continue
        stats.total_anchors += 1
        old_anchor_text = (entry.get("anchor_text") or "").strip()
        card_ids = entry.get("card_ids") or []
        if not isinstance(card_ids, list) or not card_ids:
            new_anchors.append(entry)
            stats.anchors_skipped += 1
            continue
        stats.cards_referenced += len(card_ids)
        new_anchor_text = "; ".join(str(c).strip() for c in card_ids)
        if _looks_like_slug(old_anchor_text) and old_anchor_text == new_anchor_text:
            new_anchors.append(entry)
            stats.anchors_already_slug += 1
            continue
        # Preserve key order: anchor_text first, then card_ids, then
        # description (new), then everything else
        refreshed: dict = {"anchor_text": new_anchor_text, "card_ids": card_ids}
        if old_anchor_text and "description" not in entry:
            refreshed["description"] = old_anchor_text
        for k, v in entry.items():
            if k in ("anchor_text", "card_ids"):
                continue
            refreshed[k] = v
        new_anchors.append(refreshed)
        stats.anchors_refreshed += 1
    return new_anchors, stats


def refresh_sidecar(path: Path, dry_run: bool = False) -> RefreshStats:
    text = path.read_text(encoding="utf-8")
    header, body = _split_header_and_body(text)
    try:
        data = yaml.safe_load(body) or {}
    except yaml.YAMLError as exc:
        raise RuntimeError(f"YAML parse failed for {path}: {exc}") from exc

    anchors = data.get("anchors")
    if not isinstance(anchors, list):
        return RefreshStats(sidecar_path=path)

    new_anchors, stats = refresh_anchors(anchors)
    stats.sidecar_path = path

    if stats.anchors_refreshed == 0:
        return stats

    if dry_run:
        return stats

    data["anchors"] = new_anchors
    body_out = yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        width=2_000,
        default_flow_style=False,
    )
    if not header.endswith("\n"):
        header += "\n"
    if header and not header.endswith("\n\n"):
        header += "\n"
    refresh_note = (
        "# Refreshed by scripts/refresh_sidecar_anchors.py — anchor_text now\n"
        "# carries the card slug (matching the rule-13 [CITE: <slug>] form in\n"
        "# chapter prose). The original human-readable citation moved to the\n"
        "# `description` field on each anchor. PyYAML round-trip preserves the\n"
        "# leading comment block above but may have dropped any mid-file inline\n"
        "# comments; recover from git history if needed.\n\n"
    )
    if "Refreshed by scripts/refresh_sidecar_anchors.py" not in header:
        header += refresh_note
    path.write_text(header + body_out, encoding="utf-8")
    return stats


def _cli() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else "")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--file", type=Path, default=None)
    args = p.parse_args()

    targets: list[Path] = [args.file] if args.file else sorted(SIDECARS_DIR.glob("*.sources.yml"))
    if not targets:
        print("No sidecar files found.", file=sys.stderr)
        return 1

    grand_total = grand_refreshed = grand_already = grand_skipped = 0
    for target in targets:
        try:
            stats = refresh_sidecar(target, dry_run=args.dry_run)
        except RuntimeError as exc:
            print(f"ERROR refreshing {target}: {exc}", file=sys.stderr)
            return 2
        grand_total += stats.total_anchors
        grand_refreshed += stats.anchors_refreshed
        grand_already += stats.anchors_already_slug
        grand_skipped += stats.anchors_skipped
        action = "would refresh" if args.dry_run else "refreshed"
        print(
            f"  {target.name}: {stats.total_anchors} anchors; "
            f"{action} {stats.anchors_refreshed}; "
            f"{stats.anchors_already_slug} already slug-form; "
            f"{stats.anchors_skipped} skipped"
        )
    print(
        f"\nTotal: {grand_total} anchors across {len(targets)} sidecars; "
        f"{grand_refreshed} refreshed; "
        f"{grand_already} already slug-form; "
        f"{grand_skipped} skipped (no card_ids)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
