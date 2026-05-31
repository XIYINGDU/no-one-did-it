# URL Verification Report — 2026-05-28

Owner: scripts/verify_card_urls.py (run by jerry-crew-chief)
Task: Verify primary + Wayback URLs in 283 source-ledger cards.
Inputs reviewed: `book/source-ledger/cards/*.md` (283 files)
Output: this report; cards updated with `verification.url_check` block (updated_in_place=283)
Evidence grade: N/A (operational check)
Assumptions: checkpoint is principal-author-cn (subject to GFW). URLs on known-blocked domains are reported as `pending-other-checkpoint` rather than `unreachable` on a single failure.
Open questions: any URL marked `pending-other-checkpoint` should be re-run from an unblocked checkpoint; any `not-found` whose archive is also broken should be re-sourced or re-archived via Wayback's Save Page Now.

## Summary

- Cards checked: **283**
- Cards with no URL fields: **15**
- Cards updated in place: **283**

### Primary URL status

| Status | Count |
|---|---:|
| `ok` | 200 |
| `forbidden` | 32 |
| `redirect` | 25 |
| `not-found` | 5 |
| `unreachable` | 3 |
| `pending-other-checkpoint` | 2 |
| `server-error` | 1 |
| **total** | **268** |

### Archive URL status

| Status | Count |
|---|---:|
| `ok` | 254 |
| `redirect` | 3 |
| `forbidden` | 2 |
| **total** | **259** |

## Action items

### Primary URL broken AND archive missing / also broken — re-source (0)

None.

### Primary URL broken but archive OK — demote primary, keep archive (6)

- `doj-boeing-npa-resolution-2025-05-23`
    - primary: not-found · HTTP 404
    - archive: ok · HTTP 200
- `genocide-convention-1948-art-ii-e`
    - primary: not-found · HTTP 404
    - archive: ok · HTTP 200
- `lowell-committee-report-1927-07-27`
    - primary: not-found · HTTP 404
    - archive: ok · HTTP 200
- `us-v-robert-bosch-gmbh-settlement-2017-01`
    - primary: not-found · HTTP 404
    - archive: ok · HTTP 200
- `us-v-slough-641-f3d-544-dc-cir-2011`
    - primary: not-found · HTTP 410 · HTTP 410 Gone
    - archive: ok · HTTP 200
- `venice-commission-opinion-762-2014-crimea-referendum`
    - primary: server-error · HTTP 502
    - archive: ok · HTTP 200

### Pending other-checkpoint re-verification (2)

These URLs returned timeout/connection error from the principal-author-cn checkpoint; the domain is on the GFW-suspect list. Re-run `scripts/verify_card_urls.py` from a different network (or rely on the archive URL which generally remains reachable).

- `abu-ghraib-courts-martial-and-karpinski-demotion-2004-2005`
    - primary: pending-other-checkpoint · The read operation timed out
- `nielsen-tweet-no-policy-2018-06-17`
    - primary: pending-other-checkpoint · The read operation timed out

## Cards with no URL fields

- `agents-md-core-diagnostic`
- `agents-md-eight-question-diagnostic`
- `anchor-bible-dictionary-atonement-kuppuru`
- `arthur-d-little-bhopal-1988`
- `bhopal-cost-bearer-evidence-cluster`
- `boeing-omb-tbc-19-2018-11-06`
- `cullen-maakestad-cavender-corporate-crime-under-attack-1987`
- `cuomo-eo-144-special-prosecutor-termination-1990`
- `iraqi-moi-nisour-square-findings-2007`
- `kalelkar-report-1985`
- `nielsen-dhs-memorandum-2018-05-04`
- `reichsgericht-judgment-23-dec-1933-saechsisches-staatsarchiv`
- `senate-psi-family-separation-2020-10`
- `tower-commission-report-1987-02`
- `ucc-may-1982-operational-safety-survey-bhopal`

## Handoff

- stephen-fact-check-director — re-source any `Primary URL broken AND archive missing / also broken` items; trigger Wayback Save-Page-Now for any `Primary broken / archive OK` items where the primary is genuinely gone (so the archive captures the current state before further drift).
- principal-author or any non-CN checkpoint — re-run `scripts/verify_card_urls.py` to close the `Pending other-checkpoint` list.
