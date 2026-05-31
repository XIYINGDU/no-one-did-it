# Design-Team Delivery — Inventory (2026-05-29)

> Reference record of the design package received for *No One Did It*. This is an
> inventory and assessment only; no production decisions are made here. Source of
> truth for text remains `book/chapters-v5/` and `book/toc.yml`.

## Source

| Field | Value |
|---|---|
| Archive | `No One Did It.zip` |
| Location received | `~/Downloads/No One Did It.zip` (transient — not yet archived in-repo) |
| Size | 26 MB, 66 files |
| Dated | 2026-05-29 |
| Inspected-extract (scratch, not in repo) | `<local-scratch>` |

## Bottom line

This is a **design-exploration tool**, not drop-in EPUB/print files. The bulk of it
is a React + Babel "design canvas" app (`*.jsx`, `image-slot.js`) plus screen-only
CSS that the team used to compose and screenshot concepts. The **usable production
outputs are the rendered PNG art crops** under `assets/`. The cover copy supplied is
**byte-identical** to `book/cover-copy.md`. **No cover direction is finalized**, and
**no title-composited, high-resolution cover master** is present in the package.

## The design system at a glance

The single most informative file is `uploads/pasted-1780037841705-0.png` (1536×1024) —
a one-sheet board of the whole **Dossier** system:

- **Front-cover concepts:** A · The Defendant · B · The Evidence Wall · C · The Case File — all "NO ONE DID IT" typeset on a manila case-file ground.
- **Full wraparound** (Concept A): back · spine · front.
- **Back-cover concepts:** Case Summary · Evidence Inventory.
- **Part covers (4):** I The Mechanism · II The Patterns · III The Stress Tests · IV The Anti-Laundering Rules.
- **Chapter cards (13):** one per chapter, each a small courtroom vignette.
- **Recurring animal cast:** Owl (Judge) · Fox (Defense Lawyer) · Badger (Prosecutor) · Donkey (Bailiff) · Raven (Reporter) · Eagle (Juror) · Elephant (Juror) · **Wolf (Spectator) — "the wolf is always watching."**
- **Motif / endpaper:** scales of justice. **Style:** manila/newsprint palette, linen texture, rubber stamps ("EXHIBIT 02"), wax seal.

A **second, separate aesthetic** also exists — the **Cartoon "Animal Court"** full courtroom illustration (`animal-court.png` / `cover_def.png`), captioned *"Hope is not a defense. Truth does not care."* The `cover_def` ("definitive") crop is from this cartoon, **art-only (no title)**. So the front-cover choice is effectively **titled-manila Dossier** vs **full-bleed Cartoon courtroom** — unresolved.

## File inventory by category

### 1. Entry-point renders — HTML (2)

| File | Renders |
|---|---|
| `No One Did It - Covers.html` | "Court-scratch" system: 3 front concepts (Struck List / Empty Chair / Verdict) + Illustrated edition + Cartoon "Animal Court" + chapter covers. Loads React via CDN. |
| `No One Did It - Dossier Edition.html` | "Dossier" system: Case File / Defendant / Evidence Wall fronts, wraparound, back variants, 4 part covers, 13 chapter cards, cast & style. Has a manila/newsprint paper toggle. |

### 2. Design-tool source — JSX / JS (9) · tool-internal, NOT EPUB-usable

| File | Role |
|---|---|
| `design-canvas.jsx` | The canvas/artboard framework (DesignCanvas, DCSection, DCArtboard). |
| `image-slot.js` | Image-placement/crop helper for the canvas. |
| `tweaks-panel.jsx` | Live tweak controls (e.g., paper-tone radio). |
| `covers.jsx` | Court-scratch cover components + `CHAPTERS` / `ART_CHAPTERS` data. |
| `cartoon.jsx`, `cartoon-art.jsx` | The Cartoon "Animal Court" components. |
| `dossier-front.jsx`, `dossier-back.jsx`, `dossier-chapters.jsx` | Dossier front/back/part/chapter components + `PARTS` / `CHAPTERS` data. |

### 3. Stylesheets — CSS (2) · screen-only, NOT EPUB CSS

| File | Note |
|---|---|
| `covers.css` | Styling for the court-scratch canvas. Relies on inline SVG turbulence/`feDisplacementMap` filters (`#scratch`, `#scratch2`) — screen effects that do not translate to EPUB. |
| `dossier.css` | Styling for the dossier canvas; SVG grunge/roughen filters (`#d-rough`, `#d-grunge`). Same caveat. |

### 4. Rendered art — production candidates (17 PNG) · the usable outputs

| File | Dimensions | Depicts | Likely production use |
|---|---|---|---|
| `assets/animal-court.png` | 1402×1122 | **Master** courtroom illustration (owl judge, fox counsel, goat "DEFENDANT", predator jury, prey gallery; "Hope is not a defense…"). Identical to `uploads/pasted-…596780-0.png`. | Cover/illustration master (cartoon edition) — landscape; highest-res courtroom art in the package. |
| `assets/crops/cover_def.png` | 840×1295 | Portrait crop of the courtroom (judge + fox + goat). **Art only, no title.** | Front-cover candidate (cartoon) — **low-res** for EPUB. |
| `assets/crops/cover_wrap.png` | 805×1295 | Cover wrap/variant crop. | Cover variant. |
| `assets/crops/goat.png` | 472×624 | The goat (defendant / scapegoat). | Motif / chapter art. |
| `assets/crops/judge.png` | 312×412 | The owl judge. | Motif. |
| `assets/crops/part0.png` … `part3.png` | 864×510 each | The four part-divider scenes (Parts I–IV; 0-indexed). | **Part-opener images (reflowable-EPUB usable).** |
| `assets/crops/pin0.png` … `pin3.png` | ~300–340 × 260–300 | Pushpins (evidence-board). | Decorative — print / fixed-layout. |
| `assets/crops/wolf_cast.png`, `wolf_find.png`, `wolf_sum.png`, `wolf_wrap.png` | ~240–440 wide | The wolf ("always watching") in various crops. | Recurring motif — print. |

### 5. Source uploads (5)

| File | Dimensions | What it is |
|---|---|---|
| `uploads/cover-copy.md` | — | **Identical** to `book/cover-copy.md` (title/subtitle/parts/chapter titles verbatim from v5; tagline options still open). |
| `uploads/pasted-1780034596780-0.png` | 1402×1122 | Source = the animal-court master (dup of `assets/animal-court.png`). |
| `uploads/pasted-1780037841705-0.png` | 1536×1024 | **The full design-system board** (see "at a glance" above). |
| `uploads/pasted-1780043540873-1.png`, `…542428-1.png` | 2593×2000 (identical pair) | A red **"CONFIDENTIAL" rubber stamp** (transparent PNG) — dossier decoration. *(High pixel count, but it is the stamp, not a cover master.)* |

### 6. Screenshots (31) · design iterations — NOT production

`screenshots/` holds 31 small PNGs documenting the team's iteration (focus/crop tests,
stamp-style tries, insert markers, cartoon passes, `overview.png`, `fcase-compose.png`,
etc.). Process record only; none are book assets.

## Production-relevance summary

| Bucket | Files |
|---|---|
| **Usable in a reflowable EPUB** | cover art (cartoon courtroom, *low-res*), the 4 part-divider images (`part0–3`), character motifs (`goat`, `judge`, `wolf_*`), and `cover-copy.md` (text). |
| **Print / fixed-layout only** | the dossier case-file interiors, evidence-wall, pins, stamps, wax seal — none survive reflow. |
| **Tool-internal / reference** | all `*.jsx`, `image-slot.js`, both `*.css` (SVG-filter screen effects), all `screenshots/`. |

## Open issues (for discussion)

1. **Cover direction is not finalized** — two distinct aesthetics: titled-manila **Dossier** covers (Defendant / Evidence Wall / Case File) vs the art-only **Cartoon Animal Court** (`cover_def`). A direction must be chosen.
2. **No production-ready cover file.** The cartoon crop is **840×1295 and carries no title/subtitle/author**; EPUB ideal is ~1600×2560 portrait. The best courtroom art is the 1402×1122 landscape master. The only ≥1600px assets are the CONFIDENTIAL stamp (irrelevant). A final cover needs either a **higher-res, title-composited export from the design team** or an in-house compositing pass.
3. **Tagline still open** — `cover-copy.md` lists options; none chosen.
4. **Asset preservation** — the delivery currently lives only in `~/Downloads` (transient). Recommend archiving the package into `dev-docs/` (e.g., a `06_DESIGN_TEAM_DELIVERY/` folder) so it is not lost, before any production use.
