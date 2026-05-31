#!/usr/bin/env python3
"""Build KDP paperback print cover PDF — wraparound [back][spine][front]
with bleed.

Layout (left to right):
   ┌────────────────────────────────────────────────────────────────┐
   │ bleed  │   back cover    │ spine │   front cover   │ bleed     │
   │ 0.125  │      6.0in      │ S in  │      6.0in      │ 0.125     │
   └────────────────────────────────────────────────────────────────┘
                  height = 0.125 + 9.0 + 0.125 = 9.25 in

Spine width (S) = pages × paper_thickness.
  - cream:   0.0025 in/page
  - white:   0.002252 in/page
  - premium: 0.002347 in/page

Renders at 300 DPI, embeds cover JPGs at 6×9in trim location, extends edge
color into the bleed via column-by-column edge sampling so the gradient
continues naturally past the trim line. Spine rendered as a solid color
sampled from the cover join, with rotated title + author text.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
PRINT_DIR = ROOT / "pipelines" / "print"
FONT_DIR = PRINT_DIR / "fonts"

DPI = 300
PAPER_THICKNESS = {
    "cream":   0.0025,
    "white":   0.002252,
    "premium": 0.002347,
}


def in_to_px(inches):
    return int(round(inches * DPI))


def edge_extend_left(src, bleed_w_px):
    col = src.crop((0, 0, 1, src.height))
    return col.resize((bleed_w_px, src.height), Image.NEAREST)


def edge_extend_right(src, bleed_w_px):
    col = src.crop((src.width - 1, 0, src.width, src.height))
    return col.resize((bleed_w_px, src.height), Image.NEAREST)


def edge_extend_top(src, bleed_h_px):
    row = src.crop((0, 0, src.width, 1))
    return row.resize((src.width, bleed_h_px), Image.NEAREST)


def edge_extend_bottom(src, bleed_h_px):
    row = src.crop((0, src.height - 1, src.width, src.height))
    return row.resize((src.width, bleed_h_px), Image.NEAREST)


def avg_color(img, region):
    crop = img.crop(region).convert("RGB").resize((1, 1), Image.LANCZOS)
    r, g, b = crop.getpixel((0, 0))
    return (r, g, b)


def load_font(weight, size_pt, italic=False):
    """Load EB Garamond at the requested weight + size."""
    style = "italic" if italic else "normal"
    name = f"EBGaramond-{weight}-{style}-latin.woff2"
    path = FONT_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"font missing: {path}")
    size_px = int(round(size_pt * DPI / 72))
    return ImageFont.truetype(str(path), size_px)


def build_spine(width_px, height_px, spine_color, title, author):
    """Build the spine image with rotated title + author text.

    KDP convention: spine reads top-to-bottom when the book lies flat (text
    rotated 90° clockwise so when you tilt your head right, the title reads
    left to right)."""
    spine = Image.new("RGB", (width_px, height_px), spine_color)
    draw = ImageDraw.Draw(spine)

    txt_w = height_px       # along spine length
    txt_h = width_px        # across spine thickness
    txt = Image.new("RGBA", (txt_w, txt_h), (0, 0, 0, 0))
    txt_draw = ImageDraw.Draw(txt)

    safe_margin_px = in_to_px(0.0625)
    usable_h = max(8, txt_h - 2 * safe_margin_px)

    title_size_pt = int(round(usable_h / DPI * 72 * 0.62))
    title_size_pt = max(10, min(title_size_pt, 48))
    title_font = load_font(500, title_size_pt)

    author_size_pt = int(round(title_size_pt * 0.58))
    author_size_pt = max(8, author_size_pt)
    author_font = load_font(400, author_size_pt)

    bbox = txt_draw.textbbox((0, 0), title, font=title_font)
    title_w = bbox[2] - bbox[0]
    title_h = bbox[3] - bbox[1]
    title_x = (txt_w - title_w) // 2
    title_y = (txt_h - title_h) // 2 - bbox[1]
    txt_draw.text((title_x, title_y), title, fill=(0, 0, 0), font=title_font)

    bbox = txt_draw.textbbox((0, 0), author, font=author_font)
    author_w = bbox[2] - bbox[0]
    author_h = bbox[3] - bbox[1]
    foot_margin_px = in_to_px(0.5)
    author_x = txt_w - author_w - foot_margin_px
    author_y = (txt_h - author_h) // 2 - bbox[1]
    txt_draw.text((author_x, author_y), author, fill=(0, 0, 0), font=author_font)

    rotated = txt.rotate(-90, expand=True)
    spine.paste(rotated, (0, 0), rotated)
    return spine


def compose_cover(front, back, trim_w_in, trim_h_in,
                  spine_in, bleed_in, title, author,
                  baked_tb_bleed=False):
    """Compose the wraparound cover.

    `baked_tb_bleed=True` means the front/back images already include the
    top + bottom bleed in their own height (image height = trim_h + 2*bleed).
    In that case we don't resize them and we don't add T/B bleed extension —
    only the L/R outer-edge bleed is extended.

    `baked_tb_bleed=False` (legacy) means the input is at trim size and we
    add bleed on all 4 sides via edge extension."""
    trim_w_px = in_to_px(trim_w_in)
    trim_h_px = in_to_px(trim_h_in)
    bleed_px = in_to_px(bleed_in)
    spine_px = in_to_px(spine_in)

    if baked_tb_bleed:
        # Inputs are at trim_w × (trim_h + 2*bleed). Place at native size.
        expected_h = trim_h_px + 2 * bleed_px
        if abs(front.height - expected_h) > 4 or abs(back.height - expected_h) > 4:
            print(f"  ⚠ baked_tb_bleed expected height ~{expected_h}px, got front={front.height}, back={back.height}")
        if abs(front.width - trim_w_px) > 4 or abs(back.width - trim_w_px) > 4:
            print(f"  ⚠ baked_tb_bleed expected width ~{trim_w_px}px, got front={front.width}, back={back.width}")
        front_r = front
        back_r = back
        canvas_h = front_r.height
    else:
        front_r = front.resize((trim_w_px, trim_h_px), Image.LANCZOS)
        back_r = back.resize((trim_w_px, trim_h_px), Image.LANCZOS)
        canvas_h = bleed_px + trim_h_px + bleed_px

    canvas_w = bleed_px + back_r.width + spine_px + front_r.width + bleed_px

    # Spine color sampled from inner edges meeting the spine
    back_right = avg_color(back_r, (back_r.width - 4, 0, back_r.width, back_r.height))
    front_left = avg_color(front_r, (0, 0, 4, front_r.height))
    spine_color = (
        (back_right[0] + front_left[0]) // 2,
        (back_right[1] + front_left[1]) // 2,
        (back_right[2] + front_left[2]) // 2,
    )

    base_color = avg_color(back_r, (0, 0, back_r.width, 4))
    canvas = Image.new("RGB", (canvas_w, canvas_h), base_color)

    if baked_tb_bleed:
        # Place at y=0 (image already includes T/B bleed)
        back_x = bleed_px
        back_y = 0
        canvas.paste(edge_extend_left(back_r, bleed_px), (0, back_y))
        canvas.paste(back_r, (back_x, back_y))
        spine_x = back_x + back_r.width
        spine = build_spine(spine_px, canvas_h, spine_color, title, author)
        canvas.paste(spine, (spine_x, 0))
        front_x = spine_x + spine_px
        front_y = 0
        canvas.paste(edge_extend_right(front_r, bleed_px), (front_x + front_r.width, front_y))
        canvas.paste(front_r, (front_x, front_y))
    else:
        back_x = bleed_px
        back_y = bleed_px
        canvas.paste(edge_extend_top(back_r, bleed_px), (back_x, 0))
        canvas.paste(edge_extend_bottom(back_r, bleed_px), (back_x, back_y + trim_h_px))
        canvas.paste(edge_extend_left(back_r, bleed_px), (0, back_y))
        top_left_color = back_r.getpixel((0, 0))
        bot_left_color = back_r.getpixel((0, back_r.height - 1))
        canvas.paste(Image.new("RGB", (bleed_px, bleed_px), top_left_color), (0, 0))
        canvas.paste(Image.new("RGB", (bleed_px, bleed_px), bot_left_color), (0, back_y + trim_h_px))
        canvas.paste(back_r, (back_x, back_y))
        spine_x = back_x + trim_w_px
        spine = build_spine(spine_px, trim_h_px + 2 * bleed_px, spine_color, title, author)
        canvas.paste(spine, (spine_x, 0))
        front_x = spine_x + spine_px
        front_y = bleed_px
        canvas.paste(edge_extend_top(front_r, bleed_px), (front_x, 0))
        canvas.paste(edge_extend_bottom(front_r, bleed_px), (front_x, front_y + trim_h_px))
        canvas.paste(edge_extend_right(front_r, bleed_px), (front_x + trim_w_px, front_y))
        top_right_color = front_r.getpixel((front_r.width - 1, 0))
        bot_right_color = front_r.getpixel((front_r.width - 1, front_r.height - 1))
        canvas.paste(Image.new("RGB", (bleed_px, bleed_px), top_right_color), (front_x + trim_w_px, 0))
        canvas.paste(Image.new("RGB", (bleed_px, bleed_px), bot_right_color), (front_x + trim_w_px, front_y + trim_h_px))
        canvas.paste(front_r, (front_x, front_y))

    return canvas


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--pages", type=int, default=451)
    p.add_argument("--trim", default="6x9", help="WxH in inches (default 6x9)")
    p.add_argument("--paper", default="cream", choices=list(PAPER_THICKNESS))
    p.add_argument("--bleed", type=float, default=0.125)
    p.add_argument("--wraparound", default=str(ROOT / "book" / "design" / "print-covers" / "wraparound-dossier-print.jpg"),
                   help="Single wraparound cover image (back+spine+front already composited at the design's correct print-edition proportions). Default: WraparoundPrint export from design-studio (BackFindings + Wraparound spine + FrontDefendant, 1308×925 logical at 442-pp spine proportion). If --full-wraparound is set, the image is used as-is and only L/R bleed is edge-extended; otherwise it is split using --back-frac/--front-frac and our build_spine() draws the spine.")
    p.add_argument("--full-wraparound", action="store_true", default=True,
                   help="Use the wraparound image as-is (back+spine+front composited at design time); only edge-extend L/R bleed. Default true (the WraparoundPrint design already includes the correct spine).")
    p.add_argument("--no-full-wraparound", dest="full_wraparound", action="store_false",
                   help="Legacy: split the wraparound into back+front and let build_spine() draw the spine.")
    p.add_argument("--back-frac", type=float, default=575.0 / 1200.0,
                   help="(Only with --no-full-wraparound) Fraction of wraparound width that is back-cover.")
    p.add_argument("--front-frac", type=float, default=575.0 / 1200.0,
                   help="(Only with --no-full-wraparound) Fraction of wraparound width that is front-cover.")
    p.add_argument("--in-front", default=None,
                   help="Front cover image (only used if --wraparound is not provided).")
    p.add_argument("--in-back", default=None,
                   help="Back cover image (only used if --wraparound is not provided).")
    p.add_argument("--out", default=str(ROOT / "dist" / "no-one-did-it-cover.pdf"))
    p.add_argument("--baked-tb-bleed", action="store_true", default=True,
                   help="Set when front/back images already include top+bottom bleed in their height (default true; pass --no-baked-tb-bleed for legacy 6×9 trim-only inputs).")
    p.add_argument("--no-baked-tb-bleed", dest="baked_tb_bleed", action="store_false")
    p.add_argument("--title", default="No One Did It")
    p.add_argument("--author", default="Li Xiaolai")
    args = p.parse_args()

    trim_w, trim_h = (float(x) for x in args.trim.lower().split("x"))
    spine_in = args.pages * PAPER_THICKNESS[args.paper]
    total_w = 2 * args.bleed + 2 * trim_w + spine_in
    total_h = 2 * args.bleed + trim_h

    print(f"KDP paperback cover:")
    print(f"  Trim:   {trim_w}″ × {trim_h}″")
    print(f"  Pages:  {args.pages} ({args.paper}, {PAPER_THICKNESS[args.paper]}″/page)")
    print(f"  Spine:  {spine_in:.4f}″")
    print(f"  Bleed:  {args.bleed}″ each outer edge")
    print(f"  Total:  {total_w:.4f}″ × {total_h:.4f}″ ({in_to_px(total_w)} × {in_to_px(total_h)} px @ {DPI} dpi)")

    if args.wraparound and Path(args.wraparound).exists() and args.full_wraparound and not (args.in_front or args.in_back):
        # Full-wraparound mode: the image already contains back + spine + front
        # at the design-time print-edition proportions (back 600 + spine 108 +
        # front 600 = 1308 logical px at 442-pp spine ratio). Use the image
        # as-is for the printable area; add L/R outer-edge bleed via Pillow
        # edge extension to reach the exact KDP canvas width.
        wrap = Image.open(args.wraparound).convert("RGB")
        bleed_px = in_to_px(args.bleed)
        target_w_px = in_to_px(2 * trim_w + spine_in)        # printable width = back + spine + front
        target_canvas_w = in_to_px(2 * args.bleed + 2 * trim_w + spine_in)
        target_h_px = in_to_px(trim_h + 2 * args.bleed)
        # Resize wraparound to printable area dimensions
        wrap_r = wrap.resize((target_w_px, target_h_px), Image.LANCZOS)
        canvas = Image.new("RGB", (target_canvas_w, target_h_px), (255, 255, 255))
        # Place wrap at bleed offset, edge-extend on L/R
        canvas.paste(edge_extend_left(wrap_r, bleed_px), (0, 0))
        canvas.paste(wrap_r, (bleed_px, 0))
        canvas.paste(edge_extend_right(wrap_r, bleed_px), (bleed_px + wrap_r.width, 0))
        print(f"  Wrap:   {wrap.size} from {args.wraparound}")
        print(f"  Resized to {wrap_r.size} (back+spine+front at trim) and edge-extended {bleed_px}px L/R for bleed")
        print(f"  Canvas: {canvas.size}")
        print(f"  Mode:   full-wraparound (design carries back+spine+front; L/R bleed extended)")
        # Save and return early — skip compose_cover (no rebuild of back/spine/front)
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(out_path, "PDF", resolution=DPI)
        size_mb = out_path.stat().st_size / 1024 / 1024
        print(f"\n  ✓ Cover PDF: {out_path}  ({size_mb:.2f} MB)")
        write_timestamped_snapshot(out_path)
        print(f"\nUpload to KDP:")
        print(f"  Trim size:    {trim_w}″ × {trim_h}″")
        print(f"  Page count:   {args.pages}")
        print(f"  Paper:        {args.paper}")
        print(f"  Cover file:   {out_path}")
        return 0
    elif args.wraparound and Path(args.wraparound).exists() and not (args.in_front or args.in_back):
        # Split-and-recompose mode: extract back + front halves and let
        # build_spine() draw a print-correct spine. Useful when the wraparound
        # design's spine width doesn't match the actual page count.
        wrap = Image.open(args.wraparound).convert("RGB")
        wrap_w = wrap.width
        back_end = int(round(wrap_w * args.back_frac))
        front_start = wrap_w - int(round(wrap_w * args.front_frac))
        back = wrap.crop((0, 0, back_end, wrap.height))
        front = wrap.crop((front_start, 0, wrap_w, wrap.height))
        print(f"  Wrap:   {wrap.size} from {args.wraparound}")
        print(f"  Back:   {back.size} (left 0..{back_end} of wraparound)")
        print(f"  Front:  {front.size} (right {front_start}..{wrap_w} of wraparound)")
        # Resize each half to print trim width × the wraparound's height.
        # Wraparound height is taken as trim_h + 2*bleed (baked-tb-bleed mode).
        target_w_px = in_to_px(trim_w)
        target_h_px = in_to_px(trim_h + 2 * args.bleed)
        back = back.resize((target_w_px, target_h_px), Image.LANCZOS)
        front = front.resize((target_w_px, target_h_px), Image.LANCZOS)
        print(f"  Resized to {back.size} each ({trim_w}″ × {trim_h + 2*args.bleed}″ at 300 DPI)")
    else:
        in_front = args.in_front or str(ROOT / "book" / "design" / "print-covers" / "cover-front-print.jpg")
        in_back = args.in_back or str(ROOT / "book" / "design" / "print-covers" / "cover-back-print.jpg")
        front = Image.open(in_front).convert("RGB")
        back = Image.open(in_back).convert("RGB")
        print(f"  Front:  {front.size} from {in_front}")
        print(f"  Back:   {back.size} from {in_back}")

    canvas = compose_cover(front, back, trim_w, trim_h, spine_in, args.bleed,
                           args.title, args.author,
                           baked_tb_bleed=args.baked_tb_bleed)
    print(f"  Canvas: {canvas.size}")
    print(f"  Mode:   {'top+bottom bleed baked into image (L/R extended)' if args.baked_tb_bleed else 'all-side edge-extend bleed (legacy)'}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    canvas.save(out_path, "PDF", resolution=DPI)
    size_mb = out_path.stat().st_size / 1024 / 1024
    print(f"\n  ✓ Cover PDF: {out_path}  ({size_mb:.2f} MB)")

    write_timestamped_snapshot(out_path)

    print(f"\nUpload to KDP:")
    print(f"  Trim size:    {trim_w}″ × {trim_h}″")
    print(f"  Page count:   {args.pages}")
    print(f"  Paper:        {args.paper}")
    print(f"  Cover file:   {out_path}")
    return 0


def write_timestamped_snapshot(canonical):
    import datetime
    import json
    import shutil

    i18n_path = PRINT_DIR / "i18n" / "en.json"
    try:
        version = json.loads(i18n_path.read_text()).get("version")
    except Exception:
        version = None

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    version_tag = f"-v{version}" if version else ""
    snapshot = canonical.with_name(f"{canonical.stem}{version_tag}-{stamp}{canonical.suffix}")
    shutil.copyfile(canonical, snapshot)
    print(f"  Snapshot   → {snapshot.name}")
    return snapshot


if __name__ == "__main__":
    sys.exit(main())
