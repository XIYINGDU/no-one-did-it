---
title: Ch-07 Horizon prosecutions figure — fact-check memo
owner: stephen-fact-check-director
purpose: Verify the prosecution / imprisonment counts used in v6 ch-07 line 45 and Figure 3's audio paragraph
date: 2026-05-30
chapter: 07-the-record-is-the-battlefield
status: verdict-delivered
public_release: cleared
public_release_date: 2026-05-31
public_release_note: "Mechanical pass tagged this memo as containing internal working-language formulations (1 pattern match(es)); Nancy substantive-review pass required before public push."
nancy_signoff_date: 2026-05-31
nancy_signoff_note: "Self-correction memo on Horizon prosecution counts; all claims sourced to statutory Inquiry (HC 1119) and Hamilton CoA judgment; no living-individual guilt verbs; no defamation surface."
---

# Ch-07 Horizon prosecutions figure — fact-check memo

Owner: Stephen / Fact-check Director
Task: Verify the figure used at `book/chapters-v6/07-the-record-is-the-battlefield.md` line 45 ("more than 900 sub-postmaster prosecutions between 1999 and 2015") and the matching audio paragraph in `book/diagrams/figure-captions.md` Figure 3.
Inputs reviewed: `book/chapters-v6/07-the-record-is-the-battlefield.md` lines 35–59; `book/diagrams/figure-captions.md` Figure 3 (lines 37–45) and Assumptions block (line 166); source-ledger cards `post-office-horizon-it-inquiry-final-report-vol-1-2025`, `hamilton-v-post-office-2021-court-of-appeal`, `hamilton-v-post-office-affront-to-conscience-2021`, `bates-v-post-office-no-6-horizon-issues-2019`; sidecar `book/source-ledger/sidecars/07-the-record-is-the-battlefield.sources.yml`; external corroboration via Post Office Horizon IT Inquiry portal, Wikipedia (citing Inquiry), Computer Weekly, University of Birmingham legal analysis.
Output: Verified figures table + verdict CORRECT-FURTHER + exact line replacements (see below).
Evidence grade: A — aggregate "over 900 prosecuted, 236 imprisoned, at least 13 suicides" comes from the statutory Inquiry's Vol. 1 (HC 1119); A/B — "more than 700" Post Office private-prosecutor count, multiply corroborated across Inquiry record and secondary sources, conservative wording "more than 700" recommended.
Assumptions: stated below.
Open questions: stated below.
Risks: stated below.
Handoff: Wayne — see Handoff section below.

## Verified figures

| Figure | Verified value | Primary source |
|---|---|---|
| Total sub-postmaster prosecutions 1999–2015 (Post Office + CPS + PPSNI + COPFS combined) | **over 900** | Post Office Horizon IT Inquiry Final Report Vol. 1, HC 1119, Sir Wyn Williams, 8 July 2025 |
| Prosecutions **brought by Post Office Ltd as private prosecutor** | **approximately 700** ("more than 700") | Inquiry record + multiple high-quality secondary sources (Computer Weekly; University of Birmingham / The Conversation) |
| Imprisoned | **236** | Post Office Horizon IT Inquiry Final Report Vol. 1 |
| Suicides linked (Vol. 1 finding) | **at least 13** (Williams: cannot rule out causal link; 59 contemplated, 10 attempted) | Inquiry Vol. 1, July 2025 |

Source-ledger card: `post-office-horizon-it-inquiry-final-report-vol-1-2025` (exists; B-grade pending paragraph-anchor extraction; substance A).

## Verdict: CORRECT-FURTHER

The reconciliation made during the figure-embedding session (v5 "approximately 700" → v6 "more than 900") **goes too far in the other direction**. The "more than 900" aggregate is correct **only when it includes prosecutions by the CPS, PPSNI, and COPFS alongside Post Office private prosecutions**. The v6 ch-07 prose at line 45 attributes the entire 900+ figure specifically to Post Office **private prosecutions** — "as private prosecutor under English law, without Crown Prosecution Service charging review." That attribution does not hold against the verified record.

The v5 figure of "approximately 700" was in fact the correct count *for Post Office private prosecutions specifically*. The earlier text was right; the embed correction was wrong about which figure goes where.

## Exact correction required

**Line 45** (`book/chapters-v6/07-the-record-is-the-battlefield.md`). Replace:

> "It was the **prosecutor** of every one of more than 900 sub-postmaster prosecutions between 1999 and 2015. It exercised that role as private prosecutor under English law, without Crown Prosecution Service charging review."

with:

> "It was the **prosecutor** in more than 700 of the sub-postmaster prosecutions between 1999 and 2015 — the prosecutions it brought directly as private prosecutor under English law, without Crown Prosecution Service charging review. In total, with prosecutions by the CPS, the Public Prosecution Service for Northern Ireland, and the Crown Office and Procurator Fiscal Service added, more than 900 sub-postmasters were prosecuted across the period and 236 imprisoned."

**Line 56** (the five-role table row). Replace:

> "Brought more than 900 private prosecutions (1999–2015), directly, without Crown Prosecution Service charging review."

with:

> "Brought more than 700 private prosecutions directly (1999–2015), without Crown Prosecution Service charging review; together with statutory prosecutors more than 900 sub-postmasters were prosecuted across the period."

**Figure 3 audio paragraph** (`book/diagrams/figure-captions.md` lines 43–45). Same split must be made: "more than nine hundred prosecuted and two hundred and thirty-six imprisoned" stands as the aggregate finding of the statutory Inquiry; the Post Office's *private-prosecutor* role must read "more than seven hundred private prosecutions," not "more than nine hundred." The audio paragraph also currently states "at least four documented suicides" — Vol. 1 records **at least thirteen** (Williams: cannot make definitive causal finding but does not rule it out). Update to "at least thirteen" with the Williams hedge intact.

**Figure 3 proof** (`book/diagrams/proofs/ch07-horizon-five-roles.html`) — the "Brought 900+ private prosecutions" label requires the same split.

**figure-captions.md Assumption (2)** must be reissued: ch-7 reads "more than 700 private prosecutions, more than 900 total prosecuted, 236 imprisoned."

## Evidence grade

**A** for the aggregate "over 900 prosecuted, 236 imprisoned, at least 13 suicides linked" — these are the statutory Inquiry's own published findings (Vol. 1, HC 1119, July 2025), corroborated by the Hamilton Court of Appeal judgment substrate, the House of Commons Library tracking, and consistent secondary reporting.

**A/B** for the "approximately 700 / more than 700" Post Office private-prosecutor count — universally reported across Inquiry materials, BBC, Computer Weekly, University of Birmingham legal analysis, and CCRC summaries; the precise 700 figure may carry a small margin (some sources phrase it "more than 700," some "around 700"). Stephen's recommendation: phrase as "more than 700" to track the most conservative published wording.

The B-grade carried on the source-ledger card today is pending paragraph-anchor extraction from the Inquiry PDF; the substance of the numbers is A.

## Cross-check against the prompt's concern

The prompt asked specifically whether the "more than 900" count conflates Post Office prosecutions with DWP/CPS-routed prosecutions. **It does.** The Wikipedia article (citing the Inquiry) states it plainly: "the Post Office and the statutory authorities of the UK, including the CPS, the PPSNI, and the COPFS, brought forward hundreds of criminal prosecutions ... In all ... over 900 subpostmasters were prosecuted ... The Post Office itself prosecuted 700 people." The concern was warranted; the v5→v6 reconciliation collapsed the distinction.

## Assumptions

- Vol. 1 of the Inquiry Final Report is the canonical statutory record for these aggregate figures (it is — published as HC 1119 under the Inquiries Act 2005).
- The chapter's structural claim — that the Post Office held the *prosecutor* role as one of five conflated roles — survives the correction; in fact it is strengthened, because the "more than 700 private prosecutions" figure is what makes the private-prosecutor diagnostic load-bearing, whereas the 900+ aggregate includes prosecutions where the CPS *did* perform a charging review and so does not exemplify the laundering pattern as cleanly.

## Open questions

1. Paragraph-anchor lock for Vol. 1 (the source-ledger card's deferred work). Until Delon retrieves and Stephen byte-verifies the specific Vol. 1 paragraphs, the card stays B; the substance is A.
2. Whether the chapter wants to keep the "236 imprisoned" figure attached to the 700 private-prosecution clause or to the 900 aggregate. Cleanest: attach it to the aggregate, where Vol. 1 attaches it.
3. Suicides: the v5 chapter and Figure 3 paragraph use "at least four"; Vol. 1's finding is "at least thirteen" (Williams hedged but did not rule out causation). If "at least four" is carried over from an earlier source, it is now stale and must be lifted to the Vol. 1 figure with the Williams hedge.

## Risks

- If line 45 ships as currently written ("more than 900 ... as private prosecutor"), the chapter overstates the Post Office's private-prosecution count by approximately 30 percent. The book's argument does not need the inflation — and risks a high-profile correction-target because the Post Office case is heavily covered.
- Rule 12 V7 (severity proportional to evidence): a B/C-stance on a number that is actually A-attested for the *correct* claim and not-attested for the *current* claim is a clean V7 failure.
- Rule 05 / 07: the inflation does not name a person and so does not generate defamation surface, but it does generate "the book launders its own evidence" surface, which Laura would catch on the next red-team pass.

## Handoff

`Handoff: Wayne (narrative lead)` — apply the line-45, line-56, Figure 3 audio paragraph, and Figure 3 proof corrections above; reissue figure-captions Assumption (2); lift the suicide count to "at least 13" with the Williams hedge.

Cascade: `→ Bonnie` (re-render Figure 3 proof) `→ Nancy` (confirm the corrected wording does not introduce new defamation surface — it should not; it is more conservative on the private-prosecution count and more accurate on the aggregate) `→ Stephen` (re-lock; close the source-ledger card paragraph-anchor deferred work in parallel via Delon if PDF extraction becomes feasible).

---

**Verdict in one sentence:** CORRECT-FURTHER — restore "more than 700" as the Post Office private-prosecutor count, keep "more than 900 prosecuted and 236 imprisoned" only as the aggregate including CPS/PPSNI/COPFS, and lift the suicide count from "at least four" to the Inquiry Vol. 1 finding "at least thirteen" with the Williams hedge.
