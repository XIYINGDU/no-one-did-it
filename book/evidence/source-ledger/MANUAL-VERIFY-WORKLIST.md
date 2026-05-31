# Manual source-verification worklist — owner verification complete (2026-05-27)

> Status: all 16 cards from the original worklist have been processed by the
> card owner. URLs that needed replacement have been updated; sources that
> needed manual archival have been saved to the personal verification archive
> at `book/evidence/source-ledger/human-verification-files/` (gitignored). Each card's
> `verification_log` carries an entry with `actor: xaiolai` and the date of
> manual verification.

## Final disposition

### 1. NYT — owner-verified via personal subscription (2/2)

| Card | Status | Notes |
|---|---|---|
| `bumiller-nyt-whig-2002-09-07` | ✓ owner-verified | Title corrected to "Traces of Terror: The Strategy; Bush Aides Set Strategy to Sell Policy on Iraq"; URL corrected to `/us/` path (was `/world/`); personal PDF saved. |
| `burnham-nyt-1970-04-25-graft-paid-to-police` | ✓ owner-verified | URL corrected to `survey-links.html` suffix (was `police-graft-in.html`); personal PDF saved. |

NYT bodies remain bot-unfetchable (paywall + GFW). Card grade stays A; verification rests on owner reading the live archive against the live subscription, recorded in `verification_log`.

### 2. The Times UK Downing Street Memo — upgraded to free primary (1/1)

| Card | Status | Notes |
|---|---|---|
| `downing-street-memo-2002-07-23-published-2005-05-01` | ✓ URL upgraded, sha256 + Wayback captured | Switched from paywalled `thetimes.co.uk` to George Washington University National Security Archive (NSAEBB 328, Doc. 14) — free, publicly hosted scan of the original Rycroft minute. Access constraint: paywall → open-web. The Sunday Times stays the publication of record; GWU NSAEBB is the primary-source URL. |

### 3. URL upgrades (better primary sources) with full sha256 + Wayback (5/5)

| Card | New URL | Result |
|---|---|---|
| `tower-commission-report-1987` | archive.org `_djvu.txt` full-text | sha256 + Wayback |
| `cooper-crew-doge-preservation-order-2025-03` | citizensforethics.org Order-on-Reconsideration PDF | sha256 + Wayback |
| `yale-hrl-conflict-observatory-ukrainian-children-2023-02-14` | `medicine.yale.edu` permanent page | sha256 + Wayback |
| `budapest-memorandum-1994` | UN Treaty Series Volume 3007 PDF | sha256 + Wayback |
| `putin-lvova-belova-public-defence-of-transfers-2022-2023` | `tass.com/society/1509049` | sha256 + Wayback |

### 4. Owner-verified, URL unchanged (3/3)

| Card | Result |
|---|---|
| `h-res-755-articles-of-impeachment-2019-12-18` | already fetchable; owner-verified entry added |
| `eiga-1978-title-vi-independent-counsel` | already fetchable; owner-verified entry added |
| `bybee-yoo-olc-torture-memos-2002-opr-2009` | already fetchable; owner-verified entry added |
| `milgrom-1991-anchor-bible-leviticus-azazel` | already fetchable; owner-verified entry added |
| `al-janabi-curveball-guardian-interview-2011-02-15` | owner-verified entry added; personal PDF saved |
| `j6-prosecution-dismissal-coverage-2025` | owner-verified; WaPo + Stanford Law podcast added as supplementary corroboration |

### 5. Honest downgrades

| Card | Issue | Resolution |
|---|---|---|
| `ross-memorandum-citizenship-question-2018-03-26` | Previously-cited DocumentCloud URL (id 4426203, slug `Wilbur-Ross-Memo-Citizenship-Question-March-26-2018`) is **mis-slugged** — actually serves an unrelated Dutch FOIA document about Tata Steel. Standalone free-web PDF of the actual Ross memo not located. | URL changed to Lawyers' Committee litigation landing page (secondary, freely accessible); `access_constraint` downgraded to `paywalled-archive`. Primary memo is reproduced as exhibit in 18-966 court record (verifiable through PACER/SCOTUSblog). Stephen anchor: locate a stable public primary PDF or set `access_constraint: sealed`. |
| `evans-2003-coming-of-third-reich-ch1` | Archive.org page does not allow downloading; owner used personal epub copy. | Card URL unchanged (archive.org catalog page); owner-verified via personal epub (gitignored). |
| `capitol-police-labor-committee-statement-2025-01-21` | Primary statement URL not located on live web or in Wayback. | URL changed to Wikipedia article on the J6 pardons (open-web, secondary). Grade may need Stephen review (likely downgrade to B). |

## Final link-integrity coverage (283 cards)

After this owner-verified pass:

| Metric | Coverage |
|---|---:|
| sha256 fingerprint | **219/283 (77%)** |
| real Wayback snapshot | **261/283 (92%)** |

## Verification archive

The card owner's personal copies of the source artifacts (PDFs, epubs, txt
extractions) are stored under `book/evidence/source-ledger/human-verification-files/`.
That directory is **gitignored** (it contains licensed/copyrighted material
such as NYT articles and the Evans epub; never to be redistributed) and exists
purely as a local backup against link-rot for the owner's own use.

## Open Stephen-anchor items

1. **Ross memo primary PDF** — locate a stable free-web URL or mark sealed.
2. **Capitol Police Labor Committee statement** — find a primary URL (committee
   site, news outlet that quoted the statement) or accept Wikipedia secondary.
