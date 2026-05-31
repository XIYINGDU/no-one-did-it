#!/usr/bin/env python3
"""
audit_card_content.py — full-corpus content-vs-claim audit for research cards.

For every URL-bearing card, fetch the actual document and compare its real identity
(title / first heading / first text) against the card's source.title. Flags any
card where the URL appears to deliver a document different from what the card claims.

Catches the Ross-memo defect class: a URL whose slug looks right, returns a 200,
gets a real sha256 and Wayback snapshot — but serves a different document than
the card claims.

Pipeline per card:
  1. Try fetching source.url (10s timeout, browser UA, follow redirects).
  2. If 4xx/5xx/timeout, try archive.wayback_url.
  3. Detect content type (HTML vs PDF vs other).
  4. Extract identity:
       HTML → <title>, og:title, first <h1>, first 400 chars of visible text
       PDF  → pdftotext first page (truncated)
  5. Compute token-overlap similarity between extracted identity and card.source.title.
  6. Emit a record.

The script only extracts short identifying fragments (titles + ≤400-char first
text), never reproduces long source content.

Output: book/evidence/source-ledger/.content-audit.json — list of:
  { slug, url, http_status, used_url, content_type, extracted_identity,
    card_title, similarity, flag }

Usage:
  python3 scripts/audit_card_content.py [--limit N] [--only <slug>]
"""

from __future__ import annotations

import argparse
import gzip
import io
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zlib
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CARDS_DIR = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / "cards"
OUT_PATH = PROJECT_ROOT / "book" / "evidence" / "source-ledger" / ".content-audit.json"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
)
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/pdf,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}
FETCH_TIMEOUT = 25
MAX_BYTES = 30 * 1024 * 1024
PDF_TEXT_CHARS = 8000
HTML_TEXT_CHARS = 1500


class _TitleExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._in_title = False
        self._in_h1 = False
        self._in_skip = 0
        self.title = ""
        self.h1 = ""
        self.og_title = ""
        self.text_chunks: list[str] = []
        self._text_len = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
        elif tag == "meta":
            d = {k.lower(): (v or "") for k, v in attrs}
            if d.get("property", "").lower() in ("og:title", "twitter:title") and not self.og_title:
                self.og_title = d.get("content", "")[:300]
        elif tag in ("script", "style", "noscript"):
            self._in_skip += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag in ("script", "style", "noscript"):
            self._in_skip = max(0, self._in_skip - 1)

    def handle_data(self, data: str) -> None:
        if self._in_skip:
            return
        if self._in_title:
            self.title = (self.title + data)[:300]
        elif self._in_h1 and len(self.h1) < 300:
            self.h1 = (self.h1 + data)[:300]
        elif self._text_len < HTML_TEXT_CHARS:
            d = data.strip()
            if d:
                self.text_chunks.append(d)
                self._text_len += len(d)


def _decompress(body: bytes, encoding: str) -> bytes:
    """Decompress gzip/deflate-encoded body. Returns body unchanged on failure or no encoding."""
    enc = (encoding or "").lower().strip()
    if not body or not enc or enc == "identity":
        return body
    try:
        if "gzip" in enc:
            return gzip.decompress(body)
        if "deflate" in enc:
            # Try raw deflate first, then zlib-wrapped.
            try:
                return zlib.decompress(body, -zlib.MAX_WBITS)
            except zlib.error:
                return zlib.decompress(body)
    except Exception:
        # If decompression fails, sniff for gzip magic and try anyway.
        if body[:2] == b"\x1f\x8b":
            try:
                return gzip.decompress(body)
            except Exception:
                pass
    return body


def fetch(url: str) -> tuple[int | None, bytes, str, str]:
    """Return (status, body_bytes, content_type, error). Body capped at MAX_BYTES (post-decompress)."""
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
            ctype = resp.headers.get("Content-Type", "")
            cenc = resp.headers.get("Content-Encoding", "")
            raw = resp.read(MAX_BYTES * 4)  # allow larger compressed payload
            body = _decompress(raw, cenc)
            # Some servers ignore Accept-Encoding but still serve gzip when the file is .gz-of-html
            if not cenc and body[:2] == b"\x1f\x8b":
                try:
                    body = gzip.decompress(body)
                except Exception:
                    pass
            return resp.status, body[:MAX_BYTES], ctype, ""
    except urllib.error.HTTPError as e:
        return e.code, b"", "", str(e)
    except urllib.error.URLError as e:
        return None, b"", "", str(e.reason)
    except Exception as e:
        return None, b"", "", str(e)


def extract_html_identity(body: bytes) -> dict:
    try:
        text = body.decode("utf-8", errors="replace")
    except Exception:
        text = body.decode("latin-1", errors="replace")
    p = _TitleExtractor()
    try:
        p.feed(text)
    except Exception:
        pass
    title = re.sub(r"\s+", " ", p.title).strip()
    h1 = re.sub(r"\s+", " ", p.h1).strip()
    og = re.sub(r"\s+", " ", p.og_title).strip()
    first_text = re.sub(r"\s+", " ", " ".join(p.text_chunks)).strip()[:HTML_TEXT_CHARS]
    return {"title": title[:300], "h1": h1[:300], "og_title": og[:300], "first_text": first_text}


def extract_pdf_identity(body: bytes) -> dict:
    if not body:
        return {"pdf_text": "", "pdf_meta_title": "", "error": "empty body"}
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
        f.write(body)
        tmp_path = f.name
    pdf_meta_title = ""
    try:
        # Layer 0: pdfinfo metadata Title (fastest, works on huge PDFs).
        try:
            info = subprocess.run(
                ["pdfinfo", tmp_path],
                capture_output=True, timeout=15
            )
            for line in info.stdout.decode("utf-8", errors="replace").splitlines():
                if line.lower().startswith("title:"):
                    pdf_meta_title = line.split(":", 1)[1].strip()[:300]
                    break
        except Exception:
            pass

        # Layer 1: pdftotext pages 1-5 with layout.
        result = subprocess.run(
            ["pdftotext", "-l", "5", "-layout", tmp_path, "-"],
            capture_output=True, timeout=30
        )
        text = result.stdout.decode("utf-8", errors="replace")
        text = re.sub(r"\s+", " ", text).strip()

        # Layer 2: if first 5 pages were thin OR text is shorter than the cap, expand to pages 1-30
        # without layout. Many treaty/statute compilations have TOC across pages 4-15.
        if len(text) < PDF_TEXT_CHARS:
            result2 = subprocess.run(
                ["pdftotext", "-l", "30", tmp_path, "-"],
                capture_output=True, timeout=45
            )
            text2 = result2.stdout.decode("utf-8", errors="replace")
            text2 = re.sub(r"\s+", " ", text2).strip()
            if len(text2) > len(text):
                text = text2

        combined = (pdf_meta_title + " | " + text).strip(" |")
        return {
            "pdf_text": combined[:PDF_TEXT_CHARS],
            "pdf_meta_title": pdf_meta_title,
            "error": "" if combined else "no text extracted",
        }
    except Exception as e:
        return {"pdf_text": "", "pdf_meta_title": pdf_meta_title, "error": str(e)}
    finally:
        try:
            Path(tmp_path).unlink()
        except Exception:
            pass


# JS-interstitial / bot-challenge / refresh-redirect indicators
_INTERSTITIAL_PATS = re.compile(
    r"(bm-verify=|cloudflare|cf-chl-bypass|Just a moment|Checking your browser|"
    r"Client Challenge|please enable JavaScript|enable javascript|"
    r"<meta\s+http-equiv=['\"]refresh['\"]|window\.location\s*=|"
    r"verify you are human|Access denied|You don['’]t have permission|"
    r"403 Forbidden|hcaptcha|recaptcha|datadome)",
    re.I,
)

# Interstitial-only titles (these tiny exact-match titles are themselves the signal)
_INTERSTITIAL_TITLES = {
    "making sure you're not a bot!",
    "making sure you’re not a bot!",
    "client challenge",
    "just a moment",
    "just a moment…",
    "checking your browser",
    "access denied",
    "attention required! | cloudflare",
}


def looks_like_interstitial(body: bytes, page_id: dict) -> bool:
    if not body:
        return False
    title = (page_id.get("title") or "").strip().lower()
    if title in _INTERSTITIAL_TITLES:
        return True
    if title in ("", "\xa0", "&nbsp;") and len(body) < 6000:
        return True
    if len(body) >= 14_000:
        return False
    try:
        text_head = body[:10000].decode("utf-8", errors="replace")
    except Exception:
        return False
    return bool(_INTERSTITIAL_PATS.search(text_head))


# Tokens used for similarity — lowercased word characters of length ≥3, lightly cleaned.
_TOKEN_RE = re.compile(r"[a-z0-9]{3,}")
_STOP = {
    "the","and","for","with","from","that","this","than","into","onto","over","under",
    "between","among","about","upon","through","against","not","also","com","www","https",
    "http","html","htm","pdf","doc","docx","org","gov","net","edu","page","sites","files",
    "default","content","article","story","report","memo","memorandum","document","press",
    "release","news","feb","jan","mar","apr","may","jun","jul","aug","sep","oct","nov","dec",
    "january","february","march","april","june","july","august","september","october",
    "november","december",
}


def tokens(s: str) -> set[str]:
    if not s:
        return set()
    return {t for t in _TOKEN_RE.findall(s.lower()) if t not in _STOP}


def similarity(claim_text: str, page_identity: dict) -> tuple[float, str]:
    """Best of max(recall, precision) across (title|og|h1|pdf|first_text) sources.

    Using max(recall, precision) handles two failure modes:
      - long card titles vs short page titles: short page title's tokens are mostly
        in the claim → high precision even when recall is low ("Common Cause v. Lewis"
        page title matches a verbose docket-detail card title).
      - short card claim vs long page text: claim tokens mostly on page → high recall
        even when precision is diluted.
    """
    claim_tok = tokens(claim_text)
    if not claim_tok:
        return 0.0, "(empty claim)"
    best = 0.0
    best_source = ""
    for label, text in [
        ("title", page_identity.get("title", "")),
        ("og_title", page_identity.get("og_title", "")),
        ("h1", page_identity.get("h1", "")),
        ("pdf_text", page_identity.get("pdf_text", "")),
        ("first_text", page_identity.get("first_text", "")),
    ]:
        page_tok = tokens(text)
        if not page_tok:
            continue
        overlap = claim_tok & page_tok
        if not overlap:
            continue
        recall = len(overlap) / len(claim_tok)
        precision = len(overlap) / len(page_tok)
        # Require a minimum overlap floor to avoid trivial single-token "matches"
        # on highly-generic words.
        if len(overlap) < 2:
            score = 0.0
        else:
            score = max(recall, precision)
        if score > best:
            best, best_source = score, label
    return best, best_source


def audit_card(card_path: Path) -> dict:
    raw = card_path.read_text(encoding="utf-8")
    end = raw.find("\n---\n", 4)
    if end < 0:
        return {"slug": card_path.stem, "error": "no frontmatter"}
    try:
        fm = yaml.safe_load(raw[4:end])
    except Exception as e:
        return {"slug": card_path.stem, "error": f"yaml: {e}"}
    if not fm:
        return {"slug": card_path.stem, "error": "empty frontmatter"}

    src = fm.get("source") or {}
    arc = src.get("archive") or {}
    url = src.get("url") or ""
    wb_url = arc.get("wayback_url") or ""
    title = src.get("title") or ""
    if not isinstance(title, str):
        title = str(title)
    title = title.strip()

    if not url:
        return {"slug": card_path.stem, "skipped": "no url"}
    if "/web/*/" in url:
        return {"slug": card_path.stem, "skipped": "template url"}

    def wayback_raw(u: str) -> str:
        # Rewrite https://web.archive.org/web/<ts>/<orig> → .../web/<ts>id_/<orig>
        # to strip the Wayback toolbar/chrome from the response.
        m = re.match(r"^(https?://web\.archive\.org/web/\d{14})/(.+)$", u)
        if m:
            return f"{m.group(1)}id_/{m.group(2)}"
        return u

    def do_extract(body_bytes: bytes, ctype_str: str) -> tuple[str, dict]:
        if not body_bytes:
            return "unknown", {}
        ct_lower = (ctype_str or "").lower()
        head = body_bytes[:1024]
        is_pdf = ct_lower.startswith("application/pdf") or head.startswith(b"%PDF")
        if is_pdf:
            return "pdf", extract_pdf_identity(body_bytes)
        return "html", extract_html_identity(body_bytes)

    # Try live URL first
    status, body, ctype, err = fetch(url)
    used = "live"
    used_url = url
    content_type, page_id = do_extract(body, ctype)
    sim, sim_source = similarity(title, page_id)

    # Detect HTTP-200-with-JS-interstitial responses (Cloudflare, justice.gov, etc.)
    is_interstitial = content_type == "html" and looks_like_interstitial(body, page_id)
    if is_interstitial:
        # Force fallback path; the live page is not the real document.
        sim = 0.0
        sim_source = "(interstitial)"

    # Fall back to Wayback if:
    #   (a) live fetch errored (4xx/5xx/timeout), OR
    #   (b) live fetched 200 but similarity is suspiciously low, OR
    #   (c) live returned a JS-interstitial / bot-challenge page
    try_wayback = wb_url and "/web/*/" not in wb_url
    fetch_failed = status is None or (status and (status >= 400 or status == 202))
    if try_wayback and (fetch_failed or is_interstitial or sim < 0.30):
        wb_raw = wayback_raw(wb_url)
        status2, body2, ctype2, err2 = fetch(wb_raw)
        if status2 and 200 <= status2 < 400 and body2:
            ct2, pg2 = do_extract(body2, ctype2)
            if ct2 == "html" and looks_like_interstitial(body2, pg2):
                # Wayback served the interstitial too — give up
                pass
            else:
                sim2, src2 = similarity(title, pg2)
                # Switch if live had failed/interstitial, or Wayback is strictly better.
                if fetch_failed or is_interstitial or sim2 > sim:
                    status, body, ctype, err = status2, body2, ctype2, err2
                    content_type, page_id = ct2, pg2
                    sim, sim_source = sim2, src2
                    used, used_url = "wayback", wb_raw
                    is_interstitial = False

    flag = "ok"
    if status is None or (status and status >= 400):
        flag = "fetch-failed"
    elif is_interstitial:
        flag = "interstitial-only"
    elif content_type == "unknown":
        flag = "unknown-content"
    elif sim < 0.20:
        flag = "MISMATCH-strong"
    elif sim < 0.40:
        flag = "MISMATCH-weak"

    rec = {
        "slug": card_path.stem,
        "card_title": title[:200],
        "card_url": url,
        "used": used,
        "used_url": used_url[:300],
        "http_status": status,
        "content_type": content_type,
        "extracted_title": (page_id.get("title") or page_id.get("og_title") or page_id.get("h1") or "")[:200],
        "extracted_first": (page_id.get("first_text") or page_id.get("pdf_text") or "")[:200],
        "similarity": round(sim, 3),
        "similarity_source": sim_source,
        "flag": flag,
        "fetch_error": err[:120] if err else "",
    }
    return rec


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int)
    parser.add_argument("--only", type=str)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    cards = sorted(CARDS_DIR.glob("*.md"))
    if args.only:
        cards = [c for c in cards if c.stem == args.only]
    if args.limit:
        cards = cards[: args.limit]

    out: list[dict] = []
    flagged = 0
    for i, c in enumerate(cards, 1):
        rec = audit_card(c)
        out.append(rec)
        flag = rec.get("flag", rec.get("skipped", rec.get("error", "?")))
        if flag.startswith("MISMATCH") or flag == "fetch-failed":
            flagged += 1
        if not args.quiet:
            sim = rec.get("similarity", "-")
            tag = (rec.get("flag") or rec.get("skipped") or "")[:18]
            print(f"[{i:3d}/{len(cards)}] {tag:18s} sim={sim} {c.stem[:50]}")

    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print()
    print(f"Wrote {OUT_PATH.relative_to(PROJECT_ROOT)} ({len(out)} records, {flagged} flagged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
