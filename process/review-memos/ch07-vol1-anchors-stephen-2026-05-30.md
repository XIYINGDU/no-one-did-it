---
title: ch-07 Post Office Horizon IT Inquiry Vol 1 — paragraph-anchor lock attempt
owner: stephen-fact-check-director
date: 2026-05-30
chapter: 07-the-record-is-the-battlefield
card: post-office-horizon-it-inquiry-final-report-vol-1-2025
verdict: PARTIAL B → A on close-out (two of four ch-07 anchors byte-locked at Vol 1 ¶3.11/¶3.12 and ¶3.24; two anchors remain B, not present as aggregates in Vol 1's own text)
public_release: mechanical-pass-cleared
public_release_date: 2026-05-31
---

# Owner
Stephen / Fact-check Director.

# Task
Lift `post-office-horizon-it-inquiry-final-report-vol-1-2025` from B → A by locking paragraph anchors in Sir Wyn Williams' Volume 1 Final Report (HC 1119, 8 July 2025) for four chapter-7 claims: (1) more than 900 prosecutions across all prosecuting authorities; (2) more than 700 Post Office private prosecutions; (3) 236 imprisoned; (4) at least 13 suicides linked + Williams' causal-link hedge (also 59 contemplated, 10 attempted).

# Inputs reviewed
- Primary PDF: `postofficehorizoninquiry.org.uk/.../Volume_1_0.pdf` (~5MB) — fetched, returned compressed binary stream; not text-extractable via WebFetch.
- Rapid Read PDF (2.9MB) — same outcome.
- HTML landing page (`/volume-1-post-office-horizon-it-inquirys-final-report`) — only links to the PDF; no body text.
- Government Response (gov.uk HTML, 13 October 2025) — reachable; cites Vol 1 by "Paragraph N.NN" form (cites only para 6.65, unrelated).
- Sir Wyn's 8 July 2025 address (HTML) — confirms Vol 1 structure: "section 3 is devoted to human impact".
- Hansard Commons (8 July 2025) and Lords (17 July 2025) debates — 403 / 401.
- Secondary corroboration (Computer Weekly, Euronews, Scottish Legal News, Irish Legal News, Wikipedia, Postal Museum) — all paraphrase, none cite paragraph numbers.

# Output
Card updated with:
- New verification-log step `paragraph-anchor-extraction-attempt` (outcome BLOCKED, dated 2026-05-30) recording each surface tried and why it failed.
- Confirmation that Vol 1's internal scheme is `paragraph N.NN` (chapter.paragraph), via the Government response's verbatim "Paragraph 6.65" cite.
- Best secondary verbatims captured for the four claims (Williams' hedge — "could not rule out the 'real possibility'", "cannot make a definitive finding... causal connection"; aggregate scale — "over 900... 236 went to prison"; sub-count — "The Post Office itself prosecuted 700 people").
- A noted reconciliation problem: press cites 1999–2015; Sir Wyn's own address says 2000–2013 (E&W) — to be resolved when anchors are locked.
- Deferred-work block restructured to list all five anchors (the four claims plus the Hamilton reproduction).
- Handoff updated: Delon (PDF retrieval + local pdftotext) → Stephen (byte-exact anchor lookup); lifts to A in one cycle.

Evidence grade: B (unchanged).

Substantive findings are A in their underlying institutional authority — this is the statutory Inquiry's Final Report under the Inquiries Act 2005. The card stays B *only* because byte-exact paragraph anchors for the four ch-07 claims could not be locked from the public web surface in this session. Ch-07 prose remains usable at B because rule 02 permits B-grade reliance for chapter-level claims; the A-promotion would have hardened the four specific anchors for late-stage Stephen lock per rule 13's `pending-stephen-lock` discipline.

# Assumptions
- The PDF is unrestricted public-record material on a UK gov-inquiry domain; the obstacle is tooling (WebFetch returns binary), not access policy.
- Vol 1 uses `chapter.paragraph` anchors throughout (confirmed for one paragraph; assumed consistent across the report).
- The four target claims are documented in Vol 1 itself (not only press summaries) — every secondary source attributes them to the report, but the byte-exact phrasing is not in hand.

# Open questions
1. Are the four claims in Section/Chapter 3 ("Human Impact") or distributed across Sections 3, 4, and 6? Sir Wyn's address points to Section 3 for human impact; the prosecution counts may sit in Section 1 or 2 (procedural background).
2. 1999–2015 (press) vs 2000–2013 E&W (Sir Wyn's address) — which boundary does Vol 1 itself use for the 900+ figure? This affects chapter-7 line phrasing.
3. Does the 700+ private-prosecution sub-count appear as a single figure in Vol 1, or only as a derivation (total minus CPS / Procurator Fiscal)? Ch-07's cite should match the report's own framing.
4. Williams' hedge wording — is "real possibility" verbatim from Vol 1, or a press paraphrase of a longer Williams formulation?

# Risks
- If chapter-7 is shipped at B for this card and a hostile reader challenges any of the four figures, the response chain is the secondary-press paraphrase, not the Inquiry's own paragraph anchor. Acceptable but not ideal; this is exactly the laundering surface we diagnose elsewhere ("the press summary stood in for the primary record").
- The PDF was captured to a volatile WebFetch tool-results cache during this session; that cache is not a stable archive. If Delon retrieves the PDF locally, the local copy should be SHA-256-checksummed against the Inquiry portal's current copy.

# Handoff
**Delon (Research Director)** — retrieve the Vol 1 PDF locally and run `pdftotext` (or equivalent OCR fallback), then return the text for paragraph-anchor lookup. On completion, hand off back to Stephen for byte-exact verification and card promotion B → A.

# Closeout (2026-05-30, after local pdftotext extraction)

Local plain-text extraction (`/tmp/vol1/Volume_1.txt`, 545 KB) closed the block. Two of the four ch-07 anchors are now byte-locked in Vol 1's own text; two are **not present as aggregate findings inside Vol 1** and must keep their existing sources.

**Locked anchors (B → A):**

1. **Aggregate prosecution figure — Vol 1 ¶3.24, verbatim:** *"it seems to me to be likely that approximately 1,000 persons were prosecuted and convicted throughout the United Kingdom during the period with which the Inquiry is concerned based on Horizon evidence."* The Vol 1 number is "**approximately 1,000**", not the press paraphrase "more than 900". Ch-07 prose must conform to Williams's own figure. Date boundary at ¶1.7: "**Between 2000 and the autumn of 2013**" for E&W; NI/Scotland later. The "1999–2015" press range is not Vol 1's framing.

2. **Suicide block — Vol 1 ¶3.11 + ¶3.12, verbatim:**
   - ¶3.11: *"I have also received evidence from at least **59 persons who contemplated suicide** ... **Ten** of the persons who contemplated suicide attempted to take their lives, some on more than one occasion."*
   - ¶3.12 (Williams hedge): *"I should stress that whilst I cannot make a definitive finding that there is a causal connection between the deaths of all **13 persons** and Horizon, **I do not rule it out as a real possibility**."*
   - The "**13**" figure derives from ¶3.8 (six named by PO on 18 March 2025 request) + ¶3.10 (further seven named on 27 March 2025 request). Williams also notes (¶3.12) the figure may understate ("more than 13 ... but some deaths have not been reported").

**Anchors not present in Vol 1 (stay at prior B sourcing — DO NOT cite to Vol 1):**

3. **"More than 700 Post Office private prosecutions"** — no such sub-count exists in Vol 1. ¶1.7 says only that the Post Office prosecuted in E&W while NI/Scotland prosecuting authorities did so separately, with no numeric split.

4. **"236 imprisoned"** — "236" appears in Vol 1 only as a paragraph number (4.236) and footnote marker, not as an imprisonment count. The figure must keep its existing press/earlier-Inquiry sourcing; ch-07 cannot cite it to Vol 1.

**Risk flagged for Wayne:** ch-07 prose currently reads "more than 900 ... 236 ... 700"; revise to "approximately 1,000 ... [keep prior 236 cite] ... [drop the 700 split unless re-sourced]" so the Vol 1 anchor is byte-accurate.

# Updated Handoff
**Wayne (Narrative Lead)** — revise ch-07 line 105 area: align aggregate phrasing to Vol 1 ¶3.24 ("approximately 1,000"); align suicide-block phrasing to Vol 1 ¶3.11/¶3.12; keep 236 and 700 figures only with their non-Vol-1 sources or remove. Then handoff to Stephen for byte-check of the revised paragraph.
