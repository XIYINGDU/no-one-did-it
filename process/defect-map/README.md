# Defect Maps

Per-chapter defect diagnoses produced by `/chapter-defect-diagnose`. Each map is one chapter's verdict against the 10 reader-experience values from `.claude/rules/12-reader-experience-values.md`, with cited prose evidence, and a recommended treatment class from `.claude/rules/08-treatment-class-discipline.md`.

## Filename convention

```text
process/defect-map/<n>-<slug>.md
```

Where `<n>` is the zero-padded chapter number and `<slug>` matches the chapter's slug in `book/toc.yml`. Example: `process/defect-map/02-the-four-goats.md`.

## Lifecycle

- **Stage 0 (Gate A prerequisite):** every chapter gets a defect map. Without 13 maps, Gate A cannot be authorized.
- **Re-diagnosis:** rerun when substantial revision changes which values pass or fail. Append a `reclassifications:` row to the matching `book/registries/treatment-classes.yml` entry; do not overwrite the original map silently.
- **Snapshot:** prior versions archive to `process/audits/history/<n>/<timestamp>/defect-map.md` before any new diagnosis writes over the file.

## Reading the maps

A map's "Recommended treatment class" is the input to the per-chapter rewrite cycle. The class plus the per-value verdicts answer the per-chapter question: *what needs to change in this chapter, and why?*

Use `_template.md` as the schema reference. Do not edit `_template.md` directly during normal operation; the template is the schema source.

## Authority

- `chapter-defect-diagnose` writes the maps.
- xaiolai confirms the recommended treatment class (especially for ch-01 and ch-13, per the boundary-chapter rule).
- `bonnie-book-architect` reviews when the treatment class is `structural-polish` or `full-craft-rewrite`.
- `nancy-legal-risk-counsel` reviews when the class is `defamation-safe-tighten` or when V7/V8 fail on live content.

See `.claude/skills/chapter-defect-diagnose/SKILL.md` for the full procedure.
