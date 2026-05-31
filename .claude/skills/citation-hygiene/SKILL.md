---
name: citation-hygiene
description: Prepare citation-ready notes for drafting, fact-checking, and legal review.
version: 1.0.0
---

# Citation Hygiene

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
- Links each claim to a precise source location with quote/paraphrase separation.
- Preserves dates, pagination, and dev-docs/access notes for verification.
- Assigns evidence grade and risk field per claim.
- Flags phrasing that overstates what the source supports.

Weak output:
- Uses broad source references without exact support.
- Blends quote and paraphrase without boundary.
- Omits access constraints that prevent independent verification.
- Keeps high-risk legal phrasing without counsel gate.

## Conflict handling

1. Two sources support conflicting phrasing:
Keep the narrower phrasing supported by higher evidence grade and log alternative phrasing as open question.
2. Two case classifications appear in cited material:
Do not settle classification in citation notes; handoff graded evidence to case-file owner for decision.
3. Two reviewer findings conflict on quote safety:
Prioritize legal-risk gate from Nancy when conflict concerns defamation or liability wording; otherwise prioritize strongest source support.

## Escalation conditions

- Proceed when every load-bearing claim has citation-ready support with evidence grade and risk field.
- Handoff to Delon when source access blocks exact citation.
- Handoff to Stephen when claim wording outruns source support.
- Handoff to Nancy when legally sensitive phrasing cannot be reduced safely.

## Boundary-case recipes

1. Paywalled primary source:
Record full citation metadata, use non-load-bearing paraphrase only, and handoff for access procurement.
2. Source retracts prior claim:
Log retraction as superseding record, downgrade prior claim status, and revise chapter brief language.
3. Source supports fact but not intent:
Cite factual claim only, remove intent wording, and handoff intent question for additional sourcing.

Requirements:
- One source should support one precise claim.
- Do not cite a source for a claim it does not actually make.
- Separate exact quotes from paraphrase.
- Preserve dates, page numbers, line numbers, archive links, and access notes where available.
- For live events, record the date the source was checked.

Output format:

```text
Claim:
Source:
Exact support:
Quote, if any:
Paraphrase allowed:
Evidence grade:
Risk:
```

<example>
Context: A claim that "Boeing executives knew about MCAS instability before the first crash" needs citation-grade backing before legal review.
input: claim="Boeing executives knew about MCAS instability before the Lion Air crash"
output: Returns citation-ready notes — primary anchor (DOJ 2021 deferred prosecution agreement, paragraphs cited), secondary (Seattle Times investigative series with FOIA'd emails), allegation vs. admission distinction marked (DPA contains admission of misleading FAA, not specific pre-crash internal-knowledge admission), proposed safer phrasing for legal review, handoff to Nancy.
</example>

<example>
Context: Boundary case: a primary document is paywalled and Wayne cannot quote it.
output: Returns the citation with an access note, proposes a secondary source that summarizes the same paragraph, and asks Delon to budget the paywall fee if the quote is load-bearing for the chapter.
</example>
