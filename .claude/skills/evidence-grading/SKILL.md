---
name: evidence-grading
description: Assign A/B/C/D evidence grades to claims by walking source type, corroboration count, and procedural stage through a deterministic decision tree. Used by Stephen for the verification gate and by every researcher for self-grading before handoff.
version: 1.0.0
---

# Evidence Grading

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Decision rubric

Walk every load-bearing claim through this tree in order:

1. **Source type.** What is the strongest source supporting this claim?
   - Court judgment / official inquiry / inspector general report / GAO / UN-ICC finding / statute / executive order / regulator finding / primary document / verbatim transcript / audited technical report → candidate **A**.
   - Major investigative journalism (with named sources or FOIA documents) / reputable NGO investigation / peer-reviewed scholarly article / expert forensic analysis / documentary record with partial access → candidate **B**.
   - Ongoing litigation / allegation / single-source report / unadjudicated claim / active conflict-zone event / cases with conflicting forensic claims → candidate **C**.
   - Viral claim / unsourced anecdote / partisan summary / rumor / emotionally satisfying but unverified story → **D**. Reject the claim; do not pass it to the next gate.

2. **Corroboration count.** How many independent sources support the claim?
   - 3+ independent sources at the candidate grade or better → confirm grade.
   - 2 independent sources → confirm grade only if both are primary/official; otherwise downgrade by one.
   - 1 source → downgrade by one grade unless the single source is a court judgment, formal admission, or audited primary document.

3. **Procedural stage.** Has the claim cleared the adjudicatory or institutional process that governs this claim type?
   - Final judgment / formal admission / regulator finding → confirm grade.
   - Charges filed but no judgment / DPA / settlement without admission → cap at **B**.
   - Allegation / preliminary examination / pre-charge investigation → cap at **C** until the stage advances.

4. **Interested-source check.** Is the strongest source financially or ideologically interested in the outcome?
   - Yes → downgrade by one grade unless independently corroborated by a non-interested source.
   - Document the interest in the source ledger row.

5. **Live-event check.** Is this an active event with the record still in flux?
   - Yes → cap at **C** regardless of source type. Flag the case as "live" in the ledger.

The final grade is the *lowest* grade emitted by any step above.

## Conflict handling

1. Two A-sources disagree on a factual claim:
   Record both in the source ledger with provenance, downgrade the claim to **B**, and write a disputed-claim register entry. Do not silently pick one.
2. Source is interested but the only available source:
   Cap at **C** with an explicit "single interested source" note. Cannot anchor a chapter-level claim alone.
3. Procedural stage advances mid-sprint:
   Re-run the grading; if grade rises, update every artifact that cited the old grade.
4. Disagreement between researcher's proposed grade and Stephen's verdict:
   Stephen's verdict stands. Researcher logs the original proposal in the disputed-claim register for pattern-tracking across cases.

## Escalation conditions

- Escalate to Alan (expert reviewer with the matching domain frame) when:
  - the procedural stage requires domain knowledge to interpret (e.g., ICC "preliminary examination" vs "investigation");
  - the source-type evaluation requires field-specific authority (system card analysis, accident-investigation methodology).
- Escalate to Nancy when the wording around an unconfirmed grade carries defamation risk.
- Escalate to Jerry when a chapter-anchor claim cannot reach **A** or **B** after one revision cycle and the chapter cannot proceed.

## Boundary-case recipes

1. **One A-source, one C-source, no B.** Grade is **B** (the higher source pulls the average up one step), with the C-source noted as "weak corroboration only".
2. **Two interested sources from opposing parties.** Each is a primary source for the OTHER side's accusation. Grade as **B** with both interests documented; the claim cannot anchor a chapter without an independent third source.
3. **Single primary document, never publicly released, leaked.** Treat as **C** until at least one institutional source (regulator, court, official inquiry) confirms authenticity. Flag as "authenticity-pending".
4. **Public admission inside a non-prosecutorial settlement (e.g., DPA with admitted facts).** The admitted facts are **A** for the specific points admitted; surrounding context stays **B/C** per its own grading.

## Output format

When emitting a grade, include all five tree results so Stephen can audit:

```text
Claim:
Strongest source:
Source type: A | B | C | D
Corroboration count: <n> independent sources
Procedural stage:
Interested-source: yes | no
Live event: yes | no
Grade: A | B | C | D
Rationale: <one line>
Handoff:
```

## Rules

- The chapter rule (per `.claude/rules/02-evidence-grades.md`): a chapter-level claim cannot rest only on **C**-grade evidence unless the chapter is explicitly about uncertainty or contested record control.
- A claim's grade can only be raised by adding sources or by an advancing procedural stage, never by editorial judgment.
- Every grade change must update the source ledger row and the disputed-claim register if applicable.

<example>
Context: Selina submits a Bucha civilian-harm case. Source ledger lists OHCHR report (A), ICC arrest warrant docket (A), Ukrainian Prosecutor General registry (A), Reuters wire (B), AP forensic team (B), Russian MoD statement (denied).
input: claim="Russian forces killed N civilians in Bucha in March 2022"
output: Strongest source: OHCHR report (A). Corroboration count: 3 independent A-sources for OHCHR-corroborated counts. Procedural stage: ICC arrest warrants issued (B-cap stage). Interested-source: no for OHCHR; yes for Russian MoD (excluded). Live event: yes — overall conflict ongoing but this incident has cleared institutional verification. Grade: A for OHCHR-corroborated counts, C for any single-source attributions of specific perpetrators. Handoff to Alan (IHL frame) for procedural-stage interpretation before chapter use.
</example>

<example>
Context: A draft cites "Boeing executives knew about MCAS instability before the Lion Air crash." Only source is a Seattle Times investigative piece quoting FOIA'd emails plus the 2021 DOJ deferred prosecution agreement.
input: claim="Boeing executives knew about MCAS instability before the Lion Air crash"
output: Strongest source: DOJ 2021 DPA (A — formal admission). Corroboration count: 2 (DPA + Seattle Times). Procedural stage: DPA stage caps at B for non-admitted facts. Interested-source: no. Live event: no. Grade: **B**. The DPA admitted Boeing misled the FAA but did not specifically admit pre-crash internal knowledge by named executives. Rationale: the DPA's admitted facts support "Boeing misled the FAA"; "executives knew" requires the Seattle Times email evidence to carry weight that the DPA does not vouch for. Handoff to Nancy for safer wording: "Boeing has admitted to misleading the FAA per the 2021 DPA; FOIA'd emails reported by the Seattle Times suggest internal knowledge of MCAS issues before the first crash."
</example>
