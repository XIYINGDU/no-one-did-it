---
description: "Implication burden rule: narrative implication of mental state, motive, knowledge, causation, or chain responsibility carries the same evidence burden as a verb-level claim. Catches structural overclaim from sentence sequence, focalization, juxtaposition, and naming order. Sibling to rule 05; flagged by scan-implication.py."
---

**Narrative implication of mental state, motive, knowledge, causation, or chain responsibility carries the same evidence burden as a verb-level claim; implication-by-structure is not a citation loophole.**

# Implication Burden Rule

**Scope:** binds every prose artifact in `book/evidence/case-files/`, `book/chapters-v2/`, `process/review-memos/`, and `book/proposals/`. Sibling to rule `05-overclaim-language.md`. Rule 05 catches *verb-level* overclaim (`knew`, `lied`, `proves`, `deliberately`). Rule 07 catches *structural* overclaim — when sentence sequence, paragraph adjacency, focalization, juxtaposition, or naming order implies a mental state, motive, knowledge, causation, or chain responsibility the cited evidence does not support.

The book argues that responsibility laundering hides chains behind procedural surfaces. Craft moves can do the inverse: surface a chain the record does not document. Both fail the book's discipline. Rule 07 is the catch.

## Implication patterns that require citation or hedging

Each pattern below is flagged as a candidate overreach. A flagged passage clears if it cites within the adjacent paragraph (`[CITE:]`), hedges with a rule-05-compatible qualifier, or is plainly inside a verbatim quotation.

| Pattern | What it implies | What the chapter must show |
|---|---|---|
| **Focalization-then-fact.** A scene presents events through one actor's perceptual frame, then states a fact the actor would have had to know. | That actor knew. | Either the source documenting their knowledge, or a hedge ("though the record does not say whether X was told"). |
| **Juxtaposed event sequence.** Two events are placed back to back with no intervening text, implying the first caused the second. | Causation. | Either a source establishing the causal link, or an explicit "the records do not show a direct link, but" framing. |
| **Named-then-named-then-named ladder.** Three or more actors named in ascending hierarchy in successive sentences, implying each authorized the next. | Chain authorization. | Per-actor source for the authorization claim, or a "the chain of authorization is partly documented and partly inferred" note. |
| **Delayed naming with structural blame.** The chapter withholds an actor's name until the recognition beat, then names them as the source of the laundering. | That actor is the load-bearing decision-maker. | Source supporting the load-bearing role, or a "the public record names X; whether higher-level approval existed is contested" hedge. |
| **Adjacent benefit + adjacent decision.** A paragraph describes a decision; the next paragraph describes who benefited. | The deciders benefited intentionally. | Source documenting the benefit-flow at the time of the decision, or a "benefit accrued; whether it motivated the decision is not in the record" frame. |
| **Sympathetic-then-cold cut.** A sympathetic portrayal of the goat is immediately followed by a cold analytical paragraph naming the chain. | The chain coldly engineered the goat's harm. | Source supporting the engineering claim, or revised framing. |
| **Anonymous chain reference.** "Someone in the chain decided" / "a higher office authorized" / "approval came from above." | A real but unnamed authority. | Either name the office or specify "the public record does not identify which office; investigators have asked." |

## Required hedge forms

Use one of these patterns within the implication-bearing paragraph or the adjacent paragraph:

- "the record does not establish whether..."
- "per the <inquiry / court / inspector>, ..."
- "no document in the public record names..."
- "<source> reconstructed this sequence; the underlying authorization remains contested"
- "this is the order in which the events appear in the public record"
- "<X> later said that <Y>, though contemporaneous notes show <Z>"

## Distinguishing implication from valid inference

Inference is permitted; implication-without-evidence is not. The difference:

- **Permitted inference.** The chapter names the inferential step explicitly: "Three weeks after the memo, the order issued. The memo and the order are both in the record; the connection is not signed." The reader sees the bridge.
- **Forbidden implication.** The chapter presents the two facts in sequence and leaves the reader to bridge them silently. The bridge is not named, so the chapter cannot be challenged for asserting it — that is the laundering surface.

<example>
Before (focalization-then-fact pattern, no hedge):

> The minister opened the file. The figures inside contradicted the morning press release.

The scene is focalized through the minister. The next sentence states a fact only someone who read the file could know. By placement, the chapter implies the minister knew the press release was false. The cited evidence shows the file existed and the press release existed — not that the minister read either.

After (rule-07 cleared, inferential step named):

> The file was on the minister's desk that morning; the morning press release contradicted its figures. The public record does not establish whether the minister read the file before the release went out.

The two facts remain. The implication is replaced with the explicit limit of the record. A hostile reader cannot extract a knowledge claim the source does not support.
</example>

## How rule 07 interacts with craft moves

The fiction-craft moves authorized in `dev-docs/fiction-craft-rewrite-analysis.md` (focalization, delayed naming, document-as-protagonist, two-track time, voice braid) are the exact moves that generate rule-07 risk. Rule 07 does not forbid them. It requires that any chapter using them either (a) cites the implication, (b) hedges it, or (c) names the inferential step as inference.

A chapter rewrite that uses these craft moves without rule-07 discipline is a defamation surface that the existing citation-based scanners cannot see.

## Why this rule exists

The book accuses other institutions of letting weak evidence harden into fact through structural placement (committee minutes, sealed reports, careful sequencing). The same charge applies to the crew the moment narrative sequence is allowed to substitute for documented chain. Rule 07 catches the substitution.

Stephen verifies during fact-check; Laura red-teams chapters specifically for rule-07 violations; Nancy vetoes on implication-driven defamation surface; the `scan-implication.py` hook flags candidate patterns at edit time.
