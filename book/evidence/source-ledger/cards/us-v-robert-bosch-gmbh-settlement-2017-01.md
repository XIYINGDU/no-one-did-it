---
id: us-v-robert-bosch-gmbh-settlement-2017-01
source:
  title: United States v. Robert Bosch GmbH, civil settlement and DOJ-Bosch joint statement of facts, filed January 2017 (E.D. Mich. and N.D. Cal. multi-district docket)
  type: court-order
  publisher: U.S. District Court; U.S. Department of Justice; Federal Trade Commission
  author: U.S. Department of Justice; Robert Bosch GmbH
  publication_date: 2017-01-31
  url: https://www.justice.gov/archives/opa/pr/bosch-agrees-pay-327-5-million-resolve-claims-violations-clean-air-act
  archive:
    wayback_url: https://web.archive.org/web/20260527030528/https://www.justice.gov/archives/opa/pr/bosch-agrees-pay-327-5-million-resolve-claims-violations-clean-air-act
    wayback_captured: '2026-05-27'
  access_constraint: open-web
claim:
  text: 'The January 2017 settlement involving Robert Bosch GmbH — the tier-1 software supplier to Volkswagen for the EA189 engine control unit — records Bosch''s payment of approximately $327.5 million to resolve civil claims arising from its role in the Volkswagen diesel emissions matter. Public DOJ filings and the In re: Volkswagen Clean Diesel multidistrict litigation (MDL 2672, N.D. Cal.) record that Bosch personnel had communicated in writing to Volkswagen in 2007-2008 warning that the requested defeat-device software functionality could constitute an illegal defeat device under US law; Bosch also sought and received an indemnification letter from Volkswagen, the existence of which is referenced in DOJ filings supporting the Volkswagen AG plea agreement of 11 January 2017.'
  quote_alteration: none
  quote_permission: not-required-fair-use
  page_anchor: DOJ press release 11 Jan 2017 (Volkswagen + Bosch joint announcement); MDL 2672 (N.D. Cal.) consumer-class settlement filings
verification:
  evidence_grade: A
  grade_rationale: 'Primary court filings in the Volkswagen MDL (No. 2672, N.D. Cal.) and DOJ-announced civil settlement involving Bosch. The reference to Bosch''s 2007-2008 written warnings to Volkswagen appears in DOJ-Volkswagen filings as a fact Volkswagen has admitted; the Bosch warning is A-grade for the fact of the warning''s existence, B-grade for the precise wording of the underlying memos (which have not been publicly released in unredacted form per the case file). The chapter cites the warning''s existence (A) and characterises the wording (B) per the Statement of Facts.

    '
  verified_by: stephen
  verified_on: 2026-05-26
  body_sha256: bbdb027592e94e4980ed2c10a4b43988c824ad6df766dbbba20fba56996e53b8
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
    primary:
      url: https://www.justice.gov/archives/opa/pr/bosch-agrees-pay-327-5-million-resolve-claims-violations-clean-air-act
      status: not-found
      http_code: 404
    archive:
      url: https://web.archive.org/web/20260527030528/https://www.justice.gov/archives/opa/pr/bosch-agrees-pay-327-5-million-resolve-claims-violations-clean-air-act
      status: ok
      http_code: 200
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: DOJ press release 11 January 2017 announces the Bosch settlement as part of the broader Dieselgate enforcement package. MDL 2672 (N.D. Cal.) public docket records the Bosch settlement filings.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: A-grade for the fact of the settlement and the public-record reference to Bosch's 2007-2008 warnings to Volkswagen. The underlying Bosch warning memos themselves remain non-public per the vw-dieselgate case file open-question 5.
- step: url-correction
  actor: stephen
  timestamp: 2026-05-27 11:02:15+00:00
  outcome: PASS
  notes: Original URL was the Volkswagen AG plea press release (the wrong company); replaced with the canonical archived DOJ press release for the Bosch civil settlement ('Bosch Agrees to Pay $327.5 Million to Resolve Claims of Violations of the Clean Air Act'). Slug verified against the case description; live page returns 200 but JS-interstitial on scraping — Wayback fallback handles content verification.
dispute:
  status: undisputed
defamation:
  living_subjects: []
  nancy_cleared: true
  nancy_cleared_on: 2026-05-26
  nancy_notes: Corporate-respondent card. Robert Bosch GmbH is a corporate entity, not a living individual. Bosch personnel who authored the 2007-2008 warning memos are referenced only by position descriptors in public DOJ filings; the chapter does not name individuals based on these descriptors. Inherits ch-03 Nancy gate clearance from chapter promotion 2026-05-26.
references:
  cases_affected:
  - vw-dieselgate
  chapters_citing:
  - 03-who-could-have-stopped-it
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: null
---

# United States v. Robert Bosch GmbH — January 2017 settlement and supplier warning record

The card anchors the chapter-3 hidden-architecture (Q4 knowledge) references to the Bosch
supplier settlement and the 2007-2008 written warnings Bosch sent Volkswagen.

## Why this card exists

Chapter 3 cites the Bosch settlement at two anchor occurrences (lines 71 and 137) as the
supplier-side primary-source record of upstream knowledge in the Dieselgate chain. The Bosch
warning is one of the chapter's strongest Q4 anchors because it documents that the cheating was
flagged by a third party with a documentary trail before deployment continued.

## Diagnostic significance

The Bosch warning extends the chain upward and outward from the named Volkswagen engineers
already convicted (Liang, Schmidt) to a supplier that put its concerns in writing. The chapter
uses this as evidence that the cost-bearer dimension of the diagnostic must also account for the
risk taken on by the supplier when commercial pressure overrides written warnings.
