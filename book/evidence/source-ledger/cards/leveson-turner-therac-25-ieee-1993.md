---
id: leveson-turner-therac-25-ieee-1993
source:
  title: 'Nancy G. Leveson and Clark S. Turner, "An Investigation of the Therac-25 Accidents," IEEE Computer 26(7): 18-41 (July 1993); republished with the full reconstruction in Nancy G. Leveson, "Safeware: System Safety and Computers," Appendix A (Addison-Wesley, 1995)

    '
  type: academic-peer-reviewed
  publisher: IEEE Computer Society / Addison-Wesley
  author: Nancy G. Leveson and Clark S. Turner
  publication_date: 1993-07
  url: https://dl.acm.org/doi/10.1109/MC.1993.274940
  archive:
    wayback_url: http://web.archive.org/web/20250311090632/https://dl.acm.org/doi/10.1109/MC.1993.274940
    wayback_captured: '2025-03-11'
  access_constraint: open-web
claim:
  text: Leveson and Turner's 1993 IEEE Computer investigation reconstructed the six Therac-25 radiation-therapy overdose accidents between June 1985 and January 1987 (Table 1), identified the race condition between the Treat task and the keyboard-handler task on shared state variables as the proximate software cause, and documented the patient quote (Ray Cox, East Texas Cancer Center, 21 March 1986) about being hit 'between the shoulders with a baseball bat.' The reconstruction was republished with expanded reverse-engineering detail in Leveson's 1995 monograph Safeware (Appendix A).
  quote_verbatim: between the shoulders with a baseball bat
  quote_alteration: none
  quote_permission: not-required-fair-use
  page_anchor: IEEE Computer 26(7) (July 1993) pp. 18-41; Table 1; Safeware (1995) Appendix A
verification:
  evidence_grade: A
  grade_rationale: 'Peer-reviewed engineering forensics in IEEE Computer (refereed) plus standard-monograph treatment in Leveson''s Safeware (Addison-Wesley). The Leveson-Turner reconstruction is the load-bearing source on Therac-25 in the software-safety literature; cited as definitive in subsequent FDA case studies, the IEEE software-engineering curriculum, and follow-on research. A-grade for the operative facts the chapter draws on (accident timeline, race condition, patient quote, design choices that removed hardware interlocks).

    '
  verified_by: stephen
  verified_on: 2026-05-26
  url_check:
    verified_on: '2026-05-28'
    verifier_checkpoint: principal-author-cn
    primary:
      url: https://dl.acm.org/doi/10.1109/MC.1993.274940
      status: forbidden
      http_code: 403
      error: HTTP 403 Forbidden
    archive:
      url: http://web.archive.org/web/20250311090632/https://dl.acm.org/doi/10.1109/MC.1993.274940
      status: ok
      http_code: 200
verification_log:
- step: source-existence
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: IEEE Computer paper widely hosted (MIT 6.033 course materials, university coursepacks); Safeware monograph in print.
- step: independent-corroboration
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: PASS
  notes: Corroborated by FDA recall correspondence, ECRI investigative report (1987), and subsequent software-safety scholarship.
- step: grade-assignment
  actor: stephen
  timestamp: 2026-05-26 00:00:00+00:00
  outcome: A
  notes: A-grade peer-reviewed engineering investigation plus standard monograph.
dispute:
  status: undisputed
defamation:
  living_subjects:
  - Nancy G. Leveson
  - Clark S. Turner
  nancy_cleared: true
  nancy_cleared_on: 2026-05-26
  nancy_notes: Authors named in their scholarly capacity. No defamation surface. The Cox quote is reported as Leveson and Turner preserved it; the chapter inherits ch-2 Nancy gate clearance.
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

# Leveson & Turner — Therac-25 IEEE Computer investigation (July 1993) / Safeware (1995)

Anchors chapter 2 system/object-alibi opening case: the Cox "between the shoulders" quote,
the Table 1 accident timeline, and the race-condition reconstruction.

Url updated 2026-05-26 by stephen: the prior MIT 6.033 course coursepack URL now
returns 404 (course materials rotated). Replaced with the canonical ACM Digital
Library DOI page for IEEE Computer 26(7), 1993, doi:10.1109/MC.1993.274940 — the
authoritative publisher record for the original IEEE article. The course-pack
copies (Columbia CS, Bowdoin, MIT sunnyday) remain reachable as open-web mirrors;
the DOI URL is the permanent citation.
