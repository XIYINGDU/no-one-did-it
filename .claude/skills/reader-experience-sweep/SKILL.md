---
name: reader-experience-sweep
description: Cold-read the whole assembled manuscript (dist/manuscript-v3.md) in one continuous sitting AS A READER and report cross-chapter experience — repetition fatigue, arc legibility, callback recognition, cumulative-trust drift, taxonomy coherence across chapters. The book-level companion to reader-cold-read (which is per-chapter). Reports lived experience with HARD/SOFT severity; never fixes; reads only the manuscript. Used by the-reader agent. Output: process/reader-reports/sweep-<date>.md.
version: 1.0.0
---

# Reader Experience Sweep

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After all chapters have passed `/reader-cold-read` with zero HARD findings.
- Before xaiolai's final Gate B read.
- After any change that touches multiple chapters (a sweep-level rebuild, a cross-chapter motif or callback edit).

This is the whole-book read. The friction it finds is invisible at chapter level — it only appears when you read the book the way a reader does: in sequence, in fewer sittings, holding the cumulative argument in your head.

## The two principles (non-negotiable)

Same as `/reader-cold-read`: **read cold** (only `dist/manuscript-v3.md`; no briefs, rules, registries) and **report, never fix**.

## Procedure

1. **Announce the cold read.** State that you are reading the assembled manuscript only, no briefs/rules/registries.

2. **Read in sequence.** Read front-to-back as a reader who is building a cumulative understanding. You are allowed to remember earlier chapters (a real reader does); you are NOT allowed to consult the registries to check whether your memory is "correct" — your memory IS the data.

3. **Walk the five cross-chapter axes:**

   - **Arc legibility** — Does the book feel like it is *building*, or like a list of cases? At the end, can you state the through-line? Did any chapter feel out of place in the sequence?
   - **Repetition fatigue** — Which phrases, framings, or cases recurred until you tired of them? (The book caps "responsibility laundering" at once per chapter — but what about the *uncapped* repetitions: the eight questions, "the chain climbs," the four categories, recurring cases like MH17 / Therac-25 / Boeing?) Did a recurrence feel like a useful callback or like the author repeating themselves?
   - **Callback recognition** — When a chapter said "as we saw with X," did you actually recognize X, or had you forgotten it? Did any callback assume you remembered a detail you didn't?
   - **Cumulative trust** — Across the whole book, did the author stay fair, or did a pattern of selection emerge that made you suspect a thumb on the scale (e.g., every villain from one side; every sympathetic figure from another)? Did trust build or erode chapter over chapter?
   - **Cumulative taxonomy coherence** — Were the four categories applied consistently across chapters, or did the same kind of case get sorted differently in different chapters in a way that confused you?

4. **Also note book-level engagement:** Where, across the whole arc, would a reader put the book down and not pick it up again? Which chapter was the slog? Which was the peak?

5. **Tag severity.** HARD (blocks the book's publication-ready promotion): the arc was illegible (you couldn't state the through-line); a pattern of unfairness eroded your trust in the author; a load-bearing callback failed across the book; the taxonomy felt incoherent across chapters. SOFT: mild fatigue, a slow chapter, a callback you had to think about.

6. **Write the report** to `process/reader-reports/sweep-<ISO-date>.md`.

## Report schema

```text
Owner: the reader
Task: Cold-read the assembled manuscript end-to-end
Inputs reviewed: dist/manuscript-v3.md (cold; no briefs/rules/registries)
Output: this report

## Verdict
<CLEAN | BLOCKED — N HARD findings>

## The through-line, in my words
<one paragraph: what the book argued, as a reader who just finished it. If you can't write this, that is itself a HARD finding on arc legibility.>

## Findings (HARD)
- [axis] location/chapter-span — what happened to me across the book

## Findings (SOFT)
- [axis] location — what happened

## Book-level engagement map
- Peak chapter(s):
- Slog chapter(s):
- Put-down risk points:

## Clean axes
<cross-chapter axes with no findings>

Evidence grade: N/A (experiential report)
Assumptions: <read in N sittings; read as first encounter with the whole book>
Open questions:
Risks: <which HARD findings leave a reader-hostile book if unresolved>
Handoff: <Bonnie for arc/structure; Wayne for prose-level repetition; Jerry for triage>
```

## Example

<example>
Context: all 13 chapters cleared /reader-cold-read; sweep before Gate B.
input: /reader-experience-sweep
output: Reads only dist/manuscript-v3.md. Through-line written cleanly (arc legible). Verdict: BLOCKED — 1 HARD. HARD [repetition fatigue] chs 7–12 — "the eight questions were walked in full at least four more times after chapter 3 installed them; by chapter 9 I was skimming the walk because I already knew the moves." SOFT [callback] ch-11 — "'as we saw with the Post Office' assumed I remembered the five-role conflation precisely; I remembered the gist, not the five." Engagement: peak ch-2 and ch-10; slog ch-8 (densest); put-down risk at the ch-6 administrative-law middle. Handoff: Bonnie (decide whether the eight-question walk should compress after its third full appearance) + Jerry (triage).
</example>
