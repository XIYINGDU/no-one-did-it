---
name: scene-construction
description: Build narrative scenes from approved case files following the project's chapter rhythm. Covers opening-hook patterns, hidden-architecture reveal mechanics, recognition-reversal beats, and anti-laundering-rule endings. Used by Wayne to turn a chapter brief into prose; integrates audio-cadence considerations so audiobook narration works without rework.
version: 1.0.0
---

# Scene Construction

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## Decision rubric

A scene works when it satisfies ALL of:

- **Concrete particularity.** Names a specific person, place, document, or moment. No "in the 1970s a company did" — must be "in October 1973 the chairman of X signed the memo".
- **Hidden-architecture preview.** The opening pushes toward the public story while planting the fair clue that the chapter will later use to reverse it. The fair clue is documented evidence, not authorial omniscience.
- **No invented interior.** No thoughts, motives, intentions, or dialogue that aren't on the public record. If a primary source quotes a thought, the scene quotes the source.
- **Voice match.** Matches the project voice per `.claude/rules/04-style-guide.md`: precise, severe, readable, non-flattering, nonpartisan, evidence-driven.
- **Audio-readable.** A narrator can read it cold without choking. No sentence longer than ~30 spoken words. No dense clause stacks at moral turning points.

A scene fails when:
- It opens with a thesis statement or a generalization.
- It invents a quote, an expression, a sigh, an exchange of glances.
- It uses "must have", "would have", "presumably" for mental states.
- A reader has to re-read to parse it aloud.

## Conflict handling

1. **Brief says use case A as opening but case A has C-grade sourcing.**
   Refuse to open with C-grade. Either swap to a B-grade alternative scene or wait for Stephen to lift the source. The opening is the chapter's promise; weak evidence at the opening discredits the whole.
2. **The compelling scene exists only in a single secondary source.**
   Use the scene; cite the secondary source explicitly inside the scene's prose ("according to the Seattle Times's reconstruction") rather than narrating as omniscient. Add `[EVIDENCE NEEDED: corroboration for X detail]` inline for anything load-bearing not in the primary record.
3. **Required hedging language makes the prose dead.**
   The hedge stays; the prose rhythm gets reworked around it. Better to be alive AND legally accurate than alive at the expense of evidence. If the rhythm absolutely cannot survive the hedge, route to Stephen for a re-grade or to Jerry for a structural rewrite.
4. **The anti-laundering rule at the end sounds like a slogan.**
   Replace with a rule of action: name what a competent reader could DO with the chapter's lesson, not what they should believe. Slogans signal motivated reasoning; protocols invite test.

## Escalation conditions

- Escalate to Stephen when scene draft contains any claim graded below B.
- Escalate to Nancy when a named living person is given attributed conduct, mental state, or motive.
- Escalate to Laura when the scene's reveal feels too clean — Laura tests whether the hidden architecture is actually documented or whether it leans on narrative convenience.
- Escalate to Bonnie when scene order or chapter rhythm requires restructuring beyond the brief.

## Boundary-case recipes

1. **Opening on a document (preferred default).**
   First sentence names the document, its date, and one piece of its specific text. Second sentence places the document in the public chain. The third introduces the actor whose role the chapter will reframe. Example skeleton: "On 17 October 1973, the chairman of X signed a memo. The memo authorized Y. Three weeks later, a junior clerk was named the cause of the disaster that followed."
2. **Opening on a person already at the consequence.**
   Start at the moment the cost-bearer faces the harm. Move from harm to attribution to chain. Used for cost-bearing-goat chapters. Avoid pathos accumulation — name the specific harm in one sentence and move.
3. **Reveal beat without italics or asides.**
   The reveal sentence stands alone as a short paragraph, no italics, no "but in fact". Trust the contrast.
4. **Anti-laundering rule as a protocol.**
   Format: "When you see X, ask Y." Not: "We must remember Z." A protocol is portable; a sentiment is decorative.
5. **Audio-cadence repair pass.**
   After drafting, read every paragraph aloud once. Flag any sentence over ~30 words; either split it or move its tail to a new sentence. Flag any sentence with three or more nested clauses; flatten one clause to its own sentence.

## Output format

A scene is delivered as a Markdown section ready for the chapter's `## Accusation scene` or equivalent rhythm slot. Inline annotations use these markers:

```text
[CITE: <ref>]                   — citation marker for fact-check pass
[EVIDENCE NEEDED: <claim>]      — claim that needs sourcing before status: ready
[HEDGE: <stronger form>]        — note for legal pre-clearance
[CADENCE: <issue>]              — audio-cadence concern for revision
```

Annotations stay in the draft through `status: draft`; all must be resolved before `status: ready`.

<example>
Context: Wayne is drafting the opening scene of the Boeing 737 MAX chapter from Bonnie's approved brief.
input: brief specifies Boeing MAX as anchor, partial scapegoat (Lion Air + Ethiopian crashes, pilots named).
output: A 4-paragraph scene opens on the specific date the FAA issued the type certification, names the MCAS software in one specific line of the DPA's admitted facts, then introduces the Lion Air captain by name as the cause publicly named after the first crash. Every claim carries a [CITE] marker. No invented dialogue. Ends on the fair clue — the line from a Boeing internal email (FOIA, Seattle Times) that the chapter will return to in §3 when it reverses the captain-as-cause framing.
</example>

<example>
Context: A draft scene contains the sentence "The CEO must have known about MCAS instability."
input: scene draft with overclaim
output: Refuses to ship the sentence. Replaces with: "Boeing's 2021 DPA admits the company misled the FAA about MCAS [CITE: DPA §III.A]. Internal emails reported by the Seattle Times show employees discussing MCAS instability before the Lion Air crash [CITE: Seattle Times series, 2019]. Which Boeing executives saw which emails when remains contested in pending litigation [HEDGE: Nancy review]." Handoff: Stephen (verify Seattle Times citation reaches B) → Nancy (defamation review on the pending-litigation hedge).
</example>
