---
name: defamation-wording
description: Convert allegation-stage facts into legally defensible chapter wording. Maps every claim about a living person or company to the correct procedural stage (alleged / reported / charged / admitted / settled / found-liable / convicted) and proposes safer phrasings tied to the documented public record. Used by Nancy for legal review and by Wayne for self-policing during drafting.
version: 1.0.0
---

# Defamation Wording

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Procedural-stage wording table

The defamation risk of a sentence about a living person or company is determined by whether the wording is consistent with the procedural status of the underlying claim. Match wording to stage; never reach above the stage's ceiling.

| Procedural stage | Allowed verbs | Forbidden verbs | Attribution pattern |
|---|---|---|---|
| Reported / alleged (journalism, no charge) | "is alleged to", "is reported to", "according to <named source>", "X says Y did Z" | "guilty", "lied", "deliberately", "knew", "is responsible for" (without qualifier) | Always name the source. Never present as fact. |
| Under investigation / preliminary examination | "is under investigation by X for", "X is examining whether Y" | charges-implying verbs ("indicted", "charged"); guilt-implying verbs | Name the investigating body + the date of the status. |
| Charges filed / indictment / preliminary ICC examination | "was charged by X with", "was indicted on", "faces charges of" | guilt verbs ("is guilty", "did", "committed"); "war crime" before that stage advances | Distinguish indictment from conviction in every sentence. |
| Settled without admission / DPA / consent decree | "settled the matter with X for $N without admitting wrongdoing", "entered into a DPA in which X admitted <specific admitted facts only>" | "admitted guilt"; "was found"; any guilt verb beyond what is literally inside the settlement document | Quote the admitted facts verbatim; do not paraphrase into broader admission. |
| Found liable (civil) | "was found civilly liable by <court> for", "a jury found that X" | criminal-guilt verbs ("convicted", "is a criminal") | Distinguish civil from criminal in the sentence. |
| Convicted (criminal, including plea) | "was convicted of", "pleaded guilty to", "was sentenced to" | hedging language that suggests open question ("alleged to have", "is reported to have") | Cite the court + date of judgment. |
| Conviction overturned / vacated / pardoned | "was convicted in <year> and the conviction was vacated by <court> in <year>", "was pardoned by X in <year>" | language that implies the original conviction stands | Always include the reversal. |

## Decision rubric

For every sentence that names a living person or company AND attributes conduct, harm, mental state, or motive:

1. **Identify the strongest procedural-stage source.** If none reaches charges-filed or higher, you are in journalism-allegation territory.
2. **Determine what the source actually says.** Quote the operative verb (e.g., the DOJ press release says "misled the FAA" — the chapter can say "misled" because the source uses that verb; it cannot escalate to "deceived" or "knowingly lied").
3. **Match the wording to the stage.** Use only verbs in the row's "allowed" column. Reject anything in "forbidden".
4. **Add the attribution.** Every claim names its source on the same line or in the same paragraph. No floating accusations.
5. **Distinguish person from entity.** A corporation can "violate", "settle", "be found liable" without implicating any named individual. A named individual needs their own per-person procedural status.
6. **Live-event check.** If the underlying event is still developing, add a date stamp: "as of <date>, X is under investigation". Flag the chapter for re-verification before publication.

## Conflict handling

1. **The chapter argument needs the stronger verb but the procedural stage doesn't support it:**
   Rewrite the claim to attribute through the available verb. If the argument collapses without the stronger verb, the claim is not yet ready for the chapter. Handoff to Stephen for a re-grade after sourcing, or to Bonnie for a structural rewrite that does not require the stronger claim.
2. **Two sources disagree on procedural stage (e.g., a press release says "settled" but a regulator filing says "consent decree"):**
   Use the narrower, more conservative formulation. Cite both.
3. **The named person disputes the public record:**
   Their dispute is recorded; the public record stands unless they have produced an authoritative correction. Do not soften the chapter just because the subject objects.
4. **A quote from a primary source uses a forbidden verb:**
   The quote may stand verbatim inside quotation marks with attribution. The chapter's surrounding prose must not adopt the verb as its own narration.

## Escalation conditions

- Escalate to Stephen when the underlying procedural status is unclear or contested — wording cannot be decided until the status is fixed.
- Escalate to Jerry when removing the unsupported claim would gut the chapter — this is a structural decision, not a wording fix.
- Escalate to a real attorney when the proposed wording involves: an active US/UK defamation suit against a publisher; a non-US jurisdiction with stricter libel law; a per se defamation category (criminal accusation, professional misconduct accusation, loathsome-disease accusation); or any named-individual claim where the chapter cannot reach evidence grade A or B.

## Boundary-case recipes

1. **Named executive accused in a press piece, no charges.**
   Allowed: "The Wall Street Journal reported that X said Y in an internal email obtained by the paper." Forbidden: "X knew Y." Use journalism-allegation phrasing only.
2. **DPA with specific admitted facts about a corporation but not about named individuals.**
   Allowed: "Boeing admitted in its 2021 DPA that it misled the FAA about MCAS." Forbidden: "Boeing executives knew." Distinguish corporate admission from personal knowledge.
3. **A subject's quote that itself defames a third party.**
   Quote the subject verbatim with attribution: "X told Reuters that Y 'lied repeatedly' about the matter." The chapter is now reporting that X said this; it is not adopting X's claim. Add Y's response if on record.
4. **Conviction later overturned.**
   Allowed: "X was convicted in 2018 of fraud; the conviction was vacated in 2022 by the Ninth Circuit." Forbidden: "X is a convicted fraudster." Including the reversal is mandatory, not optional.
5. **The chapter wants to call something a "scapegoat".**
   The word "scapegoat" carries an evaluative claim that the blame is unjust. It is acceptable as a category label (per `.claude/rules/01-case-taxonomy.md`) when the documented chain evidence supports the classification (run the `taxonomy-classification` skill first). It is not acceptable as a rhetorical flourish without that classification.

## Output format

```text
Subject (named person/company):
Claim being made:
Strongest procedural-stage source:
Procedural stage:
Source's operative verb:
Proposed safer wording:
Attribution pattern:
Open question:
Handoff:
```

<example>
Context: A draft contains the sentence "Boeing executives knew about MCAS instability before the Lion Air crash." Stephen has graded the underlying claim B (DPA + Seattle Times FOIA).
input: claim="Boeing executives knew about MCAS instability before the Lion Air crash"
output: Subject: Boeing (corporation) + unnamed executives. Strongest source: 2021 DPA. Procedural stage: settlement-with-admission (B-cap). The DPA admitted Boeing misled the FAA; it did not admit specific pre-crash knowledge by named executives. Proposed safer wording: "Boeing has admitted, in its 2021 DPA, to misleading the FAA about MCAS. FOIA'd internal emails reported by the Seattle Times indicate that Boeing employees expressed concern about MCAS instability before the Lion Air crash." Attribution: DPA + Seattle Times on same line as the clause making the attribution claim. Open question: which specific named individuals' knowledge is documented vs. inferred. Handoff: Wayne (revise paragraph) → Stephen (verify Seattle Times sourcing reaches B).
</example>

<example>
Context: A chapter calls a named federal judge's recent injunction "an illegal overreach of authority."
input: claim="Judge X's injunction is an illegal overreach of authority"
output: Subject: Judge X. Stage: a sitting federal judge's published order is the strongest source; until an appellate court reverses, the order is law within its jurisdiction. "Illegal" is not supported. Proposed safer wording: "Judge X's injunction, issued <date>, has been appealed by <party> on the grounds that <stated grounds>; as of <date>, the appeal is pending in the <circuit>." Attribution: docket citation. Open question: what specifically the chapter is trying to claim — that the injunction is wrong, that it is reversible, or that the judge acted in bad faith? Each requires a different sentence. Handoff: Loki (provide docket details) → Alan (admin-law frame) → Wayne (rewrite paragraph).
</example>
