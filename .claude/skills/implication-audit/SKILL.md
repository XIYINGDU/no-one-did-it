---
name: implication-audit
description: Audit a chapter or case file for narrative implication of mental state, motive, knowledge, causation, or chain responsibility that exceeds what cited evidence supports. Catches structural implication (sentence sequence, focalization, juxtaposition, named-then-named ladders) that verb-level overclaim scanning misses. Used by Stephen, Laura, and Nancy.
version: 1.0.0
---

# Implication Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- Stephen runs this skill during fact-check on every chapter before promotion to `status: ready`.
- Laura runs this skill during red-team specifically against rule-12 V8 (no internal laundering).
- Nancy runs this skill before sign-off when the chapter uses any Bucket 1 craft move from `dev-docs/fiction-craft-rewrite-analysis.md`.
- Wayne self-runs this skill during drafting whenever focalization, delayed naming, two-track time, or voice braid is in play.

The `scan-implication.py` hook is the cheap pattern-level pass that runs on every edit. This skill is the deeper read.

## Decision rubric

A chapter passes implication-audit when every implication-bearing paragraph satisfies AT LEAST ONE of:

- **Cited.** A `[CITE:]` anchor in the paragraph or adjacent paragraph names the source for the implied claim.
- **Hedged.** A rule-07 hedge pattern (e.g., "the record does not establish whether", "per the inquiry") appears within the paragraph or adjacent paragraph.
- **Named as inference.** The chapter explicitly names the inferential step: "the two events appear in the record in this order; the connection is not signed."
- **Inside a verbatim quotation.** Per rule 06, verbatim quotes may carry any implication the source's words carry.

A chapter fails implication-audit when:

- One or more implication patterns from rule 07's pattern table appear without any of the above mitigations.
- A chain-ladder pattern (3+ named actors in hierarchical succession) appears with fewer than 2 per-actor source citations.
- A delayed-naming structure attributes load-bearing responsibility to the last-named actor without a source for that load-bearing role.
- An anonymous-chain reference ("a higher office", "someone authorized") appears without a hedge naming the public record's silence.

## Conflict handling

1. **Implication-bearing paragraph IS the recognition beat of the chapter.**
   The recognition beat is the most load-bearing prose moment; it must be the most cited, not the least. If the recognition currently rests on implication, route to Stephen for source lift OR revise to ground the recognition in cited evidence + named inferential bridge. Do not lower the audit bar for "literary effect."

2. **The implication pattern is true to the public record but the record itself is C-grade.**
   The chapter cannot rest a load-bearing claim on C-grade evidence per rule 02. Either lift the grade (Stephen) or revise the implication to match the C-grade with explicit "according to <source>'s reconstruction, which the underlying records do not corroborate" framing.

3. **Hedge language kills the rhythm at the recognition moment.**
   Better dead-on-evidence than alive-on-overreach. The hedge stays; rhythm is reworked around it. If rhythm cannot survive, route to Wayne for restructuring or to Stephen for source upgrade.

4. **Implication pattern appears in a verbatim quotation by an investigator / inquiry.**
   The quotation may stand; the chapter still owes attribution and venue per rule 06. The audit reports the pattern as "quoted-finding, source-attributed" rather than failure.

## Escalation conditions

- Escalate to Stephen when a flagged implication could be resolved by adding a single citation already in the source ledger but not anchored in the chapter.
- Escalate to Nancy when a flagged implication targets a named living person or active corporate entity.
- Escalate to Laura when a flagged implication appears at the chapter's recognition beat — the recognition beat carrying implication weight is the highest-priority audit failure.
- Escalate to Wayne when the fix requires structural change (paragraph reorder, focalizer reassignment, motif reinsertion).
- Escalate to xaiolai when more than 3 implications appear in the same chapter and none have available citations or workable hedges — the chapter may need reclassification under rule 08 from `full-craft-rewrite` to `defamation-safe-tighten` until the source surface is rebuilt.

## Boundary-case recipes

1. **Reading a focalization choice.**
   Identify the focalizer (the consciousness through which the scene is presented). For every fact stated in the focalized passage that the focalizer would have had to know, the chapter must either cite the source for that knowledge or hedge ("the record does not say whether the focalizer was told"). Focalization makes implication free; the audit makes the cost explicit.

2. **Reading a delayed-naming structure.**
   Track every actor referred to by structural role before being named. At the moment of naming, verify whether the chapter has accumulated cited sources for the structural role assigned. If the structural role is "load-bearing decision-maker" and the citations support only "approved one of multiple documents in the chain," the implication exceeds the evidence; flag.

3. **Reading two-track time.**
   The "now" track (archive / FOIA / inquest) typically carries hedges naturally. The "then" track (the original event) is the implication risk. Apply the audit to the "then" track paragraphs; the "now" track usually clears on its own.

4. **Reading a chain ladder.**
   Count proper-noun actors per paragraph; count hierarchical verbs per paragraph. If 3+ actors and 2+ hierarchical verbs appear in the same paragraph or successive paragraphs, every authorization link must have its own citation. Two unsupported links in a five-link chain is enough to fail the audit.

5. **Reading anonymous chain language.**
   Search for the patterns enumerated in `scan-implication.py` (`anonymous-chain` finding). Each match is either a missing name (Stephen to find) or a missing hedge (Wayne to add). Both fixes are cheap; the audit failure is also cheap to clear.

## Output format

A skill run builds a Markdown audit memo following the project's audit-output schema. Required fields:

```text
Owner: implication-audit (skill run by <stephen|laura|nancy|wayne>)
Task: Audit <chapter-id-or-case-file-id> for rule-07 implication burden.
Inputs reviewed:
  - book/chapters-v2/<n>-<slug>.md (or other artifact)
  - book/evidence/source-ledger/<n>-<slug>.yml
  - .claude/rules/07-implication-burden.md
Output: implication-audit memo at process/audits/<n>-<slug>-implication-audit.md
Evidence grade: N/A (this is a meta-audit, not a factual claim)
Assumptions: <e.g., chapter is at status in-rewrite or in-review; sidecar is current per rule 09>
Open questions: <unresolved patterns + recommended owner>
Risks: <patterns most likely to introduce defamation surface if not resolved>
Handoff: <next owner — usually Wayne to revise, Stephen to source, or Nancy to clear>
```

Findings table per pattern type:

| Paragraph (line) | Pattern | Snippet | Mitigation present? | Suggested fix | Owner |
|---|---|---|---|---|---|

Summary row: `total findings / findings-with-fix-available / findings-requiring-source-lift / findings-requiring-Nancy-clearance`.

The audit passes when the summary row reads `N / N / 0 / 0` — every finding has a fix the author can apply without escalation.

## Examples

<example>
Context: Wayne has drafted a focalize-then-break version of the chapter-02 opening; the focalizer is the visible scapegoat for beats 1–2, then the frame breaks to the chain in beat 3. Wayne self-runs implication-audit before handing to Stephen.

assistant: "Run implication-audit on book/chapters-v2/02-the-four-goats.md. The focalized passage states the scapegoat 'knew the order would go to him' on L47 with no cite. The chain ladder at L91-L95 names three superiors with 'authorized' verbs across the three lines; only one citation present. Both flag. Fixes: add [CITE:] for the L47 knowledge claim (already in the source ledger as anchor CITE_02_018) or hedge to 'the record shows he was on the list; whether he had been told is not in the contemporaneous notes'. For L91-L95, add two missing per-link citations from the ledger (CITE_02_034, CITE_02_037). No Nancy escalation required; both are author-resolvable."
<commentary>
The skill found two real implication-burden issues, identified that both have fixes available in the existing source ledger, and routed back to Wayne rather than escalating. This is the cheap-fix path — the audit's most common outcome on well-sourced chapters.
</commentary>
</example>

<example>
Context: Stephen runs implication-audit on a chapter that uses delayed-naming structure to reveal a senior official as the chain authorizer at the recognition beat. The chapter cites the senior official's role broadly but not their specific authorization of the disputed decision.

assistant: "Implication-audit flags the recognition beat at L210 as delayed-naming with structural blame — the senior official is named at the load-bearing moment, but cited sources only support their organizational role, not the specific authorization. This is a Laura red-team trigger AND a Nancy defamation surface. Recommend: either find the contemporaneous authorization document (Stephen + source ledger lookup), reframe to 'X's office is in the documented chain of authority; whether X personally signed off remains unresolved' (Wayne hedge), or escalate to xaiolai for treatment-class reconsideration from full-craft-rewrite to defamation-safe-tighten."
<commentary>
This is the high-priority audit failure: the recognition beat carrying implication weight on an under-sourced load-bearing role. The audit escalates to both Laura (red-team) and Nancy (defamation) per the rubric and offers xaiolai a class-reduction path.
</commentary>
</example>
