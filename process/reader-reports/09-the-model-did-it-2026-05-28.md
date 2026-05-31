Owner: the-reader
Task: Cold-read of book/chapters-v3/10-the-model-did-it.md as a first-time reader (sequential; chs 1–9 assumed read), walking the seven reader-experience axes.
Inputs reviewed (cold): book/chapters-v3/10-the-model-did-it.md only. No briefs, rules, registries, other chapters, or prior reports.
Output: Friction report below.

## Verdict

CLEAN

## Findings (HARD)

None.

## Findings (SOFT)

1. **Engagement / pacing — three near-identical "no liability adjudicated" stanzas land in close succession (paragraphs at lines 65, 87, 101).** Each named executive (Amodei, Altman, Zuckerberg/Al-Dahle) gets the same three-beat formula: "X is CEO of Y / No public statement attributing [decision] to X personally has been documented as of May 2026 / No civil or criminal liability has been adjudicated against X as of May 2026." By the third instance (Zuckerberg + Al-Dahle, line 101) I clocked the template and skim-read it. I understood *why* it's there — the chapter is policing its own overclaim, and that's consistent with the diagnostic stance — but as a reader I felt the repetition as a slight drag rather than a fresh beat. SOFT: I followed everything; I just wanted the third instance compressed or varied. Severity: SOFT (managed; mild repetition fatigue).

2. **Comprehension — "PiLiMi" appears unexpanded (first at line 17, recurs throughout).** "LibGen" reads as a recognizable shadow-library name; "PiLiMi" does not, and it's never spelled out (Pirate Library Mirror). I parsed it from context as a second shadow library and never lost the thread, so this did not block comprehension. But the first encounter produced a small "what is that?" stumble. Severity: SOFT (managed via context; mild friction on first contact).

3. **Engagement — the closing run (lines 177–201) stacks four distinct "what to do" framings in sequence.** The recognition trigger question (line 179), the by-layer diagnostic markers (181–187), the three role-based positions (191–195), "refuse to become the goat" (197), the signature-is-the-seam callback (199), and the emerging fourth-layer note (201). Each is individually strong and clear, but arriving one after another after an already long chapter, I felt the ending widen rather than tighten. The chapter is information-dense to the last line. SOFT: I stayed with it and the final image ("When the agents arrive in our work, we already know what to ask") landed well; I simply noticed the takeaway section asks the reader to hold a lot at once. Severity: SOFT (slightly slow at the close; no loss).

## Clean axes

- **Comprehension (largely clean).** The three-layer architecture (input / deployment / evaluation) is set up in the opening three case vignettes and stays distinct the entire way through. I always knew which layer I was in. The eight-question diagnostic walk at the input layer (lines 41–67) was legible question by question. Technical terms (reward-shaping, A/B testing, transformative fair use, summary judgment) were each given enough in-line grounding that I never had to stop. Only PiLiMi (SOFT above) produced a stumble.

- **Engagement.** The opening — "three separate AI companies told the public... that the model had decided" across "three structurally distinct layers of the same technology stack" — is a strong hook and I wanted to see all three. The Llama-4 leaderboard story (the #2-then-#32 gap) was the most gripping single thread. Apart from the two repetition notes above, the chapter held me.

- **Recognition.** The central recognition — that "the model decided / the data showed / the variant performed / the policy didn't match" are one family of grammatical operations, each displacing a named human decision — is *earned*, not delivered. The chapter shows me the three quotes first (lines 31–35), then names the pattern ("The grammar is the laundering," line 37). "Alibi escalation" at line 105 (caught at level N, moves to level N+1) was the standout earned-recognition moment: I saw the LMArena policy-revision shift one rung up *before* the chapter named it, which is exactly the reader-does-the-work feeling. I did not feel told what to think.

- **Orientation.** I always knew where I was. The section headers double as plain-language signposts ("A 72-hour rollback," "Alibi escalation at the leaderboard," "Alsup draws the line at acquisition," "Run the diagnostic three times"). The callbacks to chapters 2 and 7 (Therac, MAX, Horizon) were each re-grounded in a sentence or two before being used, so I didn't need to remember the earlier chapters in detail. The reference at line 175 to chapter 8 as "the next stress-test in Part III" read naturally as a forward signpost to the next chapter — no confusion (and per instruction, not flagged).

- **Trust (clean — and this is the chapter's strongest axis).** The $1.5 billion settlement claim is handled exactly right on first contact. At line 19 — the first time I meet the number — it is immediately hedged: "what would be, if the court grants final approval, the largest reported copyright settlement in United States history by acknowledged press reporting. As of our manuscript-freeze date that approval is pending; we hold the superlative to that condition here and below." I was never sold a flat "largest in history" and then quietly walked back. Every subsequent restatement (lines 117, 169) carries the same conditional. The fairness-hearing detail (line 119: 92.77% claims rate, 350 opt-outs, matter under submission, distribution by 11 June 2026 if final approval issues) and the explicit "no order granting final approval has been recorded... we use the procedural language the docket supports" (line 121) made me trust the chapter *more*, not less — it showed its work on a live, contested number. Throughout, the chapter is scrupulous about what the record does and does not support ("No public statement attributing... has been documented"; "characterisation of Altman's contemporaneous knowledge... is what the record cannot support, and we do not advance it," line 87). I never disbelieved a load-bearing claim at the moment it was made.

- **Takeaway.** I can complete the test. The chapter taught me: run the diagnostic three times per AI system (input / deployment / evaluation), because at each layer a different non-human noun absorbs a different displaced human decision and a different interception instrument is required. And the portable recognition trigger — "Did a non-human verb-subject just absorb a decision that affects me?" — is a tool I can carry. The capacity survives the affect.

- **Mechanics (clean).** No production markers, internal filenames, or build-system leakage anywhere in prose or footnotes. I specifically checked the footnotes [^372]–[^380]: each is a reader-facing citation (title, archive URL, capture date, verification annotation). The earlier-flagged AGENTS.md-style internal citation is absent. The one HTML comment at line 206 is an authoring note about per-chapter vs back-of-book footnote handling; it is inside an HTML comment and would not render in published output, and as a reader viewing rendered text I would not see it — so I did not treat it as a visible production marker. The footnote verification annotations ("[primary URL no longer resolves as of 2026-05-28; canonical archive]") read as deliberate, reader-facing transparency rather than as leaked internal state. No uninterpretable shortened-form citations; no footnote reference without an inline target (every [^N] in prose has a matching definition).

## Evidence grade: N/A

## Assumptions

- I read sequentially, assuming chapters 1–9 are already in the reader's head; I relied on the chapter's own re-grounding of the chapter-2 (Therac, MAX) and chapter-7 (Horizon, five-role conflation) callbacks rather than on independent memory.
- I treated the reference to chapter 8 as the next chapter in reading order (per task instruction) and did not flag it as a forward-reference error.
- I read the HTML comment at line 206 as non-rendering authoring metadata, not as reader-facing prose.

## Open questions

- Is "PiLiMi" expanded anywhere earlier in the book (e.g., an earlier AI chapter or a glossary)? If a first-time reader of this chapter has not met it before, the unexpanded acronym is a (minor, SOFT) first-contact stumble. If it is established elsewhere in reading order, even the SOFT note dissolves.

## Risks

- None blocking. The three SOFT findings are all repetition/density tradeoffs at points where the chapter is deliberately being scrupulous (executive non-liability stanzas) or comprehensive (the closing toolkit). A crew member may reasonably judge them acceptable; I report them only as lived friction, not as defects requiring a fix.

## Handoff

Next owner: jerry-crew-chief — verdict is CLEAN, no HARD findings, no v3-promotion block from the reader. Three SOFT findings (executive-stanza repetition; unexpanded "PiLiMi"; dense closing run) are optional polish candidates for wayne-narrative-lead if a future prose pass touches this chapter; none requires action for publication-readiness.
