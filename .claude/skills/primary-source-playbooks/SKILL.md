---
name: primary-source-playbooks
description: Per-domain playbook for finding load-bearing primary sources — names the canonical archives, docket systems, FOIA paths, primary-document repositories, and standard-of-evidence rules for the four research domains (historical, war/statecraft, AI/technology, public law/politics) plus the cross-domain ICC/UN bodies. Used by every researcher to know where to look first and by Alan to verify domain-authority citations.
version: 1.0.0
---

# Primary Source Playbooks

## Global Five Over-Rules

<!-- GENERATED:five-over-rules:start -->
1. **Evidence before elegance.** Never improve the story by weakening the evidence.
2. **Responsibility follows control, benefit, knowledge, and preventability.** Do not stop at the most visible actor.
3. **Keep the taxonomy intact.** Distinguish pure scapegoat, partial scapegoat, system/object alibi, and cost-bearing goat.
4. **Steelman before judgment.** Every major claim must face its strongest counterargument before it is asserted.
5. **Handoff cleanly.** Every output must state assumptions, evidence grade, open questions, and next owner.
<!-- GENERATED:five-over-rules:end -->

## How to use this skill

For each case, identify the dominant domain (historical / war / AI / politics), open the corresponding playbook section, and work top-down: start at the highest-authority source in that domain and stop when corroboration reaches the grade the chapter needs. **Do not skip to secondary sources before the primary-source path has been exhausted.**

If a case spans multiple domains, run multiple playbooks and reconcile in the source ledger.

## Decision rubric

For every load-bearing claim, the strongest available primary source must be:

- **From the highest tier of the domain playbook below** that is reachable given access constraints (paywall, archive closure, language).
- **Verifiable**: a third party with the citation can confirm the claim by retrieving the document.
- **Permanently archived** or, if not, captured via `web.archive.org` snapshot with the snapshot URL in the source ledger.

If no source from tier 1 or 2 of the matching domain playbook can be obtained, the claim caps at evidence grade C until that changes (per `.claude/skills/evidence-grading/SKILL.md`).

## Conflict handling

1. **Tier-1 source says X; tier-2 source says not-X:**
   Tier 1 wins for the specific fact, but log the disagreement and the tier-2 reasoning in the disputed-claim register. Many tier-2 sources have synthesized later evidence; if the synthesis predates the tier-1 publication, escalate to Alan.
2. **Tier-1 source is behind a paywall the project cannot reach:**
   Record the citation with `[PAYWALLED]` marker. Use the strongest tier-2 source that summarizes the tier-1 document. Cap the claim at B. Hand off to Delon to budget the paywall fee if the claim is load-bearing.
3. **The case predates digital archives and the tier-1 source is physical-only:**
   Use the best published transcription with provenance. Cap at B unless an academic editor of acknowledged authority has authenticated the transcription.
4. **Two state actors give contradictory tier-1 statements:**
   Each is a tier-1 source for the OTHER side's accusation, not for the underlying fact. Treat the claim as contested per the dispute rule above.

## Escalation conditions

- Escalate to Alan (with the matching domain frame) when the tier hierarchy is ambiguous in a fast-moving case.
- Escalate to Delon when access blocks (paywall, sealed records, language gap) prevent reaching tier 1 and the claim is load-bearing.
- Escalate to Nancy when the primary source itself contains material that carries defamation risk if quoted.

## Historical domain playbook (Shirley)

Tier 1 (court / official inquiry / regulator):
- Final court judgments + opinions (national supreme/federal court systems; cite docket + date + judge).
- Official inquiry reports (e.g., Warren Commission, Hutton Inquiry, Bloody Sunday Inquiry, ICMR/Madras High Court reports for Bhopal, Pecora Commission, Pujo Committee, Truth Commissions).
- Regulator findings: SEC litigation releases, OSHA citations, USDA recall notices, NTSB reports.
- Statutes / executive orders as enacted; not summaries of them.

Tier 2 (peer-reviewed scholarship / acknowledged archival editions):
- Peer-reviewed academic monographs on the case; multiple-edition standard works (e.g., specific Bhopal monographs by Kim Fortun, Lapierre & Moro).
- Published archival editions: Foreign Relations of the United States (FRUS), Public Papers of the Presidents, established collected editions of correspondence.

Tier 3 (acknowledged investigative journalism with source disclosure):
- Major investigative work with FOIA documents disclosed (e.g., NYT investigations with sidebars listing source documents, Washington Post Watergate-tier reporting).
- Established newspapers of record at the time of the case (paper of record varies by country and era — name the paper and its standing in the period).

Tier 4 (do not use as primary):
- Wikipedia summary; popular history without source apparatus; quote attributed without primary citation.

## War / statecraft domain playbook (Selina)

Tier 1 (international tribunals + UN / ICRC / OHCHR):
- ICC arrest warrants, indictments, judgments (cite docket: ICC-XX/XX-XX/XX).
- ICTY / ICTR / SCSL / KSC judgments and trial transcripts.
- UN Security Council resolutions; UN Commission of Inquiry reports (Syria, Myanmar, Ukraine); OHCHR human-rights reports.
- ICRC commentaries on the Geneva Conventions and Additional Protocols (definitive authority on IHL).
- National courts of universal jurisdiction (German Higher Regional Court Koblenz, Swedish Higher Court) judgments.

Tier 2 (acknowledged conflict-monitoring NGOs + state inquiry):
- Human Rights Watch reports; Amnesty International detailed investigations.
- Bellingcat open-source-intelligence investigations with documented chain of custody.
- National-level commissions of inquiry (Chilcot Inquiry on Iraq, the Bloody Sunday Inquiry).
- Forensic Architecture investigations with published source documents.

Tier 3 (high-quality conflict journalism with named sources):
- AP, Reuters, AFP wire reports with named correspondents on the ground.
- Major outlets with documented FOIA / leaked documents (NYT, WaPo, Guardian, Spiegel, Le Monde).

Tier 4 (do not use as primary):
- Party-to-conflict press releases as fact (use as evidence of that party's STATEMENT only).
- Anonymous Telegram channels, partisan analysis aggregators, single-source social media claims.

## AI / technology domain playbook (Warren)

Tier 1 (primary documents from the entity + court filings):
- Model cards and system cards published by the lab (link to the specific version + date; Wayback Machine snapshot for any model card that has since been edited).
- Pre-registered benchmark protocols and peer-reviewed evaluation papers (NeurIPS, ICML, ACL with reproducibility code).
- Court filings: complaints, depositions, exhibits filed in AI lawsuits (PACER docket cites).
- Regulator filings: FTC complaints + consent orders; EU AI Act conformity assessments; CMA / EU competition rulings.
- Official lab safety reports (e.g., Anthropic's RSP releases, OpenAI's Preparedness Framework reports, Google's Frontier Safety Framework documents).

Tier 2 (peer-reviewed independent evaluations + acknowledged AI safety research):
- Independent benchmark papers (METR, Apollo Research, MLCommons audited results).
- Mechanistic interpretability publications from non-lab research groups.
- Established AI policy research (Stanford HAI, Oxford GovAI, AI Now).

Tier 3 (specialist investigative journalism):
- Wired, MIT Tech Review, The Information, Bloomberg AI coverage with named sources.
- Specialist tech reporters with documented FOIA / leaked-document use.

Tier 4 (do not use as primary):
- Lab marketing posts, conference keynotes, podcast interviews as fact about capabilities.
- Twitter/X discussions of benchmark results without the underlying paper.
- LessWrong / EAForum posts as primary; use only as commentary pointing to primary sources.

## Public law / politics domain playbook (Loki)

Tier 1 (court docket + agency action + statute):
- Federal court dockets via PACER / CourtListener / RECAP (cite case number + court + date + filing type).
- Executive orders as enacted (whitehouse.gov + Federal Register citation).
- Federal Register notices of proposed and final rulemaking (FR cite: vol + page + date).
- GAO reports, Inspector General reports, CRS reports.
- Congressional records: bills as introduced, committee reports, floor speeches in the Congressional Record.

Tier 2 (acknowledged legal scholarship + administrative-law-focused outlets):
- Just Security, Lawfare, Election Law Blog (Hasen), Volokh Conspiracy, SCOTUSblog — cite the specific post + author.
- Peer-reviewed legal scholarship in law reviews.

Tier 3 (specialist political journalism with documented sourcing):
- AP, Reuters, NYT, WaPo political reporting with named officials or documented memos.
- Specialist beat reporters (immigration, EPA, DOJ, Pentagon) with FOIA disclosures.

Tier 4 (do not use as primary):
- Cable news commentary; partisan think-tank press releases; Twitter/X threads from anonymous accounts.
- "A senior official said" without an organization, role, or context.

## Cross-domain bodies (use as tier 1 for the matching frame)

- ICC, ICJ, ICTY/R, SCSL, KSC: war crimes / atrocity attribution.
- UN Special Rapporteurs (country and thematic mandates): UN-aligned tier 1.
- OECD anti-bribery working group reports, FATF mutual evaluation reports: financial-crime cross-domain.
- WHO outbreak reports, ECDC, CDC MMWR: public-health-cross-domain.

## Output format

For each claim, the source-ledger row produced by this skill must include:

```text
Claim:
Domain:
Tier 1 source attempted: <citation> | not available because <reason>
Tier 2 source used: <citation>
Tier 3 source used (if any): <citation>
Access notes: <paywall / archive / language>
Wayback snapshot URL (if applicable):
Evidence grade (per evidence-grading skill):
Open questions:
Handoff:
```

<example>
Context: Selina needs a primary source for the OHCHR-corroborated civilian-harm count in Bucha.
input: case="Bucha civilian harm March 2022"
output: Domain: war/statecraft. Tier 1 attempt: OHCHR Report on the human rights situation in Ukraine (specific report + paragraph cite); ICC arrest warrant for Putin (ICC-01/22 docket cite); Ukrainian Prosecutor General registry (URL + access date). Tier 2 used: HRW report on Bucha (Sept 2022). Tier 3 used: AP/Reuters reconstructions for specific contested counts. Access notes: ICC docket public; PGO registry in Ukrainian — translation needed for two specific entries. Wayback snapshot: yes for OHCHR + PGO URLs. Evidence grade: A for OHCHR-corroborated counts, C for single-source attributions of specific perpetrators. Handoff: Stephen (verify the translations) → Alan (IHL frame on attribution).
</example>

<example>
Context: Warren needs a primary source for "Anthropic's safety claims about Claude 4.7" for an AI-governance chapter.
input: case="Anthropic Claude 4.7 safety claims"
output: Domain: AI/technology. Tier 1 attempt: Anthropic's Claude 4.7 system card (cite URL + Wayback snapshot taken on access date because system cards are versioned); Anthropic's Responsible Scaling Policy current release; any FTC or court filings (none yet). Tier 2 used: METR independent capability evaluations if published for this model; Apollo Research evaluation if published. Tier 3 used: Wired/Information/Bloomberg AI coverage WITH named Anthropic sources or documented memos (NOT marketing posts). Access notes: system card public; some appendices may be paywalled. Wayback snapshot: mandatory for the system card. Evidence grade: A for what the system card admits; B for METR/Apollo independent evaluations; C for any single-source journalism without document corroboration. Handoff: Stephen → Alan (AI governance frame) for whether the system card's hedging language supports the chapter's claim.
</example>
