# Release Preparation — Public push to `github.com/xiaolai/responsibility-laundering`

**Status:** pre-push
**Last updated:** 2026-05-30
**Decision-of-record:** ship all (A1) — production audit trail and review memos are included in the public repo per author decision 2026-05-30.

This file is the ordered sequence to take the standalone repo public. Each step has an owner and a clear "done" criterion. The push does not happen until every blocking step is cleared.

## Sequenced steps

### Step 1 — Nancy public-release pass on `process/review-memos/`

- **Owner:** `nancy-legal-risk-counsel`
- **Scope:** 13 per-chapter review memos under `process/review-memos/`, plus the portfolio-level Nancy sweep memo.
- **Why:** The memos were authored as internal working notes. Per-chapter formulations like *"ch-N paragraph X is defamation surface; we should hedge to Y"* were safe in a private working context but read differently when public — a roadmap to the legal seams. Some may need rewording before they ship, even though the underlying chapter prose Nancy vetoed survived to publication.
- **Done when:** Every Nancy-authored review memo carries (a) a clean public-release sign-off in its frontmatter, or (b) a redaction-applied pass that rewrites internal-language formulations for public consumption without losing the substance.
- **Blocking:** Yes.

### Step 2 — Secret / sensitive-data sweep

- **Owner:** automated scan + manual review
- **Scope:** entire working tree, including `dev-docs/`, `dev-docs/` (once populated), and all hidden directories
- **Looking for:** API keys, tokens, credentials in any form; internal hostnames or private IPs; email addresses (other than the author's intentionally public ones); `.env`-shaped files; any "personal notes / FYI / xaiolai-only" content that was never intended for public consumption.
- **Done when:** Zero findings or all findings remediated.
- **Blocking:** Yes.

### Step 3 — Repository reorganization

- **Owner:** mechanical edits
- **Scope:**
  - Create top-level `dev-docs/`; move v1–v5 chapter directories from `dev-docs/04_ARCHIVE_SUPERSEDED_OR_REFERENCE/` to `dev-docs/`. Write `dev-docs/README.md` noting v6 in `book/chapters-v6/` is canonical.
  - Verify `book/proposals/` exclusion (per the direct-KDP-publish decision, files are source-pool, not for public).
  - Verify `.codex/`, `.gemini/`, `.agents/` are excluded or left as empty placeholders.
  - Verify `pipelines/print/node_modules/`, `pipelines/print/out/`, `pipelines/print/package-lock.json`, and `.venv/` are excluded (gitignored — runtime artifacts).
- **Done when:** Tree matches the README layout block; no excluded directories carry content; all tests still pass.
- **Blocking:** Yes.

### Step 3b — Print PDF artifacts (already built)

- **Status:** ✓ complete — `dist/no-one-did-it-interior.pdf` (446pp, 6×9, 20MB) + `dist/no-one-did-it-cover.pdf` (full wrap, 13.365×9.25, 1.4MB) built 2026-05-30 via the `pipelines/print/` pipeline ported from The Half Second.
- **Reproduction:** `cd print && node pipeline.mjs` — assumes Node + .venv prereqs per `pipelines/print/README.md`.
- **KDP submission readiness:** interior fonts embedded (EB Garamond + JetBrains Mono + Georgia Italic overlay); cover at 300 DPI with 0.125″ bleed; spine width computed for cream paper. Both pass `pdfinfo` dimension checks.

### Step 4 — `LICENSE` file

- **Owner:** mechanical
- **Scope:** Create top-level `LICENSE` carrying both license texts: CC BY-NC 4.0 for prose (with the explicit directory mapping in the README), and MIT for the apparatus.
- **Done when:** `LICENSE` exists with both texts and a directory-to-license table.
- **Blocking:** Yes.

### Step 5 — KDP listing link

- **Owner:** xiaolai
- **Scope:** When the KDP listing goes live, replace the placeholder `[link added on publication]` in `README.md` with the actual Amazon URL.
- **Done when:** Real link in README; no placeholder.
- **Blocking:** Soft. The repo can go public before the listing, with the placeholder visible. Tighter sequencing: KDP first, then push.

### Step 6 — Create the GitHub repo

- **Owner:** xiaolai
- **Scope:** Create `xiaolai/responsibility-laundering` on GitHub as a public repo. The `LICENSE` file in the tree handles license declaration; do not select GitHub's auto-license picker.
- **Done when:** Empty repo exists at the URL, ready to receive the initial push.
- **Blocking:** Required for push.

### Step 7 — Initial push

- **Owner:** xiaolai
- **Scope:** Push from local to the new remote. Decision before push: squash 195+ internal commits into a single "initial public release," or preserve history. Trade-off: preserving shows the discipline (visible audit trail of how the book was built); squashing gives a clean public-history start.
- **Done when:** Repo is live on GitHub with the agreed history.

## Post-push items (non-blocking)

- Create `CORRECTIONS.md` on first correction landing.
- GitHub issue templates: correction, evidence challenge, source dispute.
- `CONTRIBUTING.md` if needed.
- `CODE_OF_CONDUCT.md` if needed.

## Current state

| Step | Status |
|---|---|
| 1. Nancy public-release pass | **complete** (2026-05-31) — all 27 memos carry a public-release contract in frontmatter. Distribution: 18 `mechanical-pass-cleared` (no working-language formulations detected by initial scan); 8 `cleared` (Nancy substantive sign-off as-is — flagged language sat in legitimate analytical/process contexts); 1 `cleared-with-redaction` (`nancy-portfolio-sweep-2026-05-28.md` — Nancy rewrote color-coded risk ratings, the named-list-of-living-adversaries formulation, "MISMATCH"/"citable defamation surface" wording → narrative procedural-discipline notes; every finding, action, and recommendation preserved verbatim). Zero memos remain pending. |
| 2. Secret sweep | **complete** (2026-05-31) — 0 API keys, tokens, or credentials in tracked files; `.secrets.env` exists but is gitignored (real keys, never committed); `.secrets.env.template` tracked with blank values only. |
| 3. Reorganization | **complete** (a290db8, 2026-05-31) — `dev-docs/` restored from `archive/` rename; 215 references swept; tree shape matches README layout block. |
| 3b. Print PDFs built | **complete** — interior + cover in dist/ |
| 4. LICENSE file | **complete** (2026-05-31) — CC BY-NC 4.0 (prose) + MIT (apparatus) with directory mapping matching the README license table. |
| 5. KDP listing link | placeholder in README |
| 6. GitHub repo created | not started |
| 7. Initial push | held per 2026-05-30 decision |
