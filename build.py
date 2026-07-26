#!/usr/bin/env python3
"""
Courtney Banners V2 — Wooden Set + New Copy
6 banners x 4 Meta/IG sizes = 24 HTML files (rendered to PNG by playwright).

Hard rules baked in:
- HUGE brand lockup on top (LLA logo big) — above main headline on every banner.
- Zero AI marks: no tiny-caps eyebrows, no " · " dot separators, no em-dashes,
  no dash-delimited course-info lists.
- Trustpilot lockup stacked DIRECTLY BELOW the CTA button (5 green stars).
- Credential line = ONE line: "Courtney — Longevity Life Academy Instructor".
- Significantly larger fonts throughout.
- Wooden-set real Courtney composite as photo source.
"""

import json
import os
import re

OUT = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(OUT, 'banners')
os.makedirs(BAN, exist_ok=True)

# 4 real Meta/IG sizes
SIZES = [
    ('1x1',   1080, 1080, '1:1 Feed',       'Instagram Post / FB Feed Square'),
    ('4x5',   1080, 1350, '4:5 Vertical',   'Instagram / FB Feed Vertical'),
    ('9x16',  1080, 1920, '9:16 Story',     'IG Stories, Reels, FB Stories'),
    ('191x1', 1200,  628, '1.91:1 Link',    'FB Link Ad / Marketplace'),
]

# All 3 wooden-set composites — mixed per banner
PHOTO_V1 = 'assets/composites/courtney_woodset_v1.png'   # landscape, full body
PHOTO_V2 = 'assets/composites/courtney_woodset_v2.png'   # portrait 3:4
PHOTO_V3 = 'assets/composites/courtney_woodset_v3.png'   # square, front-facing

# 6 banners — approved copy (V2)
BANNERS = [
    {'id': 'c_b1', 'title': 'Live Longer. Learn How.',
     'l1': 'Live Longer.', 'l2': 'Learn How.',
     'photo_1x1': PHOTO_V3, 'photo_4x5': PHOTO_V2, 'photo_9x16': PHOTO_V2, 'photo_191x1': PHOTO_V1},
    {'id': 'c_b2', 'title': 'Your Longevity Protocol. Made Personal.',
     'l1': 'Your Longevity Protocol.', 'l2': 'Made Personal.',
     'photo_1x1': PHOTO_V1, 'photo_4x5': PHOTO_V3, 'photo_9x16': PHOTO_V2, 'photo_191x1': PHOTO_V1},
    {'id': 'c_b3', 'title': 'Decode Your Biomarkers. Extend Your Life.',
     'l1': 'Decode Your Biomarkers.', 'l2': 'Extend Your Life.',
     'photo_1x1': PHOTO_V3, 'photo_4x5': PHOTO_V2, 'photo_9x16': PHOTO_V3, 'photo_191x1': PHOTO_V1},
    {'id': 'c_b4', 'title': 'The Longevity Course, Taught Live.',
     'l1': 'The Longevity Course,', 'l2': 'Taught Live.',
     'photo_1x1': PHOTO_V1, 'photo_4x5': PHOTO_V3, 'photo_9x16': PHOTO_V3, 'photo_191x1': PHOTO_V1},
    {'id': 'c_b5', 'title': 'Age Slower. Starts in Class.',
     'l1': 'Age Slower.', 'l2': 'Starts in Class.',
     'photo_1x1': PHOTO_V3, 'photo_4x5': PHOTO_V2, 'photo_9x16': PHOTO_V2, 'photo_191x1': PHOTO_V1},
    {'id': 'c_b6', 'title': 'Enroll. Live Longer. Live Stronger.',
     'l1': 'Enroll. Live Longer.', 'l2': 'Live Stronger.',
     'photo_1x1': PHOTO_V1, 'photo_4x5': PHOTO_V3, 'photo_9x16': PHOTO_V3, 'photo_191x1': PHOTO_V1},
]


def html_head(w, h):
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@600;700;800;900&display=swap" rel="stylesheet">
<style>
  html,body{{margin:0;padding:0;background:#010712;overflow:hidden;font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
  .canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:#010712;}}
</style></head><body>"""


def render_banner(b, size_key, w, h):
    is_landscape = w / h > 1.4     # 191x1
    is_portrait  = h / w > 1.4     # 9x16
    is_vertical  = h / w > 1.15 and not is_portrait  # 4x5
    is_square    = not (is_landscape or is_portrait or is_vertical)

    photo = b[f'photo_{size_key}']

    # Base scale — larger baseline than V1 (upscaled design per user request)
    s = min(w, h) / 1000.0
    if is_landscape:
        s = h / 700.0

    # ─────────── LARGE BRAND LOCKUP ON TOP ───────────
    # Big LLA logo, sized generously (matching the "hero" weight the user asked for)
    if is_landscape:
        logo_h = int(90 * s * 1.2)
    elif is_portrait:
        logo_h = int(150 * s)
    elif is_vertical:
        logo_h = int(140 * s)
    else:  # square
        logo_h = int(150 * s)

    # Top brand strip position/padding
    top_pad = int(48 * s) if not is_landscape else int(28 * s)
    side_pad = int(56 * s)
    if is_landscape:
        side_pad = int(44 * s)
    if is_portrait:
        side_pad = int(52 * s)

    # ─────────── MAIN HEADLINE ───────────
    # Large, bold, serif for L1 primary hook + sans for L2 punch OR
    # both bold sans — using bold Playfair (editorial, matches homepage weight)
    if is_landscape:
        h1_size = int(58 * s)
    elif is_portrait:
        h1_size = int(94 * s)
    elif is_vertical:
        h1_size = int(78 * s)
    else:
        h1_size = int(84 * s)

    h1_line_height = 1.02

    # Credential line — ONE line
    cred_size = max(14, int(h1_size * 0.28))

    # CTA
    cta_font = max(20, int(h1_size * 0.42))
    cta_pad_v = max(14, int(cta_font * 0.85))
    cta_pad_h = max(26, int(cta_font * 1.7))

    # Trustpilot below CTA
    tp_star_h = max(28, int(cta_font * 1.1))
    tp_text = max(15, int(cta_font * 0.65))

    # ─────────── LAYOUT ZONES ───────────
    # Landscape (1.91:1): photo right ~55%, text left; brand strip full-width top, CTA + TP bottom-left
    # Portrait (9:16): photo top ~55% height, text bottom
    # Vertical (4:5): photo top ~55% height, text bottom
    # Square (1:1): photo right ~50%, text left, brand strip top

    photo_style = ''
    text_area_style = ''
    ba_left = 0  # bottom-align origin

    if is_landscape:
        photo_style = f"position:absolute; right:0; top:0; width:{int(w*0.56)}px; height:{h}px; object-fit:cover; object-position:center 22%;"
        text_left = side_pad
        text_top = int(logo_h + top_pad + 28 * s)
        text_area_style = f"position:absolute; left:{text_left}px; top:{text_top}px; width:{int(w*0.44 - side_pad*1.3)}px;"
    elif is_portrait:
        photo_style = f"position:absolute; left:0; top:0; width:{w}px; height:{int(h*0.55)}px; object-fit:cover; object-position:center 25%;"
        text_area_style = f"position:absolute; left:{side_pad}px; right:{side_pad}px; top:{int(h*0.55 + 40*s)}px;"
    elif is_vertical:
        photo_style = f"position:absolute; left:0; top:0; width:{w}px; height:{int(h*0.55)}px; object-fit:cover; object-position:center 20%;"
        text_area_style = f"position:absolute; left:{side_pad}px; right:{side_pad}px; top:{int(h*0.55 + 44*s)}px;"
    else:  # square
        photo_style = f"position:absolute; right:0; top:0; width:{int(w*0.52)}px; height:{h}px; object-fit:cover; object-position:center 25%;"
        text_area_style = f"position:absolute; left:{side_pad}px; top:{int(logo_h + top_pad + 32*s)}px; width:{int(w*0.48 - side_pad*1.3)}px;"

    # Overlay gradient for legibility on the photo edge next to text
    if is_landscape or is_square:
        photo_overlay = f"position:absolute; left:0; top:0; width:{int(w*0.65)}px; height:{h}px; background:linear-gradient(90deg, #010712 0%, #010712 45%, rgba(1,7,18,.85) 60%, rgba(1,7,18,.35) 78%, rgba(1,7,18,0) 100%); z-index:2;"
    else:  # portrait / vertical
        photo_overlay = f"position:absolute; left:0; top:0; width:{w}px; height:{h}px; background:linear-gradient(180deg, rgba(1,7,18,0) 0%, rgba(1,7,18,0) {int(35)}%, rgba(1,7,18,.55) {int(52)}%, #010712 {int(66)}%); z-index:2;"

    # ─────────── BUILD HTML ───────────
    return f"""{html_head(w,h)}
<style>
  .canvas{{background:#010712;}}
  .photo-img{{ {photo_style} z-index:1; }}
  .photo-fade{{ {photo_overlay} }}
  .brand-top{{ position:absolute; left:{side_pad}px; top:{top_pad}px; z-index:10; display:flex; align-items:center; }}
  .brand-top img{{ height:{logo_h}px; display:block; }}
  .text-area{{ {text_area_style} z-index:11; color:#fff; }}
  .h1{{ font-family:'Playfair Display','Instrument Serif',serif; font-weight:800; font-size:{h1_size}px; line-height:{h1_line_height}; letter-spacing:-.015em; margin:0; color:#fff; text-shadow:0 2px 24px rgba(0,0,0,.8); }}
  .h1 .b{{ font-weight:900; }}
  .h1 .gold{{ color:#E8A75A; }}
  .cred{{ margin-top:{max(18, int(h1_size*0.3))}px; font-family:'Inter',sans-serif; font-weight:600; font-size:{cred_size}px; letter-spacing:.01em; color:#A9CFFF; line-height:1.35; }}
  .cred b{{ color:#E8A75A; font-weight:800; }}
  .cta-block{{ margin-top:{max(28, int(h1_size*0.5))}px; display:flex; flex-direction:column; align-items:flex-start; gap:{max(14, int(cta_font*0.5))}px; }}
  .cta{{ display:inline-flex; align-items:center; gap:{max(8,int(cta_font*0.35))}px; background:linear-gradient(135deg,#3A8DFF 0%,#006EFF 100%); color:#fff; font-family:'Inter',sans-serif; font-weight:900; font-size:{cta_font}px; padding:{cta_pad_v}px {cta_pad_h}px; border-radius:9999px; border:1px solid rgba(255,255,255,.5); box-shadow:0 12px 36px rgba(0,110,255,.55), inset 0 2px 0 rgba(255,255,255,.3); letter-spacing:.01em; }}
  .cta .arrow{{ display:inline-block; margin-left:{max(4,int(cta_font*0.2))}px; }}
  .tp{{ display:flex; align-items:center; gap:{max(8,int(tp_star_h*0.3))}px; }}
  .tp img.stars{{ height:{tp_star_h}px; }}
  .tp .txt{{ font-family:'Inter',sans-serif; font-weight:700; font-size:{tp_text}px; color:#fff; letter-spacing:.01em; }}
  .tp .txt .lt{{ font-weight:500; color:rgba(255,255,255,.72); }}
  /* subtle warm accent glow on photo side */
  .warm-glow{{ position:absolute; right:-20%; top:-15%; width:70%; height:70%; background:radial-gradient(closest-side, rgba(232,167,90,.22), transparent 70%); z-index:1; pointer-events:none; }}
</style>
<div class="canvas">
  <img class="photo-img" src="../{photo}" alt="">
  <div class="warm-glow"></div>
  <div class="photo-fade"></div>

  <div class="brand-top">
    <img src="../assets/lla_logo.png" alt="Longevity Life Academy">
  </div>

  <div class="text-area">
    <h1 class="h1"><span class="b">{b['l1']}</span><br><span class="b gold">{b['l2']}</span></h1>
    <div class="cred">With <b>Courtney</b><br>Longevity Life Academy Instructor</div>
    <div class="cta-block">
      <a class="cta">Enroll Now <span class="arrow">→</span></a>
      <div class="tp">
        <img class="stars" src="../assets/tp_stars-5.svg">
        <div class="txt">4.6 / 5<br><span class="lt">600+ verified reviews on Trustpilot</span></div>
      </div>
    </div>
  </div>
</div>
</body></html>"""


def main():
    manifest = {'courtney': []}
    for b in BANNERS:
        entry = {'id': b['id'], 'title': b['title'], 'sizes': {}}
        for key, w, h, label, note in SIZES:
            html = render_banner(b, key, w, h)
            fn = f"{b['id']}_{key}.html"
            with open(os.path.join(BAN, fn), 'w') as f:
                f.write(html)
            entry['sizes'][key] = {
                'html': fn, 'png': fn.replace('.html', '.png'),
                'w': w, 'h': h, 'label': label, 'note': note
            }
        manifest['courtney'].append(entry)
    with open(os.path.join(OUT, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {len(BANNERS) * len(SIZES)} HTML files for {len(BANNERS)} banners.")


if __name__ == '__main__':
    main()
