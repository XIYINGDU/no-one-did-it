---
artifact_id: in-quote-emphasis-pass-2026-05-30
title: "In-quote emphasis pass — rule 06 annotation worksheet for Stephen"
owner: stephen-fact-check-director
status: open
upstream_audit: scripts/audit_emphasis.py (judgment-based classifier)
audit_seed: 2026-05-30
related: process/audits/emphasis-pass-2026-05-30.md
---

# In-quote emphasis pass — for Stephen (rule 06)

Each entry below is an `<em>` or `<strong>` mark sitting inside a `>`
block-quote. Per rule 06 (quote integrity), every emphasis inside a
cited quote needs an explicit annotation:

- **(emphasis added)** — we added the emphasis for readability
- **(emphasis in original)** — the source's own typography

For each instance Stephen verifies against the source-ledger card, then
either adds the annotation to the chapter prose or confirms an existing
annotation already covers it.

## How to use this worksheet

1. Work through each chapter section below.
2. For each instance, open the chapter file at the noted file line and
   inspect the surrounding `> ` block-quote.
3. Identify the source-ledger card via the `[CITE: <slug>]` marker
   inside or immediately after the block-quote.
4. Open the card. Check whether the original document carried the
   emphasis at the same point.
5. Mark the verdict in the per-instance row (KEEP-ORIGINAL,
   ADD-ANNOTATION-ORIGINAL, ADD-ANNOTATION-ADDED, REMOVE-EMPHASIS, or
   ALREADY-ANNOTATED if a covering `(emphasis …)` is in scope).
6. Apply the prose edit if any; commit per chapter.

## Aggregate

| Chapter | Instances | Notable shape |
|---|---:|---|
| ch-01 | 1 | Chapter epigraph only |
| ch-02 | 2 | Chapter epigraph + 1 quoted passage |
| ch-03 | 10 | Epigraph + 8-mark quoted list + 1 |
| ch-04 | 8 | Epigraph + 2 quoted lists (3 each) + 1 |
| ch-05 | 3 | Epigraph + 1 |
| ch-06 | 10 | Epigraph + 1 dense quoted passage (~9 marks) |
| ch-07 | 4 | Epigraph + 2 |
| ch-08 | 2 | Epigraph + 1 |
| ch-09 | 2 | Epigraph + 1 |
| ch-10 | 2 | Epigraph + 1 |
| ch-11 | 2 | Epigraph + 1 |
| ch-12 | 1 | One quoted instance (no epigraph emphasis) |
| ch-13 | 68 | Quoted field-guide examples (separate pass) |
| **Total** | **115** | |

## Per-chapter worksheet

### ch-01 — The Altar Moves

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter-opening epigraph |

### ch-02 — The Four Goats

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Plato, *Phaedrus* (epigraph) |
| 17 | 25 | em | | | Mid-chapter quote |

### ch-03 — Who Could Have Stopped It?

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 41 | 49 | strong | | | 8-mark quoted block — likely numbered list with bolded openers, file L49-56 contiguous |
| 42 | 50 | strong | | | (same block) |
| 43 | 51 | strong | | | (same block) |
| 44 | 52 | strong | | | (same block) |
| 45 | 53 | strong | | | (same block) |
| 46 | 54 | strong | | | (same block) |
| 47 | 55 | strong | | | (same block) |
| 48 | 56 | strong | | | (same block) |
| 80 | 88 | em | | | Single italic in mid-chapter quote |

### ch-04 — The Proxy and the Sponsor

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 135 | 143 | strong | | | 3-mark quoted block, file L143-145 contiguous |
| 136 | 144 | strong | | | (same block) |
| 137 | 145 | strong | | | (same block) |
| 153 | 161 | em | | | Single italic in mid-chapter quote |
| 183 | 191 | strong | | | 3-mark quoted block, file L191-193 contiguous |
| 184 | 192 | strong | | | (same block) |
| 185 | 193 | strong | | | (same block) |

### ch-05 — The Guilty Goat

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 6 | 14 | em | (epigraph) | | Chapter epigraph (×2 marks on same line) |
| 6 | 14 | em | (epigraph) | | (same line) |
| 106 | 114 | em | | | Single italic in mid-chapter quote |

### ch-06 — The Pretext

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 51 | 59 | strong | | | Dense quoted passage — 1 strong + 2 em on L59 |
| 51 | 59 | em | | | (same line) |
| 51 | 59 | em | | | (same line) |
| 53 | 61 | strong | | | (continuation of quoted block) |
| 55 | 63 | strong | | | (same) |
| 57 | 65 | strong | | | (same) |
| 59 | 67 | strong | | | (same) |
| 61 | 69 | strong | | | (same) |
| 189 | 197 | em | | | Single italic in late-chapter quote |

### ch-07 — The Record Is the Battlefield

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 3 | 11 | em | (epigraph) | | Epigraph (×2 on same line) |
| 3 | 11 | em | (epigraph) | | (same line) |
| 5 | 13 | em | (epigraph) | | (epigraph continued or attribution) |
| 41 | 49 | em | | | Mid-chapter quoted italic |

### ch-08 — When Power Calls Itself the Goat

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 135 | 143 | em | | | Single italic in late-chapter quote |

### ch-09 — The Model Did It

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 135 | 143 | em | | | Single italic in mid-chapter quote |

### ch-10 — War Is the Perfect Laundry

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 121 | 129 | em | | | Single italic in mid-chapter quote |

### ch-11 — Make Responsibility Follow Control

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 5 | 13 | em | (epigraph) | | Chapter epigraph |
| 57 | 65 | em | | | Mid-chapter quoted italic |

### ch-12 — Keep the Record

| Audit L | File L | Kind | Source-ledger slug | Verdict | Notes |
|---:|---:|---|---|---|---|
| 150 | 157 | em | | | Single italic in late-chapter quote (no epigraph emphasis) |

### ch-13 — A Reader's Field Guide (separate sub-pass)

Ch-13 carries 68 in-quote emphasis marks across the field-guide
quoted examples. The chapter quotes verbatim passages from the
book's prior chapters and from external sources as worked examples
of the diagnostic in action. Per the upstream worksheet
(`emphasis-pass-2026-05-30.md`, Pattern I), ch-13's in-quote pass
runs as its own session — the field-guide format means most marks
are quoting marks already in the source, and the annotation pass
should follow the chapter's two-section structure (own-prose
recall-examples vs external-source examples).

Inventory placeholder (audit lines from `audit_emphasis.py --chapter 13 --verbose`):
L 5 (epigraph), L 60, L 62, L 64, L 66, L 78, L 80, L 82, L 90, L 92,
L 94, L 96, L 98, L 108, L 110, L 112, L 114, L 116, L 118, L 122 (×4),
L 124, L 126 (×2), L 128, L 130 (×2), L 132, L 134, and the remainder
covering ~38 strong + ~30 em marks. Stephen runs this sub-pass against
the field-guide's two source modes.

## Bulk patterns to apply once

Stephen may find that many epigraphs need the same annotation
(`(emphasis in original)`) once verified against the source. If the
source's typography carries the italics — common for ancient Greek
terms in Plato, biblical Hebrew in Leviticus, classical legal Latin —
the annotation goes on the chapter's epigraph attribution line
("— Plato, *Phaedrus* 265e, trans. Benjamin Jowett (emphasis in
original)").

Equally, the dense quoted blocks (ch-03 L49-56, ch-04 L143-145 and
L191-193, ch-06 L59-69) are likely numbered or bulleted lists from a
single source where bolding is the source's own list-marker. One
verification per source covers all marks in the block.

## Sequencing

1. Verify epigraph emphases (13 chapters; mostly one verdict per chapter
   covers the chapter epigraph) — fastest tier.
2. Verify dense quoted-block emphases by source (ch-03 L49-56,
   ch-04 L143-145 + L191-193, ch-06 L59-69) — one source per block;
   ~3 verifications cover ~17 marks.
3. Verify single isolated em/strong marks (ch-02 L25, ch-03 L88,
   ch-04 L161, ch-05 L114, ch-06 L197, ch-07 L49, ch-08 L143,
   ch-09 L143, ch-10 L129, ch-11 L65, ch-12 L157) — one verification
   per mark; ~11 verifications.
4. ch-13 sub-pass — separate session per Pattern I.

Total Stephen effort outside ch-13: roughly 13 epigraph + 3 block + 11
isolated = **27 source verifications** to resolve ~47 marks.

---

Owner: stephen-fact-check-director
Auditor source: `scripts/audit_emphasis.py --verbose | grep IN_QUOTE`
Upstream worksheet: `process/audits/emphasis-pass-2026-05-30.md`
(Pattern H)
Rule reference: `.claude/rules/06-quote-integrity.md`
