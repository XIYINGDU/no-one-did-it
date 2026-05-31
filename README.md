# No One Did It

![No One Did It — full wraparound cover](book/design/cover-wraparound.webp)

> ***No One Did It: Responsibility Laundering, from the Scapegoat to the Algorithm***
> by Li Xiaolai · Xiaolai Books, first edition 2026
> Kindle: **[amazon.com/dp/B0H3GDDL6H](https://www.amazon.com/dp/B0H3GDDL6H)** · eBook ISBN 978-1-80826-002-5 · paperback ISBN 978-1-80826-003-2

Civilization did not stop sacrificing substitutes when it stopped sacrificing goats. It moved the altar — from the temple to the org chart, from the org chart to the legal entity, from the legal entity to the algorithm — and at each move the part where someone announces *"this one will carry it for us"* went further underground. *No One Did It* names the move — **responsibility laundering** — and hands the reader an eight-question diagnostic and four recognizable shapes that walk a laundered case back to a name.

This repository is the open source of the book: the full prose, the 292-card source ledger behind every cited claim, and the complete record of how it was written, edited, fact-checked, cleared for law, and published.

## The book

Four parts, thirteen chapters, one instrument carried throughout.

- **Part I — The Mechanism.** Installs the four shapes laundering takes (pure scapegoat, partial scapegoat, system/object alibi, cost-bearing goat) and the eight questions that separate who was blamed from who held control — worked against Reichstag 1933, Therac-25, Abu Ghraib, Boeing, Bhopal, Volkswagen, the Ford Pinto.
- **Part II — The Patterns.** The same shape across centuries and domains: the proxy and the sponsor (Crimea, MH17, Blackwater); the partial scapegoat as design (Bhopal, the 737 MAX); the legal-administrative pretext (family separation, the census citizenship question, the Ukraine aid hold); the record as battlefield (the Post Office Horizon scandal).
- **Part III — The Stress Tests.** The diagnostic held against contested modern terrain: Iraq WMD and war; reverse-scapegoating in the second-term Trump administration; the AI stack at three layers — training (*Bartz v. Anthropic*), deployment (GPT-4o), evaluation (Llama 4 / LMArena).
- **Part IV — The Anti-Laundering Rules.** The diagnostic turned into design: statutes that already embed responsibility-follows-control (Park, Sarbanes-Oxley, the UK Senior Managers Regime, the Inquiries Act 2005 §21); three record-discipline rules; and a reader's field guide.

The thirteen chapters are in [`book/chapters-v6/`](book/chapters-v6/).

## How it was written, edited, and published

The book was built by a human principal author working with a **13-agent crew**, each agent a role in a working publishing house, all operating under a written constitution of rules ([`.claude/rules/`](.claude/rules/)) that the validators in [`tests/`](tests/) enforce. The discipline the book demands of the institutions it analyzes is applied first to itself.

- **Research** — four domain researchers (history, war/statecraft, AI/technology, public law) assemble primary-source case files; nothing enters a chapter without a graded source.
- **Writing** — a narrative lead turns approved case files into prose under a style and authorial-stance discipline (severe, evidence-driven, the author standing beside the reader).
- **Fact-checking** — every load-bearing claim earns an A/B/C/D evidence grade against a **292-card source ledger** ([`book/evidence/source-ledger/`](book/evidence/source-ledger/)); quotes are byte-exact; court and inquiry findings are anchored to paragraph.
- **Red-team and reader** — an adversarial editor attacks overclaim and cliché; a cold reader checks that the recognition is earned, not delivered.
- **Legal** — risk counsel maps every claim about a living person or company to its correct procedural stage (charged / settled / convicted / alleged), tightening wording to the documented record.
- **Publishing** — a single canonical text (`book/chapters-v6/`) drives both editions through reproducible pipelines: an EPUB build (epubcheck + Kindle Previewer gates) and a 6×9 print interior + cover.

The full apparatus — the crew, the skills and rules they operate under, the validators — lives in [`.claude/`](.claude/), [`scripts/`](scripts/), and [`tests/`](tests/). The framework itself is the [eou-foundry plugin](https://github.com/xiaolai/eou-foundry); this book is one application of it. The author's note on motive, use, and how the book was built is at [`book/back-matter/note-from-the-author.md`](book/back-matter/note-from-the-author.md); the process records (audits, red-team and legal memos, reader reports, defect maps) are in [`process/`](process/). If you want to work this way, the [`.claude/rules/`](.claude/rules/) directory and that author's note are the entry points.

## Read and verify

The prose is openly licensed (below) — read it, quote it, check it. To verify a claim, start at [`book/evidence/source-ledger/cards/`](book/evidence/source-ledger/cards/): every cited claim has a card naming the source, its evidence grade, and the primary document. Corrections are welcome (see below) and held to the same evidence bar the book holds itself to.

## Build the editions

The packaged editions are sold on Amazon; this repository holds the **source**. Both editions regenerate from the v6 text — the `dist/` outputs are build artifacts, not the master.

```bash
# Kindle EPUB
python3 pipelines/epub/assemble_v6_manuscript.py   # spine-v6.yml → dist/manuscript-v6.md
python3 pipelines/epub/build_kdp_epub.py           # manuscript → EPUB (cover, title, contents)
python3 pipelines/epub/validate_kdp_epub.py        # epubcheck + Kindle Previewer + gates

# KDP paperback (6×9 interior + full-wrap cover)
cd pipelines/print && node pipeline.mjs

# Verify the discipline holds
python3 -m pytest tests/ -q
```

## Repository map

```
book/chapters-v6/    the 13 chapters (canonical text)
book/front-matter/   copyright, dedication, epigraph, preface, note-on-cases
book/back-matter/    references, bibliography, methods, glossaries, author notes
book/evidence/       source ledger (292 cards), case files, diagrams, photos
book/design/         cover + EPUB metadata/CSS + the 4 part-divider plates
book/registries/     callback-graph, cognitive-arc, motif-registry
process/             how the book was made — audits, review memos, reader reports
pipelines/           EPUB build, print-PDF build, cover design studio
.claude/             the 13-agent crew + skills + rules + hooks
scripts/ · tests/    validators and the 119-test discipline gate
dev-docs/            research material, proposals, working notes
```

## License

Dual-licensed.

| What | License |
|---|---|
| **Prose** — `book/chapters-v6/`, `book/front-matter/`, `book/back-matter/`, and any edition built from them (the assembled manuscript, the EPUB, the print PDFs) | [**CC BY-NC 4.0**](https://creativecommons.org/licenses/by-nc/4.0/) — attribution required; no commercial reuse. Quote for review, criticism, scholarship. Do not republish or sell. |
| **Apparatus** — everything else: `.claude/`, `scripts/`, `pipelines/`, `tests/`, `process/`, `book/evidence/source-ledger/`, `book/registries/`, `book/design/`, `dev-docs/` | [**MIT**](https://opensource.org/license/mit) — copy, adapt, build your own book with it. |

Full texts in [`LICENSE`](LICENSE).

## Corrections, evidence challenges, source disputes

Open an issue. The book's evidence-grade discipline applies to corrections too: a correction needs a citation at least as good as the one the book carries. Pull requests against `book/chapters-v6/` are reviewed against the same gates the original chapters passed. The corrections record will live in [`CORRECTIONS.md`](CORRECTIONS.md) once any land.

## Author

Li Xiaolai — writer, teacher, investor, builder. See [`book/back-matter/about-the-author.md`](book/back-matter/about-the-author.md), [lixiaolai.com](https://lixiaolai.com), or [github.com/xiaolai](https://github.com/xiaolai).
