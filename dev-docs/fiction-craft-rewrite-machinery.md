# Craft machinery — treating the rewrite as a typed system

> **Status:** machinery spec for a potential craft-rewrite cycle. Companion to [`fiction-craft-rewrite-analysis.md`](./fiction-craft-rewrite-analysis.md), which scopes *whether* and *which* moves; this note specifies *how the rewrite stays under control* once moves are chosen.
>
> **Implementation:** the machinery described here is built and operational. See [`book/plans/fiction-craft-rewrite-workflow.md`](../book/plans/fiction-craft-rewrite-workflow.md) for the active workflow, and `.claude/skills/` + `.claude/rules/07-09,12` + `.claude/hooks/scan-implication.py` for the executable artifacts.
>
> **Author:** Claude (Opus 4.7) — pre-pilot scoping note, drafted 2026-05-27.
>
> **Audience:** xaiolai (principal author), jerry-crew-chief, bonnie-book-architect, wayne-narrative-lead, stephen-fact-check-director.
>
> **Decision needed before action:** the same binary as the analysis note — Phase 1 pilot or polish-pass. This file describes the audit/registry apparatus that would back Phase 1 if it runs.

---

## Framing

If we rewrite 13 chapters with fiction-craft moves while keeping the evidence regime, the way to not lose control is to treat the book the way we'd treat a program: declared contracts per chapter, registries per cross-chapter device, audits that check the contracts hold.

What follows is the data shape and check for each item in the question (reader-state pre/postcondition, callbacks, setups, failure modes, voice register, motif tracker, cognitive arc, dependency check). Most fits the project's existing YAML-card + skill + script pattern; very little new infrastructure.

---

## 1. Reader-state precondition / postcondition

A Hoare triple per chapter: chapter N requires `{state_before}`, produces `{state_after}`. "Reader state" decomposes into four orthogonal slots so the check is mechanical, not vibes-based:

```yaml
# book/chapters-v2/<n>-<slug>.contract.yml
reader_state_before:
  knows:            [concept-ids the reader can name]
  can_discriminate: [distinction-ids the reader can apply]
  feels:            [declared-stance-ids — e.g. "sympathy:visible-goat:on"]
  primed_for:       [fair-clue-ids planted earlier]
reader_state_after:
  knows:            [...]   # must be superset (or declared retirement)
  can_discriminate: [...]   # ditto
  feels:            [...]   # may flip; flip must be declared
  primed_for:       [...]   # new plants for later chapters
```

**Check:** `/contract-audit <chapter>` reads the contract, walks the prose, confirms (a) every `knows` item is named in the chapter and used, (b) every flip in `feels` has a recognition beat that earns it, (c) every retired discrimination is explicitly retired (not silently dropped).

**Failure mode it catches:** chapter declares the reader will exit feeling `sympathy:visible-goat:off, sympathy:chain:on` but no recognition beat performs the transfer. Currently invisible; with the contract, fails the audit.

**Honest limit:** "earns it" is partly judgment. The audit can confirm the structural beat is present; it cannot confirm it lands.

---

## 2 + 3. Callbacks and setups — one graph, two views

Callbacks and setups are the same edge in a DAG, viewed from opposite ends. One book-level registry:

```yaml
# book/callback-graph.yml
- id: foia-folder-marked-classified
  planted:
    chapter: 02
    section: §3
    line_anchor: "the manila folder, edge stamped"
  paid_off:
    chapter: 09
    section: §7
    line_anchor: "the same edge stamp, now meaningless"
  type: object_callback | phrase_callback | scene_callback | rule_callback
  payoff_kind: re-reading | reversal | confirmation | refutation
  required: true   # if false, payoff is bonus; if true, missing payoff fails audit
```

**Check:** `/callback-audit` runs three passes — (1) every `planted` line anchor exists in its chapter; (2) every `paid_off` line anchor exists; (3) no orphans (planted with no payoff, or payoff with no plant) unless explicitly marked `payoff_kind: ambient` for atmospheric setups.

**Failure mode it catches:** ch-02 revision removes the manila folder; ch-09's recognition beat now references a thing the reader never saw. Currently you would notice on a re-read, maybe. With the graph, fails immediately.

**Honest limit:** cannot verify the payoff *lands*; only that anchors exist and the edge is wired.

---

## 4. Failure modes — per craft move, declared with its catching audit

Keep this as a table the audits reference, not as prose:

| Craft move | Failure mode | Catching audit |
|---|---|---|
| Delayed naming upward | Reader does not know who is being discussed at the recognition beat | fair-clue-audit + contract-audit (`knows` slot) |
| Focalize-then-break | Sympathy never transfers from goat to chain | contract-audit (`feels` slot transition) |
| Document-as-protagonist | Artifact appears once, never returns | motif-tracker (frequency floor) |
| Voice braid | One register dominates; chapter reads as monolithic | voice-register-audit (distribution check) |
| Resonant return | Closing coda does not re-read the opening object | contract-audit (postcondition: `re_reads_opening: true`) |
| Reversal-beat hammer line | Recognition arrives as analytical paragraph, not as turning sentence | audit-chapter (existing) + sentence-length check at declared beat |
| Two-track time | One track collapses; chapter becomes single-track again | structural audit on declared `tracks: [event, record]` |
| One image | Two competing major images per chapter | device-audit (existing rule) |

This table is also the rollback rubric: when a chapter pilot fails, the table tells you which craft move and which audit threw.

---

## 5. Voice register

Three registers, tagged at the paragraph level:

- `R-primary` — primary document quoted at full force
- `R-frame` — newsroom-style paraphrase / reportorial frame
- `R-analytic` — the book's analytical voice

Tag in manuscript Markdown via a thin convention — e.g. a pre-paragraph HTML comment `<!-- voice: R-frame -->` the audit can read without altering rendered prose.

**Check:** `/voice-register-audit` computes per-chapter distribution; fails if any register is <10% or >70% (numbers tunable from the pilot). Also confirms transitions are marked, not silent.

**Failure mode it catches:** an "evidence-heavy" chapter that turns out to be 95% analytical with primary docs paraphrased into the analytical voice — the texture the craft move is supposed to produce simply never appears.

**Honest limit:** does not know if the register choice is *right* for the passage. Only knows the distribution.

---

## 6. Motif tracker

Motifs are distinct from the master metaphor field. The field is the image-world ("evidence-forensics"); a motif is a specific recurring object/phrase/image inside it ("the empty chair," "the FOIA stamp," "the closed envelope"). Book-level registry:

```yaml
# book/motif-registry.yml
- id: empty-chair
  field: evidence-forensics
  literal_or_metaphorical: both
  appearances:
    - {chapter: 01, treatment: literal,      role: scene-anchor}
    - {chapter: 04, treatment: metaphorical, role: callback}
    - {chapter: 11, treatment: literal,      role: resonant-return}
  evolution: "literal absence → felt absence → structural absence"
  forbidden_in: [05, 06]   # chapters where it would dilute
```

**Check:** `/motif-audit` — (a) each declared appearance is in the chapter; (b) no motif appears in a `forbidden_in` chapter; (c) frequency floor (a motif that appears only once is not a motif; either promote to a real motif or demote to a one-off image); (d) evolution actually progresses (no flat repetition without development).

**Failure mode it catches:** motif drift — "the closed envelope" appears in ch-3, ch-7, and ch-10 with identical treatment and no evolution. Currently invisible; with the tracker, demotes to one-off.

**Honest limit:** cannot tell decorative-but-pretty from diagnostic. The `role:` field forces the author to declare it; the audit just enforces the declaration matches what is there.

---

## 7. Cognitive arc

Book-level reader epistemic journey, separate from per-chapter contracts. One table:

```yaml
# book/cognitive-arc.yml
discriminations:
  - id: distinguish-pure-from-partial-scapegoat
    introduced_in: 02
    consolidated_by: 04
    required_by:    [05, 07, 09, 11, 13]
  - id: identify-system-or-object-alibi
    introduced_in: 03
    consolidated_by: 06
    required_by:    [10, 12, 13]
  - id: read-cost-bearing-goat-pattern
    introduced_in: 05
    consolidated_by: 08
    required_by:    [09, 11, 13]
concept_introductions:
  - {id: responsibility-chain, ch: 01}
  - {id: alibi-shell,          ch: 03}
  - {id: record-control,       ch: 04}
retirements:
  - {id: pre-book-frame:complexity-equals-innocence, retired_by: 02}
```

**Check:** `/cognitive-arc-audit` — for every chapter that uses a discrimination, that discrimination must be introduced and consolidated before it; concept references must postdate introductions; retired pre-book frames must not reappear unmarked.

**Failure mode it catches:** ch-09 asks the reader to apply the system/object-alibi discrimination, but ch-03/06 do not actually consolidate it. Currently you would find this in beta-read confusion; with the audit, fails before beta.

---

## 8. Dependency check — the umbrella

The cognitive arc plus the callback graph together produce a DAG. The dependency check runs over it:

- **Forward deps** (chapter K requires concept introduced in chapter K+M, M>0) — hard fail.
- **Lateral deps** (chapter K requires a callback from chapter K-M to chapter K-N, and K-M is being revised) — soft fail: flag every downstream chapter that uses the affected node.
- **Cut-chapter blast radius** — if chapter K is deleted, list every callback, discrimination, and motif appearance that breaks. (This is the part that protects ready chapters during the craft-rewrite cycle.)

The dependency check is the gate at the end of every pilot rewrite: change ch-04, run the check, see exactly which other chapters' contracts the change touched.

---

## How the pieces wire together

```text
per-chapter rewrite cycle
  1. edit chapter
  2. /contract-audit <chapter>            # pre/post hold?
  3. /voice-register-audit <chapter>      # distribution OK?
  4. /callback-audit                      # cross-chapter edges still wired?
  5. /motif-audit                         # tracker still consistent?
  6. /cognitive-arc-audit                 # discriminations still installed?
  7. /dependency-check <chapter>          # blast radius identified?
  8. existing pipeline: /audit-chapter, /evidence-audit, /fair-clue-audit,
     defamation-wording, Nancy clock if applicable
  9. accept | rewrite | rollback per failure-mode table
```

Contract/registry files are the new artifacts. Audits are new skills that read those files plus the prose. The existing pipeline does not change — the new checks layer in front of it.

---

## What this machinery cannot do — and what that means

It cannot tell you whether a chapter is *good*. It can tell you whether the chapter delivers what its author declared it would deliver, with the textures and edges declared, without breaking the book's accumulating contracts. That gap — between "delivers the contract" and "is good" — is exactly where the principal-author read at Phase 2 of the pilot lives. The machinery's purpose is to make that read about quality, not about bookkeeping.

The smaller risk worth naming: the registries (callback graph, motif tracker, cognitive arc) cost real authorial time to declare. If we build them and then do not use them, we have added bureaucracy and gotten nothing back. The reason to build them is that without them, the craft-rewrite cycle has no rollback signal — you change ch-04 and discover the cost in ch-09 weeks later. The registries pay for themselves on the first prevented regression.

---

## Build order — if Phase 1 pilot is green-lit

Build the minimum to run the pilot, not the full apparatus on day one:

1. **Pilot-only (one chapter):** `*.contract.yml` + `/contract-audit` + `/voice-register-audit`. No book-level registries yet.
2. **Pilot + one adjacency:** add `/callback-audit` and `book/callback-graph.yml` populated with edges touching the pilot chapter and its nearest two neighbors.
3. **Full apparatus:** add `book/motif-registry.yml`, `book/cognitive-arc.yml`, `/motif-audit`, `/cognitive-arc-audit`, `/dependency-check`. Backfill from existing 13 chapters.

The build is itself a check: if step 2 cannot be populated without inventing edges that do not exist in the current manuscript, the craft moves are not yet in the book — which is useful information.

---

## Handoff

- **Owner of this note:** `jerry-crew-chief` (routes to `bonnie-book-architect` for the registries; to `wayne-narrative-lead` for the contracts; to `stephen-fact-check-director` for audit-skill build).
- **Purpose:** specify the audit + registry apparatus that backs a fiction-craft rewrite cycle without losing evidence-regime control.
- **Evidence grade:** N/A — methodological proposal.
- **Assumptions:** A2B Engine V2.2, the 10-beat rhythm, and all `.claude/rules/` files remain governing; this apparatus layers in front of the existing pipeline, does not replace it.
- **Open questions:**
  - Are voice-register distribution thresholds (10%/70%) the right starting numbers, or should they be set from the pilot?
  - Should the registries live under `book/` (current proposal) or under `foundry/` (treating them as Foundry-level instance state)?
  - Does the `<!-- voice: -->` tag convention survive `/compile-book` Markdown export, or does it need a different carrier?
- **Handoff:** xaiolai for the green-light on Phase 1; if yes, `jerry-crew-chief` to dispatch the minimal pilot build (step 1 in the build order above).
