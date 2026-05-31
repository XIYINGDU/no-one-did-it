---
name: project-motif-registry-baseline
description: Stage 2 baseline build of book/registries/motif-registry.yml — 9 motifs identified across v2 corpus (2026-05-27). Records the per-motif rationale and the boundary chapters that govern forbidden_in lists.
metadata:
  type: project
---

Built `book/registries/motif-registry.yml` baseline by walking all 13 v2 chapters on 2026-05-27.

**Why:** The registry was empty (`motifs: []`); /motif-audit and /dependency-check rely on it. Without a baseline, no cross-chapter motif coordination is auditable.

**How to apply:**
- 9 motifs registered, frequency_floor ranging 3–8.
- The two most pervasive (`the-record` at 11 chapters, `the-court-or-inquiry` at 12 chapters) are nearly book-wide and have empty `forbidden_in:`.
- The boundary motifs are `the-altar` (ch-1 + ch-10 + ch-13 only; forbidden in every other chapter to preserve its framing-arc weight) and `the-chain` (forbidden in ch-1, where the ritualistic register precedes the diagnostic vocabulary).
- `signature-as-seam` is forbidden in ch-1 and ch-2 because the signature motif gets installed at ch-3 (eight-question diagnostic); appearing earlier would dilute its installation.
- `the-classified-or-sealed-file` is forbidden in ch-13 because the reader-instrument chapter must not introduce new classified-file material; it inherits via index only.

**Candidates demoted to ambient (NOT in registry):**
- "unmarked uniform" — appears only in ch-4. Single-chapter image; not a motif.
- "verb-subject" as a phrase — appears in ch-10 + ch-13 only. The grammatical observation it names is captured by [[the-named-cause]] motif.
- "fair clue" appears in 4 chapter prose files (ch-7, ch-10, ch-11, ch-12). At first I demoted ch-1, ch-3 because the literal phrase doesn't appear; but the device is fair-clue-shaped throughout. Kept the 4-chapter literal-phrase motif rather than over-claiming.
- "the seam" (without "signature") is too abstract to be a concrete image; folded into [[signature-as-seam]].

**Related to:** [[installing-chapter-rule]] (ch-1 installs ritual register; ch-2 installs taxonomy; ch-3 installs diagnostic — each motif's appearance list respects these installation boundaries).

**Open question:** Whether the chain motif should fork into a parent (`the-chain`) and child (`the-chain-climbs-or-stops`) — currently the single motif captures both stop/climb axes. Decide after the first /motif-audit run shows whether evolution Pass 4 reads cleanly.
