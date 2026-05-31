---
id: fda-therac-25-recall-and-cap-1986-1987
source:
  title: U.S. Food and Drug Administration, Therac-25 Medical Device Report and recall correspondence (Apr.-May 1986); FDA Class I recall designation and Corrective Action Plan (Feb. 1987), Atomic Energy of Canada Limited Medical Division
  type: regulation
  publisher: U.S. Food and Drug Administration, Center for Devices and Radiological Health
  author: U.S. Food and Drug Administration
  publication_date: 1987-02
  url: https://onlineethics.org/cases/therac-25/history-introduction-and-shut-down-therac-25
  archive:
    wayback_url: http://web.archive.org/web/20260526080222/https://onlineethics.org/cases/therac-25/history-introduction-and-shut-down-therac-25
    wayback_captured: '2026-05-26'
  access_constraint: open-web
claim:
  text: AECL filed a Medical Device Report with the FDA on 15 April 1986 after the second East Texas Cancer Center accident. The FDA declared the Therac-25 defective on 2 May 1986 and ultimately designated the recall as Class I — the FDA's highest severity tier, reserved for products with a reasonable probability of causing serious adverse health consequences or death. AECL's initial 'fix' (disabling the Up-Arrow editing key) did not address the underlying race condition; a sixth accident at Yakima Valley Memorial Hospital in January 1987 occurred under the supposedly-fixed software. The FDA's February 1987 Corrective Action Plan forced AECL into a comprehensive hardware-and-software redesign, including reinstating the independent hardware interlocks the Therac-25 had removed from its predecessor models.
  quote_alteration: none
  quote_permission: not-applicable
  page_anchor: FDA MDR filing 15 Apr. 1986; defective-device declaration 2 May 1986; Class I recall; CAP Feb. 1987
verification:
  evidence_grade: A
  grade_rationale: 'Primary U.S. regulator action by FDA / Center for Devices and Radiological Health. The recall sequence and CAP are documented in FDA records and reconstructed in detail in Leveson & Turner (1993) Appendix and Leveson Safeware (1995) Appendix A. A-grade.

    '
  verified_by: stephen
  verified_on: 2026-05-26
  body_sha256: 43b15bc7a5f37f54c84d60d1ce67f1b277770e7380ba1bc54b6db88365713c2a
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
    primary:
      url: https://onlineethics.org/cases/therac-25/history-introduction-and-shut-down-therac-25
      status: ok
      http_code: 200
    archive:
      url: http://web.archive.org/web/20260526080222/https://onlineethics.org/cases/therac-25/history-introduction-and-shut-down-therac-25
      status: ok
      http_code: 200
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: FDA recall record publicly indexed; full correspondence reconstructed in Leveson-Turner 1993.
- step: independent-corroboration
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Corroborated by Leveson-Turner (1993), Leveson (1995), ECRI investigation (1987).
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: A-grade primary regulator action.
dispute:
  status: undisputed
defamation:
  living_subjects: []
  nancy_cleared: true
  nancy_cleared_on: 2026-05-26
  nancy_notes: Regulator-action card. Corporate subject (AECL Medical Division, since wound down). No individual living subject in defamation surface.
references:
  cases_affected:
  - therac-25
  chapters_citing:
  - 02-the-four-goats
provenance:
  created_by: stephen
  created_on: 2026-05-26
  superseded_by: null
---

# FDA Therac-25 recall and Corrective Action Plan (1986-1987)

Anchors chapter 2 system/object-alibi case: the FDA regulator's escalation from MDR receipt to
Class I recall to the February 1987 CAP that forced the comprehensive redesign.

Url updated 2026-05-26 by stephen: the fda.gov current-recalls landing page (404) does not
host the 1986-1987 Therac-25 recall records, which predate FDA's online archive. Replaced
with the Online Ethics Center (NSF/NAE-supported repository) detailed Therac-25 case page,
which is the standard scholarly reference reproducing the FDA correspondence sequence (MDR
filing 15 Apr 1986; defective-device declaration 2 May 1986; Feb 1987 CAP). The primary FDA
correspondence record itself is reconstructed in Leveson & Turner (1993) IEEE Computer
Appendix and Leveson Safeware (1995) Appendix A — both already cited in the card's
verification_log as A-grade corroborating sources.
