---
audit: dependency-check
scope: baseline (first run, all three registries populated)
date: 2026-05-27
run_by: bonnie-book-architect
mode: baseline
---

# Dependency Check — Baseline Run, 2026-05-27

Owner: dependency-check (skill run by bonnie-book-architect)
Task: First cross-chapter dependency analysis combining the three book-level registries into one DAG. Baseline mode: identify pre-existing forward-dep violations, cut-blast-radius per chapter, and footprint-per-chapter top-3.
Inputs reviewed:
- `book/callback-graph.yml` (22 edges, 0 removed)
- `book/motif-registry.yml` (9 motifs, 0 candidates)
- `book/cognitive-arc.yml` (18 discriminations + 36 concept introductions + 6 retirements)
- `book/toc.yml` (4 parts, 13 chapters)
- `book/STATUS.md` (Part III authorized reading order 9 → 10 → 8)
- `book/chapters-v2/*.md` (13 chapters; sampled for callback-anchor verification — not re-verified, deferred to sister audits)
Output: this memo at `book/audits/dependency-check-2026-05-27.md`
Evidence grade: N/A (graph-level analysis; no factual claims)
Assumptions: authorized reading order per `book/STATUS.md` (forced 1→2→3, parallel-siblings {4,5,6,7}, sequenced 9→10→8, forced 11→12→13); motif appearance chains treated as soft lateral edges; callbacks and cognitive-arc dependencies treated as hard; lateral-verification delegated to `/callback-audit`, `/motif-audit`, `/cognitive-arc-audit`
Open questions:
- whether the registered sibling-internal motif-chain edges (12 across 7 motifs) are intentional cross-references or registration-only artefacts;
- whether `recognize-signature-as-seam.required_by[7]` should be removed or whether ch-7 should be promoted out of the Part II sibling set;
- whether mh17-state-layer-callback (ch-4 → ch-7) should be removed or whether ch-7 needs an in-chapter MH17 mini-install
Risks:
- two HARD forward-dep violations exist in the baseline graph; both touch ch-7;
- ch-13 footprint (31) is 24% above the next-highest chapter; any scope reduction is Gate-B equivalent;
- ch-7 is the heaviest Part II chapter and the receiver of both forward-dep violations — it is structurally drifting toward being a fifth Part I chapter while the spine treats it as a parallel sibling of ch-4/5/6
Handoff: bonnie-book-architect for forward-dep resolution decisions; xaiolai for whether to formally re-shape Part II reading-order or correct the registries

## Reading-order rank function

The combined graph is evaluated against the authorized reading-order DAG, not raw chapter numbers. Ranks:

| Chapter | Reading-order rank | Part |
|---|---:|---|
| ch-1 | 1 | I |
| ch-2 | 2 | I |
| ch-3 | 3 | I |
| ch-4 | 4P | II (sibling) |
| ch-5 | 4P | II (sibling) |
| ch-6 | 4P | II (sibling) |
| ch-7 | 4P | II (sibling) |
| ch-9 | 8 | III |
| ch-10 | 9 | III |
| ch-8 | 10 | III |
| ch-11 | 11 | IV |
| ch-12 | 12 | IV |
| ch-13 | 13 | IV |

Edge `a → b` is forward-safe iff `r(a) < r(b)`, OR `a = b`. Sibling-internal edges (both endpoints at rank 4P with different chapter numbers) are violations of the parallel-siblings property.

## Pass 1 — Forward-dependency findings

### Hard forward-dep violations: 2

| From chapter | To chapter | Dependency type | Reading-order distance | Action |
|---|---|---|---|---|
| ch-4 | ch-7 | callback (`mh17-state-layer-callback`, object_callback re-reading; required: true; ch-7 prose explicitly reads "In Chapter 4 we met MH17") | sibling-internal (Part II) | Either remove the explicit "in Chapter 4" reference and replace with an in-ch-7 MH17 mini-install, OR formally promote ch-7 to read after the other three Part II siblings, OR remove the edge from the registry and replace ch-7's MH17 callback with a forward-only callback from ch-2 or ch-8 |
| ch-6 | ch-7 | cognitive-arc (`recognize-signature-as-seam` discrimination; introduced_in: 6; required_by includes 7) | sibling-internal (Part II) | Either remove ch-7 from required_by (ch-7's Horizon sub-postmaster daily-balance signature is a re-install, not a requirement), OR add a brief in-ch-7 signature-as-seam re-install paragraph, OR formally re-sequence Part II reading-order so ch-6 precedes ch-7 |

Both violations terminate at ch-7. This is not coincidence — ch-7 is doing more conceptual work than the spine's "Part II parallel sibling" treatment allows. Per the in-file notes (cognitive-arc.yml at the recognize-signature-as-seam discrimination), the consolidation was already collapsed to ch-6 to handle the parallel-sibling constraint; the required_by[7] line breaks that resolution.

### Soft sibling-internal motif-chain edges: 12

These are motif appearance-chain edges where two parallel siblings carry the motif's adjacent appearances. Motif appearances are presence registers, not dependency contracts (unlike callbacks), so these do not block on their own — but they signal an implicit reading-order assumption that the parallel-siblings DAG does not honour.

| Motif | Sibling-internal edges (in reading-order sort) |
|---|---|
| `the-chain` | ch-4 → ch-5; ch-5 → ch-7 |
| `the-named-cause` | ch-4 → ch-5; ch-5 → ch-6 |
| `signature-as-seam` | ch-6 → ch-7 |
| `the-record` | ch-4 → ch-7 |
| `the-signed-document` | ch-4 → ch-6 |
| `the-court-or-inquiry` | ch-4 → ch-5; ch-5 → ch-6; ch-6 → ch-7 |
| `the-classified-or-sealed-file` | ch-5 → ch-6; ch-6 → ch-7 |
| `the-fair-clue` | (none — clean) |
| `the-altar` | (none — clean) |

The pattern: ch-7 is the terminus of most Part II motif chains (4 of 12 soft edges land at ch-7). Combined with the two hard forward-deps, this confirms ch-7's structural drift.

### Cross-part forward-dep findings: 0

All callback and cognitive-arc edges that cross Part boundaries resolve forward in reading-order. The Part III authorized order (9 → 10 → 8) is honoured by every edge that touches Part III. The Part I → Part IV bookframe callbacks (altar-moves, two-goats, four-category-taxonomy, eight-question-diagnostic, recognition-without-method) all resolve cleanly.

## Pass 2 — Cut-blast-radius per chapter

Footprint = number of distinct registry participations (callback endpoint, motif appearance, discrimination intro/consol/required, concept introduction, retirement) per chapter.

| Chapter | Footprint | Callback edges | Motif appearances | Concept intros | Discrim roles | Retirements |
|---|---:|---:|---:|---:|---:|---:|
| ch-1 | 11 | 3 | 5 | 3 | 0 | 0 |
| ch-2 | 24 | 6 | 6 | 4 | 5 | 3 |
| ch-3 | 16 | 2 | 5 | 3 | 6 | 0 |
| ch-4 | 13 | 1 | 5 | 3 | 4 | 0 |
| ch-5 | 14 | 3 | 4 | 1 | 5 | 1 |
| ch-6 | 16 | 2 | 5 | 3 | 6 | 0 |
| ch-7 | 23 | 5 | 6 | 3 | 9 | 0 |
| ch-9 | 16 | 1 | 6 | 1 | 7 | 1 |
| ch-10 | 25 | 3 | 7 | 3 | 12 | 0 |
| ch-8 | 23 | 3 | 6 | 4 | 9 | 1 |
| ch-11 | 25 | 4 | 6 | 3 | 12 | 0 |
| ch-12 | 24 | 4 | 7 | 4 | 9 | 0 |
| ch-13 | **31** | 7 | 6 | 1 | 17 | 0 |

### Top-5 cut-blast-radius chapters

1. **ch-13 — A Reader's Field Guide (footprint 31).** The book's resonant return. Paid-off endpoint for 7 callbacks (more than any other chapter); required_by terminus for 17 of 18 discriminations. A cut here would orphan every bookframe plant. Any scope reduction is Gate-B equivalent.
2. **ch-10 — The Model Did It (footprint 25).** Heaviest Part III chapter. Introduces 3 concepts and 2 discriminations the field guide explicitly requires (three-record-demand, AI-stack-three-layers, alibi-escalation). A cut would break ch-13's beat-9 algorithmic-denial walk and the 7→10→13 signature-seam chain.
3. **ch-11 — Make Responsibility Follow Control (footprint 25).** Heaviest Part IV chapter on the design side. Introduces design-vs-forensic-frame discrimination and named-attribution-design concept; pays off the EO-13328 callback from ch-8 and signature-seam from ch-6; plants beat10-moves-to-crosswalk to ch-13. A cut would orphan the EO-13328 design-asymmetry contrast.
4. **ch-2 — The Four Goats (footprint 24).** The taxonomy workhorse. Introduces 4 of the 8 foundational concepts, 4 discriminations, retires 3 pre-book frames. Six chapters carry callbacks planted in ch-2. A cut would force re-installing the taxonomy somewhere else — likely impossible without restructuring Part I.
5. **ch-12 — Keep the Record (footprint 24).** The record-discipline chapter. Pays off 4 callbacks (record-is-first from ch-7, design-rule from ch-11, walsh from ch-9, hofeller from ch-6). Introduces 4 concepts the field guide indexes. A cut would orphan four upstream plants and break the cognitive-arc's record-discipline rules requirement.

### Lowest footprint chapters (potential cut candidates: NONE)

ch-1 at footprint 11 is the lowest — but ch-1's load-bearing role is concentrated in three high-leverage bookframe callbacks (altar-moves, two-goats, recognition-without-method) and the altar motif. Footprint understates ch-1's structural value. **No chapter has footprint = 0; no chapter is a viable cut candidate.**

## Pass 3 — DAG safety

The combined graph is acyclic. The two hard forward-dep violations (ch-4 → ch-7; ch-6 → ch-7) both point in the same direction (toward ch-7) and have no reverse-path companions. No cycle exists.

However, the graph is **not consistent with the spine's parallel-siblings property for Part II.** The graph implicitly orders ch-4 before ch-7 and ch-6 before ch-7. The spine claims {4, 5, 6, 7} are parallel siblings. Two readings are possible:

- **Reading A — Registry-correct.** ch-7 actually does depend on ch-4 (MH17 callback) and ch-6 (signature-as-seam discrimination). The spine's "parallel siblings" claim is inaccurate; Part II is internally sequenced 4/6 before 7. Fix: amend the spine to acknowledge a partial order in Part II, or formally re-sequence Part II reading-order to {4, 5, 6} ‖ 7 with 7 last.
- **Reading B — Spine-correct.** Part II is genuinely parallel; the registry edges are over-commitments by the chapter prose. Fix: rewrite ch-7's MH17 callback and signature-as-seam reference to be self-contained, or move both to chapters that genuinely precede ch-7 (ch-2 already plants Therac-25 and Ukrainian children for ch-7/ch-8; ch-2 could absorb MH17 as well; the signature-as-seam can be re-installed inside ch-7 with no upstream dependency).

Either resolution is acceptable. The current state (Reading C — both spine and registry asserted, in contradiction) is the only state that should not persist.

## Unexpected graph properties

1. **ch-7 is the Part II structural keystone.** Footprint 23 (highest in Part II by 7 points over ch-6 at 16). Consolidation endpoint for two discriminations (identify-system-or-object-alibi, distinguish-alibi-collapse-from-architectural-reform). Introduces a third (detect-five-role-conflation). Required_by endpoint for two more (apply-eight-question-diagnostic, read-multi-channel-interception-asymmetry, recognize-signature-as-seam). The "Part II parallel siblings" framing under-represents ch-7's structural load. The two hard forward-dep violations are the visible symptom.

2. **ch-13's footprint (31) is structurally singular.** The next-highest chapters (ch-10, ch-11) sit at 25 — a 24% gap. ch-13 receives 17 of 18 discriminations' required_by, 7 of 22 callbacks' payoffs, and the resonant-return roles for 6 of 9 motifs. The resonant-return logic of the book concentrates here in a way that makes ch-13 essentially uncuttable.

3. **ch-1 understates by footprint.** At 11, ch-1 is the lightest chapter, but it plants three of the most resonant bookframe callbacks (altar-moves to ch-13; two-goats to ch-13; recognition-without-method to ch-13). Footprint alone misclassifies ch-1 as low-leverage; the callback weight tells the truer story.

4. **The retirement load is front-loaded.** Of 6 retirements, 3 land at ch-2, 1 each at ch-5, ch-8, ch-9. ch-2 retires three pre-book frames (weakness-equals-innocence, system-is-not-an-agent, bad-apples-closes-the-case) on top of installing the four-category taxonomy. ch-2 carries more conceptual lift than its 24 footprint suggests; if any chapter in Part I is a defect risk, it is ch-2 by load.

5. **Part III sequencing (9 → 10 → 8) holds cleanly under audit.** Every edge that crosses into or within Part III resolves forward under the Jerry-authorized order. ch-8's callbacks (Abu Ghraib, Ukrainian children) come from ch-2 (rank 2 → rank 10); ch-9's Walsh callback feeds forward to ch-12 (rank 8 → rank 12); ch-10's three-record-demand feeds forward to ch-13 (rank 9 → rank 13). The non-standard sequencing was set deliberately and the graph confirms it works.

6. **The Part IV closure pattern (11 → 12 → 13) is tight.** Each Part IV chapter has 4+ callbacks paying off in the next Part IV chapter or in ch-13. No cross-Part-IV forward-dep violations.

7. **No registered candidate edges, motifs, or discriminations.** All three registries are `candidates: []`. The first /dependency-check produces no candidate-edge discovery findings against prose — but this also means no chapter prose has been re-scanned against the registries for orphan references. A follow-up candidate-discovery pass (Wayne reading each chapter against the registries) is the natural next step but is out of scope for this baseline run.

## Action items by owner

| Owner | Action | Priority |
|---|---|---|
| bonnie-book-architect | Decide Reading A or Reading B for the Part II / ch-7 forward-dep resolution; document in `book/STATUS.md` cross-cutting items | HIGH |
| bonnie-book-architect | If Reading A: amend `book/toc.yml` and `book/cognitive-arc.yml` comments to declare Part II partial order ({4,5,6} ‖ 7 with 7 last) | conditional |
| wayne-narrative-lead | If Reading B: rewrite ch-7's "in Chapter 4 we met MH17" reference and signature-as-seam reference to be self-contained | conditional |
| /callback-audit | Verify ch-7's MH17 callback prose still reads correctly under whatever resolution is chosen | follow-up |
| /motif-audit | Re-evaluate the 12 sibling-internal motif-chain edges under the chosen resolution; trim or re-anchor as appropriate | follow-up |
| /cognitive-arc-audit | Re-evaluate `recognize-signature-as-seam.required_by[7]` under the chosen resolution | follow-up |
| xaiolai | Approve or override Bonnie's Reading A / Reading B decision | DECISION |
| bonnie-book-architect | Schedule next /dependency-check after first cross-Part rewrite; baseline this memo as the comparison point | scheduled |

## Confirmation

This is the first /dependency-check run with all three cross-chapter registries populated. The graph is acyclic. Two hard forward-dep violations exist in the baseline, both touching ch-7. Footprint distribution is top-loaded at ch-13 (31) and balanced through Parts II/III at 13-25; no chapter has footprint 0; no chapter is a viable cut. The Part III 9→10→8 sequencing and the Part IV 11→12→13 closure are clean.
