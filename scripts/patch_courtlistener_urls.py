#!/usr/bin/env python3
"""
patch_courtlistener_urls.py — apply Class-A repair: fix CourtListener docket URLs
that point to wrong cases per the content audit.

Strategy:
  - Replace the wrong docket URL in source.url
  - Clear stale archive.body_sha256 and archive.wayback_url (verifier will refresh)
  - Append a verification_log entry recording the URL correction
"""
from __future__ import annotations
import re
import sys
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = PROJECT_ROOT / "book" / "source-ledger" / "cards"

# wrong_url → (new_url, reason)
REPLACEMENTS = {
    "https://www.courtlistener.com/docket/69820567/abrego-garcia-v-noem/":
        ("https://www.courtlistener.com/docket/69777799/abrego-garcia-v-noem/",
         "Wrong docket id (69820567 served United States v. Neumeyer); CourtListener API confirms 69777799 is Abrego Garcia v. Noem 8:25-cv-00951 (D. Md.)"),
    "https://www.courtlistener.com/docket/69782838/jgg-v-trump/":
        ("https://www.courtlistener.com/docket/69742076/jgg-v-trump/",
         "Wrong docket id (69782838 served Gloria Ann Scott); CourtListener API confirms 69742076 is J.G.G. v. TRUMP 1:25-cv-00766 (D.D.C.)"),
    "https://www.courtlistener.com/docket/69703927/citizens-for-responsibility-and-ethics-in-washington-v-us-doge-service/":
        ("https://www.courtlistener.com/docket/69658871/citizens-for-responsibility-and-ethics-in-washington-v-us-doge-service/",
         "Wrong docket id (69703927 served Tonya N. Corley); CourtListener API confirms 69658871 is CREW v. U.S. DOGE Service 1:25-cv-00511 (D.D.C.)"),
    "https://www.courtlistener.com/docket/4259014/united-states-v-slatten/":
        ("https://www.courtlistener.com/docket/5095365/united-states-v-slatten/",
         "Wrong docket id (4259014 served IPC The Hospitalist Co.); CourtListener API confirms 5095365 is United States v. SLATTEN 1:14-cr-00107 (D.D.C., filed 2014-05-08)"),
}


def patch_card(path: Path) -> tuple[bool, str]:
    raw = path.read_text(encoding="utf-8")
    fm_end = raw.find("\n---\n", 4)
    if fm_end < 0:
        return False, "no frontmatter"
    fm = raw[:fm_end]
    body = raw[fm_end:]

    changed = False
    matched_old = None
    for old, (new, reason) in REPLACEMENTS.items():
        if old in fm:
            fm = fm.replace(old, new)
            matched_old = old
            changed = True
            break
    if not changed:
        return False, "no matching URL"

    new_url, reason = REPLACEMENTS[matched_old]

    # Clear stale archive block (body_sha256, wayback_url) — verifier will re-capture.
    # Match archive: { ... } single-line OR multi-line block.
    fm = re.sub(
        r"  archive:\s*\{[^}]*\}",
        "  archive: {}",
        fm,
    )
    # Multi-line archive block: clear its children, leave key for the verifier.
    fm = re.sub(
        r"(  archive:\n)(?:    [^\n]+\n)+",
        r"\1",
        fm,
    )

    # Append verification_log entry for the URL correction.
    ts = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = (
        "  - step: url-correction\n"
        "    actor: stephen\n"
        f"    timestamp: {ts}\n"
        "    outcome: PASS\n"
        f"    notes: \"{reason}\"\n"
    )
    # Insert after the last existing verification_log entry; if no log, append after verification block.
    m = re.search(r"(verification_log:\n(?:  - [^\n]+\n(?:    [^\n]+\n)+)+)", fm)
    if m:
        fm = fm[:m.end()] + entry + fm[m.end():]
    else:
        # Add verification_log if missing
        fm += "\nverification_log:\n" + entry

    path.write_text(fm + body, encoding="utf-8")
    return True, f"patched ({matched_old[-40:]} → {new_url[-40:]})"


def main() -> int:
    targets = [
        "abrego-garcia-2019-withholding-of-removal-order",
        "abrego-garcia-procedural-status-may-2026",
        "abrego-garcia-v-noem-d-md-complaint-2025",
        "xinis-abrego-garcia-facilitate-effectuate-order-2025",
        "boasberg-jgg-contempt-finding-2025-04-16",
        "j-g-g-v-trump-ddc-complaint-2025-03-15",
        "crew-v-doge-service-ddc-complaint-2025-02-20",
        "ddc-docket-1-14-cr-00107-rcl",
    ]
    patched = 0
    for slug in targets:
        path = CARDS_DIR / f"{slug}.md"
        if not path.exists():
            print(f"  MISS  {slug}")
            continue
        ok, msg = patch_card(path)
        tag = "OK   " if ok else "SKIP "
        print(f"  {tag} {slug:60s} {msg}")
        if ok:
            patched += 1
    print(f"\npatched {patched}/{len(targets)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
