# Fiction-craft rewrite — implementation plan

> **Status:** SUPERSEDED 2026-05-27 by [`book/plans/fiction-craft-rewrite-workflow.md`](../book/plans/fiction-craft-rewrite-workflow.md). Original plan retained here as design history (Codex review verdict: MAJOR GAPS — the workflow document addresses every Codex finding via the new toolkit). This file is read-only design context; do not edit further.
>
> **Original status:** implementation plan, drafted 2026-05-27 for critical review. Not yet authorized.
>
> **Author:** Claude (Opus 4.7).
>
> **Companion notes:**
> - [`fiction-craft-rewrite-analysis.md`](./fiction-craft-rewrite-analysis.md) — *what* moves to apply and avoid, the three open questions.
> - [`fiction-craft-rewrite-machinery.md`](./fiction-craft-rewrite-machinery.md) — the contract/registry/audit apparatus that backs the cycle.
>
> **Audience:** xaiolai (principal author), jerry-crew-chief.
>
> **Decision needed before action:** explicit green-light at Gate A (below). No prose changes, no skill builds, no registry creation before Gate A.

---

## 1. Objective

Apply Bucket 1 craft moves from the analysis note (document-as-protagonist, two-track time, focalize-then-break, delayed naming upward, voice braid, hammer-line reversal, resonant return, one image per chapter) to the 13 `status: ready` chapters, **without** breaking the evidence regime, defamation wording, taxonomy discipline, or the existing audit pipeline.

Out of scope: thesis revision, taxonomy change, new case files, A2B engine change, rule edits under `.claude/rules/`.

---

## 2. Two divergent paths the plan must serve

The analysis note ended on a binary question. The plan branches on the answer:

- **Path R (full craft rewrite).** Reader experience defect is *"reads as analytical when I want inevitable."* This plan's body covers Path R.
- **Path P (polish pass).** Reader experience defect is *"want it more gripping."* Path P applies only Bucket 1 moves #5 (voice braid), #6 (hammer-line reversal), #7 (resonant return), #8 (one image), inside the existing chapter architecture. Path P is a 3–5 day surgical cycle, not a re-production cycle, and does not require the machinery in the companion note. Path P appendix at §11.

Gate A (below) selects path. Everything after Gate A assumes Path R unless otherwise noted.

---

## 3. Gates and authority

Four hard gates. No work begins after a gate without its approval recorded.

| Gate | Trigger | Authority | Output of gate |
|---|---|---|---|
| **A. Path selection** | This plan is read | xaiolai | Path R or Path P or kill |
| **B. Pilot acceptance** | Phase 1 pilot complete + all audits run | xaiolai | Proceed to rollout, restrict scope, or roll back |
| **C. Mid-rollout health** | After every 4 rewritten chapters | xaiolai + jerry-crew-chief | Continue, slow, or stop |
| **D. Re-integration** | All 13 chapters rewritten + machinery audits green | xaiolai | Resume publication-pack sprint |

A failed Gate B is not a setback; it is the apparatus working. Roll back to Path P, log the failure mode, ship.

---

## 4. Sprint impact — what the rewrite displaces

Green-lighting Path R **pauses or invalidates** the current publication-pack sprint:

| Current sprint item | Effect of Path R |
|---|---|
| Blair proposal pack | **Pause.** Comp set and positioning may shift toward literary nonfiction; Blair work pre-rewrite would be re-done post-rewrite. Provisional Blair work is permitted only if Blair flags it as such. |
| Nancy final portfolio sweep | **Defer.** Defamation surface changes with focalization/naming choices; sweep must run on post-rewrite text. |
| Manuscript compile | **Defer.** Pointless until rewrite done. |
| Principal author final read | **Defer.** Same. |
| ch-13 closing sentence (xaiolai authors) | **Defer to last.** The closing sentence is the book-level resonant return; craft choices in ch-01 may reshape what it re-reads. |
| 2026-06-24 Nancy clock (ch-02) | **Re-runs after ch-02 rewrite**, not on calendar date. |
| 2026-06-25 Nancy clocks (ch-08/09/10/12) | Same — re-run after each rewrite, calendar dates void. |

If this displacement is unacceptable, the answer is Path P, not Path R.

---

## 5. Phase 0 — Inventory (no edits)

**Duration:** ≈1 cycle. **Owners:** `bonnie-book-architect` + `wayne-narrative-lead`, consolidated by `jerry-crew-chief`.

Per chapter (13 outputs), produce a one-page audit in `book/craft-inventory/<n>-<slug>.md`:

```markdown
- central artifact (current; candidate replacement if weak)
- current focalizer (who the reader sees through in beats 1–2)
- recognition beat location (which beat, which paragraph)
- what is withheld, where the fair clue plants it
- which Bucket 1 moves are already present implicitly
- which would require real surgery (low / medium / high)
- evidence-grade stability of the chapter's anchor claims (A-stable / mixed / contested)
```

**Phase 0 deliverable:** 13 inventory files + one consolidated ranking by `(surgery-need × evidence-stability)`. The pilot chapter is selected from this ranking (see §6).

**Phase 0 does not edit any chapter.** It exists so the pilot selection is principled.

**Gate A applies before Phase 0 begins.** Do not run the inventory speculatively.

---

## 6. Phase 1 — Pilot (one chapter)

**Duration:** ≈1 chapter-production cycle. **Owners:** `wayne-narrative-lead` (prose), `bonnie-book-architect` (structure), `stephen-fact-check-director` (audits), `nancy-legal-risk-counsel` (if chapter has live content), `jerry-crew-chief` (dispatch).

### 6.1 Pilot selection criteria

The pilot chapter must satisfy **all** of:

- **High surgery need** (so the pilot actually tests the craft moves; a chapter already 80% craft-augmented teaches us nothing).
- **A-grade-stable evidence anchors** (so craft change is not entangled with evidence change; one variable at a time).
- **No active Nancy clock** within 14 days (so the legal review window stays clean).
- **Not ch-01 or ch-13** (the boundary chapters carry book-level resonance; they should rewrite last, after the middle chapters have set the contracts they will resonate with).

If no chapter satisfies all four, the pilot is paused and the criteria are renegotiated at Gate A redux.

### 6.2 Pilot machinery build (minimal)

Per machinery note §"Build order," step 1 only:

- Create `book/chapters-v2/<n>-<slug>.contract.yml` for the pilot chapter (declare `reader_state_before`, `reader_state_after`, declared craft moves, declared voice-register distribution).
- Build `.claude/skills/contract-audit/` — reads contract + prose, checks `knows`/`feels`/`primed_for` slots.
- Build `.claude/skills/voice-register-audit/` — counts paragraph-tagged registers, checks distribution.
- **No** callback graph yet. **No** motif registry yet. **No** cognitive arc yet. **No** dependency check yet. Those come at Gate C if rollout proceeds.

### 6.3 Pilot execution

1. Read current chapter, contract, and inventory file.
2. Wayne drafts the craft-augmented rewrite against the contract.
3. Run new audits: `/contract-audit`, `/voice-register-audit`.
4. Run existing audit chain: `/audit-chapter`, `/evidence-audit`, `/fair-clue-audit`, defamation-wording scan.
5. Laura red-teams the rewrite specifically for: sympathy distortion (Bucket 2 #3), false symmetry (Bucket 2 #4), invented interiority creep (Bucket 2 #1).
6. Nancy reviews if chapter has live content.
7. Package diff + audit reports + red-team memo for Gate B.

### 6.4 Pilot acceptance criteria (Gate B)

The pilot **passes** if and only if:

- All existing audits green (parity with pre-rewrite state).
- New contract-audit and voice-register-audit green.
- Laura's red-team memo finds no Bucket 2 violations.
- Nancy clears (if applicable).
- **xaiolai reads both versions and judges the rewrite genuinely stronger.** This is the load-bearing criterion; the audits are necessary, not sufficient.

The pilot **fails** if any of the above fails. A failed pilot triggers a forced choice: (a) restrict rollout to Path P, (b) revise the craft moves selected and re-pilot, or (c) kill.

---

## 7. Phase 2 — Rollout (chapters 2..13 of the rewrite, not chapter numbers)

**Duration:** ≈12 chapter-production cycles, one at a time. **Owners:** same as Phase 1.

### 7.1 Order

Selected by ranking from Phase 0 inventory, with constraints:

- ch-01 and ch-13 last (boundary chapters absorb everything downstream of them).
- Adjacent chapters not back-to-back (so the dependency check has time to surface lateral-dep failures before the next rewrite compounds them).
- Live-content chapters (ch-08, ch-09, ch-10, ch-12) interleaved, not clustered (so Nancy is not back-loaded).

### 7.2 Machinery build at start of Phase 2

Per machinery note "Build order," steps 2 and 3:

- Build `book/callback-graph.yml` by backfilling from the rewritten pilot + the 12 unrewritten chapters' existing cross-references.
- Build `book/motif-registry.yml` by backfilling.
- Build `book/cognitive-arc.yml` by backfilling.
- Build `.claude/skills/callback-audit/`, `motif-audit/`, `cognitive-arc-audit/`, `dependency-check/`.

**Critical step:** before any chapter-2 rewrite, run all new audits on the **pre-rewrite** corpus to establish baseline state. Without baseline, the audits will flag pre-existing lateral debt as new damage.

### 7.3 Per-chapter cycle (executes 12 times)

Per machinery note §"How the pieces wire together":

```text
1. edit chapter
2. /contract-audit <chapter>
3. /voice-register-audit <chapter>
4. /callback-audit          (book-wide)
5. /motif-audit             (book-wide)
6. /cognitive-arc-audit     (book-wide)
7. /dependency-check <chapter>
8. existing pipeline: /audit-chapter, /evidence-audit, /fair-clue-audit,
   defamation-wording, Nancy clock if applicable
9. accept | rewrite | rollback per failure-mode table
```

### 7.4 Gate C — Mid-rollout health (every 4 chapters)

After chapters 1, 5, 9, 13 of the rewrite sequence (not chapter numbers), pause for xaiolai + jerry-crew-chief review:

- Are post-rewrite chapters reading as the analysis note predicted (inevitability rather than analysis)?
- Is the audit apparatus catching real failure modes, or is it crying wolf?
- Is the Nancy load sustainable, or back-loading?
- Is positioning drifting toward literary nonfiction faster than Blair can re-comp?

A negative answer at any Gate C stops rollout. Remaining chapters revert to Path P or stay as-is.

---

## 8. Phase 3 — Re-integration (Gate D)

**Duration:** ≈1 cycle.

- Run full machinery audit pass on entire post-rewrite corpus.
- Stephen runs cumulative fact-check delta against pre-rewrite source ledger.
- Nancy runs final portfolio sweep on post-rewrite text (replaces the deferred sweep from §4).
- Blair updates proposal pack with post-rewrite positioning, comps, sample-chapter strategy.
- xaiolai writes ch-13 closing sentence against the now-finalized resonant-return chain.
- `/compile-book` against the rewritten manuscript.
- xaiolai final read.

---

## 9. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Pilot fails Gate B; cycle was wasted | medium | low (one chapter cost) | Pilot is the cheapest possible failure; design accepts this |
| Mid-rollout fatigue → quality drift in late chapters | medium | medium | Gate C every 4 chapters; explicit slow/stop authority |
| Audit apparatus produces false positives → real prose is rejected | medium | medium | Phase 2 baseline run before any rewrite; tune thresholds before locking |
| Audit apparatus produces false negatives → degraded prose ships | low | high | Laura red-team per chapter is independent of the audit chain; xaiolai final read at Gate D |
| Defamation surface change unnoticed | low | high | Nancy reviews every live-content chapter individually + final portfolio sweep at Gate D |
| Positioning shift breaks comp-set | medium | medium | Blair work paused, not abandoned; resumed at Gate D with post-rewrite text |
| Rewrite introduces forward dependencies | medium | medium | `/dependency-check` per chapter; hard fail on forward deps |
| Sprint displacement is rejected mid-flight | low | high | Gate A makes displacement explicit and authorized before Phase 0 |
| `<!-- voice: -->` tag breaks `/compile-book` export | medium | low | Verify in pilot; alternative carrier (separate `.voice.yml` sidecar) if export breaks |

---

## 10. Cost estimate

In agent-time, not wall-clock; assumes Opus 4.7 on all crew roles per `AGENTS.md` model policy.

| Phase | Estimate | Notes |
|---|---|---|
| Phase 0 inventory | ≈13 chapter-audit units | one per chapter, parallelizable across bonnie/wayne |
| Pilot machinery build (minimal) | ≈2 skill-build units | contract-audit, voice-register-audit |
| Pilot chapter | ≈1 chapter-production unit | including audits and Gate B package |
| Full machinery build | ≈4 skill-build units + 3 registry-backfill units | between pilot and rollout |
| Rollout | ≈12 chapter-production units | one per chapter |
| Re-integration (Phase 3) | ≈3 cycle units | machinery audits + Blair re-comp + ch-13 + compile + final read |
| **Total Path R** | **≈35 units** | roughly equivalent to original chapter-production cycle ×3 |
| **Total Path P (for comparison)** | **≈5 units** | polish-pass only, no machinery, no registries |

The 7× ratio between Path P and Path R is the cost of the binary in §2.

---

## 11. Path P appendix — the polish-pass alternative

If Gate A selects Path P:

- No machinery, no registries, no new audits.
- One Wayne polish pass over each of the 13 chapters applying Bucket 1 moves #5 (voice braid via prose treatment, not paragraph tags), #6 (hammer-line reversal — already permitted by style rule, just commit harder), #7 (resonant return — append/strengthen the closing coda), #8 (one image — device-audit already enforces).
- Existing audit chain only. No contract files. No callback graph.
- Nancy clocks proceed as scheduled (2026-06-24, 2026-06-25); polish pass does not touch the prose surfaces that re-open defamation.
- Blair proposal pack continues in parallel; no positioning shift.
- ≈5 agent-cycle units total. Could complete in current sprint window.

Path P is not lesser. Path P is the right answer if the defect is "more gripping," not "reads as analytical."

---

## 12. Owner and dispatch map (Path R)

| Phase | Owner | Dispatch from |
|---|---|---|
| Gate A | xaiolai | — |
| Phase 0 | bonnie + wayne (parallel) | jerry-crew-chief |
| Phase 1 prose | wayne | jerry-crew-chief |
| Phase 1 audits | stephen | jerry-crew-chief |
| Phase 1 red-team | laura | jerry-crew-chief |
| Phase 1 legal | nancy (if needed) | jerry-crew-chief |
| Gate B | xaiolai + jerry-crew-chief | — |
| Phase 2 per chapter | same as Phase 1 | jerry-crew-chief |
| Gate C | xaiolai + jerry-crew-chief | — |
| Phase 3 fact-check delta | stephen | jerry-crew-chief |
| Phase 3 final legal | nancy | jerry-crew-chief |
| Phase 3 proposal re-comp | blair | jerry-crew-chief |
| Phase 3 ch-13 closing | xaiolai | — |
| Phase 3 compile | (skill `/compile-book`) | jerry-crew-chief |
| Gate D | xaiolai | — |

No agent gets craft authority outside its declared role per `03-no-overlap-role-map.md`. Wayne does not legal-clear. Nancy does not rewrite prose. Bonnie does not draft. The plan respects the existing crew architecture.

---

## 13. Kill-switch criteria

The plan terminates (not pauses; terminates) on any of:

- Three consecutive Gate B / Gate C failures with no path forward.
- Nancy raises an unresolvable defamation risk introduced by craft moves.
- Stephen detects a fact-check regression that the rewrite caused (not pre-existing).
- xaiolai withdraws Gate A authorization.

Termination defaults to Path P for any not-yet-rewritten chapters; rewritten chapters keep their rewrites if they passed Gate B individually, even if rollout terminates.

---

## 14. Handoff

- **Owner of this plan:** `jerry-crew-chief`.
- **Purpose:** implementation plan for a fiction-craft rewrite cycle on 13 `status: ready` chapters, with explicit gates, owners, and kill-switch.
- **Evidence grade:** N/A — methodological proposal.
- **Assumptions:** all `.claude/rules/` files remain governing; A2B Engine V2.2 unchanged; 10-beat chapter rhythm unchanged; crew model policy unchanged.
- **Open questions:**
  - Is the pilot-chapter selection rubric in §6.1 correct, or is "no ch-01/ch-13" too restrictive?
  - Are the machinery build thresholds (10%/70% voice register) tunable from the pilot, or should they be set from a separate experiment?
  - Does the displacement of the publication-pack sprint (§4) survive Gate A, or does that displacement itself force Path P?
- **Handoff:** xaiolai for Gate A; if Path R selected, `jerry-crew-chief` to dispatch Phase 0 across `bonnie-book-architect` and `wayne-narrative-lead`.
