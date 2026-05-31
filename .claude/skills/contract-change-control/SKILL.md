---
name: contract-change-control
description: Manage versioned amendments to a chapter's per-chapter contract during a rewrite cycle. Diffs pre vs post contract, requires a reason for every changed field, flags amendments that would mask Gate B failure (e.g., a `feels:` slot weakened to match the rewrite rather than its promise), and snapshots both versions into the chapter's audit history. Used by Wayne, Bonnie, and jerry-crew-chief at Gate B.
version: 1.0.0
---

# Contract Change Control

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- Whenever a chapter's `book/chapters-v2/<n>-<slug>.contract.yml` is edited after the chapter has entered `status: in-rewrite` per rule 09.
- Before `/contract-audit` runs on a chapter whose contract has changed since the prior audit — otherwise contract-audit grades against the moved goalpost.
- At Gate B, automatically, by jerry-crew-chief, to verify the contract the Gate B package presents is identical to the contract the rewrite was authorized against (or to verify any amendments meet the cited-reason requirement in this skill's rubric).

## The change-control invariant

The invariant the skill enforces is **the contract may change; the change must be visible**.

A rewrite cycle can legitimately reveal that a declared contract slot was wrong. Wayne discovers the focalize-then-break does not produce the declared `feels: sympathy:chain:installed` transition; the actual result is `feels: sympathy:split:installed` (sympathy genuinely splits between goat and chain in this case). That is a real finding, not failure to deliver. The contract should change to match the finding, and the change should be recorded with its reason. What the skill prevents is the silent revision that weakens a slot to match an under-performing rewrite.

## Decision rubric

A contract amendment passes change-control when:

1. **Pre-amendment contract is snapshotted.** A copy of the contract as it stood before the amendment exists in `process/audits/history/<n>/<timestamp>/<n>-<slug>.contract.preamend.yml`.
2. **Every changed field has a `change_reason:` annotation.** The reason names the prose finding that motivated the change, with line anchors.
3. **Field-by-field classification.** Each amendment is classified as:
   - `discovery` — the rewrite revealed the original slot was structurally wrong (e.g., the case taxonomy was misidentified in the original contract).
   - `clarification` — the slot was right but ambiguously stated; the amendment sharpens without weakening.
   - `weakening` — the slot is being reduced to match an under-performing rewrite. **Hard flag.** Requires explicit Laura red-team and xaiolai approval before the amendment can be accepted.
   - `strengthening` — the slot is being raised because the rewrite over-delivered. Permitted; flag for Gate B as a "conditional pass: over-delivery" note.
4. **No weakening of core values.** Per rule 12, slot amendments that touch declared `feels:` transitions linked to core values V1, V3, V5, V7, V8 cannot be classified `weakening` without Laura veto-clearance under rule 03 amendment.
5. **Cross-chapter dependencies updated.** If the amended slot is referenced by another chapter's contract (callback graph dependency), the downstream contracts are flagged for re-audit.

## Conflict handling

1. **Wayne amends `feels: sympathy:chain:installed → feels: sympathy:split:installed` because the chapter is genuinely about partial-scapegoat.**
   Classification: `discovery`. Permitted; record reason with prose line anchor. The amendment aligns the contract with the rule-01 case taxonomy. Cross-chapter audit: does this change leave callbacks intact in chapters that depended on the chain-sympathy installation? If yes, accept; if no, escalate to Bonnie for cognitive-arc revision.

2. **Wayne amends `knows: [responsibility-chain-mapping]` → `knows: []` because the chapter no longer installs the concept.**
   Classification: `weakening` if responsibility-chain-mapping is a core book concept; `discovery` if the concept was misplaced in this chapter's contract and is installed by a different chapter. Resolution: verify against `book/registries/cognitive-arc.yml` — if this chapter is the declared introduction point, escalate to Bonnie; if another chapter is the introduction point, accept.

3. **Bonnie amends the contract after structural review to change scene order.**
   Classification: `clarification` for slots whose evidence anchors just shifted line numbers; `discovery` for slots whose recognition beat moved to a different scene. Either way the amendment is permitted because Bonnie's owns structural changes per rule 03.

4. **Amendment passes change-control but Laura subsequently red-teams the new contract as V3 violation.**
   The amendment stands as an amendment (change-control passed); the chapter still fails Gate B on V3. The amendment trail is preserved in the audit history; xaiolai can see exactly what was changed and why before the V3 failure.

5. **Amendment removes a `primed_for:` fair-clue that a downstream chapter depends on.**
   Hard fail; the amendment is rejected. Either the downstream chapter's contract must also amend (cross-chapter coordinated amendment, requires Bonnie), or the fair-clue must be replanted elsewhere in this chapter.

## Escalation conditions

- Escalate to Laura whenever an amendment is classified `weakening` and the affected slot is a `feels:` transition touching rule 12 core values.
- Escalate to xaiolai for final approval on any `weakening` amendment regardless of slot.
- Escalate to Bonnie when an amendment requires cognitive-arc revision or cross-chapter coordinated amendment.
- Escalate to Stephen when an amendment changes `knows:` slot concepts whose underlying source-ledger anchors are affected.
- Escalate to Nancy when an amendment to a `feels:` transition affects a chapter with live content (named living individuals, active litigation).

## Boundary-case recipes

1. **Multiple amendments to the same contract in a single cycle.**
   Each amendment runs its own change-control pass; amendment chains are recorded as `amendment_chain:` in the audit memo. Three or more amendments to the same slot in one cycle suggests the underlying defect-diagnose was wrong; escalate to xaiolai for treatment-class re-evaluation.

2. **Contract amendment alongside cognitive-arc amendment.**
   Treat as coordinated amendment; both files are diffed and reasoned about together. Bonnie owns both; Wayne's role is to identify the prose evidence motivating the coordinated change.

3. **Contract amendment after Gate B failure, before re-attempt.**
   Permitted. Record the prior Gate B failure as the change reason. The amended contract becomes the new pre-rewrite baseline; the next contract-audit grades against the amended target. This is the "learning" path the rule preserves.

4. **Contract amendment where the pre-amendment snapshot is missing.**
   Hard fail; the snapshot is the invariant's foundation. Either reconstruct from git history or refuse the amendment until the rule-09 snapshot can be built.

5. **Amendment to add new slot that did not exist in pre-amendment.**
   Treat as `strengthening` by default; the chapter is now committing to deliver more than it originally promised. Accept; verify the chapter actually delivers via the next contract-audit run.

## Output format

```text
Owner: contract-change-control (skill run by <wayne|bonnie|joe>)
Task: Validate amendment to book/chapters-v2/<n>-<slug>.contract.yml
Inputs reviewed:
  - book/chapters-v2/<n>-<slug>.contract.yml (post-amendment)
  - process/audits/history/<n>/<timestamp>/<n>-<slug>.contract.preamend.yml
  - book/registries/cognitive-arc.yml (if knows/can_discriminate slot touched)
  - book/registries/callback-graph.yml (if primed_for slot touched)
Output: change-control memo at process/audits/<n>-<slug>-contract-change-control.md
Evidence grade: N/A
Assumptions: <e.g., pre-amendment snapshot was archived by pre-edit-chapter-snapshot.py>
Open questions: <amendments awaiting Laura or xaiolai approval>
Risks: <downstream chapters whose contracts may need coordinated amendment>
Handoff: <next reviewer or xaiolai if weakening>
```

Field-by-field diff table:

| Field | Pre-amendment value | Post-amendment value | Classification | Reason | Approval status |
|---|---|---|---|---|---|

Cross-chapter dependency audit:

| Downstream chapter | Slot referenced | Impact | Required action |
|---|---|---|---|

## Examples

<example>
Context: Wayne completes the rewrite of ch-08 and discovers the chapter's actual `feels:` transition is `sympathy:split:installed`, not the declared `sympathy:chain:installed`. He amends the contract and runs `/contract-change-control`.

A: "Change-control for ch-08 contract amendment. One field changed: feels.transition_1. Pre: sympathy:visible-goat:on → sympathy:chain:on. Post: sympathy:visible-goat:on → sympathy:split:installed. Classification: discovery (case is documented partial-scapegoat per case-files; original contract misidentified as pure-scapegoat-target). Reason: 'Recognition beat at L420 produces split sympathy because the visible actor IS culpable at one level; the chain extends further but the goat is not innocent. Aligns with rule-01 partial-scapegoat taxonomy.' Cross-chapter audit: ch-10 callback graph depends on ch-08's chain-sympathy installation; that callback no longer fires. Escalate to Bonnie for ch-10 coordinated amendment OR for cognitive-arc revision to move the chain-sympathy installation to a different chapter. No Laura escalation required (discovery, not weakening)."
<commentary>
The skill classifies this as discovery per the rubric (the rewrite revealed a real structural finding, not a weakening), records the reason with line anchor, identifies the cross-chapter consequence, and routes to Bonnie for the dependency. This is how the rule keeps amendment honest without making it impossible.
</commentary>
</example>
