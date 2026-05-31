# Design Studio — *No One Did It* visual production

A local, offline re-host of the design team's "omelette" canvas, plus a
headless-Chrome export pipeline. Renders the cover/part/chapter artwork JSX
faithfully (real fonts + SVG filters, no CDN), lets you tweak it, and exports
production-resolution assets for the KDP EPUB.

Governed by `.claude/rules/16-kdp-epub.md`. Node **stdlib only** — no `npm install`.

## Run the studio (view + tweak)

```bash
node design-studio/serve.mjs          # -> http://localhost:5180/   (PORT overrides)
```

- Switch **Illustrated / Cartoon** ↔ **Dossier** in the top bar.
- **Edit mode** (on by default): double-click a filled `<image-slot>` to re-crop
  (drag to reposition, corner-drag/scroll to zoom); move tweak sliders (e.g. the
  Dossier paper tone). Edits persist to `design/.image-slots.state.json` /
  `design/.design-canvas.state.json` on disk via the write bridge.
- Scroll/pinch to zoom the canvas, drag to pan.

**Which art is drag-editable:** only the court-scratch fronts (`covers.jsx`) use
editable `<image-slot>`s. The **Illustrated/Cartoon** cover (`cartoon-art.jsx`) and
the **Dossier** fronts use fixed `<img>`/positions — tweak those by editing the JSX
crop values (`objectPosition`, `pos`, `zoom`, font sizes) and refreshing; the studio
is the live preview + the export source.

## Export an asset

```bash
# Cover: Illustrated framed plate, 1.6:1 box, 1600x2560 sRGB JPEG -> book/design/epub/cover.jpg
node design-studio/export.mjs --cover

# A different cover layout / edition:
node design-studio/export.mjs --board ill-bleed --cover            # full-bleed
node design-studio/export.mjs --board f-case --ed dossier --cover  # Dossier "Case File"

# Any board to a PNG/JPEG under out/ (add --jpeg for JPEG):
node design-studio/export.mjs --board cart-1 --w 1600 --jpeg
```

It reuses a running studio if one answers on the port, else starts a temporary one.
Board ids are the `DCArtboard` ids in the entry HTMLs (shown as labels in the studio):
`ill-front`, `ill-bleed`, `ill-back`, `ill-ch-I…VI`, `cart-1`, `f-list/-chair/-verdict`
(covers); `f-case/-def/-wall`, `b-sum/-inv/-find`, `part-I…IV`, `ch-1…13`, `cast`,
`style` (dossier).

After `--cover`: `python3 pipelines/epub/build_kdp_epub.py && python3 pipelines/epub/validate_kdp_epub.py`.

## Two lanes (don't rasterize text)

- **Raster (this studio):** the front cover, and part-divider / chapter-opener **art**.
  These embed in the EPUB as images.
- **Reflowable XHTML (NOT this studio):** title page, dedication, epigraph, chapter
  epigraphs/titles — authored as text, styled by `book/design/epub/kdp.css`, so they reflow,
  carry `alt`, survive audio, and stay canonical in v5. The studio render of such a
  page is a visual *spec*, never the shipped artifact.

## Before the FINAL cover ships

The `cartoon-art.jsx` template still carries the design team's **placeholder byline
"A. Reyes"** and the tagline **"How power keeps the benefit and launders the blame"**.
The real cover must use the byline **Xiaolai Li** and the real subtitle **"Responsibility
Laundering, from the Scapegoat to the Algorithm"** (to match `book/design/epub/metadata.yml`).
Fix those JSX values, then re-export. (Dossier templates carry "Scapegoat Press" / similar placeholders.)

## Layout

```
design-studio/
  serve.mjs          # static server + omelette write bridge + parent shell + /solo route
  export.mjs         # headless-Chrome screenshot -> sRGB JPEG (spawn-poll-kill; self-contained)
  omelette-shim.js   # window.omelette.writeFile -> POST /__omelette/write
  design/            # the design package (JSX/CSS/assets), rewired to local deps
  vendor/            # React 18.3.1, ReactDOM, @babel/standalone 7.29, fonts (woff2 + fonts.css)
  out/               # screenshot scratch (gitignored)
```

Vendored deps + the sidecar state JSON are tracked so the render is reproducible and
GFW-proof (nothing is fetched from a CDN at render time).
