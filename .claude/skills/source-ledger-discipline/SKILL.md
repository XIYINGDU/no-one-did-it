---
name: source-ledger-discipline
description: Build source ledgers, evidence grades, quote logs, and disputed-claim registers.
version: 1.0.0
---

# Source Ledger Discipline

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
- Builds source ledger rows with complete required fields and one claim-source link per row.
- Assigns evidence grade using source type and corroboration quality.
- Flags disputed claims and preserves a separate unusable-claim list.
- Uses precise dispute status language and clear handoff owner.

Weak output:
- Bundles multiple claims into one row with unclear support.
- Assigns evidence grade without rationale or corroboration notes.
- Hides financial-interest or live-litigation conflicts.
- Mixes verified claims with disputed claims in one status.

## Conflict handling

1. Two sources conflict on the same claim:
Keep separate rows, grade independently, and flag claim disputed until corroboration resolves.
2. Two case classifications are implied by different source clusters:
Do not classify in ledger rows; handoff to case-file owner with graded conflict summary.
3. Two reviewer findings conflict on source reliability:
Prefer the finding tied to explicit source-method reasoning; unresolved disputes handoff to Stephen for decision log.

## Escalation conditions

- Proceed when core chapter claims have ledger support at evidence grade A or B with transparent gaps.
- Handoff to Delon when primary source access is blocked.
- Handoff to Stephen when dispute status blocks case inclusion.
- Handoff to Nancy when quote permission or legal exposure is ambiguous.

## Boundary-case recipes

1. Leaked document without provenance:
Record as provisional source, grade C or lower, and require independent corroboration before chapter use.
2. Official report later corrected:
Keep both versions in ledger, flag superseded claims, and revise downstream claim mappings.
3. Single-source numerical estimate:
Record estimate with uncertainty field, gate deterministic phrasing in chapter brief, and handoff for corroboration search.

Every source entry must include:

```text
Source title:
Source type:
URL or archive path:
Publication date:
Author/issuer:
Claim supported:
Evidence grade:
Quote limit / permission note:
Dispute status:
Reliability notes:
Cases affected:
```

Requirements:
- Prefer primary documents for controversial claims.
- Never let a secondary source carry a claim that a primary source can verify.
- Mark live litigation, active conflict, and unadjudicated allegations clearly.
- Maintain a separate list of claims that cannot yet be used.

<example>
Context: Selina (war/statecraft researcher) is starting the source ledger for a Ukraine-front case.
input: "Bucha, March 2022"
output: Returns a source-ledger row set — primary (OHCHR report, ICC arrest warrant docket, Ukrainian Prosecutor General registry); secondary (Reuters wire, AP forensic team); contested (Russian MoD statements; logged with status="denied; not corroborated by independent forensic evidence"); evidence grade A for OHCHR-corroborated counts, C for single-source attributions; handoff to Stephen.
</example>

<example>
Context: Boundary case: a source is financially interested (paid by a party to the case).
output: Records the financial interest in the ledger row, downgrades the source by one grade unless an independent corroboration is paired with it, and flags the row for Stephen's review.
</example>
