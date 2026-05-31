---
name: case-file-method
description: Build a structured responsibility-laundering case file from a historical, political, legal, corporate, war, or AI event.
version: 1.0.0
---

# Case File Method

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
- Builds one complete case file with all required fields and one explicit case type.
- Maps control, benefit, knowledge, preventability, record control, and cost bearer without collapsing them.
- Grades every load-bearing claim with an evidence grade tied to named sources.
- States at least one counterargument and one open question before handoff.

Weak output:
- Leaves required fields blank or mixes two case types without a decision record.
- Treats allegation as finding or finding as judgment.
- Uses inference as fact when the record is incomplete.
- Omits handoff owner or next action.

## Conflict handling

1. Two sources conflict:
Use the higher evidence grade source as the working anchor, log the lower-grade claim in open questions, and handoff to Delon for source packet expansion if the conflict changes case type.
2. Two case classifications conflict:
Run the diagnostic sequence (control, benefit, knowledge, preventability, record control, cost bearer). Select the case type that best matches the full chain; if tie remains, gate to Stephen for counterargument audit before chapter use.
3. Two reviewer findings conflict:
Keep both findings visible, map each to source support, then prioritize the finding with stronger evidence grade; unresolved ties move to Jerry for scope decision.

## Escalation conditions

- Proceed when evidence grade is A or B for the core responsibility chain and only non-load-bearing details remain open.
- Handoff to Delon when source access blocks a classification decision.
- Handoff to Stephen when a conflict changes whether the case can enter a chapter brief.
- Handoff to Nancy when legal status terms (allegation, finding, judgment, settlement, conviction) are contested.

## Boundary-case recipes

1. Single-language archive only:
Build the case file as provisional, grade core claims C, flag translation gap, handoff to Delon for independent translation sources.
2. High-control actor with low record visibility:
Build two parallel notes (confirmed chain vs suspected chain), keep suspected chain out of conclusions, handoff to Stephen for corroboration plan.
3. Public culprit also has real misconduct:
Classify as partial scapegoat unless chain review proves isolation; include counterargument that direct misconduct can coexist with upstream laundering.

Build a case file with this structure:

```text
Case name:
Domain:
Dates and place:
Case type: pure scapegoat / partial scapegoat / system/object alibi / cost-bearing goat
Crisis:
Official story:
Blame container:
Actual responsibility chain:
Control:
Benefit:
Knowledge:
Preventability:
Record controller:
Cost bearer:
How the alibi hardened:
How the alibi weakened:
Best counterargument:
Evidence grade:
Sources needed:
Narrative scenes:
Book function:
Handoff owner:
```

Rules:
- Do not infer motive unless the record supports it.
- Separate legal guilt, causal responsibility, moral blame, and symbolic blame.
- Flag unresolved issues instead of forcing a clean conclusion.

<example>
Context: Shirley (historical case researcher) is opening a new case for the partial-scapegoat chapter.
input: "Bhopal — Union Carbide India, 1984"
output: Returns a filled case-file template — case name, dates, place, case type (partial scapegoat: Warren Anderson scapegoated but Union Carbide Corp. shielded by parent-subsidiary structure), crisis, official story, blame container, actual responsibility chain, control/benefit/knowledge/preventability, record controller (UCC archives + Indian gov't), cost bearer (5,000+ dead, 500,000 injured), how the alibi hardened, how it weakened, strongest counterargument, evidence grade A (court judgments, ICMR studies), sources needed, narrative scenes, book function, handoff owner.
</example>

<example>
Context: Boundary case: the historical record exists only in one language with no English-language scholarship.
output: Returns a case-file skeleton marked status: source-language-only, with a 'translation needed' open question, evidence grade C until at least one independent translation is available, and a handoff to Delon for translation-resource assignment.
</example>
