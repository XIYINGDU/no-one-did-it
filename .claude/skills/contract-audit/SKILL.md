---
name: contract-audit
description: Audit a chapter against its declared per-chapter contract (Hoare triple of reader-state pre/postconditions) and verify the chapter delivers the declared `knows`, `can_discriminate`, `feels`, and `primed_for` slots. The `feels:` slot resolves through rule 12 reader-experience values; passing requires both structural delivery AND core-value preservation.
version: 1.0.0
---

# Contract Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After a chapter rewrite pass under treatment class `structural-polish` or `full-craft-rewrite` per rule 08 (these classes require a contract file).
- Whenever the chapter's contract YAML is edited mid-cycle — the audit then verifies the edit is consistent with prose changes.
- Before any `status: in-review → ready` transition for a chapter under contract per rule 09.

Lower treatment classes (`prose-polish`, `defamation-safe-tighten`) do not require a contract; this skill does not apply to those.

## Decision rubric

For each slot in the chapter's `book/chapters-v2/<n>-<slug>.contract.yml`:

### `knows:` slot
Pass: every concept-id in `reader_state_after.knows` is named in the chapter prose and used (not just mentioned in passing). The use must be observable — a sentence that depends on the concept, not just one that defines it.

### `can_discriminate:` slot
Pass: every distinction-id in `reader_state_after.can_discriminate` is installed by the chapter — meaning the chapter contains BOTH (a) a passage that names the distinction and (b) a passage that demonstrates the distinction in action. Naming without demonstration installs a label, not a discrimination.

### `feels:` slot
Pass: every declared stance transition (e.g., `sympathy:visible-goat:on → sympathy:chain:on`) has a recognition beat that earns it per rule 12 V1 (earned not manufactured) and rule 12 V3 (sympathy follows the chain). The audit must:
- Identify the recognition beat (the prose moment where the transition lands).
- Verify the transition's prose evidence is consistent with the chapter's source ledger (no V7 evidence-grade mismatch).
- Verify the transition's craft moves do not violate rule 12 V8 (no internal laundering).

Conditional pass: the transition occurs but the recognition beat is weaker than the prior chapter version (per snapshot in `process/audits/history/`). Document as Gate-B "conditional pass" per rule 12.

### `primed_for:` slot
Pass: every fair-clue-id in `reader_state_after.primed_for` is planted in the chapter at a verifiable line anchor. Plant must be implicit enough not to spoil the future payoff but explicit enough that the future chapter's recognition can refer back.

## Conflict handling

1. **Chapter delivers more than the contract declared.**
   Permitted, but record the over-delivery as `additional_state` in the audit output. Over-delivery in `feels:` is a Laura red-team flag — the chapter may be making the reader feel something the contract did not authorize, and the over-feeling may be implication-driven (rule 07).

2. **Chapter delivers less than the contract declared.**
   Failed audit. The chapter is reverted to `status: in-rewrite` per rule 09. Either revise prose to deliver, or revise contract with rule-09 contract-change-control (skill `/contract-change-control`).

3. **Contract uses concept-ids not declared in `book/registries/cognitive-arc.yml`.**
   Soft fail; the audit flags the gap and routes to Bonnie to either add the concept to the cognitive arc or use an existing concept-id. Concept-ids without arc declarations are silent fragmentation.

4. **`feels:` slot declares a transition but Laura red-teams it as V3 violation (sympathy lands on wrong actor).**
   Hard fail on rule 12 core value. Laura's veto authority under rule 03 amendment applies. The chapter cannot promote to `ready`; either revise prose to fix V3 OR revise contract to declare the actual stance the chapter produces (and re-justify it).

5. **Audit is run on a chapter whose contract was just amended.**
   Run `/contract-change-control` first to validate the amendment did not mask failure; only then run contract-audit against the new contract.

## Escalation conditions

- Escalate to Bonnie when `can_discriminate:` slot failures are structural (the distinction's installation requires scene reorder, not prose tweak).
- Escalate to Laura when `feels:` slot transitions pass structurally but fail rule 12 V1, V3, or V8.
- Escalate to Nancy when `feels:` slot transitions pass structurally but the underlying claim has rule 12 V7 (severity-evidence mismatch) on a live-content actor.
- Escalate to Stephen when `knows:` slot failures stem from evidence-grade mismatch in the cited claim (concept is named but the citation supporting it is C-grade).
- Escalate to xaiolai when the contract's declared `feels:` transition matches the chapter prose but xaiolai's Gate B read disagrees on whether the transition is "genuinely stronger" — the rubric provides outcome classes; the human still adjudicates.

## Boundary-case recipes

1. **Auditing a contract that declares `knows: []` (empty know-slot).**
   Permitted — a chapter that installs only discriminations or feelings without introducing new named concepts uses this shape. Audit only the non-empty slots.

2. **Auditing a contract with multiple `feels:` transitions.**
   Audit each transition independently. A chapter cannot pass overall if any transition fails its recognition beat; partial pass is recorded but the chapter does not promote.

3. **Auditing a contract whose `primed_for:` includes a fair-clue paid off in a chapter that does not yet exist.**
   Permitted during rollout; the cross-chapter `/callback-audit` will flag the missing payoff at book-level. Contract-audit only verifies the plant exists.

4. **Auditing a contract where `reader_state_before` references concepts the prior chapter does not deliver.**
   Hard fail; the chapter requires a precondition the corpus does not provide. Either Bonnie revises chapter order, or Wayne adds a brief precondition-installation passage near the chapter opening.

5. **Auditing a chapter with no contract because the treatment class is `prose-polish`.**
   This skill exits with `not-applicable` and routes to the class-specific audit chain (`audit-chapter`, `evidence-audit`, `fair-clue-audit`, defamation-wording).

## Output format

```text
Owner: contract-audit (skill run by <wayne|stephen|joe|laura>)
Task: Audit book/chapters-v2/<n>-<slug>.md against book/chapters-v2/<n>-<slug>.contract.yml
Inputs reviewed:
  - book/chapters-v2/<n>-<slug>.md
  - book/chapters-v2/<n>-<slug>.contract.yml
  - process/audits/history/<n>/<prior-timestamp>/contract-audit.md (if exists)
  - .claude/rules/12-reader-experience-values.md
Output: contract-audit memo at process/audits/<n>-<slug>-contract-audit.md
Evidence grade: N/A
Assumptions: <e.g., contract was drafted by Wayne pre-rewrite and signed off by Bonnie>
Open questions: <slots whose verdicts are conditional + reason>
Risks: <slots whose passing depends on unverified downstream chapters>
Handoff: <next owner — wayne if revise, laura if feels-slot review, nancy if V7/V8, xaiolai if Gate B>
```

Per-slot findings table:

| Slot | Element | Verdict (pass/conditional/fail/over-delivered) | Evidence (line anchors) | Required action |
|---|---|---|---|---|

Per-`feels:`-transition table:

| Transition | Recognition beat (line) | V1 verdict | V3 verdict | V8 verdict | Overall |
|---|---|---|---|---|---|

## Examples

<example>
Context: Wayne completed the rewrite of ch-04 under treatment class `structural-polish`. The contract declares one `feels:` transition (sympathy:chain:installed) at the recognition beat in scene 3. Wayne runs `/contract-audit` before passing to Laura.

A: "Contract-audit complete for ch-04. knows: 3/3 pass. can_discriminate: 2/2 pass (proxy-vs-sponsor demonstrated at L312 with the named example). feels: 1 transition, recognition beat at L401. V1 pass (transition rests on cited memo CITE_04_017 at L398). V3 conditional — sympathy does land on the chain by L410, but a sympathetic descriptor for the proxy at L385 (scan-implication flagged) leaves residual sympathy that competes with the transfer. V8 pass. primed_for: 2/2 pass (motif of the empty chair planted at L80 and L520; both anchored in motif-registry). Overall: conditional pass; escalate to Laura for V3 read."
<commentary>
Real audit shape: most slots pass cleanly, one transition is conditional rather than failing outright, and the route to Laura is named. The cross-skill reference (scan-implication flag) shows the audits compose.
</commentary>
</example>
