---
status: ready
case_id: therac-25
case: Therac-25 radiation-therapy overdoses
domain: medical devices / software safety engineering / regulatory failure
case_type: system/object alibi
evidence_grade: A
owner: shirley-historical-case-researcher
handoff: stephen-fact-check-director
chapter: 02-four-goats
last_updated: 2026-05-26
sources:
  - card_id: leveson-turner-therac-25-ieee-1993
    used_for: "Canonical technical reconstruction of the six 1985-1987 overdose accidents, race condition between Treat and keyboard-handler tasks, Ray Cox 'baseball bat' patient quote, removal of independent hardware interlocks from predecessors; expanded in Safeware (1995) Appendix A."
  - card_id: fda-therac-25-recall-and-cap-1986-1987
    used_for: "FDA primary regulator record: AECL MDR filing April 15 1986, FDA 'declared defective' May 2 1986, Class I designation (FDA's highest severity tier), and the February 1987 Corrective Action Plan correspondence that forced AECL into comprehensive hardware-and-software redesign including reinstated interlocks."
unwired_sources:
  - "ECRI, 'Therac-25 Accelerator Patient Treatment System,' Health Devices vol. 16 no. 4 (1987) — cross-site investigative bridge"
  - "Stephanie Saul, 'Casualties of a Healing Machine,' Newsday multi-part investigation 1986 (Tier-3 period press; Delon to confirm full citation)"
  - "Cox v Atomic Energy of Canada Limited (East Texas, 1986) — pre-trial filings (Delon to retrieve via Texas state court records)"
  - "Leveson, 'The Therac-25: 30 Years Later,' IEEE Computer 50(11): 8-11 (Nov 2017) — retrospective"
  - "Ontario Cancer Foundation Clinic / Ontario coroner's office inquest records, 1985-87 (Delon to source)"
  - "CGR engineering records via French medical-device regulatory archives (Delon to source)"
---

# Therac-25 — Case File

Case name: Therac-25 radiation-therapy machine overdose accidents (AECL / CGR)
Domain: medical devices / software safety engineering / FDA regulatory failure
Dates and place: June 3, 1985 (Kennestone Regional Oncology Center, Marietta, Georgia — first documented overdose) through January 17, 1987 (Yakima Valley Memorial Hospital, Yakima, Washington — sixth and final documented accident). Other accident sites: Ontario Cancer Foundation Clinic (Hamilton, Ontario, July 26, 1985); Yakima Valley Memorial Hospital (December 1985, first incident); East Texas Cancer Center (Tyler, Texas — March 21, 1986 and April 11, 1986). Manufacturer: Atomic Energy of Canada Limited (AECL) Medical Division, in collaboration with the French firm CGR.
Case type: system/object alibi

Classification note: The Therac-25 case is the cleanest documented instance in the 20th-century technical record of a system/object alibi pattern around a software-driven machine. AECL's first response to each accident was that the machine "could not" deliver the dose the operator and physicist reports described. Hospital physicists who reconstructed the accidents were told the machine was working as designed; operators were told their console errors were the issue; the FDA was told incidents were isolated. Only after Leveson & Turner's investigation reconstructed the race condition in the operator-console state machine and the removed hardware interlocks did the alibi weaken. The named cause shifted across the lifetime of the laundering: first "operator error", then "machine malfunction", then — only when forced — "design choices made by named people at AECL." The three layers correspond directly to the four blame-container moves the book's diagnostic identifies.

```text
Crisis:
Between June 1985 and January 1987, six patients receiving radiation
therapy from Therac-25 medical linear accelerators were given massive
radiation overdoses — in some incidents, doses estimated at 15,000–
25,000 rad to small body regions, where the prescribed treatment was
180 rad (Leveson & Turner 1993, p. 18, table 1). At least three patients
died of injuries directly attributable to the overdoses: Ray Cox (East
Texas Cancer Center, March 21, 1986; died of complications in September
1986); Verdon Kidd (Kennestone, June 3, 1985 — the first documented
case; Kidd died of cancer; whether the overdose was the proximate cause
remains disputed in the medical record); Glen Dodd (Yakima, January
17, 1987; died approximately three weeks later). Patients who survived
suffered severe radiation burns, paralysis, loss of limbs, and chronic
pain. The Therac-25 was the dual-mode successor to the Therac-6 and
Therac-20; the model removed the independent hardware interlocks that
had backstopped its predecessors' software.

Official story:
AECL's response across the first five accidents followed a consistent
template: (a) the machine "could not" have delivered the doses
described; (b) the operator must have misread the dose display or the
patient must have moved; (c) the incident was unique and not
reproducible. After the second East Texas accident (April 11, 1986),
hospital physicist Fritz Hager and AECL technician spent days
reproducing the exact keystroke sequence that triggered the dose, at
which point AECL acknowledged a software issue but characterised it as
narrow. AECL filed a Medical Device Report (MDR) with the FDA on April
15, 1986 (after the second Tyler accident); the FDA then declared the
Therac-25 defective on May 2, 1986, initiating what was ultimately
designated a Class I recall — the FDA's highest severity classification,
reserved for situations with a reasonable probability of serious adverse
health consequences or death. AECL responded with a "fix" that disabled
the Up-Arrow editing key on the operator console. Subsequent
investigation showed the underlying race condition was unaddressed by
that fix, and the Yakima accident of January 1987 occurred under the
supposedly-fixed software. Only after the FDA's stronger Corrective
Action Plan (CAP) requirements of February 1987 did AECL undertake a
comprehensive hardware-and-software redesign, including reinstating
independent hardware interlocks.

Blame container:
Three sequential blame containers, in this order:

1. The operators. AECL initially attributed the East Texas accidents to
   operator console error. The operator at Tyler, Mary Beth, became the
   focus of internal AECL analysis; she had pressed Up-Arrow to correct
   a treatment-mode entry, a sequence that — combined with the race
   condition — caused the magnetic-field-shaping electronics to remain
   in electron-beam-bending position while the high-current X-ray
   target was withdrawn. The operators were experienced, the consoles
   reported no error, and AECL's framing put the cost of explanation on
   them.

2. The machine. After operator error became untenable (multiple sites,
   experienced operators, identical symptoms), the framing shifted to
   "Therac-25 malfunction" — language that treats the device as the
   agent. FDA recall language and AECL field-service notices used
   passive constructions: "the machine produced", "the system
   delivered", "an erroneous dose was administered."

3. The unnamed software bug. When forced to acknowledge software, AECL
   characterised it as a defect — an isolated programming error — rather
   than as the predictable outcome of design choices that were made by
   identifiable people: a single programmer writing safety-critical
   real-time code without independent verification, the elimination of
   hardware interlocks that had backstopped earlier models, and the
   absence of any systematic hazard analysis. The "bug" framing kept the
   container at the level of the artifact, never climbing to the people
   who designed the artifact's safety architecture.

[Evidence grade: A — Leveson & Turner 1993; Leveson 1995, Appendix A; FDA
recall and CAP correspondence; ECRI investigative report (1987).]

Actual responsibility chain:

  Control:
  AECL Medical Division — design and software architecture of the
  Therac-25. AECL inherited code from the Therac-6 and Therac-20 (the
  predecessor machines) and modified it for the dual-mode 25; the
  modifications removed the hardware interlocks that had masked
  software faults in the earlier machines. A single programmer (named
  in Leveson's investigation but not publicly identified beyond
  Leveson's interview record) wrote and maintained the safety-critical
  PDP-11 assembly code. AECL's quality-assurance review of that code
  was minimal; no independent verification was performed; no formal
  hazard analysis was conducted on the software. AECL's response
  process — the loop from accident report to engineering review to
  customer notification — controlled what hospitals knew and when.

  Benefit:
  AECL Medical Division — sale of approximately 11 Therac-25 units
  across North America at substantial unit prices; market position in
  dual-mode linear accelerators; protection of the Therac product line
  from regulatory restriction. AECL parent corporation (the Canadian
  Crown corporation) preserved the medical division as a going concern
  through the recall period.

  Knowledge:
  By July 1985 — after the Hamilton, Ontario accident at the Ontario
  Cancer Foundation Clinic — AECL had a second documented serious
  incident with the same machine type. By December 1985 (Yakima first
  incident) it had a third. By March 1986 (first Tyler), a fourth. The
  pattern of repeated similar-symptom overdoses across geographically
  separated sites was visible to AECL well before the FDA recall.
  Internal AECL field-service records (subpoenaed in the Cox litigation
  and partially reproduced in Leveson & Turner 1993) document the
  pattern recognition that was not communicated to other Therac-25
  customer sites until the FDA forced disclosure.

  Preventability:
  The accidents were preventable at multiple points:
  - Pre-deployment: Retention of independent hardware interlocks (as in
    the Therac-6 and Therac-20) would have prevented the race condition
    from producing patient harm regardless of software state.
  - Pre-deployment: Independent verification of the safety-critical
    software by a second engineer or external review would have
    surfaced the lack of mutual exclusion on the shared state
    variables.
  - During the accident sequence: Disclosure to all Therac-25 customer
    sites after the second documented overdose (Hamilton, July 1985)
    would have permitted defensive operator protocols and likely
    prevented at least three of the six accidents.
  - Post-East-Texas: A comprehensive software audit after the March
    1986 accident — rather than the narrow Up-Arrow disabling — would
    have prevented the Yakima 1987 accident.

  Record controller:
  AECL controlled (i) the source code, (ii) the field-service incident
  database, (iii) the customer notification process, (iv) the
  engineering hazard analyses (which did not exist as standalone
  documents at the time of deployment). FDA Center for Devices and
  Radiological Health controlled the recall record and the CAP
  correspondence; FDA records are FOIA-accessible. Hospital physicists
  (Fritz Hager at East Texas; the Yakima physics staff; the Ontario
  staff) controlled the local accident-reconstruction records, which
  proved load-bearing once Leveson aggregated them. ECRI (Emergency
  Care Research Institute) controlled the cross-site investigative
  record that bridged hospital physics reports to a publishable
  account.

  Cost bearer:
  Six named patients: Verdon Kidd (Kennestone, 1985); the Hamilton
  patient (name not publicly disclosed; severe injury, died of cancer);
  Voyne Ray Cox (Tyler, March 21, 1986; died Sept 1986); the second
  Tyler patient (April 11, 1986; survived with severe injury); Glen A.
  Dodd (Yakima, January 17, 1987; died Feb 1987); and the second
  Yakima patient (December 1985; severe shoulder/neck injuries). The
  operators — particularly the Tyler operator initially blamed — bore
  reputational and psychological cost during the months when AECL was
  attributing accidents to console error. Hospital physicists who
  reconstructed the accidents bore the institutional cost of
  contradicting the manufacturer's account.

How the alibi hardened:
1. AECL's authoritative position as manufacturer: hospitals trusted that
   the manufacturer's diagnostic was more reliable than the operator's
   account. The information asymmetry around the machine's internal
   behavior was extreme — only AECL had the source code.
2. The Therac-25's clean prior service record: by mid-1985 the machine
   had operated safely at multiple sites for over a year. AECL pointed
   to the install base as evidence that single-site complaints were
   anomalies.
3. Removal of hardware interlocks invisible to operators: hospitals were
   not informed during the procurement process that the Therac-25
   removed the independent dose-monitor interlocks of the Therac-20.
   Operators believed they had hardware backstop they did not have.
4. The "could not" rhetoric: AECL's engineering responses across the
   first three accidents asserted that the dose described was
   impossible given the machine's design. This is the system/object
   alibi in its purest form — the artifact is reified as the authority
   on its own behavior.
5. Regulatory under-readiness: the FDA in 1985–86 had no software-
   specific review process for medical-device firmware. The 510(k)
   premarket clearance had treated Therac-25 as a predicate-device
   update from the Therac-20.

How the alibi weakened:
1. Hager, Fritz (medical physicist, East Texas Cancer Center) — managed
   to reproduce the exact keystroke sequence that triggered the second
   Tyler overdose, working with the operator over multiple days in April
   1986. This reconstruction forced AECL to acknowledge a reproducible
   software state-machine fault.
2. ECRI. "Therac-25 Accelerator Patient Treatment System." *Health
   Devices*, vol. 16, no. 4, 1987. ECRI's institutional bridge between
   isolated hospital physics reports and a publishable cross-site
   account opened the record.
3. FDA Class I recall (AECL's MDR filing April 15, 1986; FDA declared
   the device defective May 2, 1986; ultimately classified Class I —
   the FDA's highest severity tier) and Corrective Action Plan
   (February 1987). The FDA's CAP requirements forced AECL into
   comprehensive hardware-and-software redesign, including reinstated
   interlocks; FDA correspondence with AECL across 1986–87 documents
   AECL's reluctance to undertake the full redesign.
4. Leveson, Nancy G., and Clark S. Turner. "An Investigation of the
   Therac-25 Accidents." IEEE *Computer*, vol. 26, no. 7, July 1993,
   pp. 18–41. The canonical reconstruction: identified the race
   condition between the Treat task and the keyboard-handler task on
   shared state variables, documented AECL's response-pattern failures,
   placed the case in the broader frame of safety-critical software
   engineering. Re-published and extended in Leveson, *Safeware*,
   Addison-Wesley, 1995, Appendix A.
5. The Cox v AECL litigation (settled out of court; precise terms
   sealed). The pre-trial discovery produced the AECL internal
   field-service incident records that Leveson later cited.

Best counterargument:
"Therac-25 is a software-engineering teaching case, not a responsibility-
laundering case. The fault was technical — a race condition in real-time
code — and the resolution was technical (interlocks, redesign, FDA
software-review processes). Calling it 'system/object alibi' over-reads
a routine engineering failure and a routine post-incident regulatory
response. AECL was not 'hiding' from blame; it was running the diagnostic
loop that every medical-device manufacturer runs, and that loop
eventually produced the right answer."

Shirley's response: The technical reconstruction (Leveson 1993) is not
in dispute. What the counterargument elides is the eighteen-month gap
between the first documented serious overdose (June 1985) and the Yakima
accident (January 1987), during which AECL ran the diagnostic loop in
the direction least costly to itself — operator first, machine second,
software last — and disclosed less to other customer sites than the
pattern warranted. The system/object alibi diagnosis sits at the
intersection of three documented facts: (a) AECL's "could not" rhetoric
across the first three accidents; (b) the eighteen-month non-disclosure
pattern; (c) the absence, at deployment, of independent verification or
hazard analysis on the safety-critical code, paired with the removal of
the hardware interlocks that had absorbed the consequences of similar
faults in predecessor machines. The fault was technical; the laundering
was the institutional response that kept the named cause at the level of
the artifact for as long as the record permitted.

Evidence grade: A
- Leveson & Turner 1993 (IEEE Computer, peer-reviewed): A. The canonical
  technical reconstruction.
- Leveson, *Safeware*, 1995, Appendix A: A. Extended treatment with
  additional source material.
- FDA Class I recall record (declared defective May 2, 1986; classified
  Class I) and CAP correspondence: A (regulator primary documents,
  FOIA-accessible). [EVIDENCE NEEDED: FDA primary recall record with
  Class I designation — Delon to confirm via FDA historical-records
  request; current claim anchored to Leveson 1995 *Safeware* Appendix A
  plus Wikipedia / Ethics Unwrapped / MIT 6.033 / Cal Poly / JMU case-
  study concordance on Class I designation, pending FOIA-grade primary
  confirmation.]
- ECRI *Health Devices* 1987: B (specialist investigative outlet with
  institutional review; treated as B because ECRI is acknowledged but
  not peer-reviewed in the sense academic medicine uses).
- Hospital physicist accident-reconstruction reports (Hager at Tyler;
  Yakima physics staff): B (institutional documents, available through
  ECRI's compilation and Leveson's interviews; original site documents
  partly proprietary).

Sources needed:
Tier 1 (court / regulator / primary):
- FDA Center for Devices and Radiological Health. Therac-25 recall file
  (recall number to be confirmed via FDA historical-records request).
  Cite by document type + date.
- FDA / AECL Corrective Action Plan correspondence, February 1987 –
  September 1987. FDA records, FOIA.
- 510(k) premarket clearance documents for Therac-25 (1980s),
  available via FDA's historical 510(k) database.
- Cox v Atomic Energy of Canada Limited (East Texas, 1986 suit).
  Precise docket and venue [EVIDENCE NEEDED — Texas state court records;
  settled out of court, terms sealed, but pleadings and pre-trial
  filings may be retrievable. Delon to source.]

Tier 2 (peer-reviewed scholarship and acknowledged institutional
investigations):
- Leveson, Nancy G., and Clark S. Turner. "An Investigation of the
  Therac-25 Accidents." *Computer* (IEEE), vol. 26, no. 7, July 1993,
  pp. 18–41.
- Leveson, Nancy G. *Safeware: System Safety and Computers*.
  Addison-Wesley, 1995. Appendix A: "Medical Devices: The Therac-25
  Story."
- Leveson, Nancy G. "The Therac-25: 30 Years Later." *Computer* (IEEE),
  vol. 50, no. 11, November 2017, pp. 8–11 (retrospective; useful for
  the 30-year view of what changed in medical-device software
  regulation).
- ECRI. "Therac-25 Accelerator Patient Treatment System." *Health
  Devices*, vol. 16, no. 4, 1987.

Tier 3 (period press, named):
- Saul, Stephanie. "Casualties of a Healing Machine." *Newsday*,
  multi-part investigation 1986 (the period reporting that pushed
  national coverage of the East Texas accidents). [EVIDENCE NEEDED —
  full citation chain; Delon to confirm via Newsday archive.]
- *Wall Street Journal* coverage of the FDA recall, April 1986 (cite
  by date and author).

Open questions:
1. **The single programmer.** Leveson's investigation identifies the
   safety-critical code as the work of a single programmer (with prior
   work on the Therac-6 and -20), but does not name him publicly.
   Whether this anonymity should be respected, or whether the named
   individual should be pursued through litigation records, is a
   judgment call for Bonnie/Nancy. The book's argument does NOT require
   naming him — the laundering claim sits at the institutional level,
   not the individual programmer level.
2. **Settlement seal in Cox v AECL.** Terms are sealed; pre-trial
   filings may be publicly retrievable. [EVIDENCE NEEDED — pre-trial
   pleadings from the Cox suit. If retrievable, would lift the
   "internal field-service incident records" claim from B to A. Delon
   to source.]
3. **Hamilton, Ontario, patient identity.** The Ontario Cancer
   Foundation Clinic patient (July 26, 1985) is not publicly named in
   the canonical sources. Whether the patient name appears in Canadian
   provincial inquest records is unconfirmed. [EVIDENCE NEEDED —
   Ontario coroner's office inquest record search, 1985–87. Delon
   to source.]
4. **First-incident causal attribution.** Whether the Kennestone June
   1985 overdose was the proximate cause of Verdon Kidd's later death
   is contested in the medical record. The other two confirmed deaths
   (Cox, Dodd) have clearer causal chains. Stephen to verify before
   chapter use; if disputed, the chapter should cite "at least two
   deaths directly attributable" rather than three.
5. **CGR's role.** Therac-25 was developed with French firm CGR. The
   record on CGR's contribution to the software architecture and
   safety-design choices is sparse in English-language sources.
   [EVIDENCE NEEDED — CGR engineering records, French regulator
   correspondence. Delon to source via French medical-device
   regulatory archives.]

Narrative scenes (for Wayne, not for Shirley to draft):
- East Texas Cancer Center, March 21, 1986. Voyne Ray Cox, a 33-year-old
  oil-field worker receiving treatment for a tumor removed from his
  shoulder. The console displays "Malfunction 54." The operator,
  separated from Cox by the shielding wall, sees no patient. Cox
  reports a sensation he later described as "being hit between the
  shoulders with a baseball bat" — a description that became, in
  Leveson's reconstruction, the inflection point that physicist Fritz
  Hager could use to reproduce the keystroke sequence.
- East Texas Cancer Center, April 1986. Hager and the AECL field engineer
  in the treatment room, attempting to reproduce the fault. Hager
  pressing Up-Arrow at varying speeds. The moment when the keystroke
  timing reproduces the "Malfunction 54" — the alibi's first crack.
- The Yakima physics staff in January 1987, reading the East Texas
  patient injury reports and recognising the same symptom pattern in
  Glen Dodd's case. The FDA recall is supposed to have fixed this.
- Nancy Leveson at MIT, 1990–93, interviewing AECL engineers, FDA
  reviewers, and hospital physicists, and reconstructing the race
  condition by reading the PDP-11 assembly code.

Book function:
Canonical system/object alibi case in Chapter 2 ("The Four Goats").
Replaces Bhopal in the installing chapter (Bhopal moves to ch-5, where
its partial-scapegoat-via-Anderson and system-alibi-via-corporate-
architecture hybrid serves the "Guilty Goat" chapter on hybrid
classifications). Therac-25 is a cleaner installing case for system/
object alibi because (i) the named cause migrates explicitly across
three blame containers in the historical record (operators → machine →
unnamed software bug), making the laundering legible to the reader;
(ii) the responsibility chain is unusually well documented through
Leveson's investigation; (iii) the technical-versus-institutional
distinction is sharp — the fault was a race condition, but the
laundering was the institutional response to it. The chapter uses
Therac-25 to teach the reader to recognise system/object alibi at the
machine-and-software level, before the book takes that recognition into
algorithm-and-model territory in Part III.

Handoff owner: stephen-fact-check-director
```

## Assumptions

- Treating Leveson & Turner 1993 as the canonical technical
  reconstruction (it is the most-cited primary technical source on
  the case in the safety-engineering literature).
- Treating the cost-bearer count as "six documented overdose
  accidents; at least three deaths directly attributable" — the more
  conservative phrasing pending verification of the Kennestone causal
  chain.
- Treating the "single programmer" detail as institutionally relevant
  but individually anonymized — Leveson's choice to not name him is
  respected in this case file; book treatment can be revisited if
  litigation records publicly name him.
- Treating CGR's role as under-documented in English-language sources;
  the case file currently rests on AECL-side documentation.

## Evidence grade

A. Load-bearing claims rest on Leveson & Turner 1993 (IEEE Computer,
peer-reviewed primary technical reconstruction), Leveson 1995 *Safeware*
Appendix A, FDA recall correspondence (regulator primary documents),
and ECRI's 1987 *Health Devices* cross-site investigation. The Cox
litigation pre-trial filings, if retrieved, would lift the internal
AECL field-service incident record claims from B-corroborated to
A-direct.

## Open questions

Five [EVIDENCE NEEDED] items flagged for Delon: (1) Cox v AECL
pre-trial filings from Texas state court; (2) Newsday Saul investigation
full citation chain; (3) Ontario coroner's inquest record for the
Hamilton patient; (4) FDA 510(k) Therac-25 file with precise recall
number; (5) CGR engineering records via French regulator archives.

## Handoff

stephen-fact-check-director — verify (a) the six-incident / three-death
count against Leveson 1993 table 1 and Leveson 1995 Appendix A; (b)
the FDA recall sequence — AECL MDR filing April 15, 1986; FDA "declared
defective" May 2, 1986; Class I designation (the FDA's highest severity,
NOT Class III as the earlier brief stated) — and CAP timing (February
1987); (c) the Leveson 1993 *Computer* citation (volume 26, issue 7,
July 1993, pp. 18–41); (d) the Hager reconstruction date and method
against Leveson's interview record; (e) the named patients (Cox, Dodd,
Kidd) and whether Kennestone causal attribution is supportable, before
gating to status: draft. Onward route: wayne-narrative-lead for chapter
brief integration into ch-02 ("The Four Goats"), system/object alibi
slot.
