---
status: ready
case_id: ai-training-data-litigation
case: AI training-data copyright litigation cluster and California transparency law
domain: AI / copyright law / S.D.N.Y. and N.D. Cal. federal litigation / UK High Court / California legislation
case_type: system/object alibi
secondary_case_type: |
  cost-bearing goat (authors / rights-holders absorbing scraped-corpus value while AI developers extracted it; the chapter must surface both layers without collapsing them)
evidence_grade: A
owner: warren-ai-technology-researcher
handoff: stephen-fact-check-director
chapter: 10-the-model-did-it
last_updated: 2026-05-26
sources:
  - card_id: bartz-settlement-preliminary-approval-2025-09-25
    used_for: "Judge Alsup's Sept. 25, 2025 preliminary-approval order — settlement amount, ~500,000-work class size, ~$3,000 per-work gross figure"
  - card_id: bartz-v-anthropic-fairness-hearing-2026-05-14
    used_for: "May 14, 2026 final fairness hearing procedural posture (under-submission status as of manuscript freeze)"
  - card_id: wang-order-chatgpt-log-preservation-2025-05-13
    used_for: "Magistrate Judge Wang preservation order on ChatGPT conversation logs in NYT v. OpenAI (S.D.N.Y. 1:23-cv-11195)"
unwired_sources:
  - "Authors Guild v. OpenAI Inc., No. 1:23-cv-08292 (S.D.N.Y., Stein, J.) — complaint Sept. 19, 2023; MTD denial Oct. 2025 — no card (task referenced authors-guild-v-openai-stein-2025-10; not yet in registry)"
  - "Getty Images (US) Inc. v. Stability AI Ltd., [2025] EWHC 2863 (Ch), Nov. 4, 2025 (Mrs Justice Smith) — no card (task referenced getty-v-stability-ai-2025-11-04; not yet in registry)"
  - "NYT v. OpenAI, No. 1:23-cv-11195 (S.D.N.Y.) — complaint Dec. 27, 2023; class-cert briefing 2026 — no card"
  - "Bartz v. Anthropic PBC, No. 3:24-cv-05417 (N.D. Cal., Alsup, J.) — complaint Aug. 19, 2024; summary judgment June 23, 2025; class certification July 17, 2025 — no card for the underlying complaint or SJ order distinct from the preliminary-approval card"
  - "California SB-942 (signed Sept. 19, 2024) and AB-853 (signed Oct. 13, 2025) — California AI Transparency Act — no card"
  - "OpenAI written submission to UK House of Lords Communications and Digital Committee, January 2024 ('impossible to train today's leading AI models without using copyrighted materials') — no card"
  - "EU AI Act, Article 53 and Annex XI; Regulation (EU) 2024/1689 — no card"
  - "17 U.S.C. § 107 (US fair use) and UK Copyright Designs and Patents Act 1988 — no cards"
  - "Sharma et al., 'Towards Understanding Sycophancy in Language Models,' arXiv:2310.13548 — out-of-scope for this case file (belongs to GPT-4o sycophancy)"
  - "Specialist legal commentary (Norton Rose Fulbright; Kluwer Copyright Blog; Mayer Brown; Latham; Bird & Bird; Sidley Austin; McKool Smith) on the Bartz settlement and Getty judgment — no cards"
  - "NPR (Sept. 5, 2025); The Verge; Wired; Reuters coverage of the Bartz settlement — no cards"
  - "Authors Alliance, 'Bartz v. Anthropic Fairness Hearing,' May 14, 2026 — partial coverage via [[bartz-v-anthropic-fairness-hearing-2026-05-14]]"
---

# AI Training-Data Copyright Litigation — Case File

Case name: The cluster of training-data copyright lawsuits brought against OpenAI, Microsoft, Anthropic, Stability AI, and others (2023-2026), the Bartz v. Anthropic settlement, the Authors Guild and New York Times suits against OpenAI/Microsoft, the UK Getty v. Stability AI judgment, and the California AI Transparency Act — collectively, the legal-procedural surface where the "training data" framing of human creative work meets copyright law.

Domain: AI / large language model training; US copyright law (17 U.S.C. § 107 fair use); UK Copyright Designs and Patents Act 1988; California Business and Professions Code (SB-942 / AB-853); class-action procedure.

Dates and place:
- *Authors Guild v. OpenAI Inc.* filed September 19, 2023, S.D.N.Y.,
  Case No. 1:23-cv-08292, Judge Sidney H. Stein. Motion to dismiss
  certain claims denied (October 2025; Judge Stein allowed
  copyright-infringement claims related to ChatGPT output to proceed).
- *The New York Times Company v. Microsoft Corp.* filed December 27,
  2023, S.D.N.Y., Case No. 1:23-cv-11195. Consolidated MDL proceedings.
  Multiple discovery orders including the November 2025 OpenAI order
  to preserve ~20 million ChatGPT conversation logs. Class certification
  hearing scheduled in 2026.
- *Bartz v. Anthropic PBC* filed August 19, 2024, N.D. Cal., Case No.
  3:24-cv-05417, Judge William Alsup. Plaintiffs: Andrea Bartz,
  Charles Graeber, Kirk Wallace Johnson. Summary judgment ruling
  June 23, 2025: training on lawfully acquired books = transformative
  fair use; downloading and retaining LibGen and PiLiMi pirated copies
  = NOT fair use. Class certification: July 17, 2025. Settlement
  announced: September 5, 2025. Settlement amount: $1.5 billion, the
  largest reported copyright settlement in US history. Final
  fairness hearing in early 2026 (verify exact date).
- *Getty Images (US) Inc. v. Stability AI Ltd.* (UK proceedings),
  judgment of Mrs Justice Joanna Smith, High Court (Chancery
  Division), November 4, 2025. Primary copyright claims dismissed on
  territorial grounds (training did not occur in the UK); limited
  trademark infringement found for specific watermark generations.
  Getty granted permission to appeal on secondary copyright
  infringement.
- California SB-942 (the California AI Transparency Act): signed by
  Governor Gavin Newsom September 19, 2024. Operative date pushed to
  August 2, 2026 by AB-853 (signed October 13, 2025).

Case type: system/object alibi
Hybrid note (per `.claude/skills/taxonomy-classification/SKILL.md`): primary is system/object alibi; cost-bearing goat fires as a documented secondary layer (authors and rights-holders absorb cost while AI developers extract value). The chapter must surface both layers without collapsing them; the primary classification holds because the load-bearing alibi is the "data" / "model abstraction" framing, not the substitution of an innocent bearer of accusation.

Classification note (per `.claude/skills/taxonomy-classification/SKILL.md`):
This is a hybrid case and must be filed as such. Block 3 fires
clean: "training data" is reified as the input substance, and "the
data" / "the corpus" / "the model trained on" becomes the
grammatical subject of public discourse about what AI systems
contain. The language laundering operates at the *input layer*: the
labor and creative work of millions of authors, photographers,
journalists, and code contributors is renamed as "data" and treated
as a substance to be acquired (lawfully, semi-lawfully, or via
shadow libraries) rather than as a corpus of human work each piece of
which has a named author with rights. Block 4 also fires: authors
and rights-holders absorb the cost — their work is used without
compensation or consent at training time, the value flows to model
developers, and the cost-bearer is the rights-holder class.

The primary classification is system/object alibi because the *framing
mechanism* (the "data" language; the model-output abstraction layer
that separates the system's behaviour from any individual training
example) is the load-bearing laundering structure. The cost-bearing
goat layer is secondary because the cost is real but absorbed within
a framework that does not classify the rights-holders as
*accusers-being-deflected* (the more typical scapegoat structure) —
they are positioned as ordinary plaintiffs in copyright litigation,
which is the institutional venue the alibi pre-supposed.

```text
Crisis:
Between 2020 and 2023, large language models and image-generation
systems were trained on internet-scale corpora that included
substantial quantities of copyrighted text, code, and images
acquired without licensing agreements. Specific included sources for
text models, per the public record across the litigation cluster,
include: Common Crawl (web-scraped pages including paywalled and
copyrighted content); Books3 (a corpus of approximately 196,640
books assembled from Bibliotik, a shadow library, by independent
researcher Shawn Presser in 2020); LibGen and PiLiMi (shadow
libraries of pirated books); Reddit; GitHub (code repositories with
varying licenses); and many others. For image models including
Stable Diffusion, LAION-5B (a dataset of 5.85 billion image-text
pairs scraped from the open web, including watermarked Getty Images
content) was the load-bearing corpus.

The crisis the litigation cluster surfaces is not a single event but
a structural one: at the moment of model training, the input corpus
contains human work whose creators were not asked, were not
compensated, and in many cases were not even aware that their work
had been included. The "training data" framing functioned as the
public account of what model developers were doing — an act
described in the grammar of substances being processed, not in the
grammar of human work being used.

Official story:
The AI industry's load-bearing framings across 2020-2024:

(a) Fair use. AI developers' uniform legal position has been that
    training is transformative fair use under 17 U.S.C. § 107.
    This position appears in OpenAI's January 8, 2024 written
    submission to the UK House of Lords Communications and Digital
    Committee ("it would be impossible to train today's leading AI
    models without using copyrighted materials"). It appears across
    Anthropic, Stability AI, and Microsoft's defensive filings.

(b) "Trained on publicly available data." A frequently used framing in
    model cards and corporate communications that conflates "available
    on the public internet" with "licensed for AI training." The
    framing displaces the legal and ethical question of consent.

(c) The model abstraction. Once a model is trained, the framing shifts
    from input (specific copyrighted works) to output (statistical
    weights). Defendants in the litigation argue that model weights
    are not copies of training examples in the copyright-relevant
    sense. The UK High Court accepted a version of this argument on
    November 4, 2025 in Getty v. Stability AI ("an AI model contains
    statistically trained parameters, not stored copies or
    reconstructions of photographs"), though the ruling turned
    primarily on UK territoriality.

Blame container:
Four sequential containers across the litigation cluster:

1. "Data" / "the corpus." The most basic alibi: human work renamed
   as substance. Once the work is "data," responsibility for what is
   in the data devolves to data curators (often the open-source
   community: Common Crawl, LAION, EleutherAI for The Pile, Shawn
   Presser for Books3) rather than to the labs that used the
   data. This is the input-layer system/object alibi.

2. "The shadow library." When the suit gets specific (Bartz v.
   Anthropic), the named blame container becomes LibGen / PiLiMi.
   Anthropic's pre-2024 acquisition of LibGen and PiLiMi corpora was
   the conduct Judge Alsup ruled was NOT fair use. The shadow
   library is the *named non-human actor* the laundering points to:
   a pirated library, indifferent to which works it contained, used
   by a company that — per the Alsup ruling — had also obtained
   books lawfully and could have used those instead.

3. "The model." Once trained, the model is the artifact whose
   outputs are at issue. The NYT v. OpenAI suit alleges
   "regurgitation" — that ChatGPT can be induced to produce
   substantial verbatim or near-verbatim passages from NYT
   articles. OpenAI's defenses include framing regurgitation as
   "rare misuse" rather than as a property of the model. The model
   is positioned as a quasi-autonomous entity whose outputs are
   either licit (transformative) or aberrant (jailbroken), with
   no middle ground in which the model is a derivative work
   carrying training-data residue.

4. "The market" / "the public interest." A higher-order alibi
   visible in policy commentary: AI training of large models is
   so economically and strategically important that copyright law
   should not be interpreted to constrain it. OpenAI's House of
   Lords submission frames the choice as binary: license-by-
   license consent is impossible at scale, therefore training-as-
   fair-use must hold. The framing places agency on "the market"
   or "national AI competitiveness" as the entity whose interest
   trumps individual rights-holders'.

Actual responsibility chain:

  Control:
  Each AI developer controlled (i) the choice of which corpora to
  include in training; (ii) the choice between lawful acquisition
  (e.g., licensing deals such as OpenAI's later agreements with
  News Corp, AP, Axel Springer, Le Monde) and shadow-library
  acquisition; (iii) the model release decision; (iv) the
  pre-litigation messaging that framed the activity. Per the Alsup
  ruling on Bartz v. Anthropic, Anthropic had the option to acquire
  books lawfully and in fact did so for some — making the
  shadow-library acquisition a discretionary choice, not a
  necessity.

  Common Crawl, LAION, EleutherAI, and Shawn Presser (Books3
  curator) controlled the assembled corpora that were available to
  the labs. These actors are generally treated as upstream
  facilitators in the litigation; the load-bearing controlled
  entities are the labs that chose to use the corpora.

  Benefit:
  AI developers — model capabilities and the resulting commercial
  position. OpenAI, Anthropic, Microsoft, Google, Meta, Stability
  AI captured the value of the training corpora in model weights,
  which generated billions in revenue (OpenAI's late-2025 valuation
  exceeded $150 billion; Anthropic's exceeded $30 billion;
  Microsoft's Azure OpenAI revenue ran to tens of billions).
  Rights-holders received no compensation at training time;
  post-litigation settlements (Bartz: $1.5B; subsequent licensing
  deals: case-dependent) capture only a fraction of the value.

  Knowledge:
  Per the Bartz v. Anthropic ruling and exhibits, Anthropic
  internal communications referenced LibGen and PiLiMi by name and
  acknowledged that the corpora were unlicensed. Per the
  NYT v. OpenAI complaint, OpenAI's internal records — sought in
  discovery — are alleged to include awareness that training-data
  copyright issues were a known risk. The level of internal
  knowledge varies by defendant; the Bartz summary judgment ruling
  is the highest-evidence-grade finding that a major AI lab
  knowingly trained on pirated books.

  Preventability:
  Preventable at multiple architectural and procedural points:
  - Pre-training: licensing agreements with publishers, news
    organizations, image agencies, and code-license-aware curation
    were available paths. Some labs took some of these paths
    (Microsoft+NYT pre-litigation discussions; OpenAI's later
    News Corp / AP / Axel Springer / Le Monde / Reddit deals;
    Anthropic's subsequent lawful book acquisition). The point is
    that the lawful path existed and was, in places, taken.
  - Pre-training: opt-out registries (e.g., a Robots.txt-equivalent
    for AI training; the C2PA provenance standard) existed in
    embryonic form and could have been honoured.
  - Post-training: output filters (more aggressive than the
    deployed ones) to prevent verbatim regurgitation of substantial
    passages were technically feasible.
  - Disclosure: training-data manifests at the level California
    SB-942 contemplates were technically feasible and would have
    allowed rights-holders to opt out before training rather than
    sue after.

  Record controller:
  AI labs controlled (i) the training-data manifests (most of which
  are not public; Anthropic's was partially disclosed under court
  order in Bartz); (ii) the internal communications about corpus
  acquisition; (iii) the model weights themselves; (iv) the
  inference logs that could (per the November 2025 NYT discovery
  order) reveal which user prompts produced regurgitation. US
  federal courts (S.D.N.Y., N.D. Cal., MDL) control the litigation
  record; UK High Court controls the Getty record; California
  legislature controls the SB-942 / AB-853 statutory record.

  Cost bearer:
  Authors and rights-holders. Per the Bartz settlement, the
  certified class includes copyright owners of approximately
  500,000 works appearing in the LibGen / PiLiMi datasets that
  Anthropic acquired; compensation is approximately $3,000 per
  work after fees. The class structure recognises a measurable
  cost; the per-work figure measures one corporation's settlement,
  not the full economic value extracted from the corpus.

  Diffuse cost: journalists whose work is now competed against by
  ChatGPT-as-news-summariser; photographers whose stock-imagery
  market has been hollowed by image generators trained on their
  archives; programmers whose code was used to train Copilot and
  similar systems; visual artists whose distinctive styles can be
  invoked by prompt. The diffuse cost is structural and partially
  invisible in the case-by-case litigation record.

  Not a cost bearer in the scapegoat sense: rights-holders are not
  being publicly *blamed* for AI's growing pains; they are being
  *erased* from the grammar of how AI training is described. The
  alibi here is not "the authors caused this" but "training data is
  a substance, not a body of human work" — a cost-absorbing
  silence rather than an active accusation.

How the alibi hardened:
1. The "data is the new oil" framing of the 2010s. Pre-LLM, the
   data-as-resource grammar of the big-tech era already conditioned
   readers and regulators to think of human work as "data" once it
   appeared on the internet. AI training inherited the framing.
2. The technical model-weights argument. The claim that model
   weights are not "copies" in the copyright sense is technically
   sophisticated, judicially attractive (it gives courts a clean
   legal hook), and has now been accepted in at least one major
   jurisdiction (UK High Court, Getty v. Stability AI, November
   2025). The argument is not absurd; the laundering is that the
   argument shifts the responsibility surface to the abstract
   output rather than addressing the input-layer consent question.
3. The "competitiveness" framing. The argument that constraining
   AI training will cede ground to less-constrained jurisdictions
   (China; or pre-Brexit-divergence UK; depending on the
   speaker's audience) is a policy-level alibi that places blame
   on geopolitical structure rather than on the labs' input
   decisions.
4. The shadow-library distance. Books3, LibGen, PiLiMi, and
   similar corpora were assembled by third parties; the labs
   acquired them at one remove from the original piracy. The
   distance — the curator-in-between — provided a deniability
   layer until courts (Alsup, June 2025) ruled that lawful
   downstream use of unlawful upstream acquisition does not
   wash the unlawfulness.

How the alibi weakened:
1. The Bartz v. Anthropic summary judgment (June 23, 2025). Judge
   Alsup's ruling split fair use along a clean line: training on
   lawfully acquired books was transformative fair use; downloading
   and retaining shadow-library copies was not. The ruling pierces
   the input-layer alibi at the acquisition stage. The subsequent
   $1.5 billion settlement (September 5, 2025) is the largest
   reported copyright settlement in US history and converts the
   training-data-as-free-resource framing into a multi-billion-
   dollar liability for the specific conduct.
2. The NYT v. OpenAI discovery order (November 2025). The order
   that OpenAI preserve approximately 20 million ChatGPT
   conversation logs (the figure widely reported; verify exact
   number against the docket) reattaches the model-output layer to
   the input layer: the regurgitation question can be answered
   only with logs, and the logs were ordered preserved.
3. Judge Stein's October 2025 ruling allowing Authors Guild and
   Times to proceed on certain claims, including the claim that
   ChatGPT outputs may be substantially similar to plaintiffs'
   copyrighted works.
4. The California AI Transparency Act (SB-942, signed September 19,
   2024; operative August 2, 2026 per AB-853). The act does not
   directly regulate training-data disclosure (it focuses on
   AI-generated content provenance), but the legislative posture —
   California recognising transparency obligations on covered AI
   providers — opens the procedural surface for training-data
   disclosure mandates in subsequent legislation.
5. Getty v. Stability AI (UK, November 4, 2025), notwithstanding
   Getty's loss on the primary copyright claim, established (a)
   that trademark infringement can be found where image generators
   produce identifiable third-party watermarks, and (b) that the
   territoriality of training is the load-bearing legal hook —
   meaning the EU's AI Act training-data provisions, applied in
   the territory where training occurs, become the binding
   surface.

Best counterargument:
"AI training-data litigation is not responsibility laundering; it
is law working as designed. Copyright disputes have always
proceeded through litigation. The Bartz settlement is the law
*successfully* extracting accountability from Anthropic. The
NYT v. OpenAI suit is proceeding through normal discovery. The UK
Getty ruling correctly identified jurisdictional limits. The
California Transparency Act extends the procedural surface.
Calling the case 'system/object alibi' criminalises ordinary
copyright defendant behaviour — every defendant takes the legal
position most favourable to itself; that is what defendants do.
The 'data' framing is not a laundering grammar; it is the
technically accurate description of how machine learning works.
The book is conflating *the existence of unsettled law* with
*deliberate evasion of responsibility*, which is unfair to AI
developers, judges, and legislators alike."

Warren's response: The counterargument is strongest on the
litigation-is-law-working point. The Bartz settlement is a
significant institutional accountability moment, and the
NYT v. OpenAI case advancing on the regurgitation claim is a
significant procedural advance. The diagnosis the book offers
sits one level up. The system/object alibi is not that any
individual lab is unilaterally evading responsibility; it is
that the *input-layer grammar of "training data"* — the
collective conceptual move by which human work becomes
substance — preceded the litigation and shaped which legal
remedies are available. By the time the law is litigated, the
question is "is the use fair?" rather than "was consent
required?" The first framing is a property-law question; the
second framing would be a labour or moral-rights framing. The
book's argument is that the substance-grammar at the input layer
is the laundering mechanism, and the litigation surface is the
*belated procedural response* to a categorical move that
preceded it. The Bartz ruling validates this analysis at the
acquisition-of-pirated-corpora layer; it does not yet reach the
broader question of whether the consent default should run
the other way.

The cost-bearing goat secondary classification is load-bearing:
the rights-holders absorbing the cost are not visible at the
narrative center of the AI story (the centre is the model and
its capabilities); they are visible only when they sue, which
itself is shaped by who can afford litigation (the Authors
Guild and the New York Times can; most individual authors and
photographers cannot). The Bartz class structure is the
procedural mechanism by which uncompensated rights-holders
become legally legible at all.

Evidence grade: A
- Authors Guild v. OpenAI, S.D.N.Y. 1:23-cv-08292, docket and
  rulings (esp. October 2025 MTD denial): A (federal court
  docket; primary).
- NYT v. OpenAI, S.D.N.Y. 1:23-cv-11195, docket (esp. November
  2025 log-preservation order; April 2026 class cert schedule):
  A (federal court docket; primary).
- Bartz v. Anthropic, N.D. Cal. 3:24-cv-05417: A.
  Specifically: Judge Alsup's June 23, 2025 summary judgment
  order; the July 17, 2025 class certification order; the
  September 5, 2025 settlement notice.
- Getty Images v. Stability AI, [2025] EWHC 2863 (Ch), Mrs
  Justice Joanna Smith judgment November 4, 2025: A
  (UK High Court judgment, primary).
- California SB-942 (signed September 19, 2024) and AB-853
  (signed October 13, 2025): A (signed statute, primary).
- OpenAI written submission to UK House of Lords Communications
  and Digital Committee, January 2024: A (primary corporate
  position document).
- Anthropic settlement website (anthropiccopyrightsettlement.com):
  A for the settlement administration facts; B for any contextual
  characterisation on the site.
- NPR, Reuters, Bloomberg, Authors Guild, Copyright Alliance
  reporting on the Bartz settlement (September 5, 2025): B
  (acknowledged journalism citing primary docket).

Sources needed:
Tier 1 (court / statute / primary documents):
- Authors Guild v. OpenAI Inc., 1:23-cv-08292 (S.D.N.Y.). PACER /
  CourtListener: full docket. Specifically:
  - Complaint, September 19, 2023.
  - Motion to dismiss ruling, October 2025 (Judge Sidney H. Stein).
- NYT v. OpenAI, 1:23-cv-11195 (S.D.N.Y.):
  - Complaint, December 27, 2023.
  - Discovery order on ChatGPT log preservation (November 2025).
  - Class certification briefing schedule.
- Bartz v. Anthropic PBC, 3:24-cv-05417 (N.D. Cal.):
  - Complaint, August 19, 2024.
  - Summary judgment order, June 23, 2025 (Judge Alsup).
  - Class certification order, July 17, 2025.
  - Settlement papers and final approval order (early 2026 —
    verify status).
- Getty Images (US) Inc. v. Stability AI Ltd., [2025] EWHC 2863
  (Ch), November 4, 2025 (UK High Court, Chancery Division, Mrs
  Justice Joanna Smith). Published at judiciary.uk.
- California SB-942 (CA Stats. 2024, Chapter 291) — signed
  September 19, 2024. Bill text at leginfo.legislature.ca.gov.
- California AB-853 (signed October 13, 2025) — the SB-942
  amendment package.
- OpenAI written evidence to the UK House of Lords Communications
  and Digital Committee, January 2024 (the "impossible to train
  today's leading AI models without using copyrighted materials"
  statement). Parliamentary record.
- EU AI Act, Article 53 and Annex XI (training-data summary
  obligations for general-purpose AI model providers), Regulation
  (EU) 2024/1689.

Tier 2 (specialist legal commentary + investigative journalism):
- Norton Rose Fulbright, "Bartz v. Anthropic: Settlement reached
  after landmark summary judgment and class certification."
  September 2025.
- Wolters Kluwer Kluwer Copyright Blog, "The Bartz v. Anthropic
  Settlement: Understanding America's Largest Copyright
  Settlement." 2025.
- Susman Godfrey LLP firm publication on the Bartz settlement
  (plaintiffs' counsel; cite as interested but informed source).
- Mayer Brown, Latham & Watkins, Bird & Bird, Sidley Austin
  alerts on Getty v. Stability AI judgment (November 2025).
- McKool Smith AI Infringement Case Updates (recurring tracker;
  cite specific updates by date).
- Authors Guild advocacy publications on the Bartz settlement.
- NPR (September 5, 2025), The Verge, Wired, Reuters coverage
  of the Bartz settlement.

Tier 3 (period press):
- Bloomberg, WSJ, FT coverage of the litigation cluster.
- Stratechery (Ben Thompson) analytical pieces, where applicable.

Open questions:
1. **Status of Bartz settlement final approval.** Settlement
   announced September 5, 2025; final approval and disbursement
   schedule under the standard Rule 23(e) process. Whether final
   approval has been entered as of May 26, 2026 is to be verified
   on the docket; the chapter must use precise procedural-stage
   language ("settlement announced September 5, 2025; final
   approval pending / entered on <date>").
2. **NYT v. OpenAI class certification outcome.** Class cert
   hearing scheduled in 2026; whether the class has been certified
   as of May 26, 2026 is to be verified.
3. **Authors Guild v. OpenAI procedural state.** Discovery is
   substantial as of late 2025; summary judgment briefing
   timeline (early 2026 reporting suggests April 2, 2026 close)
   needs verification against the actual docket.
4. **Other ongoing cases not enumerated here.** Multiple smaller
   author class actions exist (Tremblay et al. v. OpenAI;
   Silverman et al. v. OpenAI; the consolidated MDL filings).
   For chapter purposes, the four named cases above are
   load-bearing; the others contribute to the procedural-cluster
   picture but are not individually anchored.
5. **California training-data disclosure legislation status.**
   SB-942 / AB-853 are signed; specific training-data manifest
   obligations are not the primary focus of SB-942 (which
   focuses on AI-generated content provenance). Whether
   subsequent California legislation has introduced training-data
   disclosure obligations as of May 26, 2026 needs verification;
   the chapter should not overstate SB-942's scope.
6. **EU AI Act Article 53 implementation.** The EU AI Act's
   general-purpose AI training-data summary obligations took
   effect August 2025 (verify); the implementing detail (template,
   level of disclosure required) is settled by Commission
   guidance. The European procedural surface is more advanced
   than the US one on training-data disclosure and should be
   referenced.

Narrative scenes (for Wayne, not for Warren to draft):
- January 2024: OpenAI's written submission to the UK House of
  Lords states that "it would be impossible to train today's
  leading AI models without using copyrighted materials." A
  public position is laid down: the framing is necessity.
- September 19, 2023: Maya Shanbhag Lang, then-president of
  the Authors Guild, holds the press conference announcing the
  Authors Guild suit alongside named author plaintiffs (John
  Grisham, George R.R. Martin, Jodi Picoult, Michael Connelly,
  among others). The grammar shifts: "data" is met by named
  authors with named books.
- December 27, 2023: The New York Times files its complaint. The
  complaint includes exhibits showing ChatGPT producing
  near-verbatim Times articles. The model-as-abstraction framing
  is met by exhibit-level regurgitation.
- August 19, 2024: Bartz, Graeber, and Johnson file in N.D. Cal.
  The complaint includes specific allegations about Anthropic's
  internal communications referencing LibGen and PiLiMi.
- June 23, 2025: Judge Alsup's courtroom. The summary judgment
  order divides Anthropic's conduct in two: lawful book acquisition
  (transformative fair use); shadow-library acquisition (not fair
  use). The line is drawn at the input layer — the acquisition
  decision — not at the output layer.
- September 5, 2025: The settlement announcement. $1.5 billion;
  approximately $3,000 per work for approximately 500,000 works in
  the LibGen / PiLiMi class. The cost of the alibi is, for one
  defendant on one corpus subset, monetised.
- November 4, 2025: Mrs Justice Smith's judgment in Getty v.
  Stability AI. The English court accepts the model-weights-are-
  not-copies argument as to copyright; finds limited trademark
  infringement; the territoriality hook means the European
  procedural surface (EU AI Act) becomes the more important venue.

Book function:
Anchor case for chapter 10 ("The Model Did It") at the
*input-layer / data-framing* shell. Pairs with Llama 4 / LMArena
(evaluation-layer) and GPT-4o sycophancy (deployment-layer) to
install the three-layer chapter structure: input, output (behaviour),
and evaluation.

The case is load-bearing because it shows the alibi operating across
the longest time horizon (2020-2026+) and at the highest stakes
(billions of dollars, hundreds of thousands of rights-holders, the
shape of the data-economy commons). It also shows the alibi
*meeting institutional pushback at scale* — the Bartz settlement is
not the alibi succeeding, it is the alibi paying. The chapter must
not flatten this into either "the law worked" or "the labs won";
the more accurate reading is that the input-layer framing succeeded
at shaping which legal questions are litigable, and the law's
catch-up is real but partial.

Co-anchor with the Boeing 737 MAX case file from chapter 2: both
cases show the *procedural shell* layer of the system/object alibi.
Boeing's was the certification regime (DPA → NPA); this case's is
the copyright-litigation surface and the legislative-transparency
surface. The book teaches readers to recognise that the procedural
shell can take many forms (regulatory delegation; fair-use defense;
class settlement; transparency statute) and that each form has its
own load-bearing structural feature.

Legal risk:
Moderate. The case is a live, multi-front litigation cluster as of
May 26, 2026. Multiple cases are pre-judgment. The chapter must
use precise procedural-stage language ("filed September 19, 2023"
/ "MTD denied October 2025" / "settled September 5, 2025, final
approval [pending / entered]" / "judgment November 4, 2025"). Risk
surfaces:

- Characterising AI labs' conduct as "piracy" outside the specific
  Bartz finding: only Anthropic's LibGen and PiLiMi acquisition has
  been ruled non-fair-use; characterisations of other defendants'
  training-data choices must stick to the complaints' allegations
  and the post-summary-judgment record (where applicable).
- Characterising Anthropic post-settlement: Bartz settled WITHOUT
  Anthropic admitting liability beyond the summary judgment
  finding. The summary judgment finding (shadow-library
  acquisition not fair use) is settled law-of-the-case; the
  settlement does not extend findings to other corpora or other
  conduct.
- Characterising OpenAI / NYT: the regurgitation evidence is in
  the complaint and the discovery record; specific allegations
  about OpenAI internal knowledge are unproven until adjudicated.
- Naming individual executives: Sam Altman, Dario Amodei,
  Daniela Amodei, Mark Zuckerberg, Satya Nadella are publicly
  associated with their companies' AI strategies but have not been
  personally adjudicated for training-data decisions. Permissible
  references are to public statements they have made; impermissible
  references attribute personal liability or motive beyond what
  they have themselves said.

Specific wording cautions:
- "Anthropic pirated books": permissible ONLY in the specific
  finding context, i.e., "per Judge Alsup's June 23, 2025
  summary judgment order, Anthropic's acquisition and retention
  of books from LibGen and PiLiMi was not fair use." NOT
  generalisable to all Anthropic training-data conduct.
- "OpenAI infringed copyright" / "OpenAI stole from authors":
  FORBIDDEN as bare verbs absent a final adjudication.
  Permissible: "Authors Guild alleges in its September 19, 2023
  complaint that OpenAI infringed copyright by..."; "Judge Stein
  in October 2025 denied OpenAI's motion to dismiss certain
  output-similarity claims, allowing those claims to proceed."
- "Sam Altman / Dario Amodei / Mark Zuckerberg knew": FORBIDDEN
  absent specific cited admissions or court findings. Permissible:
  references to written submissions and public statements
  (e.g., OpenAI's House of Lords submission), attributed to the
  company.
- "Getty lost": permissible but precise: "Getty's primary copyright
  claim was dismissed by the UK High Court on November 4, 2025
  on territorial grounds; Getty has been granted permission to
  appeal on secondary copyright infringement; limited trademark
  infringement was found."
- "California has mandated training-data transparency":
  permissible ONLY with the precise scope: SB-942 mandates
  AI-generated content provenance disclosure for covered
  providers from August 2, 2026; it does NOT, as of May 26, 2026,
  mandate training-data manifest disclosure.

Handoff to Nancy for full defamation-wording sweep before chapter use.
This case file should also be reviewed by Alan (AI governance frame)
on the input-layer / output-layer framing question, which is partly
a governance-theory characterisation that may benefit from
discipline-specific review.

Handoff owner: stephen-fact-check-director
```

## Assumptions

- Treating the four named lawsuits and SB-942 / AB-853 as the
  load-bearing institutional surface of the case; many other
  individual and class-action filings exist and are referenced in
  passing but not anchored.
- Treating the Bartz v. Anthropic summary judgment (June 23, 2025)
  and settlement (September 5, 2025) as the highest-evidence-grade
  judicial findings on shadow-library training-data acquisition.
- Treating the Getty v. Stability AI judgment (November 4, 2025) as
  the load-bearing UK ruling; the Court of Appeal proceedings on
  secondary copyright are pending.
- Treating SB-942 as a procedural-surface signal rather than a
  training-data-disclosure mandate; the chapter must not overstate
  SB-942's scope.
- Case file is current as of May 26, 2026.

## Evidence grade

A overall on procedural and legal facts (court dockets, signed
statutes, published judgments). B on the broader characterisation
of the input-layer "data framing" as a laundering grammar; this
is the book's diagnostic claim and is supported by the cumulative
pattern across the litigation cluster but is not itself a
court-adjudicated finding. The chapter must respect the difference
between A-grade procedural facts and B-grade diagnostic interpretation.

## Open questions

Six flagged above: (1) Bartz settlement final-approval state; (2)
NYT v. OpenAI class certification outcome; (3) Authors Guild
v. OpenAI summary judgment briefing timeline and rulings; (4)
exhaustive enumeration of other ongoing cases — out of scope for
this case file but tracked for chapter completeness; (5) any
post-SB-942 California training-data disclosure legislation; (6)
EU AI Act Article 53 implementation status.

## Handoff

stephen-fact-check-director — verify (a) the four primary docket
numbers and judge assignments; (b) the June 23, 2025 Alsup summary
judgment order language separating lawful book acquisition
(transformative fair use) from shadow-library acquisition (not fair
use); (c) the September 5, 2025 Bartz settlement amount ($1.5
billion), the class size (approximately 500,000 works), and the
approximately $3,000 per-work figure; (d) the November 2025 OpenAI
discovery order text on ChatGPT log preservation, including the
specific log-count figure; (e) the November 4, 2025 Getty v.
Stability AI judgment citation and the territoriality holding;
(f) SB-942 signing date (September 19, 2024) and AB-853 signing date
(October 13, 2025), and the August 2, 2026 operative date; (g) the
OpenAI House of Lords January 2024 written submission quote;
(h) the procedural state of the Authors Guild and NYT cases as of
May 26, 2026. Then handoff to alan-expert-reviewer (AI governance
frame) on the input-layer / output-layer framing characterisation.
Onward route: nancy-legal-risk-counsel for the full
defamation-wording sweep — this is the highest legal-risk case file
of the three because it involves named living individuals at
companies with active litigation. Then bonnie-book-architect for
chapter-10 placement and the input/output/evaluation three-shell
chapter structure.
