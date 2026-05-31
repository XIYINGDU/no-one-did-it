# Book Production Workflow

> The proof-of-shape that produced chapter 2 (case files → brief → draft → six gates → status:ready), generalized into a scalable workflow for the remaining twelve chapters. The orchestrator reads `book/STATUS.md` for state and dispatches per the workflow below.

## Roles in the workflow

| Role | Held by | What they decide |
|------|---------|------------------|
| **Orchestrator** | `xiaolai` (surrogate agent) when dispatched; the human Principal Author in fresh sessions | What stage runs next; which agent gets dispatched; when to surface to the principal |
| **Crew chief** | `jerry-crew-chief` | Cross-act sequencing; routing between leads; consolidating handoffs |
| **Cell leads** | Bonnie (architecture), Wayne (prose), Delon (research), Stephen (fact-check), Laura (red-team), Nancy (legal), Blair (market) | Their cell's gate; no cross-cell authority |
| **Researchers** | Shirley, Selina, Warren, Loki | Source packets + case files in their domains |
| **Expert reviewer** | Alan | Domain-aware verification across six frames |
| **Principal Author surrogate** | `xiaolai` agent | Judgment calls per the Six Values-Over-Rules |
| **Principal Author (human)** | xaiolai | Commits, pushes, scope expansions, strategic pivots, beat-10 sanity check |

## Per-chapter pipeline (10 stages)

Each chapter passes through these stages in order. Stages 3–8 are the gate sequence Bonnie's chapter-2 brief established. The pipeline is **resumable** — if a session ends mid-pipeline, the next session reads `STATUS.md` and resumes at the next incomplete stage.

### Stage 1 — Spine confirmation

**Owner:** Bonnie.
**Input:** `book/toc.yml` chapter entry; reader-state target; act_reversal claim.
**Output:** Confirmation that the chapter's role in the spine is unchanged, OR a flagged architectural drift. If drift, surface to the principal before proceeding.
**Skip condition:** Stage 1 was already confirmed when `toc.yml` was pinned (2026-05-25). Re-run only if architecture has visibly drifted since.

### Stage 2 — Case file research

**Owner:** Delon dispatches the relevant domain researchers (Shirley / Selina / Warren / Loki) per the chapter's case mix. Argumentative chapters (Part IV) skip this stage.
**Input:** The chapter's case shortlist (from spine + chapter brief if it exists, or from `dev-docs/02_RESEARCH_PACKAGES/.../04_Book_Integration/Book_Grade_Case_Shortlist.md` if not).
**Output:** Scapegoat case files in `book/evidence/case-files/<slug>.md` + counter-case files in `book/evidence/case-files/<slug>-counter.md`. Each carries `status: brief` until Stephen verifies.
**Constraints:**
- Counter-cases must match the pattern of their paired scapegoat case (per `.claude/skills/counter-case-method/SKILL.md`).
- Evidence grade A target for load-bearing claims; B acceptable for investigative-journalism material.
- All living-individual sentences must already hold procedural-stage discipline before handoff (Selina's wording-with-source-implication responsibility).
- Pure-scapegoat anchors for ch-5 / ch-7 / ch-11 / ch-13 must pass the downstream gate (Dreyfus-shaped, not Sacco-shaped; see `bonnie-book-architect/project_downstream_pure_scapegoat_gate`).

### Stage 3 — Verification gate (Stephen)

**Owner:** Stephen.
**Input:** Every case file from Stage 2.
**Output:** Per-file evidence-grade assignment + `[VERIFICATION GAP]` flags + `brief → draft` promotion for files that clear.
**Pattern note (from chapter-2 production):** watch for **gloss-attribution drift** — where two close-but-not-identical numbers, doctrinal categories, or source statements get glossed together. The gloss must be quoted-and-attributed, not asserted as the source's own language. See `jerry-crew-chief/feedback_research_gloss_attribution`.

### Stage 4 — Chapter brief

**Owner:** Bonnie.
**Input:** All case files at `status: draft` from Stage 3; the spine entry; the 10-beat rhythm; the reader-value template.
**Output:** `book/chapters-v2/<NN>-<slug>-brief.md` — the structural scaffold Wayne drafts from.
**Required brief sections:**
- Beat-by-beat structural map (which case feeds which slot)
- Beat-9-and-10 plan (counter-case anchor for beat 9; four reader-questions wording for beat 10)
- Defamation-risk inventory (every named-individual sentence pattern that needs Nancy gate)
- Hand-off block (what blocks chapter-draft promotion to status: ready)
- Open decisions for the principal (any judgment calls only the human can make)

### Stage 5 — Prose draft

**Owner:** Wayne.
**Input:** The brief + all case files + Bonnie's architecture decisions.
**Output:** `book/chapters-v2/<NN>-<slug>.md` at `status: draft`, 6,000–8,000 words, all 10 beat markers present as structural headers or label-lines (validator-required).
**Constraints:**
- All defamation discipline holds at the prose level (case-file wording is the floor)
- Vocabulary discipline (R51): canonical terms from `.claude/skills/vocabulary/registry.yaml`
- Procedural-stage language for living individuals
- Cost-of-escape enumeration preserved in slot 9
- Reader-state shift respects the chapter's target (do not overshoot the next-state)

### Stage 6 — Citation re-verification (Stephen, chapter-level)

**Owner:** Stephen.
**Input:** The chapter prose + the case-file source ledgers.
**Output:** Per-claim drift check (chapter ↔ case-file consistency); gate decision to proceed to Alan/Nancy/Laura layer.
**This is not a re-verification of the case files** — the case files are the contract from Stage 3. Stage 6 catches **prose drift** beyond the envelope the case files set.

### Stage 7 — Defamation pass (Nancy, chapter-level)

**Owner:** Nancy.
**Input:** Wayne's defamation-risk inventory from Stage 4 + the chapter prose.
**Output:** Per-sentence wording verdict; revisions required (verbatim text Wayne or Selina applies); 30-day re-pass clock recorded for any live-case content.
**Pattern note:** Wayne's prose can compress case-file wording under flow pressure. Nancy's chapter-stage pass is the catch.

### Stage 8 — Doctrinal frames (Alan, slot-specific)

**Owner:** Alan.
**Input:** The chapter prose + Bonnie's brief + the relevant case files.
**Output:** Per-frame verification + load-bearing revisions + cross-frame note where the chapter synthesizes multiple frames.
**Frames Alan may apply (per the chapter's content):** ancient ritual; responsibility theory; IHL; AI governance; complex systems failure; administrative / constitutional law.

### Stage 9 — Red-team (Laura)

**Owner:** Laura.
**Input:** The chapter prose, standalone (hostile-reader simulation).
**Output:** Overclaim audit; taxonomy install audit; standalone beat-10 read; cross-pattern adversarial passes; specific revisions with verbatim text.
**Specific honoring required:** if Nancy's pass said a paragraph's tonal tightness is **discipline survived, not craft failure**, Laura must not loosen the discipline under craft pressure.

### Stage 10 — Structural confirmation + principal sanity + promotion

**Owner sequence:** Bonnie → Principal (human) → Jerry.

- **Bonnie:** confirms the post-revision chapter still matches her brief's architecture decisions.
- **Principal:** beat-10 sanity check — reads the four reader-questions, the threshold rule (if any), the chapter's exit closer. Approves or requests revision.
- **Jerry:** promotes `status: draft → status: ready` and records the promotion in agent memory with any date-fired re-pass clocks (e.g., 30-day Nancy for live-case content).

## Wave structure

Chapters are produced in waves to respect the reading DAG, parallelize where possible, and concentrate review work.

### Wave 1 — Part I closeout (sequential)

Order: **ch-3 → ch-1**. Sequential because ch-3 unblocks the most (eight-question diagnostic for chapters 4–13); ch-1 last so its opening voice can tune to ch-2 and ch-3.

Per-chapter pipeline runs end-to-end; commit milestone after each chapter reaches `status: ready`.

### Wave 2 — Part II (parallel cell, sequential gates)

Chapters: **ch-4, ch-5, ch-6, ch-7**. These are siblings in the reading DAG (all consume Part I, none depend on each other).

Production approach:
1. **Case-file research in parallel** across all four chapters (Stage 2). Dispatch all relevant researchers in one batch. ch-5 already has Bhopal; needs three more.
2. **Stephen verification batch** (Stage 3) after all case files land. One Stephen pass per chapter, run in parallel.
3. **Chapter briefs in parallel** (Stage 4). One Bonnie dispatch per chapter; can run concurrently.
4. **Drafts in parallel** (Stage 5). One Wayne dispatch per chapter; can run concurrently.
5. **Per-chapter gate sequence** (Stages 6–10) runs sequentially within each chapter but four chapters' gates can interleave.
6. **Portfolio Nancy pass after the wave** — cumulative defamation surface across Part II.

### Wave 3 — Part III (sequenced reading order, parallel research)

Chapters: **ch-9 → ch-10 → ch-8** per Jerry's authorized reading order.

Case-file research runs in parallel (Stage 2) since the three chapters' research domains differ — ch-9 is public-law (Loki); ch-10 is AI / tech (Warren); ch-8 is war / statecraft (Selina).

Chapter briefs and drafts follow the reading order: ch-9 brief → ch-9 draft → ch-9 ready → ch-10 brief → ch-10 draft → ch-10 ready → ch-8 brief → ch-8 draft → ch-8 ready. The reading order matters because cross-references in each chapter assume the agreed sequence.

### Wave 4 — Part IV (sequential, argumentative)

Chapters: **ch-11 → ch-12 → ch-13**. Sequential because each consumes the previous.

No new case-file research — Part IV consumes earlier chapters' material. Stage 2 skipped; pipeline starts at Stage 4 (chapter brief).

### Wave 5 — Manuscript compile + proposal pack

- `/compile-book` produces the single-file manuscript.
- Blair builds the proposal pack (positioning, comp titles, sample-chapter strategy).
- Final Nancy portfolio sweep on cumulative defamation surface.
- Principal Author final read.

## Cross-cutting items

These do not belong to any one chapter's pipeline. They fire on dates, on commit triggers, or on cumulative state.

### Date-fired

- **30-day Nancy re-pass on live-case content** — fires 30 days after each chapter with live-case content reaches `status: ready`. Current open: ch-02 slot 8 (Ukrainian children), due 2026-06-24.

### Commit-triggered

- **NLPM R51 + score check** before any commit. The book project must hold 100/100 on the NLPM corpus with R51 active (per AGENTS.md). If a chapter or revision drops the score, fix before committing.

### Wave-end-triggered

- **Portfolio Nancy pass** after each wave. Nancy reviews the cumulative defamation surface across all chapters produced to date; catches cross-chapter consistency issues a per-chapter pass can miss.

### Background

- **Delon coordinates `[EVIDENCE NEEDED]` items** in parallel with chapter production. Items improve provenance but rarely block draft promotion. The list lives in each case file's "Open questions" section; STATUS.md tracks the headline open items.

## Orchestrator role

When invoked (via `/produce-chapter <slug>` or `/book-status`), the orchestrator:

1. **Reads `book/STATUS.md`** to identify current state.
2. **Identifies the next stage** for the named chapter (per the per-chapter pipeline above) OR the next chapter to start (per the wave structure).
3. **Dispatches the appropriate agent** with a focused prompt referencing this workflow and the chapter's accumulated artifacts.
4. **Updates `STATUS.md`** after each stage completes.
5. **Surfaces to the principal** when:
   - A stage produces a finding only the principal can resolve
   - The beat-10 sanity check is reached
   - Cumulative defamation surface looks concerning
   - A scope expansion would be required to proceed
   - The principal's preferences (style, taste, working title) are implicated

## What this workflow does NOT do

- It does not commit or push. Commits are principal-author decisions.
- It does not skip gates under pressure. Every chapter passes Stages 3–10 in order.
- It does not auto-resolve dated re-passes. The principal fires the re-pass when the date arrives.
- It does not modify the spine. Architecture drift surfaces to the principal; the principal calls toc.yml changes.
- It does not finish argumentative chapters (Part IV) without principal involvement. Argumentative chapters carry more of the principal's voice; their drafts get heavier principal-author input.

## Resumability

Every artifact this workflow produces is on disk. Every state transition is recorded in `STATUS.md`. Every gate decision is recorded in the deciding agent's memory directory under `.claude/agent-memory/`. A fresh session opens, reads `STATUS.md`, and picks up at the next incomplete stage.

The workflow is **session-agnostic**. If chapter 4's draft completes in session N, chapter 4's Stephen gate can run in session N+1.
