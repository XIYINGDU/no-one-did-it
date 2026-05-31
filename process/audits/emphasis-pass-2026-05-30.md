---
artifact_id: emphasis-pass-2026-05-30
title: "Emphasis pass — walk of 105 flagged emphasis instances across 13 chapters"
owner: xaiolai
status: open
auditor: scripts/audit_emphasis.py (judgment-based classifier)
audit_seed: 2026-05-30
---

# Emphasis pass — 2026-05-30

Walk of every flagged `<em>` / `<strong>` instance from
`scripts/audit_emphasis.py` against the v6 corpus. Each finding gets a
verdict; recurring patterns are addressed once and pointed at the
affected lines.

## Verdict codes

| Code | Meaning |
|---|---|
| **KEEP** | Mark earns its position; leave as is |
| **CUT** | Remove the emphasis (plain prose) |
| **REVISE** | Rewrite the sentence so emphasis is unnecessary |
| **CONVERT-H4** | Convert to `####` H4 sub-heading |
| **MOVE-INSTALL** | Move the bold install to the term's actual first mention |
| **NOTE** | Defers — needs out-of-band check (e.g. verify whose emphasis it is in a cited quote) |
| **HEURISTIC-GAP** | Auditor missed an exemption; widen the classifier, not the prose |

## Aggregate verdicts

Patterns that recur across chapters resolve once here; per-chapter
sections below point at the affected lines.

### Pattern A — Foreign proper nouns the classifier missed
**Verdict: HEURISTIC-GAP, not a prose change.**

The classifier's `_is_exempt_em` heuristic correctly catches Latin
diacritics, single proper nouns ≥ 4 chars, Title Case 2–8 word
publication names, and a Latin shorthand list. It misses:

- Long German institutional names ("Internationaler Komitee zur
  wissenschaftlichen Erforschung der Ursachen…" 9+ words) — exceeds
  the 8-word Title Case cap. Widen `_looks_like_publication_title` to
  accept 12+ word phrases when ≥ 80 % of tokens are capitalised
  German connectors (`zur`, `und`, `der`, `des`, `nationalsozialistischer`).
- Long German statute names ("Gesetz zur Aufhebung
  nationalsozialistischer Unrechtsurteile in der Strafrechtspflege" —
  same width problem).
- "Lex" + proper name ("Lex van der Lubbe") — Roman/civil-law
  convention for laws named for their first prosecution; rare in
  English-language nonfiction, no current heuristic. Add: if first
  token is `Lex` or `Loi` or `Ley` followed by a proper name, exempt.
- "pharmakos" — ancient Greek transliterated, single word, lowercase,
  no diacritic. The `SINGLE_PROPER_NOUN_RE` requires uppercase.
  Optional refinement: a small Greek/Latin foreign-term allowlist that
  this book actually uses.

**Affected lines (KEEP all):** ch-01 L85, L101, L115, L117, L119, L159.

### Pattern B — The 8 diagnostic questions (recall vs install)
**Verdict: CUT the italics on later recalls; KEEP only on the formal
list-install in ch-03.**

The book installs an 8-question diagnostic in ch-03's middle section.
Each later chapter (ch-05, ch-07, ch-09, ch-10) recalls the
questions in italics inside its own diagnostic block. The audit
flags these because each chapter's setup prose mentions "who had
control" or "who knew" before italicising the question form.

The right discipline:

1. The **install** lives in ch-03, formally listed once, italicised.
2. Every later chapter's recall should drop the italics. The reader
   has the framework; further italics is decorative.

Exception: when a chapter literally **runs the diagnostic in-text**
(walking through the 8 questions one by one), the italicised
question-form acts as a structural label and earns its position.
The four chapters that do this (ch-03, ch-08, ch-10, and an inline
block in ch-13) keep the question italics; chapters that *cite the
framework in passing* drop them.

**Affected lines:**
- ch-03 L105, L107, L109, L113, L115, L117, L119: KEEP — this is the
  install chapter; the questions are listed formally.
- ch-03 L127, L131, L135: KEEP — same chapter still running the
  install in its diagnostic block.
- ch-03 L137 (`*not*` repeat): CUT — single-word stress already used.
- ch-07 L67, L121 (italicised question sentences): CUT — recall, not
  install.
- ch-09 L59 (italicised question sentence): CUT — recall.
- ch-09 L81 series (6 single-word italicised "answers": *blamed*,
  *benefit*, *record*, *control*, *knowledge*, *preventability*):
  KEEP — this is the chapter's own diagnostic-as-list at line 81;
  it functions as the install of the **5-element responsibility-chain
  framework specifically for AI** (input/deployment/evaluation layers).
- ch-09 L103 series (5 single-word italicised repeats of same):
  CUT all — the install just happened 22 lines earlier; this is
  decorative recall.
- ch-11 L37 (`Who would bear the cost if the layer fails?`): CUT — recall.

### Pattern C — The 5-element responsibility-chain (control, benefit, knowledge, preventability, record)
**Verdict: KEEP at the chapter's own formal install; CUT later repeats.**

Same pattern as B but with the responsibility-chain components. These
five words appear in italics as a list-install in chapters that
re-introduce them in a new context (ch-05 introducing the chain;
ch-09 transposing to AI; ch-11 making it doctrine).

**Affected lines:**
- ch-05 L38, L40, L42, L44, L46 (*control*, *benefit*, *knowledge*,
  *preventability*, *record*): KEEP — formal install for this chapter.
- ch-09 L81 series: KEEP (covered under Pattern B above).
- ch-09 L103 repeats: CUT all.
- ch-12 L15 (*existed*, *existed*, *published*, *ruled*): CUT — these
  are stress emphasis on common verbs, not list-installs. The
  sentence reads as overemphasised.

### Pattern D — Single-word stress emphasis on common verbs / pronouns
**Verdict: mostly CUT; KEEP only where contrast is load-bearing.**

Single-word italics on common words (*not*, *where*, *order*,
*which*, *could*, *function*, *person*, *named*, *attached*,
*removed*) are stress emphasis. The book's discipline (rule 14,
authorial stance; rule 04, style) says: let prose carry stress
through sentence structure, not italics.

**Affected lines (CUT all unless noted):**
- ch-03 L173 (*where*), L177 (*order*), L181 (*which*), L195
  (*acquitted*): CUT.
- ch-04 L169 (*closed*, *resolved*, *addressed*), L177 (*procedural
  shell*): CUT — these are quoted euphemisms named-as-examples;
  use quotation marks instead of italics ("closed", "resolved",
  "addressed").
- ch-05 L84 (*system*), L153 (*isolated*), L155 (*foreign*,
  *junior*, *deceased*): CUT all — these are the words the chapter
  is examining. Use quotation marks if the goal is to mark "the
  word as the institution used it"; otherwise CUT.
- ch-06 L69 (*permits*, *require*): CUT — these are contrast words
  in a single sentence; the prose can carry the contrast.
- ch-11 L15 (*not*), L98 (*named*, *attached*, *removed*), L174
  (*could*), L188 (*function*, *person*): CUT.

### Pattern E — Italicised whole sentences (italics-as-wallpaper)
**Verdict: REVISE — convert to plain prose with structural rhythm
carrying the point, OR convert to H4 if it is a quasi-heading.**

Long italicised sentences are decorative — they violate V10
(audio-survivable). The narrator's voice cannot reproduce
sentence-length italics; they read as a tonal shift the listener
cannot follow.

**Affected lines:**
- ch-03 L76, L153, L167, L197, L203: REVISE — drop italics; let
  prose stand.
- ch-05 L34, L48, L80, L88, L92: REVISE.
- ch-07 L67, L121 (×2), L178: REVISE.
- ch-09 L189, L207: REVISE.
- ch-11 L120, L122, L146, L188: REVISE.
- ch-12 L61, L119, L140: REVISE.
- ch-13 L168, L186: REVISE.

### Pattern F — `**bold**` term-recall that's not actually a first install
**Verdict: KEEP if first formal install in this chapter; CUT
otherwise.**

- ch-07 L37 (*complainant*, *prosecutor*): KEEP — this is the 5-role
  Post Office list-install (deployer, holder of the audit trail,
  complainant, prosecutor, disclosure controller). The audit
  pseudo-install fires because "complainant" and "prosecutor" appear
  in earlier prose; but L37 is the formal list-install, the only
  place all 5 are named together. Keep.
- ch-07 L147 (*first*): CUT — single-word stress.
- ch-09 L27 (*input layer*): MOVE-INSTALL — the install belongs at
  L7 where the 3-layer schema is first named. Cut the bold at L27
  and bold the L7 mention instead. Same applies to *deployment
  layer* and *evaluation layer* if they're flagged the same way
  (they probably are — re-check).
- ch-11 L166 (*SOX §§ 302/906*, *UK SMCR*): KEEP — these are the
  formal install in the numbered doctrine list. Pseudo-install
  fires because the doctrines were named in setup prose; but L166
  is the canonical install. (The H4 demotion earlier converted the
  enclosing "2. SOX §§ 302 and 906" to an H4; this leaves the
  inline italic as the formal install — keep.)

### Pattern G — Single-word italic repeats
**Verdict: CUT the repeat; KEEP only the first install.**

- ch-01 L31 (*scapegoat*) → KEEP (first install); L33 → CUT.
- ch-09 L103 series (5 repeats): all CUT (covered above).
- ch-12 L136 (*features*) → CUT (L73 already installed); also
  L138, L154, L180 (*counter-record from outside*, *enforcement
  architecture*, *index*): each REVISE — these are concept-tags
  in prose, not first installs.

### Pattern H — In-quote emphasis without `(emphasis added)` annotation
**Verdict: NOTE — requires source verification per quote.**

Rule 06 requires every emphasis inside a quoted passage to be
annotated as `(emphasis added)` or `(emphasis in original)`. The
audit flags chapters where this annotation is absent:

| Chapter | In-quote emphasis count |
|---|---|
| ch-03 | 9 |
| ch-04 | 7 |
| ch-06 | 9 |
| ch-07 | 4 |
| ch-09 | 1 |
| ch-10 | 1 |
| ch-12 | 1 |
| ch-13 | 12 |

**Action:** This is a separate Stephen-led pass. For each quote
containing italics or bold, the source-ledger card must record
whether the emphasis is original (annotate `(emphasis in
original)`) or added (annotate `(emphasis added)`). Do not change
the emphasis itself until the source ledger has been consulted.

### Pattern I — ch-13 reader's field guide
**Verdict: NOTE — separate pass.**

Ch-13 contains 38 in-quote `<strong>` and 30 in-quote `<em>` — 68
marks total inside quotation blocks. The chapter is a quoted
field-guide format; most marks are inside the quoted examples.
This chapter needs its own pass with rule 06 in hand. Out of scope
for this worksheet.

## Per-chapter walks

### ch-01 — The Altar Moves
*9 flagged; 0 structural.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 31 | *scapegoat* | pseudo_install | KEEP | First install. |
| 33 | *scapegoat* | redundant_repeat | CUT | Install already happened L31. |
| 85 | *Internationaler Komitee zur…* | review | KEEP | Pattern A (heuristic gap). |
| 101 | *Gesetz zur Aufhebung…* | review | KEEP | Pattern A. |
| 115 | *Gesetz zur Aufhebung…* | redundant_repeat | KEEP | Pattern A — publication convention italicises every mention. |
| 117 | *"Die Bundesanwaltschaft…* | review | KEEP | German verbatim quotation. Add `(emphasis in original)` if italics are theirs; otherwise it's a citation. |
| 119 | *Lex van der Lubbe* | redundant_repeat | KEEP | Pattern A — civil-law naming convention. |
| 159 | *pharmakos* (×2) | redundant_repeat | KEEP | Pattern A — Greek transliteration. |

### ch-02 — The Four Goats
*PASS.* No flags. Confirmed: 4 strong term-installs (Pattern F) all
classified `logical_install_first`; 24 em are publication titles or
foreign terms.

### ch-03 — Who Could Have Stopped It?
*20 flagged + 9 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 29 | *software* | pseudo_install | CUT | Pattern D — single-word stress. |
| 33 | *sequence* | pseudo_install | CUT | Pattern D. |
| 76 | italicised sentence | review | REVISE | Pattern E. |
| 105–119 | 8 diagnostic-question italics | pseudo_install | KEEP | Pattern B — install lives here. |
| 127, 131 | (covered in question install) | redundant_repeat | KEEP | Same install block. |
| 135 | italicised sentence | review | REVISE | Pattern E. |
| 137 | *not* | redundant_repeat | CUT | Pattern D. |
| 153, 167 | italicised sentences | review | REVISE | Pattern E. |
| 173, 177, 181 | *where*, *order*, *which* | pseudo_install | CUT | Pattern D. |
| 195 | *acquitted* | pseudo_install | CUT | Pattern D. |
| 197, 203 | italicised sentences | review | REVISE | Pattern E. |
| (9 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-04 — The Proxy and the Sponsor
*4 flagged + 7 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 169 | *closed*, *resolved*, *addressed* | pseudo_install | CUT | Pattern D — convert to "scare-quotes" if marking institutional language. |
| 177 | *procedural shell* | pseudo_install | CUT | Pattern D. |
| (7 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-05 — The Guilty Goat
*15 flagged + 1 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 34 | italicised sentence | review | REVISE | Pattern E. |
| 38, 40, 42, 44, 46 | *control*, *benefit*, *knowledge*, *preventability*, *record* | pseudo_install | KEEP | Pattern C — formal 5-element install. |
| 48 | italicised sentence | review | REVISE | Pattern E. |
| 80, 88, 92 | italicised sentences | review | REVISE | Pattern E. |
| 84 | *system* | pseudo_install | CUT | Pattern D. |
| 153 | *isolated* | pseudo_install | CUT | Pattern D. |
| 155 | *foreign*, *junior*, *deceased* | pseudo_install | CUT all 3 | Pattern D — quoting institutional language; use "scare-quotes" if marking. |
| (1 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-06 — The Pretext
*2 flagged + 9 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 69 | *permits*, *require* | redundant + pseudo | CUT both | Pattern D — contrast carries in prose. |
| (9 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-07 — The Record Is the Battlefield
*7 flagged + 4 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 37 | **complainant**, **prosecutor** | pseudo_install | KEEP | Pattern F — 5-role formal list-install. |
| 67 | italicised question | review | REVISE | Pattern E (recall, not install). |
| 121 | italicised sentence (×2) | review | REVISE | Pattern E. |
| 147 | *first* | pseudo_install | CUT | Pattern D. |
| 178 | italicised sentence | review | REVISE | Pattern E. |
| (4 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-08 — When Power Calls Itself the Goat
*PASS.* No flags except 1 in-quote SOFT (Pattern H, NOTE).

### ch-09 — The Model Did It
*16 flagged + 1 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 27 | **input layer** | pseudo_install | MOVE-INSTALL | The 3-layer schema is named at L7; move the bold to L7 and unbold L27. (Verify L29 *deployment layer* and L31 *evaluation layer* in the same pattern; apply uniformly.) |
| 59 | italicised question sentence | review | REVISE | Pattern E (recall, not install). |
| 81 (×6) | *blamed*, *benefit*, *record*, *control*, *knowledge*, *preventability* | pseudo_install | KEEP all | Pattern B/C — formal install for the AI-context 6-element list. |
| 103 (×5) | repeats of L81 components | redundant_repeat | CUT all 5 | Pattern G. |
| 103 | *record-control* | pseudo_install | KEEP if first formal install of this compound term; otherwise CUT. Check L81 — if "record" was the install, "record-control" at L103 is a new compound and KEEP. |
| 111 | *where* | pseudo_install | CUT | Pattern D. |
| 189, 207 | italicised sentences | review | REVISE | Pattern E. |
| (1 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-10 — War Is the Perfect Laundry
*PASS.* No flags except 1 in-quote SOFT (Pattern H, NOTE). The
chapter's 8 in-quote `<strong>` are quoted material — the
diagnostic questions appear quoted from ch-03.

### ch-11 — Make Responsibility Follow Control
*14 flagged + 1 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 15 | *not* | review | CUT | Pattern D. |
| 37 | italicised question | review | CUT | Pattern B (recall, not install). |
| 98 | *named*, *attached*, *removed* | pseudo_install | CUT all 3 | Pattern D — contrast triplet, let prose carry it. |
| 120, 122, 146, 188 | italicised sentences | review | REVISE | Pattern E. |
| 166 | **SOX §§ 302/906**, **UK SMCR** | pseudo_install | KEEP both | Pattern F — formal doctrine-name installs (post H4 demotion, these are the surviving inline installs). |
| 174 | *could* | pseudo_install | CUT | Pattern D. |
| 188 | *function*, *person* | pseudo_install | CUT both | Pattern D. |
| (1 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-12 — Keep the Record
*13 flagged + 1 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 15 (×4) | *existed*, *existed*, *published*, *ruled* | pseudo_install | CUT all 4 | Pattern D — stress on common verbs. |
| 55 | *before* | pseudo_install | CUT | Pattern D. |
| 59 | *which* | pseudo_install | CUT | Pattern D. |
| 61, 119, 140 | italicised sentences | review | REVISE | Pattern E. |
| 136 | *features* | redundant_repeat | CUT | Pattern G — install already at L73. |
| 138 | *counter-record from outside* | pseudo_install | REVISE | Pattern G — concept-tag in prose; either fold into the surrounding sentence or convert the surrounding paragraph to formally install the term once. |
| 154 | *enforcement architecture* | pseudo_install | REVISE | Pattern G — same shape. |
| 180 | *index* | pseudo_install | REVISE | Pattern G. |
| (1 SOFT) | in-quote unmarked | — | NOTE | Pattern H. |

### ch-13 — A Reader's Field Guide
*2 flagged + 12 in-quote SOFT.*

| L | Mark | Cat. | Verdict | Note |
|---:|---|---|---|---|
| 168 | italicised sentence | review | REVISE | Pattern E. |
| 186 | italicised sentence | review | REVISE | Pattern E. |
| (38 in-quote strong) | quoted material | — | NOTE | Pattern I — separate pass. |
| (30 in-quote em) | quoted material | — | NOTE | Pattern I. |

## Summary by verdict

| Verdict | Count | What it costs |
|---|---|---|
| KEEP | ~25 | Nothing — these are doing structural work |
| CUT | ~45 | Mechanical sentence-level edits |
| REVISE | ~17 | Each is a sentence-level prose pass (italic sentence → prose) |
| MOVE-INSTALL | 1–3 | ch-09's input/deployment/evaluation layer pattern |
| HEURISTIC-GAP | ~8 (ch-01) | Widen `_is_exempt_em` in audit_emphasis.py |
| NOTE | ~34 | Source-verify in-quote emphasis (Pattern H) — Stephen pass |
| Defer (ch-13) | ~68 | Separate field-guide pass |

## Sequencing the actual edits

1. **First — auditor refinement (Pattern A):** widen
   `_looks_like_publication_title` for long German names; add `Lex
   <Name>` and a small Greek/Latin allowlist. Re-run audit. Expect
   ~8 fewer flags. (No prose change.)
2. **Second — mechanical CUTs (Patterns D, G):** ~45 single-word
   italic removals across ch-03, ch-04, ch-05, ch-06, ch-09, ch-11,
   ch-12. Each is a `*word*` → `word` edit. Verify no
   structural_subheader fires on a remaining adjacent bold.
3. **Third — REVISE passes (Pattern E):** ~17 italicised whole
   sentences become plain prose. Each is a sentence-level rewrite
   that must preserve the diagnostic point. Stephen reviews any
   that touch a cited claim's framing.
4. **Fourth — MOVE-INSTALL (Pattern F edge case):** ch-09's
   input/deployment/evaluation layer install relocates to its true
   first mention.
5. **Fifth — Stephen pass on Pattern H:** verify and annotate every
   in-quote emphasis per rule 06.
6. **Sixth — ch-13 field guide pass:** separate worksheet; not
   resolved here.

After steps 1–4, re-run `python3 scripts/audit_emphasis.py` and
expect a substantially smaller flag list with most surviving flags
in Pattern H (in-quote, owned by Stephen) or REVIEW for
chapter-specific judgments xaiolai keeps.

---

Owner: xaiolai
Auditor: scripts/audit_emphasis.py (commit da335e6, judgment-based)
Generated from: `python3 scripts/audit_emphasis.py --flagged-only`
Open question: should single-word italics on **the diagnostic action
verbs** ("blamed", "knew", "controlled") survive as a deliberate
in-text marking convention? Pattern B/C above assumes yes for the
formal install, no for recalls. Confirm before sweeping the CUTs in
ch-09 L103.
