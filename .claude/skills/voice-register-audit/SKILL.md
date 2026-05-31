---
name: voice-register-audit
description: Audit a chapter for voice-register distribution across three registers — R-primary (primary document quoted at full force), R-frame (newsroom-style paraphrase), R-analytic (the book's analytical voice). Verifies paragraph-level register tags exist, distribution falls within tunable thresholds, and register transitions are marked rather than silent. Used by Wayne and Stephen on `structural-polish` and `full-craft-rewrite` chapters.
version: 1.0.0
---

# Voice Register Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- During chapter rewrite under treatment class `structural-polish` or `full-craft-rewrite`.
- Whenever Wayne uses the Bucket 1 craft move "voice braid" from `dev-docs/fiction-craft-rewrite-analysis.md`.
- During pre-promotion audit to verify the chapter does not read as monolithic.

The audit does not apply to `prose-polish` or `defamation-safe-tighten` chapters — those classes do not commit to register braid.

## The three registers

| Register | Tag | What it sounds like | Source of authority |
|---|---|---|---|
| **R-primary** | `<!-- voice: R-primary -->` | Quoted document text at full force; the source's words, formatting preserved where useful; verbatim under rule 06. | The cited document itself. |
| **R-frame** | `<!-- voice: R-frame -->` | Reportorial paraphrase; attributes statements to sources ("the inspector found", "the court ruled"); third-person, journalistic. | The reporter / inquiry / court whose finding is being paraphrased. |
| **R-analytic** | `<!-- voice: R-analytic -->` | The book's diagnostic voice; names the laundering pattern, applies the taxonomy, runs the responsibility-chain map. | The author's analytic frame, anchored in the chapter's responsibility-chain map and the project's taxonomy. |

Tagging convention: each paragraph carries a leading HTML comment naming its register. Untagged paragraphs default to `R-analytic` (the book's home register), but a chapter using voice braid must tag the non-default paragraphs explicitly.

## Decision rubric

A chapter passes voice-register-audit when:

1. **Tagging coverage.** At least 90% of substantive paragraphs (excluding section headings, list items, blockquote sources) carry a register tag. The 10% slack permits short transitional paragraphs.
2. **Distribution within thresholds.** No register is below 10% or above 70% of substantive paragraphs. (Thresholds are tunable from pilot data per rule 09; current defaults are the starting point.)
3. **Transitions marked.** Adjacent paragraphs in different registers are separated by an explicit transition cue — either a section break, an explicit attribution ("The inspector general's report states:" before an R-primary block), or a marked shift ("Stepping back from the inspector's account:" before an R-analytic block).
4. **R-primary contents pass rule 06.** Verbatim quotation discipline holds inside every R-primary paragraph.
5. **R-frame contents pass rule 05.** Newsroom-frame paragraphs use rule-05-compatible attribution verbs and hedging.
6. **R-analytic contents pass rule 12 V8.** The analytic voice does not commit internal laundering — it names structure rather than emoting at structure.

A chapter fails when:

- Tagging coverage is below the 90% threshold (the chapter is not actually braided; it is monolithic with sporadic flags).
- Any register exceeds 70% (monolithic by collapse) or falls below 10% (declared braid that does not happen).
- Register transitions appear silently between paragraphs — the reader does not feel the shift, so the braid does not pay its narrative cost.
- An R-primary paragraph contains paraphrase (rule-06 violation).
- An R-analytic paragraph contains emotional reasoning that exceeds the evidence (rule-12 V8 violation).

## Conflict handling

1. **Chapter contains long verbatim passage that pushes R-primary above 70%.**
   Re-split the passage into shorter R-primary blocks interleaved with R-frame explanatory glue. If the source is genuinely so important it must dominate, document the exception in the audit output and route to xaiolai for confirmation that monolithic-R-primary is the intended voice choice.

2. **Chapter has no R-primary at all.**
   Permitted only when the chapter is genuinely about absence (no primary documents survive, or all are sealed). The chapter must explicitly say so. Otherwise route to Stephen to add primary-document quotes from the source ledger.

3. **R-frame paragraph attributes a finding to a source whose evidence grade is C.**
   Pass on register-audit terms, but flag for Stephen (rule 02 evidence-grade audit). Register-audit does not grade evidence; it grades distribution.

4. **R-analytic paragraph contains the chapter's recognition beat (the hammer line).**
   Pass — recognition is the analytical voice's defining moment. The audit verifies the recognition beat is in R-analytic, not R-frame (which would weaken it) and not R-primary (which would attribute the recognition to the source).

5. **A paragraph carries two register tags.**
   Hard fail; registers do not blend at the paragraph level. Either split the paragraph or pick one register. Mixed-register paragraphs were the failure mode that motivated tagging in the first place.

## Escalation conditions

- Escalate to Wayne when distribution thresholds fail and the fix is paragraph rewriting.
- Escalate to Bonnie when distribution thresholds fail and the fix is scene reorder or new scene insertion.
- Escalate to Stephen when R-primary content fails rule 06 (quote integrity) or when R-frame content fails rule 02 (evidence grade).
- Escalate to Laura when R-analytic content fails rule 12 V8.
- Escalate to xaiolai when the chapter intentionally chooses monolithic register (e.g., entirely R-analytic by design) and the audit's distribution requirement should be waived for this chapter — waiver requires written rationale in the audit memo.

## Boundary-case recipes

1. **Auditing a chapter with three short scenes in three different registers.**
   Per-scene register distribution can be 100% one register; the chapter-level distribution still has to satisfy the thresholds. If the three scenes are roughly equal length, distribution will be ~33/33/33 and the audit passes trivially.

2. **Auditing the chapter opening.**
   The opening scene's register choice signals the chapter's voice intent. R-primary opening (open on the document) is the project's preferred default per `scene-construction/SKILL.md`. R-frame opening (open on the inquiry) and R-analytic opening (open on the pattern) are permitted but Wayne should document why in the chapter brief.

3. **Auditing the chapter ending.**
   Beat 10 ("what this might mean for us") must be R-analytic. Beat 8 ("anti-laundering rule") must be R-analytic. If either ends in R-primary or R-frame, the chapter has lost its analytical voice at the load-bearing closing moments — flag.

4. **Auditing a chapter whose voice braid was added by polish-only revision.**
   Best-effort audit; the chapter's underlying structure may not support braid (e.g., no R-primary material in the source ledger). Recommend reclassification to `prose-polish` if the underlying support is absent.

5. **Auditing a chapter that uses register-shifting within a paragraph for stylistic effect.**
   Hard reject. The audit's premise is paragraph-level register tagging; intra-paragraph shifts are noise. Either split the paragraph or accept the chapter is not voice-braided.

## Output format

```text
Owner: voice-register-audit (skill run by <wayne|stephen|joe>)
Task: Audit voice-register distribution of book/chapters-v2/<n>-<slug>.md
Inputs reviewed:
  - book/chapters-v2/<n>-<slug>.md
  - book/chapters-v2/<n>-<slug>.contract.yml (for declared register intent if present)
  - .claude/rules/06-quote-integrity.md
  - .claude/rules/12-reader-experience-values.md
Output: voice-register-audit memo at process/audits/<n>-<slug>-voice-register-audit.md
Evidence grade: N/A
Assumptions: <e.g., paragraph counts exclude headings and list items per the rubric>
Open questions: <register-tagging gaps + recommendations>
Risks: <distribution drift if revision continues>
Handoff: <wayne to revise / bonnie to restructure / stephen for quote-integrity / nancy if R-frame attribution touches live actors>
```

Distribution summary:

| Register | Tagged paragraphs | Percentage | Threshold (10%-70%) |
|---|---|---|---|

Per-register findings:

| Tag location (line) | Issue | Required action |
|---|---|---|

Recognition-beat audit:

| Recognition beat (line) | Register | Pass? |
|---|---|---|

## Examples

<example>
Context: Wayne added voice braid to ch-07 under `structural-polish`. He runs `/voice-register-audit` to verify the braid worked.

A: "Voice-register-audit for ch-07. Tagging coverage: 94% (3 untagged transitional paragraphs, within slack). Distribution: R-primary 24%, R-frame 31%, R-analytic 45%. All within thresholds. Transitions: 14 register-shifts identified; 13 marked, 1 silent at L290 (R-primary to R-analytic). Fix: add 'Set against the inspector's words:' before L290. Recognition beat at L580 in R-analytic — correct. Rule-06 spot-check on R-primary blocks: 8 verbatim, 0 paraphrase issues. Overall: conditional pass pending L290 transition marker."
<commentary>
The skill identifies one minor issue (a silent register transition), recommends a one-line fix, and verifies the structural intent. Normal "conditional pass" output.
</commentary>
</example>
