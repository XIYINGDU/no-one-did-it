---
name: responsibility-chain-mapping
description: Map control, benefit, knowledge, preventability, record control, and cost-bearing for a case.
version: 1.0.0
---

# Responsibility Chain Mapping

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Decision rubric

Usable output:
- Maps both public chain and responsibility chain with explicit actor roles.
- Records control, benefit, knowledge, preventability, record control, and cost bearer for each actor.
- Distinguishes proven facts from open questions and grades evidence for each load-bearing link.
- States where responsibility should climb and where it should stop.

Weak output:
- Lists actors without chain direction or causal sequence.
- Uses one label to stand in for all diagnostic questions.
- Infers knowledge without source support.
- Omits cost bearer or record control.

## Conflict handling

1. Two sources disagree about actor knowledge:
Keep both entries, grade each claim, and flag knowledge as contested until higher-grade support resolves it.
2. Two case classifications emerge from one map:
Test which classification better matches control/benefit distribution; preserve alternative as counterargument field only.
3. Two reviewer findings disagree on where responsibility stops:
Select the stop-point backed by stronger evidence grade; unresolved high-impact disputes handoff to Jerry.

## Escalation conditions

- Proceed when chain direction and actor burdens are supported at evidence grade A or B for core links.
- Handoff to Delon when missing records prevent actor-level mapping.
- Handoff to Stephen when a contested link changes chapter eligibility.
- Handoff to Nancy when liability language may exceed the record.

## Boundary-case recipes

1. Anonymous committee decision:
Map committee as actor for interim chain, flag identity gap, and handoff for record retrieval.
2. Actor controls design but not execution:
Assign responsibility by control scope, keep execution actor separate, and avoid totalizing blame.
3. Benefit is diffuse across institution:
Map institutional benefit and executive benefit separately, then grade each with explicit source support.

Map two chains:

```text
Public chain: crisis -> named culprit -> punishment/closure
Responsibility chain: incentive -> design -> approval -> warning -> execution -> harm -> blame transfer -> exposure/remedy
```

For each actor, record:

```text
Actor:
Role:
Control held:
Benefit received:
Knowledge available:
Preventability capacity:
Record access/control:
Consequence faced:
Evidence grade:
```

Output a short conclusion: where responsibility should climb and where it should not.

<example>
Context: Laura wants to red-team a claim that a junior analyst "caused" the 2008 mortgage crisis.
input: claim="junior analyst caused subprime collapse"
output: Returns a responsibility-chain map — control (rating committees, not analysts), benefit (firm fees + executive bonuses), knowledge (internal emails show senior awareness), preventability (model changes vetoed at managing-director level), record control (firm-owned email archives, partially preserved by FCIC subpoena), cost-bearing (homeowners, pensioners, taxpayers). Conclusion: junior analyst is a partial-scapegoat candidate at best; map collapses the claim.
</example>

<example>
Context: Boundary case: knowledge cannot be proven (no documents, no admissions).
output: Returns a chain with knowledge marked 'unproven; circumstantial inference only', refuses to fill it from inference dressed as fact, and labels the case as ineligible for the strongest-claim version of the chapter argument.
</example>
