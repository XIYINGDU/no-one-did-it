---
name: pronoun-discipline-audit
description: Audit chapter prose for rule-14 violations — meta-frame language ('this chapter', 'the book', 'the reader', 'readers', 'this section', 'the author'), author-voice 'you', modal-prescriptive forms ('you should', 'we must remember'), evasive-collective forms ('people tend to'). Catches violations the scanner can't see (judgment-level 'we' laundering, passive-voice attribution misses). Cousin of `scan-pronoun-discipline.py`. Used by Wayne during drafting and by Laura during red-team.
version: 1.0.0
---

# Pronoun Discipline Audit

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- Wayne self-runs during drafting as the Test 1–5 sweep (per rule 14) before flipping a chapter to `in-review`.
- Laura runs during red-team as a specific axis of rule-12 V8 (no internal laundering) — pronoun-laundering and meta-frame distance are internal laundering at the linguistic layer.
- jerry-crew-chief runs corpus-wide before `/compile-book` to catch any residual violations that survived the per-chapter sweep.

The `scan-pronoun-discipline.py` hook is the cheap pattern-level pass that runs on every edit. This skill is the deeper read.

## Decision rubric

A chapter passes pronoun-discipline-audit when every sentence satisfies:

1. **No meta-frame.** No "this chapter," "the book," "the reader," "readers," "this section," "this passage," "this paragraph," "the author" — outside cited quotes, frontmatter, intra-crew sections, and table-of-contents.
2. **No author-voice "you".** Outside cited quotes, "you" / "your" / "yours" / "yourself" / "for you" / "if you X" reframed to "we" / "us" / "ourselves" / "for us" / "if we X" or to imperative.
3. **No modal-prescriptive.** "You should / must / ought," "we should remember / never / always" reframed to imperative ("Ask in writing").
4. **No evasive collective.** "People tend to," "many readers will," "anyone can see," "one might think" reframed to specific named group or to "we" or dropped.
5. **"We" passes the substitution test.** Every "we" in author voice, when substituted with "I and the reader together," produces an honest sentence. Otherwise the "we" launders a specific actor that should be named.
6. **Passive voice carries actor attribution.** Per rule 07: when the source names the actor, the chapter names the actor. Passive voice without attribution is refused (or hedged explicitly).

A chapter fails when:

- Any meta-frame violation outside the permitted exemptions.
- Any author-voice "you" outside cited quotes.
- Any modal-prescriptive form outside intentional protocol design.
- Any evasive-collective form ("people tend to") in chapter prose.
- "We" used to launder a specific actor or specific group's choice.
- Passive voice hiding a named actor.

## Conflict handling

1. **"You" inside a verbatim cited quote.**
   *Preserved per rule 06.* The audit reports the pattern as "cited-quote, exempt" and moves on.

2. **"The book" in front-matter or table-of-contents.**
   *Permitted.* Meta-frame is acknowledged when the structure is the explicit subject. Refused inside chapter prose.

3. **"Earlier in this chapter" in a transitional pivot.**
   *Borderline.* Strict version: drop "in this chapter," keep "earlier" ("We saw earlier..." rather than "Earlier in this chapter, we saw..."). Acceptable in transitions but sparingly.

4. **"The reader" in a chapter that engages reader-as-artifact (ch-13 closing material).**
   *Borderline-permitted.* ch-13 has structural reader-as-artifact passages by design; flag for xiaolai confirmation rather than auto-fail.

5. **"We tend to" used as a chapter's diagnostic confession (the chapter performs the misreading and then breaks it).**
   *Permitted* if the chapter follows the confession with immediate disconfirmation. Otherwise refuse — drift toward laundering.

6. **Beat-10 prescriptive sentences originally in "you should" form.**
   *Refuse "should"; reframe to imperative.* The discipline is invariant even where the genre's beat-10 conventions historically used modal-prescriptive forms.

## Escalation conditions

- Escalate to Wayne for prose-level reframes (most violations).
- Escalate to Bonnie when a meta-frame violation reflects structural confusion (the chapter narrating its own architecture because the architecture isn't legible from the prose).
- Escalate to Laura when the audit detects pronoun-laundering — a "we" that disguises a specific failure. This is a rule-12 V8 violation by extension.
- Escalate to Nancy when "you" address drifts into implicating the reader in something that may carry defamation surface (rare).
- Escalate to xaiolai for ch-13 structural reader-address questions; for the closing sentence (xiaolai-authored, has authorial latitude).

## Boundary-case recipes

1. **Auditing a chapter heavy with "this chapter installs" / "the chapter argues" forms.**
   First sweep: count occurrences. If >10 per chapter, structural issue — escalate to Bonnie. If <10, mechanical reframe per the meta-frame table in rule 14.

2. **Auditing beat 10 ("What this might mean for us").**
   Highest concentration of "you" violations historically. Expect 10–30 reframes per chapter pre-migration. Imperative form is the dominant fix.

3. **Auditing a chapter with the "Findings for xaiolai" intra-crew section at the end.**
   Skill auto-exempts the section. Verify the section boundary is correctly identified; the hook's INTRA_CREW_SECTION_RE handles "Findings for xaiolai" / "Annotations and handoff" / "Notes for crew" / "Crew notes" / "Handoff" headers.

4. **Auditing a chapter where source-named actor is being hidden in passive voice.**
   Audit cross-references rule 07. Wayne reframes per rule 07; this audit confirms the actor surfaces in active voice with subject in the right pronoun (named third-person typically).

5. **Auditing a chapter against an updated card titles list (Chicago rule-13 work).**
   Pronoun discipline operates on author voice; cited-quote material (rule 06) and `[CITE: slug]` markers (rule 13 Layer 2) are exempt. Audit focuses on the non-cited prose between the brackets.

## Output format

```text
Owner: pronoun-discipline-audit (skill run by <wayne|laura|joe>)
Task: Audit <chapter-id-or-corpus> against rule 14.
Inputs reviewed:
  - book/chapters-v2/<n>-<slug>.md
  - .claude/rules/14-authorial-stance.md
Output: pronoun-discipline-audit memo at process/audits/<n>-<slug>-pronoun-discipline-audit.md
Evidence grade: N/A
Assumptions: <e.g., cited quotes preserved verbatim per rule 06; intra-crew section auto-exempt>
Open questions: <ambiguous patterns; borderline ch-13 structural cases>
Risks: <chapters with high meta-frame counts that may signal structural confusion>
Handoff: <wayne to reframe | bonnie if structural | laura if V8 violation | xaiolai if ch-13 / boundary>
```

Per-pattern findings table:

| Line | Pattern | Snippet | Required reframe |
|---|---|---|---|

Summary row: `total findings / meta-frame / you / modal-prescriptive / evasive-collective / pronoun-laundering (judgment-level)`.

## Examples

<example>
Context: ch-02 has 47 meta-frame violations after first pass. Wayne self-audits before flipping to in-review.

A: "Pronoun-discipline-audit for ch-02: 47 violations. Meta-frame: 31 (24 'the chapter / this chapter', 5 'the book', 2 'the reader'). You: 12 (9 in beat-10; 3 in scattered protocol sentences). Modal-prescriptive: 3 ('you should' in beat-10; 'we must remember' in beat-9 closing). Evasive-collective: 1 ('many readers'). Pronoun-laundering: 0 (judgment-level pass clean). Recommended sweep: ~1 hour. Pattern: beat-10 carries 12 'you' instances and 3 modal-prescriptive forms — the highest concentration. Imperative reframe across beat-10 closes about half the total finding count."
<commentary>
Real first-pass audit shape: meta-frame dominates, beat-10 carries the "you" concentration. Wayne's sweep is mechanical-bounded with judgment overhead on the V8-laundering check.
</commentary>
</example>
