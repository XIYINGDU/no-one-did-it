#!/usr/bin/env python3
"""Validate a built EPUB against the KDP gates in .claude/rules/16-kdp-epub.md.

Gates:
  1. epubcheck (W3C) — zero errors/fatals (warnings triaged). Spec conformance.
  2. Kindle Previewer 3 — converts to KFX/KF8 cleanly. The authoritative Kindle
     gate (a file can pass epubcheck and still break on a device).
  3. structural spot-checks — cover present, footnotes carry epub:type popup
     markup, no raw [CITE:]/[^N] text leaked into the body XHTML.

Each gate degrades gracefully if its tool is absent (reports SKIP, not FAIL), so
the script is useful on any machine; a shippable build requires gates 1 and 2 to
have actually run and passed.

    python3 pipelines/epub/validate_kdp_epub.py [path/to.epub]
"""
from __future__ import annotations

import csv
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EPUB = ROOT / "dist" / "no-one-did-it.epub"

RESULTS: list[tuple[str, str, str]] = []  # (gate, status, detail)


def record(gate: str, status: str, detail: str = "") -> None:
    RESULTS.append((gate, status, detail))
    print(f"[{status:4}] {gate}" + (f" — {detail}" if detail else ""))


def gate_epubcheck(epub: Path) -> None:
    exe = shutil.which("epubcheck")
    if not exe:
        record("epubcheck", "SKIP", "epubcheck not on PATH (brew install epubcheck)")
        return
    proc = subprocess.run([exe, str(epub)], capture_output=True, text=True)
    blob = proc.stdout + proc.stderr
    m = re.search(r"(\d+)\s+fatals?\s*/\s*(\d+)\s+errors?\s*/\s*(\d+)\s+warnings?", blob)
    if m:
        fatals, errors, warnings = (int(x) for x in m.groups())
        detail = f"{fatals} fatal / {errors} error / {warnings} warning"
        record("epubcheck", "PASS" if (fatals + errors) == 0 else "FAIL", detail)
    else:
        record("epubcheck", "PASS" if proc.returncode == 0 else "FAIL",
               f"exit {proc.returncode}")


def gate_kindle_previewer(epub: Path) -> None:
    exe = shutil.which("kindlepreviewer")
    if not exe:
        app = Path("/Applications/Kindle Previewer 3.app")
        if app.exists():
            record("Kindle Previewer", "SKIP",
                   "app installed but 'kindlepreviewer' not on PATH; run the GUI convert manually")
        else:
            record("Kindle Previewer", "SKIP", "Kindle Previewer 3 not installed")
        return
    with tempfile.TemporaryDirectory() as d:
        proc = subprocess.run([exe, str(epub), "-convert", "-output", d],
                             capture_output=True, text=True)
        blob = proc.stdout + proc.stderr
        # Kindle Previewer writes Summary_Log.csv — the authoritative result.
        summary = next(iter(Path(d).rglob("Summary_Log.csv")), None)
        if summary:
            rows = list(csv.DictReader(summary.read_text(encoding="utf-8-sig").splitlines()))
            if rows:
                r = rows[0]
                status = (r.get("Conversion Status") or "").strip()
                errs = (r.get("Error Count") or "0").strip() or "0"
                qissues = (r.get("Quality Issue Count") or "0").strip() or "0"
                detail = f"status={status}, errors={errs}, quality_issues={qissues}"
                if status.lower() == "success" and errs == "0":
                    record("Kindle Previewer", "PASS" if qissues == "0" else "WARN", detail)
                else:
                    record("Kindle Previewer", "FAIL", detail)
                return
        # fallback if no summary log
        kpf = list(Path(d).rglob("*.kpf"))
        ok = "converted successfully" in blob.lower() and bool(kpf)
        record("Kindle Previewer", "PASS" if ok else "FAIL",
               f"exit {proc.returncode}; kpf={'yes' if kpf else 'no'}")


def gate_structure(epub: Path) -> None:
    try:
        with zipfile.ZipFile(epub) as zf:
            names = zf.namelist()
            # Resolve the OPF via META-INF/container.xml (the spec rootfile),
            # falling back to the first .opf only if container.xml is missing.
            opf = None
            if "META-INF/container.xml" in names:
                cont = zf.read("META-INF/container.xml").decode("utf-8", "ignore")
                m = re.search(r'full-path="([^"]+\.opf)"', cont)
                if m and m.group(1) in names:
                    opf = m.group(1)
            if opf is None:
                opf = next((n for n in names if n.endswith(".opf")), None)
            opf_txt = zf.read(opf).decode("utf-8", "ignore") if opf else ""
            xhtml = "\n".join(
                zf.read(n).decode("utf-8", "ignore")
                for n in names if n.endswith((".xhtml", ".html")))
    except Exception as e:  # noqa: BLE001
        record("structure", "FAIL", f"not a valid zip/epub: {e}")
        return

    # cover declared?
    if "cover-image" in opf_txt or re.search(r'name="cover"', opf_txt):
        record("cover", "PASS", "cover-image declared in OPF")
    else:
        record("cover", "WARN", "no cover-image in OPF (coverless/draft build?)")

    # footnotes / references — two valid shapes:
    #   (a) pandoc-style popups: <sup epub:type="noteref"><a> ... </a></sup> +
    #       <aside epub:type="footnote"> ... </aside>. Kindle pops the note on click.
    #   (b) flip-to-back back-matter References section: superscript hyperlinks
    #       <sup><a href="text/chXXX.xhtml#cK-M">M</a></sup> pointing to anchored
    #       items in a visible References section. Reader clicks → jumps to back.
    # Either is shippable; both are recognised here.
    has_ref = 'epub:type="noteref"' in xhtml or 'type="noteref"' in xhtml
    has_note = 'epub:type="footnote"' in xhtml or 'type="footnote"' in xhtml
    # back-matter References shape: count cross-file hrefs to back-anchor ids cK-M
    # and the anchor spans they target. Pandoc emits `<a href="chXXX.xhtml#cK-M">
    # <sup>M</sup></a>` (link wraps the sup) and `<span id="cK-M">…</span>`.
    backmatter_links = len(re.findall(r'href="[^"]*#c\d+-\d+"', xhtml))
    backmatter_anchors = len(re.findall(r'id="c\d+-\d+"', xhtml))
    if has_ref and has_note:
        record("footnotes", "PASS",
               "popup style — epub:type noteref + footnote markup present")
    elif backmatter_links > 0 and backmatter_anchors > 0:
        record("footnotes", "PASS",
               f"flip-to-back style — {backmatter_links} sup-links, "
               f"{backmatter_anchors} anchor ids")
    elif has_ref or has_note:
        record("footnotes", "WARN",
               "only one side of the noteref/footnote relationship is present")
    else:
        record("footnotes", "WARN",
               "no footnote/reference markup found — neither popup nor back-matter")

    # leaked markers? — any literal [CITE:] or [^label] (numeric OR named slug) in the body
    leaks = []
    if "[CITE:" in xhtml:
        leaks.append("[CITE:]")
    if re.search(r"\[\^[\w-]+\]", xhtml):
        leaks.append("literal [^...] footnote ref")
    record("no leaked markers", "FAIL" if leaks else "PASS",
           ", ".join(leaks) if leaks else "no raw cite/footnote markers in body")

    # inline styles? — pandoc must not emit any `style="…"` attribute in the
    # built XHTML body. All presentation lives in book/design/epub/kdp.css. The build's
    # pipelines/epub/strip_inline_styles.lua filter is what enforces this; this gate
    # catches any regression — pandoc upgrade, build change, or accidental raw
    # HTML style="…" in the source.
    inline_styles = re.findall(r'\bstyle="[^"]*"', xhtml)
    if inline_styles:
        distinct = sorted(set(inline_styles))
        sample = distinct[:3]
        more = f" (+{len(distinct) - 3} more distinct)" if len(distinct) > 3 else ""
        record(
            "no inline styles",
            "FAIL",
            f"{len(inline_styles)} inline `style=\"…\"` attribute(s) in XHTML — "
            f"presentation must live in kdp.css; saw {sample}{more}",
        )
    else:
        record("no inline styles", "PASS",
               "0 inline `style=\"…\"` attributes — all presentation in kdp.css")


def main() -> int:
    allow_skips = "--allow-skips" in sys.argv
    positional = [a for a in sys.argv[1:] if not a.startswith("-")]
    epub = Path(positional[0]) if positional else DEFAULT_EPUB
    if not epub.exists():
        print(f"FAIL: EPUB not found: {epub} (build it with pipelines/epub/build_kdp_epub.py)",
              file=sys.stderr)
        return 1
    print(f"Validating {epub}\n")
    gate_epubcheck(epub)       # required gate 1
    gate_kindle_previewer(epub)  # required gate 2
    gate_structure(epub)

    fails = [g for g, s, _ in RESULTS if s == "FAIL"]
    warns = [g for g, s, _ in RESULTS if s == "WARN"]
    skips = [g for g, s, _ in RESULTS if s == "SKIP"]  # only the two required gates SKIP
    print()
    if fails:
        print(f"RESULT: NOT SHIPPABLE — {len(fails)} gate(s) FAILED: {fails}")
        return 1
    if skips and not allow_skips:
        print(f"RESULT: INCOMPLETE — {len(skips)} required gate(s) SKIPPED (tool unavailable): "
              f"{skips}. Install the tool(s) and re-run before shipping, or pass --allow-skips "
              f"for a local advisory run.")
        return 1
    if warns:
        print(f"RESULT: PASSED WITH WARNINGS — {len(warns)} warning(s): {warns}. "
              f"Resolve before shipping (e.g. coverless/draft, Kindle quality issues)."
              + (f" [{len(skips)} required gate(s) skipped via --allow-skips]" if skips else ""))
        return 0
    if skips:  # reached only with --allow-skips (un-allowed skips returned 1 above)
        print(f"RESULT: PASSED (advisory) — {len(skips)} required gate(s) skipped via "
              f"--allow-skips: {skips}. NOT a shipping certification; re-run with the tool(s) "
              f"installed before shipping.")
        return 0
    print("RESULT: all gates PASS — shippable to KDP.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
