# Book Production Status

> Status board for *No One Did It: Responsibility Laundering, from the Scapegoat to the Algorithm*. The orchestrator (xiaolai-surrogate when dispatched; the human principal when fresh sessions open) reads this file to pick up state; updates it after each stage completes. See `.claude/docs/book-production-workflow.md` for the full workflow.

**Last updated:** 2026-05-30 (Chekhov-discipline verification pass complete against v6 canonical; ch-13 final sentence improved; ch-1 `responsibility-chain` lexical install added; callback-graph.yml swept to v6 section headings. See `process/audits/chekhov-verification-2026-05-30.md`.)

**Recent updates (2026-05-30):**
- **v6 cut as canonical text.** `book/chapters-v6/` is the source of truth. Spine-driven build: `book/spine-v6.yml` → `pipelines/epub/assemble_v6_manuscript.py` → `dist/manuscript-v6.md` → `pipelines/epub/build_kdp_epub.py` → `dist/no-one-did-it.epub`. Validates clean (epubcheck 0/0/0, Kindle Previewer Success).
- **Reader cold-read closed.** All six HARD findings resolved (footnote-slug rename, preface superlative, Trump named, ch-2 reorientation, ch-6 navigator, ch-11 navigator).
- **Sprawl cleanup.** `book/chapters-v1..v5/` + 3 v3 sidecar yml + 5 dead manuscripts archived to `dev-docs/04_ARCHIVE_SUPERSEDED_OR_REFERENCE/`. Retired six scripts (incl. `build_v3.py`, `format_citations_chicago.py`, `assemble_v4/v5_manuscript.py`) and two `.claude/hooks/` (rule-09 v2 lifecycle, no longer applies). Live enforcement repointed to v6.
- **Chekhov-discipline verification pass (pre-compile).** Five parallel verification streams against v6 canonical (callback / motif / cognitive-arc / opening↔closing / per-chapter fair clues) returned zero HARD findings. Three surgical fixes applied: ch-13 final sentence sharpened ("We put names back."); ch-1 `responsibility-chain` lexical install added; callback-graph.yml swept to v6 section headings. Report at `process/audits/chekhov-verification-2026-05-30.md`.
- **Nancy portfolio sweep, Blair proposal pack, Stephen Vol-1 anchor lock — all CLEAR / complete.** ch-7 Vol 1 anchors locked at ¶1.7 / ¶3.11 / ¶3.12 / ¶3.24; prose re-aligned to "approximately 1,000 prosecuted and convicted" (Vol 1 figure) with 236-imprisoned correctly attributed to contemporaneous reporting. Blair pack: 8 files in `book/proposals/` lead with Puopolo at Doubleday.

**Prior baselines (2026-05-27/28):** Rule 14 (authorial stance) ratified and swept. Chicago Manual of Style 17th ed. Notes-Bibliography system ratified as rule 13; full corpus migration to slug-only inline `[CITE:]` markers. Cross-chapter registries populated and baseline-audited (callback / motif / cognitive-arc). URL verification pass across all 283 source-ledger cards. v3 publication-form generated (subsequently archived under sprawl cleanup; v6 is current canonical).

## Spine reference

`book/toc.yml` — 4 parts, 13 chapters. Reading order per the DAG:

- Forced: 1 → 2 → 3, then 11 → 12 → 13
- Loose parallel: Part II chapters {4, 5, 6, 7}; Part III chapters {8, 9, 10}
- Part III authorized reading order: **9 → 10 → 8** (Jerry authorization, `project_part3_sequencing_decision`)

## Chapter status

Legend: `—` not started · `▸` in progress · `✓` cleared · `★` at `status: ready`

| # | Slug | Cases | Brief | Draft | Stephen | Nancy | Alan | Laura | Bonnie | Principal | Jerry | State |
|---|------|------:|:-----:|:-----:|:-------:|:-----:|:----:|:-----:|:------:|:---------:|:---:|------|
| 1 | `01-the-altar-moves` | 2/2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 2 | `02-the-four-goats` | 9/9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **★ ready** |
| 3 | `03-who-could-have-stopped-it` | 2/2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 4 | `04-the-proxy-and-the-sponsor` | 3/3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 5 | `05-the-guilty-goat` | 2/2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 6 | `06-the-pretext` | 3/3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 7 | `07-the-record-is-the-battlefield` | 1/1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 8 | `08-war-is-the-perfect-laundry` | 4/4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 9 | `09-when-power-calls-itself-the-goat` | 4/4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 10 | `10-the-model-did-it` | 4/4 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 11 | `11-make-responsibility-follow-control` | n/a | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 12 | `12-keep-the-record` | n/a | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |
| 13 | `13-a-readers-field-guide` | n/a | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (surrogate) | ✓ | **★ ready** |

**Case-file counts are targets, not contracts.** Chapter briefs may resize them up or down as architecture dictates. `n/a` for Part IV chapters means they are argumentative chapters (no scapegoat anchors); they consume earlier chapters' material rather than producing new case files.

## Recommended production order (historical — chapters now produced)

The wave plan that drove production is retained below as historical record. All four waves are complete; chapters are at `status: ready` under v6 canonical. Manuscript compile, Blair pack, and Nancy portfolio sweep are also complete. Current focus is xiaolai's final read.

1. **Wave 1 — Part I closeout (sequential):** ch-3 → ch-1. ✓ complete.
2. **Wave 2 — Part II (parallel):** ch-4, ch-5, ch-6, ch-7. ✓ complete.
3. **Wave 3 — Part III (sequenced 9 → 10 → 8):** ✓ complete.
4. **Wave 4 — Part IV (sequential):** ch-11 → ch-12 → ch-13. ✓ complete.
5. **Manuscript compile + final passes.** ✓ EPUB ships; xiaolai read pending.
6. **Blair proposal pack.** ✓ complete.

## Cross-cutting items

| Trigger | Action | Owner | Status |
|---------|--------|-------|--------|
| 2026-06-24 (date-fired) | Nancy 30-day re-pass on slot 8 (Ukrainian children) for ch-02 | Nancy | scheduled |
| 2026-05-28 | Final portfolio-level Nancy sweep on cumulative defamation surface across 13 chapters | Jerry → Nancy | **complete** — CONDITIONAL 5 items; see `process/review-memos/nancy-portfolio-sweep-2026-05-28.md` |
| 2026-05-28 | Blair proposal pack (pitch / title / overview / audience / comps / chapter summaries / sample strategy) | Jerry → Blair | **complete** — 8 files in `book/proposals/`. Per 2026-05-30 decision (direct KDP publish; no agent route), `pitch-letter.md` and `editor-pitch.md` retire from deliverable status to source pool for KDP product description / A+ content; the remaining files (overview / audience / comps / chapter summaries / title-subtitle / sample strategy) remain useful regardless of path. |
| 2026-05-28 | Brief open-questions triage across all 13 briefs + 4-of-5 STILL OPEN items closed via xiaolai-value judgment | Jerry → Bonnie | **complete** — rollup at `process/audits/brief-open-questions-triage-2026-05-28-rollup.md`; followups in commit 595f585 |
| 2026-05-28 | Beat-10 template red-team audit across 13 chapters (Laura, in place of xaiolai sign-off on ch-2 #2) | Jerry → Laura | **complete** — CONDITIONAL CLEAR; 13/13 on V4/V5/V6, 12/13 on V9 with one fix applied; cascade-revise not warranted; memo at `process/review-memos/laura-beat-10-template-audit-2026-05-28.md` |
| 2026-05-28 | Prose-trailing Open-questions triage across all 13 chapter prose files (Stephen) | Jerry → Stephen | **complete** — 72 items: 6 resolved, 40 tracked in pending-stephen-lock or coordinated sweep, 14 deferred, 4 stale, **6 added to galley-pass scope** (ch-11(a)(b)(c) doctrine/case selection, ch-12(4)(6)(8) Pentagon Papers dates + FRCP 37(e) text + Hofeller Wake County docket entries); memo at `process/audits/prose-open-questions-triage-2026-05-28.md` |
| 2026-06-25 (galley pass) | **Stephen galley-pass scope extended:** 37 pending-stephen-lock markers + the 6 prose-OQ STILL OPEN items above + STATUS.md standing-queue items (Therac-25 FDA primary; LoC Sandoz Commentary; Fraser J "not remotely robust"; per-soldier Abu Ghraib; NYT/MS/OpenAI preservation; speaker-by-speaker "hostages"/"activist judges" attribution) | Stephen | scheduled |
| 2026-05-28 | URL verification pass across all 283 source-ledger cards — every primary + Wayback URL HTTP-checked; per-card `verification.url_check` metadata written; Chicago formatter extended to emit `(verified YYYY-MM-DD)` / demoted-to-archive / both-broken / checkpoint-dependent annotations in endnotes | Jerry → `scripts/verify_card_urls.py` | **complete** — report at `process/audits/url-verification-2026-05-28.md` |
| 2026-05-28 | Link-fix pass under global proxy: browser-UA verify catches 30 newly-reachable primaries; `forbidden` status added for anti-bot 403s; Wayback Save-Page-Now + Availability-API fallback captures the 3 cards that lacked archives; 2 broken-both items resolved (DOJ Boeing via fresh Wayback; J6 Reuters paywall substituted with NPR coverage + Wayback) | Jerry → `scripts/verify_card_urls.py` + `scripts/wayback_capture.py` | **complete** — final state: 0 broken-both; 6 cards primary-broken-archive-OK (handled by formatter promotion); 1 pending-other-checkpoint (abu-ghraib justice.gov; archive promoted); 31 forbidden (Cloudflare anti-bot; archive promoted) |
| Galley-lock minus 30 days + galley-lock | Re-run `scripts/verify_card_urls.py` + `scripts/wayback_capture.py --all` to refresh verification timestamps and capture any newly-broken URLs | Stephen | scheduled |
| 2026-05-28 | **v3 publication-form generated** — `scripts/build_v3.py` strips authoring residue (trailing `Owner:/Task:/Open questions:/Handoff:` schema blocks; `## Annotations and handoff` / `## Findings for xaiolai` H2 sections; inline `Open questions` / `Handoff:` paragraphs) from each v2 chapter; converts inline `[CITE: slug]` markers to sequential book-wide `[^N]` markdown footnote refs (1..423); generates `book/back-matter/references.md` (per-chapter sections with full Chicago NB citations + URL verification annotations) and `book/back-matter/bibliography.md` (deduplicated Selected Bibliography). Authoring metadata preserved in per-chapter `*.meta.yml` sidecars. | Jerry → `scripts/build_v3.py` | **complete** — 13 v3 chapter files in `book/chapters-v3/`; 423 references; 279 bibliography entries; manuscript at `dist/manuscript-v3.md` (3632 lines, ~123K words). v2 retained as authoring source (Stephen/Nancy galley edits land in v2, v3 regenerates from re-running build_v3.py). |
| Before each commit | NLPM R51 + score check (project corpus discipline) | Jerry → nlpm:score | ongoing |
| Per chapter | FDA primary for Therac-25 Class I designation (provenance) | Delon | open from ch-02 |
| Per chapter | LoC Sandoz Commentary §§ 3213–3247 and 3530–3563 paragraph anchors | Stephen | open from ch-02 |
| Per chapter | Fraser J "not remotely robust" paragraph anchor (BAILII institutional access) | Stephen | open from ch-02 |
| ch-5 / ch-7 / ch-11 / ch-13 | Downstream pure-scapegoat anchor gate (use Dreyfus-shaped, not Sacco-shaped) | Bonnie | gate active |
| 2026-06-25 (date-fired) | Nancy 30-day re-pass on ch-8 (Iraq WMD), ch-9 (live political content), ch-10 (live AI litigation), ch-12 (FRA / DOGE / live records litigation) | Nancy | scheduled |
| Galley-lock minus 30 days | **Coordinated Nancy+Stephen sweep** covering 5 live-docket clocks (ch-04 Putin/Prince/Trump pardons; ch-07 Vennells/Jenkins/Inquiry final report; ch-09 AEA/DOGE/J6 MSPB; ch-10 Bartz/Altman/ChatGPT preservation; ch-12 preservation-order callback) — single coordinated checkpoint to prevent stale-formulation drift, per Nancy portfolio sweep 2026-05-28 Recommended Action 3 | Jerry → Nancy + Stephen | scheduled (date-fires when manuscript freeze is declared) |
| Future (if UK edition contemplated) | UK-libel pre-flight by UK counsel — named-individual concentration (Pattern B) is higher UK-libel surface than US-defamation per Nancy portfolio sweep 2026-05-28 Recommended Action 10 | Jerry → external UK counsel | tracked |
| Per chapter | Per-soldier disposition table for Abu Ghraib (Ambuhl/Cruz/Sivits/Davis distinctions) | Stephen | open from ch-08 |
| Per chapter | Lock exact text of *NYT v. Microsoft / OpenAI* preservation order(s) | Stephen | open from ch-10 |
| Per chapter | Speaker-by-speaker dated attribution for "hostages" and "activist judges" framings | Stephen | open from ch-09 |

## Source-ledger coverage

| Chapter | Sidecar | Cards backing | Notes |
|---|---|---|---|
| 01 | ✓ | 20 cards | OED 1824 B-grade; Generalbundesanwalt 2008 A; Reichstag historiography mix |
| 02 | ✓ | 39 unique cards (65 anchor entries) | Sacco/Vanzetti + Abu Ghraib + Therac-25 + Boeing 737 + Bhopal + Ukrainian children |
| 03 | ✓ | 24 cards | VW Dieselgate + Ford Pinto + AGENTS.md diagnostic |
| 04 | ✓ | per Wave D | MH17 + Crimea + Blackwater (heavy reuse from ch-08) |
| 05 | ✓ | 12 new + 9 reused | Bhopal + Boeing 737 (Forkner/O'Connor/NPA) |
| 06 | ✓ | 24 new + 2 reused | Overton Park + State Farm + family separation + census citizenship + Ukraine aid hold |
| 07 | ✓ | 5 new + 1 reused | Hamilton & Ors + Bates v Post Office + Inquiry Volume 1 + Clarke advice |
| 08 | ✓ | 36 new + 5 reused | Iraq WMD + 4 callback layers; heaviest chapter |
| 09 | ✓ | per Wave B | AEA + J6 + DOGE + Watergate/Iran-Contra echoes |
| 10 | ✓ | 8 unique (10 anchor entries) | LMArena + Bartz + Altman + Al-Dahle + AGENTS.md + Wang preservation order |
| 11 | ✓ | 10 new + 1 reused | Park + DeCoster + SOX + SMCR + Inquiries Act §21 + EO 13328 |
| 12 | ✓ | 14 cards | NYT v. US + Walsh + Tower + FRA + FRE 901 + FRCP 37(e) + Inquiries Act §21 reused |
| 13 | n/a | zero by design | Field guide indexes prior chapters; no new citations |

Total: 283 cards, 12 sidecars. Validator `python3 scripts/validate_source_ledger.py` returns PASS with zero HARD failures and zero WARN findings. Wired into pytest at `tests/test_source_ledger.py`.

## Outstanding evidence-needed items

**v6 chapter prose is marker-clean.** Verified 2026-05-30: zero `[EVIDENCE NEEDED]` and zero `pending-stephen-lock` markers in `book/chapters-v6/`. All resolved or substituted during the v3 → v6 transition.

Markers persist in three lower layers, scheduled for the 2026-06-25 Stephen galley pass:

| Layer | Markers | Status / scope |
|---|---|---|
| `book/evidence/source-ledger/cards/` (12 cards) | ~15 `[EVIDENCE NEEDED]` | Provenance refinements (verbatim quote sourcing, primary-document pin cites, paragraph anchors). Cards back already-cited claims; the prose itself reads with the current text. |
| `book/evidence/source-ledger/sidecars/` (3 sidecars: ch-05, ch-06, ch-08, ch-09) | ~6 `[EVIDENCE NEEDED]` + 7 `pending-stephen-lock` | Per-anchor sidecar entries awaiting Stephen lock. Includes the ch-9 DOJ Capitol-breach dashboard-removal card (2 markers) and the ch-8/09 sidecar entries for live-content claims. |
| `book/evidence/case-files/` (21 case-files, ~129 markers) | Background research depth | Mostly non-load-bearing for prose. Includes deep-bibliographic items (Sahu SDNY PACER, UCC 1985 India revenue, FCA Final Notice selection, *Ms. L.* Steering Committee tally, FTCA/Bivens posture). Delon coordinates as background; not on the critical path to galley. |

The 28 source-ledger markers (cards + sidecars combined) are the Stephen-anchor work for galley lock; the 129 case-file markers are research-depth refinements that do not block ship.

Resolution log (2026-05-26 web-retrievable pass; subsequently lifted into v6 prose):

| Chapter | Item | Outcome |
|---|---|---|
| ch-01 | OED first dated figurative use of "scapegoat" | LIFTED — 1824 date + verbatim quote substituted; B-grade |
| ch-01 | Generalbundesanwalt Jan 2008 annulment German text | LIFTED — A-grade; verbatim German + Aktenzeichen 2 AR 187/07 + author's translation substituted |
| ch-06 | Hofeller 2015 study verbatim phrasing | LIFTED — B+ grade; two-clause quote substituted |
| ch-06 | Roberts pin cite *Dept of Commerce v NY* | LIFTED — B-grade; parallel cite 139 S. Ct. 2551, 2575–2576 substituted |
| ch-07 | Horizon Inquiry plea-rate figure | LIFTED — B-grade; documented aggregates (900+ prosecuted; 236 imprisoned attributed correctly to contemporaneous reporting per 2026-05-30 Vol-1 lock) |
| ch-10 | LMArena policy revision wording + date | LIFTED — A-grade; verbatim 7 April 2025 statement substituted |
| ch-10 | *Bartz* settlement final-approval status | LIFTED — A-grade; 14 May 2026 fairness hearing substituted |

## Exit condition

The book is "done" when:

- ✓ All 13 chapters at `status: ready` (achieved 2026-05-30 under v6 cut)
- ✓ Blair proposal pack complete (8 files in `book/proposals/`; per 2026-05-30 direct-KDP-publish decision, `pitch-letter.md` and `editor-pitch.md` retire to source-pool role)
- ✓ About-the-author page (`book/back-matter/about-the-author.md`) — `status: ready` (transferred from *The Half Second* per author convention)
- ✓ Final Nancy portfolio sweep complete (CLEAR per 2026-05-30 cold-read closure)
- ✓ ch-13 closing sentence authored (resolved 2026-05-30 — see `process/audits/chekhov-verification-2026-05-30.md`)
- ✓ Cross-chapter registries audited clean (2026-05-30: callback 22/22 PASS structurally; motif 9/9 fully clean incl. `the-altar` forbidden-zone discipline; cognitive arc 49/50 PASS; one concept lexical install applied)
- ✓ Manuscript compiles (v6 manuscript at `dist/manuscript-v6.md`; KDP EPUB at `dist/no-one-did-it.epub` validates epubcheck 0/0/0 + Kindle Previewer Success). `/compile-book` workshop skill not yet run formally; the spine-driven `pipelines/epub/assemble_v6_manuscript.py` + `pipelines/epub/build_kdp_epub.py` pipeline is the working substitute.
- **Open** — Principal Author (xiaolai, the human) final read complete. The xiaolai-surrogate cleared structural sign-off; the human read is the remaining exit-condition item.
- **Open** — Stephen galley-pass on source-ledger markers (28 total: ~21 `[EVIDENCE NEEDED]` + 7 `pending-stephen-lock` across 12 cards + 3 sidecars). Scheduled 2026-06-25.
- **Open** — 30-day re-pass discipline on live-case content (date-fired clocks: 2026-06-24 for ch-2 slot 8; 2026-06-25 for ch-8/9/10/12).

## How to use this file

- **Reading state:** glance at the chapter table; the rightmost "State" column is the punch-list view
- **Resuming work:** run `/book-status` to see what's next; run `/produce-chapter <slug>` to advance one chapter
- **Updating state:** after each gate clears, mark the cell in the chapter table; update "Last updated" timestamp; re-commit
- **Adding cross-cutting items:** append to the table; do not silently fold into chapter rows

The orchestrator updates this file in place. Conflicts surface to the principal author; do not auto-resolve.

## 2026-05-30 — v6 canonical + sprawl cleanup

| Date | What changed | Owner | Result |
|---|---|---|---|
| 2026-05-30 | **v6 cut as canonical text** — `book/chapters-v6/` is the source of truth. Spine-driven build (`book/spine-v6.yml` → `pipelines/epub/assemble_v6_manuscript.py` → `dist/manuscript-v6.md` → `pipelines/epub/build_kdp_epub.py` → `dist/no-one-did-it.epub`). Front matter (copyright, dedication placeholder, book epigraph by Arendt, preface, A Note on Cases) + 12 figures embedded as reflowable tables + 4 part dividers. Validates clean: epubcheck 0/0/0, Kindle Previewer Success, 89 tests pass. | Jerry → spine + assembler + build | **complete** — shippable to KDP. |
| 2026-05-30 | **Reader cold-read closed.** All six HARD findings resolved (footnote-slug rename, preface superlative, Trump named, ch-2 reorientation, ch-6 navigator, ch-11 navigator). Nancy portfolio sweep: CLEAR. Stephen Vol 1 anchors locked at ¶1.7 / ¶3.11 / ¶3.12 / ¶3.24 — chapter prose re-aligned to "approximately 1,000 prosecuted and convicted" (Vol 1 figure) with 236 imprisoned now correctly attributed to contemporaneous reporting, not Vol 1. Blair proposal pack complete (8 files, lead with Puopolo at Doubleday). | crew | **complete** |
| 2026-05-30 | **Sprawl cleanup.** `book/chapters-v1..v5/` + 3 v3 sidecar yml + 5 dead manuscripts (`no-one-did-it-v3/v4/v5/.chicago/.md`) archived to `dev-docs/04_ARCHIVE_SUPERSEDED_OR_REFERENCE/`. Retired: `scripts/{build_v3, validate_v3_refs, assemble_v4_manuscript, assemble_v5_manuscript, format_citations_chicago, operating_validators}.py`; `.claude/hooks/{pre-edit-chapter-snapshot, post-edit-status-check}.py` (rule-09 v2 lifecycle, no longer applies); `tests/{test_validate_v3_refs, test_format_citations_chicago, test_validate_operating_validators, test_hook_warn_mode}.py`. Live enforcement repointed to v6: 4 scan-* hooks, `check-agent-frontmatter`, `check_reader_reports`, `validate_source_ledger` all gate on `chapters-v6`. settings.json drops the 2 retired hook entries. | sprawl cleanup pass | **complete** — clean working tree; tests green; v6 EPUB ships. |
| 2026-05-30 | **Chekhov-discipline verification pass (pre-compile).** Five parallel verification streams against v6 canonical: callback graph (22/22 edges PASS structurally), motif registry (9/9 clean — including `the-altar` forbidden-zone discipline), cognitive arc (49/50 items PASS), ch-1↔ch-13 opening↔closing edge (PASS — reweighted return fires cleanly via scene/thesis/hammer-line callbacks), per-chapter fair clues (11/13 CLEAN, 0 gotcha, 0 orphans). Three fixes applied: (a) ch-13 final sentence improved from "Now we know where to look. And now we can say who." to "We put names back." — sharper action verb, drops parallel competence-restatement; (b) ch-1 `responsibility-chain` lexical gap closed with one inserted sentence at L157 ("Between those two sets of names runs the responsibility chain."); (c) callback-graph.yml swept — all 22 edges' `section:` fields reconciled to v6's actual H2 headings (replacing pre-v6 conventional A2B beat names), 2 paraphrase drifts updated (edges 12, 13), 1 line_anchor "slot 5" tail removed (edge 20); revision_history entries added for the 3 substantive changes. | jerry-crew-chief → 5 parallel verifiers + 3 sequential fixes | **complete** — report at `process/audits/chekhov-verification-2026-05-30.md`; manuscript compile unblocked. |
| 2026-05-30 | **Print PDF pipeline (KDP paperback) ported from The Half Second.** Six phases end-to-end: (0) `pipelines/print/` scaffold + 17 fonts (EB Garamond + JetBrains Mono) + `.venv` with pypdf/reportlab/Pillow/PyYAML + Playwright Chromium; (1) `build-prose.mjs` adapted for RL paths (book/chapters-v6/, book/front-matter/, book/back-matter/) — 26 HTML pages produced; (2) `build-print-pdf.mjs` adapted to read `book/spine-v6.yml`, add part-divider sections (Half Second has no parts), typographic chapter starts (jpg chapter covers skipped), Card-index removed — 31 sections rendered via Playwright per-section route, qpdf concat; (3) `print-pdf-finalize.py` adapted for RL spine kinds (title/front/toc/part = unnumbered, chapter/back = numbered + running header), page-number + outline overlay via pypdf+reportlab; (4) `build-print-cover.py` adapted for RL covers (book/design/epub/cover.jpg + back-cover.jpg, 1.115″ spine for 446pp cream); (5) `pipeline.mjs` orchestrator; (6) end-to-end run — **446 pages interior (20MB, 6×9 trim, all fonts embedded incl. EB Garamond Type 3 subsets + GeorgiaItalic overlay), 13.365×9.25 full-wrap cover (1.4MB, 300 DPI, bleed) ready for KDP upload**. | jerry-crew-chief → 6 sequential phases | **complete** — outputs in `dist/no-one-did-it-{interior,cover}.pdf`; pipeline at `pipelines/print/`; README at `pipelines/print/README.md`. |
