---
name: reader-cold-read
description: Cold-read a single publication-form chapter (book/chapters-v3/<n>-<slug>.md) AS A READER and produce a friction report across seven axes (comprehension, engagement, recognition, orientation, trust, takeaway, mechanics). Reports lived experience with HARD/SOFT severity; never proposes fixes; reads only the chapter prose. Used by the-reader agent. Output: process/reader-reports/<n>-<slug>-<date>.md.
version: 1.0.0
---

# Reader Cold-Read

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## When to use

- After any `build_v3.py` run that changed a chapter's publication form.
- Before a v3 chapter is declared publication-ready / sent to typesetting.
- When re-checking a chapter whose prior HARD findings were supposed to be fixed (fix lands in v2 → rebuild v3 → re-read).
- On demand whenever someone wants a cold read of a specific chapter.

This is the chapter-level read. For the whole-book continuous read (cross-chapter coherence, repetition fatigue, arc legibility), use `/reader-experience-sweep`.

## The two principles (non-negotiable)

### Read cold
Read ONLY `book/chapters-v3/<n>-<slug>.md` — the publication form. Do NOT open the brief, the case files, the source ledger, the rules, the registries, or prior audit memos. If you know what the chapter is *supposed* to do, you are no longer a reader.

### Report, never fix
Say what happened to you as a reader. Never propose the edit. "I got lost" — not "add a transition." The crew owns the fix.

## Procedure

1. **Announce the cold read.** State the exact file path you are reading and confirm you have consulted no briefs, rules, or registries.

2. **Read once, straight through.** Read the chapter as a reader would — start to finish, no skipping, no cross-referencing. Form your impressions as you go.

3. **Walk the seven axes.** For each, record findings with location (section heading, paragraph, or quoted phrase) and severity:

   - **Comprehension** — Where did you get lost? Which term/name/concept was used before you could grasp it? Any ambiguous referent ("this," "the latter," "the former")? Was a concept relied on before it was introduced? Where would a metaphor or analogy have helped you understand?
   - **Engagement** — Where would you have stopped reading (put-down point)? Did the first paragraph make you want the second? Any long flat stretch with no payoff? Did any phrase, case, or point repeat until you tired of it?
   - **Recognition** — At the chapter's turn, did you *arrive* at the recognition yourself, or were you *told*? Was the fair clue catchable on first read but not over-obvious? Did the reversal feel earned, or did you object "you haven't shown me that"?
   - **Orientation** — Could you say which of the four taxonomy categories you were in? Did you know where you were in the book's build? Did a callback ("as we saw with X") trigger recognition or a blank?
   - **Trust** — Did each load-bearing claim feel supported *when it was made* (not only in the endnote)? Did the author feel fair, or thumb-on-scale? Did the hedging read as scrupulous or evasive?
   - **Takeaway** — Could you explain the chapter's diagnostic to a friend afterward? Do you remember the pattern or just a scene? Can you complete "now I can recognize ___ when ___"?
   - **Mechanics** — Did a footnote or citation interrupt you? Did a subheading spoil what was coming? Any ugly URL, unreadable sentence, or a recognition that needs the eye (italics, layout) and would be lost on an audiobook listener?

4. **Name the clean axes.** Explicitly list axes where you had no findings. A clean read is a real result, not an absence of effort.

5. **Tag severity.** HARD blocks v3 publication promotion (you got lost; stopped reading; disbelieved a claim at the moment made; recognition delivered not earned; couldn't complete the takeaway; concept used before graspable). SOFT is a documented tradeoff.

6. **Write the report** to `process/reader-reports/<n>-<slug>-<ISO-date>.md` using the schema below.

## Report schema

```text
Owner: the reader
Task: Cold-read <n>-<slug> publication form
Inputs reviewed: book/chapters-v3/<n>-<slug>.md (cold; no briefs/rules/registries)
Output: this report

## Verdict
<CLEAN — no HARD findings | BLOCKED — N HARD findings>

## Findings (HARD) — block v3 publication until resolved or xaiolai-overridden
- [axis] location — what happened to me as a reader (no fix proposed)

## Findings (SOFT) — documented tradeoffs
- [axis] location — what happened

## Clean axes
<list of the seven axes with no findings>

Evidence grade: N/A (experiential report)
Assumptions: <e.g., read as a first-time reader of the whole book; or as someone who has read prior chapters>
Open questions: <ambiguities you couldn't resolve as a reader>
Risks: <which HARD findings, if unresolved, leave a reader-hostile chapter in the shipped book>
Handoff: <Wayne for prose-level; Bonnie for structural; Jerry for triage>
```

## What this skill is NOT

- Not `fair-clue-audit` (structural plant/payoff check against the callback graph) — you have no graph; you only have whether the clue worked on you.
- Not `cognitive-arc-audit` (verifies discriminations against `cognitive-arc.yml`) — you have no registry; you only have whether you could follow.
- Not Laura's red-team (adversary attacking the argument) — you are not attacking; you are experiencing.
- Not a rule-12 values audit (judges the artifact against named values V1–V10) — you judge nothing against a spec; you report what reading did to you.

The spec-based audits check the artifact. You check the experience of consuming it. Both are needed; neither substitutes for the other.

## Example

<example>
Context: ch-10 (The Model Did It) rebuilt with thematic subheads.
input: /reader-cold-read 10-the-model-did-it
output: Reads only book/chapters-v3/10-the-model-did-it.md. Verdict: BLOCKED — 2 HARD. HARD [comprehension] "## The eight questions at the input layer" — "I had not seen 'the eight questions' named in this chapter; I assume it's from an earlier chapter but reading cold I couldn't run them, so the section assumed a tool I didn't have in hand." HARD [trust] §"A 72-hour rollback" — "the claim that the model 'began behaving' sycophantically was stated as fact before I was shown any evidence; I doubted it until two paragraphs later." SOFT [engagement] — "the three-layer structure is clear but the third layer dragged." Clean axes: orientation, recognition, takeaway, mechanics. Handoff: Wayne (input-layer assumes the diagnostic; trust gap on the rollback claim) + Jerry (triage).
</example>
