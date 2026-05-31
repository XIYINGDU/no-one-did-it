---
name: motif-audit
description: Audit the book-level motif registry that tracks recurring objects, phrases, and images across chapters. For each motif, verifies declared appearances exist, no motif appears in its `forbidden_in:` chapters, frequency floor is met, and declared evolution actually progresses (no flat repetition). Reads `book/registries/motif-registry.yml`. Distinct from metaphor-audit and device-audit.
version: 1.0.0
---

# Motif Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After any rewrite under treatment class `structural-polish` or `full-craft-rewrite` per rule 08, run book-wide.
- Whenever `book/registries/motif-registry.yml` is edited (add, change, remove a motif).
- At Stage 2 baseline run to establish the pre-rewrite motif state.
- Before any chapter promotion when the chapter contains a registered motif appearance.

## The motif registry

`book/registries/motif-registry.yml` lists every registered motif:

```yaml
- id: empty-chair
  field: evidence-forensics
  literal_or_metaphorical: both
  appearances:
    - {chapter: 01, treatment: literal,      role: scene-anchor}
    - {chapter: 04, treatment: metaphorical, role: callback}
    - {chapter: 11, treatment: literal,      role: resonant-return}
  evolution: "literal absence → felt absence → structural absence"
  forbidden_in: [05, 06]   # chapters where it would dilute
  frequency_floor: 3       # motifs need 3+ chapters to count
```

Distinct from metaphor fields (one per book, declared in the device-audit layer) and from analogy cards (single-chapter devices). A motif is a CONCRETE recurring image — an object, a phrase, a setting — not an abstract concept.

## Decision rubric

The audit runs four passes per motif:

### Pass 1: appearance verification
For each declared appearance, the motif's identifying detail (the literal image or phrase) must appear in the named chapter's prose. The match is fuzzier than callback-audit's line anchors — the audit reads the chapter for the motif's "footprint" (the object plus 1-2 distinctive descriptors). Soft fail if not found; flag for either replanting or appearance-list update.

### Pass 2: forbidden_in compliance
For each `forbidden_in:` chapter, the motif's identifying detail must NOT appear in that chapter's prose. The `forbidden_in:` list exists because the named chapter's load-bearing imagery would be diluted by the motif's appearance there (e.g., a "courtroom bench" motif forbidden in chapters set outside court systems).

### Pass 3: frequency floor
The motif's total verified appearances must meet or exceed `frequency_floor:`. A motif declared at frequency_floor: 3 with only 2 verified appearances is not a motif — either replant to add the missing appearance or demote to a one-off image (move to `book/imagery-log.md` as ambient image rather than tracked motif).

### Pass 4: evolution progression
The motif's declared `evolution:` string is a 3+ stage progression. The audit verifies that appearances IN ORDER follow the evolution — e.g., "literal absence → felt absence → structural absence" requires the first appearance to use literal absence framing, the middle appearance to use felt absence, the last to use structural absence. Flat repetition (same treatment in all appearances) is a soft fail; the motif works as ambient repetition but does not earn its "evolution" declaration.

## Conflict handling

1. **Motif appearance moved within the chapter during rewrite.**
   No-op for the audit; appearance lists do not record line anchors. As long as the motif's identifying detail is present in the named chapter, the appearance is verified.

2. **Motif appearance moved to a different chapter during scene reorder.**
   Update the registry's appearance list to reflect the new chapter. Verify the new chapter is not in `forbidden_in:`. If it is, escalate to Bonnie — the scene reorder is incompatible with the motif registry as declared.

3. **Rewrite added an unregistered motif (motif-like recurrence not in the registry).**
   Flag as candidate motif; escalate to Bonnie + xaiolai to either add to registry or accept as ambient imagery. Unregistered motifs are not failures; they are findings.

4. **Motif appeared in a `forbidden_in:` chapter because of rewrite.**
   Hard fail. Wayne to remove the motif from the forbidden chapter, OR Bonnie to revise the registry's `forbidden_in:` list with reason (rewrite revealed the motif works in this chapter after all).

5. **Motif evolution declared but appearances do not actually progress.**
   Two options: revise the evolution declaration to match reality, OR revise prose to install the declared progression. Pick based on which is more load-bearing for the book — if the evolution is a planned recognition device, revise prose; if the motif is genuinely ambient, revise declaration.

## Escalation conditions

- Escalate to Wayne for missing appearances (replant) or forbidden-in violations (remove).
- Escalate to Bonnie for cross-chapter motif coordination, registry-structure changes, or candidate-motif decisions.
- Escalate to xaiolai when 2+ motifs fail in a single rewrite cycle — the rewrite may have damaged the book's image-world coherence.
- Escalate to device-audit (the architectural skill) when a candidate motif overlaps with the master metaphor field, the analogy bank, or a paired-scene declaration. The motif registry should not duplicate device-audit's tracking.

## Boundary-case recipes

1. **First-time motif registry build (Stage 2 baseline run).**
   Skill traverses every chapter to identify candidate recurring images, phrases, and objects. Output is a proposed-motifs list for Bonnie + xaiolai. The skill does not auto-add motifs; humans verify motifs before they become enforceable.

2. **Auditing a motif whose evolution requires the boundary chapters (ch-01 plants, ch-13 resonates).**
   These motifs are the highest-priority audit targets because they carry the book's framing arc. If ch-01 or ch-13 rewrite has cut or shifted the motif, the entire book-level resonance is at risk; hard fail and escalate to xaiolai.

3. **Auditing a "negative motif" — something that should NOT appear, declared by absence.**
   `forbidden_in:` is the registry's mechanism. A motif of "the courtroom" forbidden in chapters about AI cases reinforces that AI cases are NOT courtroom-shaped. The audit's Pass 2 enforces this.

4. **Auditing a motif whose treatment column drifts (literal → metaphorical → metaphorical).**
   Permitted if the evolution permits — e.g., declared as "literal anchor → first metaphorical use → metaphorical resonance." Failure only if the drift contradicts the declaration.

5. **Auditing a motif registered with `frequency_floor: 5` whose only verified appearances are in chapters 3, 4, 5.**
   Frequency floor fail (3 < 5). Either replant in 2 additional chapters (with `forbidden_in:` compliance) or lower frequency_floor to 3 with reason.

## Output format

```text
Owner: motif-audit (skill run by <bonnie|joe>)
Task: Audit book/registries/motif-registry.yml against current chapter prose
Inputs reviewed:
  - book/registries/motif-registry.yml
  - book/chapters-v2/*.md
  - process/audits/history/ (snapshots if baseline comparison required)
Output: motif-audit memo at process/audits/motif-audit-<ISO-date>.md
Evidence grade: N/A
Assumptions: <e.g., motif identification footprint allows minor paraphrase>
Open questions: <candidate motifs awaiting Bonnie review>
Risks: <motifs near frequency floor that another rewrite could push below>
Handoff: <wayne for prose / bonnie for registry>
```

Per-motif findings:

| Motif id | Pass 1 (appearances) | Pass 2 (forbidden_in) | Pass 3 (frequency floor) | Pass 4 (evolution) | Action |
|---|---|---|---|---|---|

Candidate-motif findings:

| Candidate image | Chapters of recurrence | Should be registered? | Recommendation |
|---|---|---|---|

## Examples

<example>
Context: ch-04 rewritten under `structural-polish`. Jerry runs `/motif-audit` book-wide.

A: "Motif-audit complete. 6 motifs in registry. 5 pass all 4 passes. 1 issue: motif `manila-folder-classified` — Pass 1: appearance in ch-04 missing (rewrite removed the explicit folder reference from the new scene at L189). Frequency floor (3) now at 2 verified appearances. Two options: (a) Wayne replants the folder in ch-04's new scene, (b) Bonnie removes ch-04 from appearance list and lowers frequency_floor to 2 with reason. Routing to Bonnie + Wayne for joint decision; preference is (a) since the folder is the chapter's central artifact in the source ledger. No forbidden_in violations. No evolution drift."
<commentary>
The skill caught a real motif loss caused by the rewrite, named two legitimate fixes, and routed to the right owners. This is the audit catching cross-chapter damage that single-chapter audits would miss.
</commentary>
</example>
