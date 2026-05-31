# KDP Listing Pack — *No One Did It*

> Source pool for the inputs KDP's web form asks for at upload time, distinct from the EPUB/PDF artefacts already built. Everything below is grounded in shipped material: `book/design/epub/metadata.yml`, `book/proposals/*.md`, and `book/back-matter/about-the-author.md`. Anything labeled **author-decision** waits on xiaolai; everything else is fill-and-go.

**Last updated:** 2026-05-30
**Status:** assembled, awaiting human review
**Companion artefacts:** `dist/no-one-did-it.epub` (manuscript upload), `book/design/epub/cover.jpg` (cover upload)

---

## 1. Product details (lock-data — already decided)

These match `book/design/epub/metadata.yml` and the cover; copy them verbatim into KDP's "Kindle eBook Details" page.

| Field | Value |
|---|---|
| Language | English |
| Book Title | `No One Did It` |
| Subtitle | `Responsibility Laundering, from the Scapegoat to the Algorithm` |
| Series | *(leave blank — not a series)* |
| Edition Number | *(leave blank — first edition)* |
| Author | `Xiaolai Li` |
| Contributors | *(none)* |
| Description | see §3 |
| Publishing Rights | "I own the copyright and I hold the necessary publishing rights." |
| Primary Audience | Not for children (does not contain sexually explicit images or title) |
| Reading age range | leave blank (adult trade nonfiction) |
| Keywords | see §4 |
| Categories | see §5 |
| Pre-order | author-decision (see §7) |

**ISBN:** `978-1-80826-002-5` (already minted; on file in `metadata.yml`). KDP will additionally assign an ASIN at upload — that's automatic, not entered.

---

## 2. Manuscript and cover upload

| KDP field | File |
|---|---|
| Manuscript | `dist/no-one-did-it.epub` (epubcheck 0/0/0; Kindle Previewer Success) |
| Book cover | `book/design/epub/cover.jpg` (1600 × 2560, RGB sRGB, JPEG, 300 DPI, titled, author byline visible) |

Choose **"Use a cover I already have"** at the cover step. Do not use KDP Cover Creator.

---

## 3. Description (the Amazon product-page block)

KDP allows up to 4,000 characters and accepts a narrow HTML subset (`<b>`, `<i>`, `<em>`, `<strong>`, `<u>`, `<br>`, `<p>`, `<ol>`, `<ul>`, `<li>`, `<h4>`–`<h6>`). The description below is built from `book/proposals/overview.md` and stays well under the limit.

### Recommended description (~2,100 chars including HTML)

```html
<p><strong>Civilization did not stop sacrificing substitutes. It changed the altar.</strong></p>

<p>From temple to org chart, from org chart to legal entity, from legal entity to algorithm — and at each move, the part where someone announces <em>this one will carry it for us</em> goes further underground.</p>

<p><em>No One Did It</em> names that move — <strong>responsibility laundering</strong>: the recurring institutional method by which power keeps control and benefit while moving blame, liability, moral cost, and public suspicion onto a weaker bearer. A junior employee. A proxy. A contractor. A machine. A market. A committee. A procedure. A record.</p>

<p>Thirteen chapters install a forensic diagnostic, walk it across cases, and hand it over as a portable instrument:</p>

<ul>
<li><strong>Four shapes</strong> the laundering takes — pure scapegoat, partial scapegoat, system-or-object alibi, cost-bearing goat — installed against Reichstag 1933, Abu Ghraib, Therac-25 and Boeing 737 MAX, and the 17 March 2023 ICC warrants for the deportation of Ukrainian children.</li>
<li><strong>Eight questions</strong> that separate publicly named blame from actual responsibility — walked through Volkswagen Dieselgate and the Ford Pinto.</li>
<li><strong>Stress tests</strong> against contested modern terrain — Iraq WMD, second-term Trump-administration reverse-scapegoating, and the AI stack at three layers (training, deployment, evaluation), including <em>Bartz v. Anthropic</em> and the GPT-4o sycophancy incident.</li>
<li><strong>Anti-laundering rules</strong> drawn from law that already works — the Park doctrine, Sarbanes-Oxley §§ 302/906, the UK Senior Managers Regime, the Inquiries Act 2005 §21 — and three record-discipline rules: write it down; timestamp and chain-of-custody; make destruction visible.</li>
</ul>

<p>For readers of Timothy Snyder, Anne Applebaum, Adam Tooze, Jane Mayer, and Steve Coll.</p>

<p>Severe. Nonpartisan. Evidence-graded. Every claim graded A/B/C/D. Every named living individual described in procedural-stage language. Complete Chicago Manual of Style 17th edition Notes-Bibliography apparatus, 283 verified source-ledger cards across twelve documentary chapters. The discipline the book demands of the institutions it analyses is applied first to itself.</p>

<p><strong>"The model decided" is arriving, this decade, in the rooms that decide the loan, the job, the diagnosis, the benefit. The oldest move power knows has acquired its most modern instrument.</strong></p>
```

### Short-form description (~280 chars; for surfaces that truncate)

```
Civilization did not stop sacrificing substitutes — it changed the altar. From scapegoat rite to corporate org chart to AI model, No One Did It names how power keeps control while moving blame. Thirteen chapters, four shapes, eight questions. For readers of Snyder, Applebaum, Tooze.
```

---

## 4. Keywords (7 of 7 — KDP cap)

KDP allows up to **seven search-keyword phrases**, each up to 50 characters. They are not BISAC categories; they are the search terms Amazon will index the book against. Title words are already searchable, so the keywords should cover **adjacent** queries that the title doesn't.

Rationale for each slot is given so the author can swap with confidence.

| # | Keyword phrase | Chars | Why this slot |
|---|---|---|---|
| 1 | `accountability and power` | 24 | The conceptual shelf the book sits on; matches how the comp set (Snyder, Applebaum, Mayer) is searched. |
| 2 | `corporate scandals and cover-ups` | 32 | Catches readers searching the case material (Boeing, Bhopal, Volkswagen, Horizon) without naming any single case. |
| 3 | `AI ethics and governance` | 24 | Front-of-store relevance; chapter 10's three-layer AI treatment. Avoids the doom/boosterism shelves the audience brief explicitly disqualifies. |
| 4 | `political philosophy modern power` | 33 | The Tooze/Applebaum register; signals serious trade nonfiction, not pamphlet. |
| 5 | `history of justice and blame` | 28 | Long-horizon historical sweep (Leviticus 16 → algorithm); catches readers who arrived via the scapegoat lineage. |
| 6 | `whistleblowers and institutional failure` | 41 | The Horizon/Pentagon-Papers/Walsh/Chilcot record-survivor material in ch-7 and ch-12; practitioner-audience signal. |
| 7 | `nonfiction for fans of Timothy Snyder` | 38 | Comp-author keyword is a documented high-conversion pattern for trade nonfiction on Amazon. Use Snyder rather than Tooze: higher Amazon search volume, same shelf. |

**Avoid:** any partisan keyword ("Trump," "Biden," "Democrats," "Republicans") — the audience brief disqualifies that segment and partisan keywords trigger Amazon's adversarial-targeting flags. Also avoid "responsibility laundering" itself — it is already in the subtitle and Amazon indexes the subtitle.

---

## 5. Categories (3 slots, picked live in the KDP dashboard)

**What changed.** KDP retired BISAC-code entry in mid-2023. You no longer type or pick a BISAC code; you navigate Amazon's own browse tree inside the KDP dashboard and pick **3 categories** (the cap was raised from 2). BISAC codes are not part of the input — they only exist now as cross-references for the print-trade side of the listing, which KDP handles internally.

**Why this section is a method, not a list of paths.** Amazon's browse tree exceeds 14,000 leaves, shifts without notice, differs by marketplace (US tree ≠ UK tree ≠ DE tree), and contains a documented ~27% of "ghost categories" (categories that appear in the picker but never assign a bestseller badge) plus large numbers of near-duplicate leaves. The exact picker is gated behind KDP login. Any path I write here as a literal browse string would be a guess; the categories below are **named anchors verified against the live Amazon pages of the comp set** as of 2026-05-31. You select these in the picker by drilling down through the visible nodes whose leaf names match.

### Workflow gate

Before the category picker becomes useful, set the two upstream fields KDP uses to filter the visible tree:

1. **Primary Marketplace:** Amazon.com (US). The recommended categories below are verified on the US tree; UK/DE/JP trees differ and would need separate verification.
2. **Primary Audience:** Adult. Not for children. No sexually explicit content.

These two fields govern which leaves render in the picker. Wrong primary marketplace can hide the right leaves entirely.

### Comp-set verification (the method these recommendations come from)

The Kindlepreneur convention is: mirror the categories your closest comp titles already rank in. Verified leaves from the live Amazon US pages:

| Comp title | Kindle category leaves it appears in (verified 2026-05-31) |
|---|---|
| Snyder, *On Tyranny* | **Democracy** (Kindle Store), **Politics & Government** (Kindle Store), **Political Ideologies & Doctrines**, **20th Century World History** |
| Mayer, *Dark Money* | **Politics & Social Sciences**, **History › Americas › United States › 21st Century**, **Conservatism & Liberalism** (under Ideologies & Doctrines) |

The intersection of the two — and the leaves where the comp set's rankings are strongest (Snyder is #5 in Democracy Kindle Store, #9 in Politics & Government) — is the target set.

### Recommended 3 slots

1. **Democracy** (under Political Ideologies & Doctrines in the Kindle Store tree).
   Snyder ranks #5 here. The book's argument is structurally about how democratic accountability is laundered through procedure; this is the closest-fit leaf.

2. **Political Ideologies & Doctrines** (the parent of #1, plus where Mayer's Conservatism & Liberalism lives).
   Broader anchor; lower bestseller-badge probability than #1 but wider browse exposure. Sits in the Snyder + Applebaum + Mayer overlap.

3. **Politics & Government** (Kindle Store).
   Snyder ranks #9 here. High-traffic anchor; broadest of the three without falling to the un-rankable "Nonfiction" or "Politics & Social Sciences" parents.

### Reasons not to use a third hierarchy

The earlier draft of this section proposed a Business Ethics slot and an AI Ethics slot. The audience brief (`book/proposals/audience.md`) is explicit: the practitioner and AI-policy audiences are **secondary**, and the AI shelf invites the O'Neil/Crawford comp set the brief explicitly disqualifies. Spreading slots across three hierarchies dilutes the Snyder/Tooze positioning the book is built for. If the author later wants algorithmic-visibility breadth at the cost of positioning clarity, swap slot 3 for one of the alternates below.

### Alternate slots (if you want to swap one)

Verified-real leaves; pick by intent.

- **Philosophy › Political** — if the philosophical register is the public framing
- **History › World** (or **History › Modern**) — leans the long-horizon comparative-method side; high competition
- **Law › Legal History** — for the Park/SOX/SMCR/Inquiries Act material; narrow but loyal
- **Business & Money › Business Ethics** — for the practitioner audience if you decide to court it; risk noted above

### Do not pick

- "Nonfiction" or "Politics & Social Sciences" (the un-rankable parents — too broad)
- "True Crime" or "Conspiracies & Scandals" (mis-shelves, degrades also-boughts)
- "Current Events" (KDP's Current Events leaf is one of the documented ghost categories — appears in the picker, never awards a bestseller badge)
- Any single-politician or single-party leaf (the audience brief disqualifies partisan framing)

### Verification responsibility

These leaves are verified as of 2026-05-31. Amazon shifts the tree silently. Before clicking submit, click the "Best Sellers Rank" line on a live Snyder or Mayer Kindle page and confirm at least two of the three leaves above still exist on the comp's page — if either has been re-shelved, the recommendation needs re-triangulation.

---

## 6. Author Central — bio + author page setup

After upload, claim the title on Amazon Author Central. The bio block on the Author Central page is separate from the book listing; the version below is drawn from `book/back-matter/about-the-author.md` and tightened for the Author Central word budget (~1,200 chars works well; the cap is 4,000).

### Recommended Author Central bio

```
Li Xiaolai (@xiaolai) is a Chinese-language bestselling author, investor, and builder. Over more than twenty years he has published more than ten titles with cumulative sales above five million copies, several translated into Korean, Japanese, and traditional Chinese.

He has been self-employed since college — for seven years a teacher at New Oriental Education & Technology Group (NYSE: EDU), then independent. He is best known internationally for long-term Bitcoin holding and as the designer and strategy-maintainer of two Hong Kong-listed ETFs (3056.HK and 3112.HK).

He maintains a Chinese-language family-education community of more than ten thousand families, and a Chinese-language reading audience of comparable scale. The arrival of capable AI made building at this scale possible for him; he authors and maintains several open-source projects (vmark, claudepot, nlpm). The writing of No One Did It leaned heavily on tools he built himself.

A recent word fits well enough: solopreneur.

Site: lixiaolai.com  ·  GitHub: github.com/xiaolai
```

**Author photo:** use the same headshot Author Central is already configured with (if any) — otherwise upload a 300×300 to 600×600 JPEG/TIFF, RGB, light background per Amazon's spec.

---

## 7. Pricing, royalty, and KDP Select — author-decision

KDP asks five linked questions here; the answers are linked, so they should be decided together.

### 7.1 KDP Select enrollment (90-day exclusive)

| Choice | What it buys | What it costs |
|---|---|---|
| **Enrol in KDP Select** | Inclusion in Kindle Unlimited (reads pay per page, ~$0.0044/page in 2026; ~450 pages × $0.0044 = ~$1.98/full read), Kindle Owners' Lending Library; access to Kindle Countdown Deals and Free Book Promotions (up to 5 days per 90-day period). | 90-day Amazon exclusivity on the digital edition; cannot sell the EPUB on Apple Books, Google Play, Kobo, or your own site for 90 days. Auto-renews unless cancelled. |
| **Decline KDP Select** | Sell the EPUB freely on Apple/Google/Kobo/Smashwords/own site in parallel with Amazon. | No KU page-read income; no countdown deals; no free-promo days. |

**Recommendation framing, not recommendation:** the audience brief (Snyder/Tooze register) suggests buyers who purchase rather than borrow, which weakens the KU upside. The author has a substantial Chinese-language audience whose access to KU is irrelevant. Counterargument: KU promotion is the cheapest way to climb the also-boughts on Amazon early, and the practitioner secondary audience is partly KU-native. Author decides.

### 7.2 Royalty option

| Tier | Conditions | Royalty |
|---|---|---|
| **70%** | List price $2.99–$9.99 USD; .mobi file ≤ 10 MB (delivery fee deducted from royalty at $0.15/MB); available in select territories (US/UK/EU/AU/JP/CA/etc.). | 70% of list price, minus delivery fee. EPUB delivery fee for ~12.5 MB book ≈ $1.88 — eats meaningfully at $2.99; manageable at $9.99. |
| **35%** | Any list price ≥ $0.99; no delivery fee deducted. | 35% of list price. |

For a 12.5 MB EPUB priced **$9.99**: 70% tier nets ~$5.10/sale (after ~$1.88 delivery). 35% tier nets $3.50. 70% wins by ~$1.60 at this size.
For the same book priced **$14.99**: 35% tier nets ~$5.25; 70% is unavailable above $9.99. 35% wins.

**Recommendation framing:** the comp-set list-price band for first-edition serious trade nonfiction eBooks in 2026 is **$12.99–$16.99**. *On Tyranny* eBook at ~$11.99; *Twilight of Democracy* at ~$13.99; *Crashed* at ~$16.99. To stay in that band, the **35% royalty tier** is forced. To use the 70% tier, the list price has to drop to ≤$9.99, which underprices against the comp set and signals self-help adjacency the audience brief disqualifies. Recommend **35% tier, list price $12.99–$14.99**, but this is author-decision.

### 7.3 Territory rights

Default: "Worldwide rights — all territories." This is correct unless a foreign-rights deal is contemplated (none is, per `book/proposals/`).

### 7.4 Pricing per marketplace

KDP lets you set per-marketplace prices or auto-convert from US. Recommend **manual pricing on US, UK, DE, FR, ES, IT, NL, JP, BR, MX, IN, AU, CA** to set country-appropriate values (especially IN/BR/MX where comp pricing is far lower). The "set automatically" option underprices several markets.

### 7.5 Pre-order

Default: skip pre-order (book ships immediately). Pre-order is useful only if a launch sequence is planned; the author hasn't indicated one. If a pre-order *is* desired, the manuscript must be uploaded ≥ 10 weeks before sale date — uploading now would set the earliest sale date around 2026-08-10.

---

## 8. A+ Content (recommended; optional)

A+ Content is the rich-media block that renders below the description on the Amazon product page. Amazon's Author Central includes a free A+ module set; you build up to 7 modules per page. For serious trade nonfiction, four modules carry most of the value:

### Module 1 — Hero banner

- **Image:** cover front (use `book/design/epub/cover.jpg` resized to 970×600 px) on the left; right panel carries the headline.
- **Headline:** "Civilization did not stop sacrificing substitutes. It changed the altar."
- **Sub-copy (~80 chars):** "From the scapegoat rite to AI. Thirteen chapters. One forensic diagnostic."

### Module 2 — What's inside (four-shape taxonomy as a visual)

- **Format:** 2×2 image grid OR text-only 4-column comparison.
- **Headline:** "Four shapes responsibility laundering takes."
- **Cells:** (1) *Pure scapegoat* — Reichstag 1933; Sacco-Vanzetti. (2) *Partial scapegoat* — Abu Ghraib's seven convicted MPs. (3) *System-or-object alibi* — Therac-25; Boeing 737 MAX. (4) *Cost-bearing goat* — Ukrainian children, ICC arrest warrants 17 March 2023.
- Each cell: 25-word case description + the diagnostic question it answers.

### Module 3 — From the author

- **Headline:** "The discipline the book demands externally is applied first to itself."
- **Body (~600 chars):** 283 source-ledger cards. Every claim graded A/B/C/D. Every named living individual described in procedural-stage language. Complete Chicago Manual of Style 17th edition Notes-Bibliography apparatus. Two-year compositional cycle through a 13-agent forensic-review crew.
- **Photo:** author headshot.

### Module 4 — For readers of

- **Format:** comparison table.
- **Headline:** "For readers of Snyder, Applebaum, Tooze, Mayer, Coll."
- **Body:** four-row table — each row pairs a comp title with one line on what *No One Did It* adds. Lift directly from `book/proposals/comp-titles.md`.

**Optional fifth module — Field guide.** A snapshot of chapter 13's six artefacts, framed as "What you can do with this book the next morning." Use only if the practitioner audience is the primary launch target.

---

## 9. Upload checklist (the order of operations at KDP)

```
[ ] 1. Sign into KDP. New Title → Kindle eBook.
[ ] 2. Enter book details from §1 (language, title, subtitle, author, etc.).
[ ] 3. Paste description from §3.
[ ] 4. Add seven keywords from §4.
[ ] 5. Pick three categories from §5.
[ ] 6. Mark "Not for children" / no sexually explicit / age range blank.
[ ] 7. Decide pre-order (§7.5). Recommendation: skip.
[ ] 8. Next page — upload manuscript (dist/no-one-did-it.epub) and cover (book/design/epub/cover.jpg).
[ ] 9. Run Kindle Previewer in the KDP page (it re-validates against KFX; should pass — already pre-validated).
[ ] 10. ISBN: enter 978-1-80826-002-5; publisher: XIAOLAI BOOKS; publication date: keep blank (KDP sets at approval).
[ ] 11. Next page — KDP Select enrolment (§7.1). Author-decision.
[ ] 12. Territories: worldwide (§7.3).
[ ] 13. Royalty + list price (§7.2). Recommendation: 35% tier, $12.99–$14.99 US.
[ ] 14. Set per-marketplace prices (§7.4) — at minimum override IN, BR, MX, JP.
[ ] 15. Confirm content guidelines + publishing rights.
[ ] 16. Submit. Review window: 72 hours typical; up to 5 days for first-time accounts.
[ ] 17. Post-approval: claim title on Author Central; paste §6 bio; build §8 A+ modules.
[ ] 18. Copy live Amazon URL into README.md (RELEASE-PREP.md Step 5).
```

---

## 10. What this pack does not contain

- **Paperback (KDP Print) listing inputs.** The print PDFs (`dist/no-one-did-it-interior.pdf`, `dist/no-one-did-it-cover.pdf`) exist and would ship through the same KDP account under "Paperback" rather than "Kindle eBook." Trim size, page count (**451** as of 2026-05-31), spine width (**1.1275″** for 451 cream pages), and paper choice (cream) are pre-decided in `pipelines/print/`. Print ISBN: **978-1-80826-003-2** (distinct from the EPUB ISBN 978-1-80826-002-5). The listing fields above are largely the same; the differences (trim, paper, page count, separate ISBN) are not yet specified here. Add a section 11 if/when the paperback edition ships in the same release window.
- **Audiobook (ACX) production.** Audio-survivability is a craft constraint already honoured in v6 (rule 12, V10), but no audio production track exists.
- **Marketing collateral beyond Amazon.** Newsletter sequences, podcast pitches, sample-chapter campaigns — these were Blair's pre-decision deliverables; `book/proposals/pitch-letter.md` and `book/proposals/editor-pitch.md` retire to source-pool status per the 2026-05-30 direct-publish decision.
