# AI-Fingerprint Sweep — 04-the-proxy-and-the-sponsor

## Tally
- Candidates considered: 16
- Confirmed tells: 1
- Preserved as intentional voice: 15
- Approve-ready edits (verified safe): 1

## Approve-ready edits

### Edit 1 — copula-stacking padding ("it is also real that")
**Before:** `The shell is real, and it is also real that someone built it.`
**After:** `The shell is real, and someone built it.`
**Preserves:** No footnotes, anchors, italics, or procedural-stage words in the string (confirmed by grep; unique single occurrence at line 147). No factual claim, no causation/knowledge upgrade — "someone built it" is the same proposition, just without the padded copula.
**Why less AI:** Drops the LLM "it is also real that" copula-restatement; lands the chapter's crisp declarative register instead of softening it with a second "is real."

## Preserved as intentional voice (close calls)

- **"Three vocabularies. Three time zones. One shape."** (line 35) — tricolon of genuinely distinct content (three named cases: Crimea/Putin, MH17/MoD, Nisour Square/State Dept) resolving into the book's reversal hammer. Rule-04 craft, not empty escalation. KEEP.
- **"The first reversal here is acoustic, not analytical."** (line 37) — "X, not Y" form, but it is a load-bearing diagnostic distinction (the shape is heard before it is argued), and it sets up the concrete "Three governments… each saying not us." Substantive, not reflexive antithesis. KEEP.
- **"MH17 carries the spine." / "MH17 is a hybrid."** (lines 41, 61) — short metaphor/declarative reversal at a structural turn. Book voice. KEEP.
- **"This is the claim." / "This is the architecture we examine in two further forms."** (lines 23, 63) — short orienting declaratives; not meta-frame "this chapter," they point at the argument itself, which rule-14 permits. KEEP.
- **"Hold that distinction. We will need it." / "Hold the rule. Use it on every case we have not yet seen."** (lines 57, 153) — imperative instruction + co-investigator "we." Explicitly rule-14-sanctioned. NEVER flag.
- **"We resolve both layers. Neither layer is rhetorical."** (line 61) — short declarative reversal with concrete referents (partial-scapegoat + system/object-alibi registers). KEEP.
- **"The mechanism is portable." / "It is a *civilizational* method…"** (line 87) — short reversal closing the Nisour Square mechanistic-equivalence argument; the italic on *civilizational*/*mechanistic* is single diagnostic emphasis, not decoration. KEEP.
- **"A record is not a remedy. We do not pretend that the two are the same."** (line 103) — "X is not Y" but it is the section's load-bearing claim and a recurring book hammer-line; concrete and testable. KEEP.
- **"The architecture survives the responses; we survive the architecture."** (line 121) — chiasmus; stylized, but carries real content (the three counterarguments did not defeat the analysis) and performs the co-investigator stance. Borderline ornamental, but it asserts something testable against the section above it. KEEP.
- **"The collapse was performed, not extracted." / "was extracted, not performed."** (lines 127, 129) — "X, not Y" parallelism, but it is the precise analytical axis the section is built on (Putin narrated his own collapse on TV; the Buk collapse was forced out by investigators). Genuinely distinct content per case. KEEP.
- **"The shape recurs. It recurs across state lines… It recurs in the seizure… It recurs in the launch…"** (line 21) — anaphora, but each "It recurs" clause names a distinct concrete case. Distinct content, not escalating abstraction. KEEP.
- **"The proxy is a method. The pierce is a method." / "The proxy is the shell."** (lines 147, 177) — recurring book motif (method/pierce), short declarative. KEEP.
- **"Knowing the proxy is half of the recognition. The other half is knowing what each channel can and cannot do…"** (line 177) — "half / the other half" structuring, but the two halves hold genuinely distinct content (recognize the proxy vs. read the multi-channel interception) and echo the chapter's explicit "first move / second move" frame. Not hollow profundity. KEEP.
- **"Recognise it first. Diagnose it next. Act on it. Avoid becoming the proxy."** (lines 179–191) — the rule-04 beat-8/beat-10 role-walk rendered as imperatives; rule-14-sanctioned instruction, not over-signposting. KEEP.
- **"we survive the architecture" / "we" throughout** — co-investigator pronoun required by rule 14. NEVER flag.

## Notes
- Both automated passes (lexical AI-vocab regex; syntactic "not-X-but-Y" / "From-X-to-Y" / summary-restatement / throat-clearing / over-signposting regex) returned **zero** hits. This is a heavily voice-engineered chapter; the only confirmed tell surfaced on the manual discerning-editor read of copula padding.
- No tell was dropped for safety reasons — the single confirmed tell was cleanly rewritable. All other flagged candidates were adjudicated PRESERVE on the merits (deliberate craft per rules 04/12/14), not deferred.
- Procedural-stage vocabulary throughout ("convicted," "acquitted," "indicted," "pardoned," "in absentia," "found liable") and the dense `[^N]` footnote apparatus were left untouched by design (legally load-bearing per rules 05/06; the one edit touches none of it).
