Owner: the reader

Task: Cold-read chapter 10 ("The Model Did It") as a sequential reader who has read chapters 1–9, and report lived experience across seven axes. Report experience, never propose fixes.

Inputs reviewed (cold): book/chapters-v3/10-the-model-did-it.md only. Nothing else.

Output: book/reader-reports/10-the-model-did-it-2026-05-28.md

## Verdict

BLOCKED — 3 HARD

## Findings (HARD)

### H1 — Orientation: the chapter-8 forward reference reads as broken sequence (lines 175)
At line 175: "Chapter 9 walked the institutional-power case — power calling itself the goat. We have walked the newest altar. Chapter 8 is the next stress-test in Part III: the war zone..."

Reading sequentially, I have just come from chapter 9. The chapter tells me chapter 8 is "the next" thing after chapter 10. That stopped me. I read chapter 8 nine chapters ago — how is it "next"? Either I misremember the whole book order, or chapter 10 sits before chapter 8 in the actual reading sequence and the numbering I'm holding in my head is wrong. Whichever it is, the sentence broke my sense of where I am in the book. A forward-pointer to a *lower* chapter number, presented as "the next stress-test," is a live contradiction at the moment I read it. I lost confidence that I understood the book's structure. HARD (got lost / disoriented on book structure at the moment of reading).

### H2 — Mechanics: footnote [^377] exposes a production marker in the reader-facing text (line 211)
At line 211: "[^377]: AGENTS.md — Core diagnostic (eight questions). access: physical-archive."

This footnote, which I would flip to from the eight-questions passage at line 41, cites "AGENTS.md" as its source. AGENTS.md is plainly an internal project file, not a book or document a reader could ever consult. The trailing "access: physical-archive" is raw metadata that means nothing to me. When I followed the superscript to learn where the eight questions come from, I got an internal filename and a database field instead of a citation. That is a visible production marker leaking into the published text. It also briefly made me distrust the other footnotes — I started wondering what else in the back-matter is internal scaffolding. HARD (production marker visible in reader-facing output).

### H3 — Trust/Comprehension: "the largest reported copyright settlement in United States history" stated twice as flat fact, then the docket says no final approval exists (lines 19, 117, 119, 121)
Line 19 and line 117 both assert the $1.5 billion *Bartz* settlement is "the largest reported copyright settlement in United States history." I accepted this as settled fact on first read at line 19 — it's stated plainly, in the opening. Then at lines 119–121 the chapter tells me the final fairness hearing happened 14 May 2026, "the court took the matter under submission rather than ruling from the bench," and "As of our manuscript-freeze date, no order granting final approval has been recorded in the public docket." So at the moment I was told (twice, confidently) that this is the largest settlement in US history, the settlement had not actually received final court approval. The load-bearing fact I was asked to believe in the opening was undercut by the chapter's own later disclosure. The confident framing outran what the chapter itself later admits the record supports. I disbelieved the opening claim retroactively, and the second confident repetition at line 117 — placed *after* I'd been set up to expect the caveat — made the friction worse, not better. HARD (disbelieved a load-bearing claim, made confidently at the moment it was made, then contradicted by the chapter's own record).

## Findings (SOFT)

### S1 — Engagement: the three-layer scaffolding is announced very explicitly and repeatedly
The chapter tells me what it's about to do at almost every transition: "We walk the eight questions at full depth through the input layer, then take the deployment and evaluation layers at focused depth" (line 43); "We can hold each of the three stories in mind separately. Our first promise here is that the three are not separate" (line 37); "The diagnostic this book installed asks eight questions" (line 41); the closing "Run the diagnostic three times" section restates the whole architecture again (lines 135–137). I followed it fine and the three layers stayed distinct for me throughout — that part worked. But the machinery is loud. I noticed the author managing my attention more than I noticed the cases. Managed despite wanting the cases to carry the structure on their own. SOFT.

### S2 — Recognition: the "alibi escalation" beat lands, but the chapter names it for me a beat early (line 105)
The LMArena sequence — variant performed, then policy didn't match expectations — was genuinely satisfying to follow at lines 99–103. I could feel the agent shifting up a rung *before* the chapter told me. Then line 105 says "Name the operation. *Alibi escalation.* When the laundering is caught at level N, it moves to level N+1." I'd already gotten it. The naming felt like being handed the recognition I had just earned a sentence earlier. Mild — I still felt the click; it was just slightly pre-empted. SOFT.

### S3 — Comprehension: "thirty places" gap repeated three times with slightly different framings
The #2-vs-#32 gap is given at line 13 ("approximately #32. A gap of about thirty places"), line 99 ("landed at approximately #32. A 30-place gap"), and implied again at line 103. By the third pass I felt the chapter re-explaining something I had firmly held since the first paragraph. Mild repetition; I managed. SOFT.

### S4 — Takeaway: the "what to do" section is long and role-split, and the fourth item arrives after I thought the list was done
Lines 189–197 give cost-bearer / bystander / institutional-actor guidance, then line 197 opens "The fourth thing to do is to refuse to become the goat" — but the preceding three were framed as *positions* (cost-bearer, bystander, institutional actor), not as a numbered list of "things to do." So "the fourth thing" pointed back to a count I hadn't been keeping. I could complete the takeaway test — "now I can recognize the model-decided alibi and demand three records" — so the core takeaway survived. But the closing instruction block made me re-scan to find what the first three "things" were. SOFT.

## Clean axes

- **Comprehension (core mechanic):** The central idea — three structurally distinct layers of one AI stack, each renaming a human decision as a non-human verb-subject — was clear and I held it the whole way. The "three layers" structure stayed distinct in my head from start to finish; I never confused input/deployment/evaluation. The fair clue ("the verb's subject is a thing," line 25) was planted early and paid off at the close (line 177). Clean on the load-bearing comprehension question I was asked to track.

## Evidence grade: N/A

Assumptions:
- I assumed standard sequential reading: chapters 1–9 already read, chapter 10 read once start to finish. I treated callbacks to chapters 2, 7, and 9 as in-context because the chapter re-grounded each (Therac/MAX/Horizon recaps at lines 73–77; chapter 7 five-role conflation restated at lines 65, 131, 147; chapter 9 named at line 175) — those did not read as callback-blanks.
- I assumed footnote superscripts ([^374]–[^383]) are something a reader follows to the References section; I evaluated [^377] as the experience of doing so.

Open questions:
- Is chapter 10's position in the published reading order actually before chapter 8? If the book's part/chapter order is non-numeric, H1 may be a deliberate structure I cannot see from inside one chapter — but as a reader I still hit the contradiction.
- Is the [^377] AGENTS.md citation a placeholder awaiting a real public source, or is the eight-questions diagnostic genuinely uncited to any external document? Either way the reader-facing footnote does not work as a citation.

Risks:
- H3 is the highest-stakes finding: the book's whole project is "don't let weak evidence harden into confident fact," and the opening hardens an unapproved settlement into "largest in US history" before disclosing the approval is pending. A hostile reader applying the book's own standard to this chapter would catch it.

Handoff: Next owner is jerry-crew-chief to triage the three HARD findings — H1 (structure/orientation, likely bonnie-book-architect on chapter-order reference), H2 (mechanics/citation, likely stephen-fact-check-director on the [^377] source-ledger card), H3 (trust/severity-evidence, likely wayne-narrative-lead for the opening framing with nancy-legal-risk-counsel / stephen on the procedural-stage accuracy of "largest in US history"). Fixes land in v2; v3 rebuilds; I re-read before this chapter's v3 promotion block lifts.
