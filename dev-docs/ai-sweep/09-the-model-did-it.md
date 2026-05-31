# AI-Fingerprint Sweep — 09-the-model-did-it

## Tally
- Candidates considered: 9
- Confirmed tells: 3
- Preserved as intentional voice: 6
- Approve-ready edits (verified safe): 3

## Approve-ready edits

### Edit 1 — filler intensifier (evaluation-substitute)
**Before:** `The 72-hour interception window is genuinely fast by historical comparison.`
**After:** `The 72-hour interception window is fast by historical comparison.`
**Preserves:** No footnotes, anchors, italics, or procedural-stage words in the string; none added or dropped. No factual claim changed — the comparison still rests on the Horizon/Therac timelines stated in the same paragraph.
**Why less AI:** "genuinely" is a filler intensifier that asserts the editor's emphasis instead of letting the cited timeline do the work; the bare claim is sharper and the next sentences already supply the proof.

### Edit 2 — empty evaluative framing / hollow superlative
**Before:** `The second move of the evaluation-layer alibi is the most operationally instructive moment we encounter.`
**After:** `The second move of the evaluation-layer alibi is the one to learn from.`
**Preserves:** No footnotes, anchors, italics, or procedural-stage words; "we" co-investigator pronoun retained per rule 14. No factual or procedural claim changed.
**Why less AI:** "the most ... moment we encounter" is a self-rating superlative that tells the reader the passage matters rather than showing it; the shorter declarative drops the LLM-flavored self-importance while keeping the pointer.

### Edit 3 — hollow-profundity injunction (sermon-adjacent)
**Before:** `The benchmark becomes, in a moment that should hold our attention, the instrument of its own anti-laundering rule.`
**After:** `The benchmark becomes the instrument of its own anti-laundering rule.`
**Preserves:** No footnotes, anchors, italics, or procedural-stage words; the substantive claim (benchmark as its own anti-laundering instrument) is intact and is reinforced by the two sentences that follow.
**Why less AI:** "in a moment that should hold our attention" is an instruction to the reader to feel significance — the exact over-signposting/sermon register the book's rule 14 forbids; cutting it lets the genuinely sharp reversal land on its own.

## Preserved as intentional voice (close calls)
- **"Our first promise here is that the three are not separate." (line 41)** — mild signposting, but cast in the rule-14 co-investigator "our" frame and immediately cashed out by the prose that follows; a specific construction, not generic-LLM throat-clearing. Deliberate scaffolding.
- **"The interception is real; the architecture is intact." (line 95)** — short reversal/hammer-line at a moral turning point; rule-04 sanctioned. KEEP.
- **"Name the operation. *Alibi escalation.*" (line 109)** — imperative instruction + diagnostic coinage in italics; rule-14 sanctioned imperative, not slop. KEEP.
- **"three structurally distinct layers" (lines 15, 45, et al.)** — "structurally distinct" recurs but is load-bearing: it names the input/deployment/evaluation distinction the whole chapter turns on, not an empty intensifier. KEEP.
- **"not being publicly blamed for AI's growing pains" (line 65)** — "growing pains" is a cliché, but it is deployed contrastively to deflate the institutions' own framing ("not ... but erased from the grammar"), so the cliché is the target, not the author's voice. KEEP.
- **"It is also the layer at which..." / "It is also the form of interception..." (lines 83, 109)** — "It is also X" reads as natural analytic prose advancing a second property, not a transition crutch like "Moreover/Furthermore." KEEP.

## Notes
- No `[CITE:]` markers appear in this v6 chapter; citations are live `[^N]`-style footnote refs (e.g., `[<sup>1</sup>](#c9-1)`). None of the three edits touch a footnote-bearing sentence, so no ref-integrity risk.
- All three BEFORE strings were grep-verified as exact and unique in the file (each occurs once).
- The severe/cold declarative register, the "we/us/our" pronoun, and the procedural-stage hedges ("No civil or criminal liability has been adjudicated...", "as of May 2026", "settlement announced") were treated as intentional and left untouched throughout.
- No tell required dropping for safety reasons; the three confirmed tells were all cleanly excisable framing with no factual or procedural payload.
