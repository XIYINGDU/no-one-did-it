---
memo_type: image-candidate record-verification (GO/NO-GO)
candidate_id: C7-1
chapter: 07-the-record-is-the-battlefield
owner: Stephen / Fact-check Director
date: 2026-05-29
verdict: GO
public_release: cleared
public_release_date: 2026-05-31
public_release_note: "Mechanical pass tagged this memo as containing internal working-language formulations (1 pattern match(es)); Nancy substantive-review pass required before public push."
nancy_signoff_date: 2026-05-31
nancy_signoff_note: "Image-candidate GO memo for Dalmellington bug, A-graded to Appendix 2 of [2019] EWHC 3408 (QB); software-fault finding only, no living-individual attribution; memo itself explicitly notes no defamation surface."
---

# C7-1 — "render the KEL" image candidate: GO/NO-GO

**Candidate:** name ONE real recorded Horizon bug so a bug becomes visible on the page instead of the KEL category.

## Verdict: GO — use the **Dalmellington bug**

### 1. Citable to primary source — yes (A-grade)

All three floated names appear by name in **Appendix 2 ("Summary of Bugs, Errors, Defects") to *Bates v Post Office (No 6: Horizon Issues)* [2019] EWHC 3408 (QB), 16 December 2019** (the judgment ch-07 already cites at [^246]):

- **#1 Receipts and Payments Mis-match bug** (Horizon Online, 2010)
- **#2 Callendar Square/Falkirk bug** (Legacy Horizon, 2000–2010)
- **#4 Dalmellington bug / Branch Outreach Issue** (Horizon Online, effects 2010–2015)

**Recommended: the Dalmellington bug.** Documented behaviour (one line): a branch transferring cash to a sub-branch hit a frozen screen; each keypress silently confirmed a *further* dispatch of the same sum, so a single transfer registered as multiple, creating a phantom shortfall the sub-postmaster was held liable for.

**Citation:** Appendix 2, item 4, to [2019] EWHC 3408 (QB) — same judgment as [^246]. Grade **A** (existence, name, account-impact, system, dates: court judgment appendix).

### 2. Not already named in ch-07 — confirmed

ch-07 names "Known Error Log (KEL)" five times as a category and never names a single bug. No duplication.

### 3. No defamation surface — confirmed

A software-fault finding (A-grade machine behaviour, court-found). No living-individual guilt attached.

## Caveat for the writer

The Appendix gives the bug's name, system, and years — **A-grade** for everything load-bearing. The vivid **£8,000-per-keypress → £24,000 phantom shortfall** figure rests on **secondary** sources (Communications of the ACM; James Christie / claro testing) describing the case, not on Appendix 2's one-line entry. If the writer wants the dramatic figure, grade it **B** and attribute it ("the £24,000 discrepancy reported in coverage of the Dalmellington case"); the bug *itself* is A-grade. Render the bug; hedge the number.

Evidence grade: A (bug name, system, account-impact, dates — Appendix 2 to [2019] EWHC 3408 (QB)); B for the £24,000 figure (secondary coverage).

Handoff: Wayne (render the Dalmellington bug per [^246]; if using the £24,000 figure, attribute to secondary source per caveat).
