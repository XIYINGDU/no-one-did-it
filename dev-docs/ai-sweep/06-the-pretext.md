# AI-Fingerprint Sweep — 06-the-pretext

## Tally
- Candidates considered: 9
- Confirmed tells: 1
- Preserved as intentional voice: 8
- Approve-ready edits (verified safe): 1

## Approve-ready edits

### Edit 1 — hedge-filler ("in essence" softening a paraphrase)
**Before:** `Chief Justice John Roberts found, in essence, that the evidence in the administrative record did not match the explanation the Secretary had offered for the decision.`
**After:** `Chief Justice John Roberts found that the evidence in the administrative record did not match the explanation the Secretary had offered for the decision.`
**Preserves:** Procedural-stage verb "found" unchanged; no footnotes/anchors inside the string (footnote [^35] sits in the following sentence, untouched); the verbatim Roberts quote that immediately follows ("the VRA enforcement rationale—the sole stated reason—seems to have been contrived") still carries the support. No new claim — the paraphrase content is identical; "in essence" only softened it.
**Why less AI:** "found, in essence, that" is a generic LLM hedge-paraphrase opener; dropping it leaves the more direct, severe declarative the book's voice prefers.

## Preserved as intentional voice (close calls)

- **"The grammar was the alibi." (l.25), "The form is the protagonist." (l.47), "The signature is the seam." (l.221), "The grammar is the recognition trigger." (l.219)** — short reversal/hammer-lines at turning points; rule-04 sanctioned, recurring book motif. KEEP.
- **"Find the name." (l.61) / "Find the invoker." (l.207) / "put the invoker back" (l.219)** — imperative instruction + recurring co-investigator motif; rule-14 sanctioned. NEVER flag.
- **"in essence" within the Roberts paraphrase (l.137)** — the only confirmed tell; see Edit 1. Distinguished from "In essence" the section-summary crutch (which does not appear).
- **Negative-parallelism throughout ("The text was old; the use was new." l.103; "What is unusual… is not the form. It is the layered visibility of the form." l.131; "the cited cause was the statute," repeated)** — this is the chapter's load-bearing diagnostic contrast (cited cause vs documented cause), each pair carrying genuinely distinct, evidence-anchored content. Not decorative "not X but Y" scaffolding. KEEP.
- **Tricolons ("a misdemeanor criminal statute… a civil-rights enforcement statute… an appropriations-procedure statute" l.45; the six numbered questions; "three modalities…" l.185/195)** — tricolons of distinct, named content (specific statutes, specific venues, specific collapse modalities), not empty escalating abstraction. KEEP.
- **Rhetorical question as the *Overton Park* gloss: "It is the courts' way of asking: does the record show what you said the record shows?" (l.51)** — not a transition-filler question-then-answer; it is the doctrine restated in plain diagnostic form, and the chapter's own recurring test sentence. KEEP.
- **Severe declarative closers ("The records exist. They are durable." l.145; "It is checkable. It is teachable. It is portable…" l.209)** — these assert testable, specific facts (records were produced; the rule names order and sufficiency condition), not hollow profundity. Severity is not a tell. KEEP.
- **Structure-naming "we" transitions ("Two more questions, then we close." l.107; "The promise begins here." l.47; "we do not walk all six at full length" l.71)** — rule-14 co-investigator structure signposting via "we," not meta-frame "this chapter/section." Pronoun "we" never flagged. KEEP.

## Notes
- The chapter is exceptionally clean for LLM tells: a full lexical scan (filler intensifiers, LLM-favorite vocab, transition crutches, hedge clusters) returned a single hit ("in essence", l.137); a syntactic-scaffolding scan ("not X but Y", "from X to Y", over-signposting, sermon register) returned zero. This is consistent with a voice-engineered manuscript.
- No em-dash clusters of 3+ in a single sentence were found; single diagnostic em-dashes (per rule) are left untouched.
- No proposal touches a procedural-stage word, a footnote ref, an anchor, or italics; the one edit is a pure filler-hedge deletion. No proposal was dropped at the VERIFY step.
- One borderline candidate not promoted to a tell: "found, in essence" could alternatively be read as a deliberate signal that what follows is paraphrase, not quotation — but the verbatim Roberts quote in the very next sentence already does that work, so the hedge is redundant rather than load-bearing. Edit 1 is safe on either reading.
