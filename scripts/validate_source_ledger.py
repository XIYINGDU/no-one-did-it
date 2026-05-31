#!/usr/bin/env python3
"""
validate_source_ledger.py — Layer A mechanical validator for research cards.

Checks:
  1. Schema compliance (hand-validated against research-card.schema.json fields)
  2. Slug uniqueness across cards/
  3. Source-type membership in bounded taxonomy
  4. URL well-formedness
  5. URL liveness (only when --check-urls passed)
  6. sha256 drift detection (only when --check-drift passed; requires --check-urls)
  7. Cross-reference integrity: every chapters_citing entry resolves to a real chapter;
     every sidecar card_id resolves to a card; every chapter [CITE:] anchor has sidecar coverage
  8. Orphan detection (warn): cards with no chapters_citing entries
  9. Grade-discipline coupling: C requires dispute non-empty; D cannot be cited from chapters
 10. Living-subject gate: living_subjects non-empty requires nancy_cleared=true

Usage:
  python3 scripts/validate_source_ledger.py [--check-urls] [--check-drift] [--strict-orphans]

Exit codes:
  0 — all checks pass (warnings allowed)
  1 — at least one HARD failure
  2 — script-level error (e.g., schema not found)
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

import yaml


def _as_string(value: Any) -> Any:
    """Coerce PyYAML-parsed date/datetime objects back to ISO strings for regex checks."""
    if isinstance(value, datetime.datetime):
        return value.date().isoformat()
    if isinstance(value, datetime.date):
        return value.isoformat()
    if isinstance(value, int):
        return str(value)
    return value

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LEDGER_ROOT = PROJECT_ROOT / "book" / "evidence" / "source-ledger"
CARDS_DIR = LEDGER_ROOT / "cards"
SIDECARS_DIR = LEDGER_ROOT / "sidecars"
SCHEMA_PATH = LEDGER_ROOT / "schema" / "research-card.schema.json"
CHAPTERS_DIR = PROJECT_ROOT / "book" / "chapters-v6"
CASE_FILES_DIR = PROJECT_ROOT / "book" / "evidence" / "case-files"

CITE_ANCHOR_RE = re.compile(r"\[CITE:\s*([^\]]*?)\]", re.DOTALL)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_RELAXED_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


class Finding:
    def __init__(self, severity: str, where: str, message: str) -> None:
        self.severity = severity  # "HARD" | "WARN"
        self.where = where
        self.message = message

    def __str__(self) -> str:
        return f"[{self.severity}] {self.where}: {self.message}"


def load_schema() -> dict[str, Any]:
    if not SCHEMA_PATH.exists():
        print(f"FATAL: schema not found at {SCHEMA_PATH}", file=sys.stderr)
        sys.exit(2)
    with SCHEMA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_frontmatter(card_path: Path) -> dict[str, Any] | None:
    raw = card_path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        return None
    end = raw.find("\n---\n", 4)
    if end == -1:
        return None
    fm_yaml = raw[4:end]
    try:
        return yaml.safe_load(fm_yaml)
    except yaml.YAMLError as exc:
        raise ValueError(f"malformed YAML in {card_path}: {exc}") from exc


def check_required_fields(card: dict[str, Any], schema: dict[str, Any], where: str) -> list[Finding]:
    findings: list[Finding] = []
    required = schema.get("required", [])
    for field in required:
        if field not in card:
            findings.append(Finding("HARD", where, f"missing required field '{field}'"))
    return findings


def check_enum(value: Any, allowed: list[str], where: str, field: str) -> list[Finding]:
    if value is None:
        return []
    if value not in allowed:
        return [Finding("HARD", where, f"{field}='{value}' not in allowed set {allowed}")]
    return []


def check_pattern(value: Any, pattern: re.Pattern[str], where: str, field: str) -> list[Finding]:
    if value is None:
        return []
    s = _as_string(value)
    if not isinstance(s, str) or not pattern.match(s):
        return [Finding("HARD", where, f"{field}='{value}' fails pattern {pattern.pattern}")]
    return []


def check_url_wellformed(url: str | None, where: str, field: str) -> list[Finding]:
    if url is None:
        return []
    try:
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return [Finding("HARD", where, f"{field}='{url}' is not a well-formed URL")]
    except ValueError as exc:
        return [Finding("HARD", where, f"{field} parse error: {exc}")]
    return []


def check_url_live(url: str, where: str) -> Finding | None:
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "source-ledger-validator/0.1"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            if 200 <= status < 400:
                return None
            return Finding("WARN", where, f"URL liveness check returned status {status}")
    except Exception as exc:
        return Finding("WARN", where, f"URL liveness check failed: {exc}")


def check_sha256_drift(url: str, expected_sha256: str, where: str) -> Finding | None:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "source-ledger-validator/0.1"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read()
        actual = hashlib.sha256(body).hexdigest()
        if actual != expected_sha256:
            return Finding(
                "WARN",
                where,
                f"sha256 drift: stored={expected_sha256[:12]}... actual={actual[:12]}...",
            )
    except Exception as exc:
        return Finding("WARN", where, f"sha256 drift check failed to fetch: {exc}")
    return None


def validate_card(card_path: Path, schema: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    where = str(card_path.relative_to(PROJECT_ROOT))

    try:
        card = parse_frontmatter(card_path)
    except ValueError as exc:
        return [Finding("HARD", where, str(exc))]

    if card is None:
        return [Finding("HARD", where, "no YAML frontmatter found")]

    # top-level required
    findings.extend(check_required_fields(card, schema, where))
    if any(f.severity == "HARD" for f in findings):
        return findings

    # id
    findings.extend(check_pattern(card.get("id"), SLUG_RE, where, "id"))

    # source
    src = card.get("source", {})
    src_required = schema["properties"]["source"]["required"]
    for field in src_required:
        if field not in src:
            findings.append(Finding("HARD", where, f"source.{field} missing"))
    src_type_enum = schema["properties"]["source"]["properties"]["type"]["enum"]
    findings.extend(check_enum(src.get("type"), src_type_enum, where, "source.type"))
    access_enum = schema["properties"]["source"]["properties"]["access_constraint"]["enum"]
    findings.extend(check_enum(src.get("access_constraint"), access_enum, where, "source.access_constraint"))
    findings.extend(check_pattern(src.get("publication_date"), DATE_RELAXED_RE, where, "source.publication_date"))
    findings.extend(check_url_wellformed(src.get("url"), where, "source.url"))
    if src.get("access_constraint") == "open-web" and not src.get("url"):
        findings.append(Finding("HARD", where, "source.url required when access_constraint=open-web"))

    # archive
    archive = src.get("archive") or {}
    findings.extend(check_url_wellformed(archive.get("wayback_url"), where, "source.archive.wayback_url"))
    findings.extend(check_pattern(archive.get("wayback_captured"), DATE_RE, where, "source.archive.wayback_captured"))

    # claim
    claim = card.get("claim", {})
    if "text" not in claim:
        findings.append(Finding("HARD", where, "claim.text missing"))
    alt_enum = schema["properties"]["claim"]["properties"]["quote_alteration"]["enum"]
    findings.extend(check_enum(claim.get("quote_alteration"), alt_enum, where, "claim.quote_alteration"))
    perm_enum = schema["properties"]["claim"]["properties"]["quote_permission"]["enum"]
    findings.extend(check_enum(claim.get("quote_permission"), perm_enum, where, "claim.quote_permission"))

    # verification
    ver = card.get("verification", {})
    grade_enum = schema["properties"]["verification"]["properties"]["evidence_grade"]["enum"]
    findings.extend(check_enum(ver.get("evidence_grade"), grade_enum, where, "verification.evidence_grade"))
    if ver.get("evidence_grade") in ("A", "B", "C"):
        if not ver.get("verified_by"):
            findings.append(Finding("HARD", where, f"verification.verified_by required for grade {ver.get('evidence_grade')}"))
        if not ver.get("verified_on"):
            findings.append(Finding("HARD", where, f"verification.verified_on required for grade {ver.get('evidence_grade')}"))
    findings.extend(check_pattern(ver.get("verified_on"), DATE_RE, where, "verification.verified_on"))
    findings.extend(check_pattern(ver.get("body_sha256"), SHA256_RE, where, "verification.body_sha256"))

    # dispute
    disp = card.get("dispute", {})
    if "status" not in disp:
        findings.append(Finding("HARD", where, "dispute.status missing"))
    else:
        status = disp["status"]
        if not re.match(r"^(undisputed|contested|withdrawn|superseded-by:[a-z0-9-]+)$", status):
            findings.append(Finding("HARD", where, f"dispute.status='{status}' fails pattern"))

    # defamation gate
    defm = card.get("defamation", {})
    if "living_subjects" not in defm:
        findings.append(Finding("HARD", where, "defamation.living_subjects missing"))
    elif defm["living_subjects"]:
        if not defm.get("nancy_cleared"):
            findings.append(Finding("HARD", where, "living_subjects non-empty but defamation.nancy_cleared not true"))
        if defm.get("nancy_cleared") and not defm.get("nancy_cleared_on"):
            findings.append(Finding("HARD", where, "nancy_cleared=true requires nancy_cleared_on date"))

    # grade-discipline coupling
    if ver.get("evidence_grade") == "C":
        if disp.get("status") == "undisputed":
            findings.append(Finding("WARN", where, "grade=C with dispute.status=undisputed; rule 02 expects dispute context for C-grade"))
    if ver.get("evidence_grade") == "D":
        refs = card.get("references", {})
        if refs.get("chapters_citing"):
            findings.append(Finding("HARD", where, "grade=D cards cannot be cited from chapters per rule 30 / 02"))

    # references
    refs = card.get("references", {})
    if "cases_affected" not in refs:
        findings.append(Finding("HARD", where, "references.cases_affected missing"))
    if "chapters_citing" not in refs:
        findings.append(Finding("HARD", where, "references.chapters_citing missing"))

    # provenance
    prov = card.get("provenance", {})
    for field in ("created_by", "created_on", "superseded_by"):
        if field not in prov:
            findings.append(Finding("HARD", where, f"provenance.{field} missing"))
    findings.extend(check_pattern(prov.get("created_on"), DATE_RE, where, "provenance.created_on"))

    return findings


def gather_all_cards() -> list[Path]:
    if not CARDS_DIR.exists():
        return []
    return sorted(CARDS_DIR.glob("*.md"))


def gather_all_chapters() -> list[Path]:
    return sorted(p for p in CHAPTERS_DIR.glob("*.md") if "brief" not in p.name)


def gather_sidecars() -> dict[str, Path]:
    if not SIDECARS_DIR.exists():
        return {}
    return {p.stem.replace(".sources", ""): p for p in SIDECARS_DIR.glob("*.sources.yml")}


def gather_case_files() -> list[Path]:
    if not CASE_FILES_DIR.exists():
        return []
    return sorted(p for p in CASE_FILES_DIR.glob("*.md") if not p.name.startswith("_"))


def validate_case_files(
    case_files: list[Path],
    cards_by_id: dict[str, dict[str, Any]],
) -> list[Finding]:
    """Check every case file's sources[].card_id resolves to a real card,
    and warn if a status:ready case file has no sources block."""
    findings: list[Finding] = []
    for case_path in case_files:
        where = f"case-files/{case_path.name}"
        try:
            card = parse_frontmatter(case_path)
        except ValueError as exc:
            findings.append(Finding("HARD", where, f"malformed YAML: {exc}"))
            continue
        if card is None:
            # Case files are not required to have frontmatter; skip silently
            continue
        status = card.get("status")
        sources = card.get("sources") or []
        # status:ready requires sources block (unless _example file)
        if status == "ready" and not sources and not case_path.name.startswith("_"):
            findings.append(
                Finding("WARN", where, "status:ready case file has no sources: block")
            )
        # Every card_id in sources[] must resolve to a real card
        for entry in sources:
            if not isinstance(entry, dict):
                continue
            cid = entry.get("card_id")
            if cid and cid not in cards_by_id:
                findings.append(
                    Finding("HARD", where, f"sources[].card_id '{cid}' does not exist in cards/")
                )
    return findings


def cross_reference_integrity(
    cards_by_id: dict[str, dict[str, Any]],
    chapters: list[Path],
    sidecars: dict[str, Path],
    strict_orphans: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    chapter_stems = {p.stem for p in chapters}

    # chapters_citing -> chapter exists
    for card_id, card in cards_by_id.items():
        where = f"cards/{card_id}.md"
        for ch_stem in card.get("references", {}).get("chapters_citing", []) or []:
            if ch_stem not in chapter_stems:
                findings.append(Finding("HARD", where, f"references.chapters_citing entry '{ch_stem}' is not a real chapter"))

    # sidecar card_ids resolve
    sidecar_card_refs: dict[str, set[str]] = {}  # chapter_stem -> set of card_ids referenced
    for ch_stem, sidecar_path in sidecars.items():
        where = f"sidecars/{sidecar_path.name}"
        try:
            with sidecar_path.open("r", encoding="utf-8") as f:
                sidecar = yaml.safe_load(f) or {}
        except yaml.YAMLError as exc:
            findings.append(Finding("HARD", where, f"malformed YAML: {exc}"))
            continue
        if ch_stem not in chapter_stems:
            findings.append(Finding("HARD", where, f"sidecar stem '{ch_stem}' does not match any chapter"))
        sidecar_card_refs.setdefault(ch_stem, set())
        for anchor in sidecar.get("anchors", []) or []:
            for cid in anchor.get("card_ids", []) or []:
                sidecar_card_refs[ch_stem].add(cid)
                if cid not in cards_by_id:
                    findings.append(Finding("HARD", where, f"sidecar references card_id '{cid}' that does not exist in cards/"))

    # orphan cards (no chapter cites) — skip cards explicitly superseded or withdrawn
    for card_id, card in cards_by_id.items():
        refs = card.get("references", {})
        chapter_refs = set(refs.get("chapters_citing") or [])
        sidecar_refs = {ch for ch, ids in sidecar_card_refs.items() if card_id in ids}
        dispute_status = (card.get("dispute") or {}).get("status", "")
        is_superseded_or_withdrawn = (
            dispute_status.startswith("superseded-by:") or dispute_status == "withdrawn"
        )
        if not chapter_refs and not sidecar_refs and not is_superseded_or_withdrawn:
            severity = "HARD" if strict_orphans else "WARN"
            findings.append(Finding(severity, f"cards/{card_id}.md", "orphan: no chapter references this card"))

    # orphan anchors (chapter [CITE:] not in sidecar) — only when sidecar exists for that chapter
    for chapter_path in chapters:
        ch_stem = chapter_path.stem
        if ch_stem not in sidecars:
            continue  # no sidecar yet; not an error during incremental rollout
        prose = chapter_path.read_text(encoding="utf-8")
        anchors_in_prose = CITE_ANCHOR_RE.findall(prose)
        try:
            with sidecars[ch_stem].open("r", encoding="utf-8") as f:
                sidecar = yaml.safe_load(f) or {}
        except yaml.YAMLError:
            continue
        anchors_in_sidecar = {a.get("anchor_text") for a in (sidecar.get("anchors") or [])}
        for anchor_text in anchors_in_prose:
            anchor_text_norm = " ".join(anchor_text.split())[:200]
            matched = any(
                anchor_text_norm in (existing or "") or (existing or "") in anchor_text_norm
                for existing in anchors_in_sidecar
            )
            if not matched:
                findings.append(
                    Finding(
                        "WARN",
                        f"chapters/{chapter_path.name}",
                        f"[CITE:] anchor not covered by sidecar: '{anchor_text_norm[:80]}...'",
                    )
                )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the source-ledger.")
    parser.add_argument("--check-urls", action="store_true", help="HEAD-request each source.url (slow; network).")
    parser.add_argument("--check-drift", action="store_true", help="Re-fetch source.url, compare sha256 (slow; network).")
    parser.add_argument("--strict-orphans", action="store_true", help="Treat orphan cards as HARD failure.")
    parser.add_argument("--quiet", action="store_true", help="Only print failures.")
    args = parser.parse_args()

    schema = load_schema()

    cards = gather_all_cards()
    chapters = gather_all_chapters()
    sidecars = gather_sidecars()
    case_files = gather_case_files()

    if not args.quiet:
        print(f"Source-ledger validator")
        print(f"  cards      : {len(cards)} in {CARDS_DIR.relative_to(PROJECT_ROOT)}")
        print(f"  chapters   : {len(chapters)} in {CHAPTERS_DIR.relative_to(PROJECT_ROOT)}")
        print(f"  sidecars   : {len(sidecars)} in {SIDECARS_DIR.relative_to(PROJECT_ROOT)}")
        print(f"  case-files : {len(case_files)} in {CASE_FILES_DIR.relative_to(PROJECT_ROOT)}")
        print()

    all_findings: list[Finding] = []
    cards_by_id: dict[str, dict[str, Any]] = {}
    seen_ids: set[str] = set()

    for card_path in cards:
        card_findings = validate_card(card_path, schema)
        all_findings.extend(card_findings)
        if not any(f.severity == "HARD" for f in card_findings):
            try:
                card = parse_frontmatter(card_path)
            except ValueError:
                continue
            if card and card.get("id"):
                cid = card["id"]
                if cid in seen_ids:
                    all_findings.append(Finding("HARD", str(card_path.relative_to(PROJECT_ROOT)), f"duplicate id '{cid}'"))
                seen_ids.add(cid)
                cards_by_id[cid] = card

    # cross-reference integrity
    all_findings.extend(cross_reference_integrity(cards_by_id, chapters, sidecars, args.strict_orphans))

    # case-file gate
    all_findings.extend(validate_case_files(case_files, cards_by_id))

    # optional network checks
    if args.check_urls or args.check_drift:
        for card_id, card in cards_by_id.items():
            url = card.get("source", {}).get("url")
            if not url:
                continue
            where = f"cards/{card_id}.md"
            if args.check_urls:
                f = check_url_live(url, where)
                if f:
                    all_findings.append(f)
            if args.check_drift:
                stored = card.get("verification", {}).get("body_sha256")
                if stored:
                    f = check_sha256_drift(url, stored, where)
                    if f:
                        all_findings.append(f)

    # report
    hard = [f for f in all_findings if f.severity == "HARD"]
    warn = [f for f in all_findings if f.severity == "WARN"]
    if hard:
        print(f"HARD failures ({len(hard)}):")
        for f in hard:
            print(f"  {f}")
        print()
    if warn and not args.quiet:
        print(f"Warnings ({len(warn)}):")
        for f in warn:
            print(f"  {f}")
        print()

    if hard:
        print("FAIL: source-ledger validation found HARD failures.")
        return 1
    if not args.quiet:
        print(f"OK: source-ledger ({len(cards)} cards, {len(sidecars)} sidecars).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
