#!/usr/bin/env python3
"""
Courtney Banners V3 — Luxury / Apple-tier Editorial Redesign
6 banners × 4 Meta/IG sizes = 24 PNGs.

Same copy, same person, same brand. New everything else.

Art direction:
- FULL-BLEED cinematic photo (no split canvas, no vertical seams).
- Text sits low over a deep espresso vignette gradient on the photo.
- Fraunces (luxury display serif) + Inter (micro typography).
- No pills, no divider lines, no dashes, no dot separators, no chunky candy CTA.
- Refined outlined CTA button (thin border, minimal fill, restaurant-menu elegance).
- LLA lockup: quiet, ivory, top-center or top-left, whisper-soft.
- Trustpilot: minimal — 5 green stars, 4.6, tiny Trustpilot wordmark.
- Color: warm oak, deep espresso, ivory, single soft gold accent.
"""

import json, os, html

OUT = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(OUT, 'banners')
os.makedirs(BAN, exist_ok=True)

SIZES = [
    ('1x1',   1080, 1080, '1:1 Feed',       'Instagram Post / FB Feed Square'),
    ('4x5',   1080, 1350, '4:5 Vertical',   'Instagram / FB Feed Vertical'),
    ('9x16',  1080, 1920, '9:16 Story',     'IG Stories, Reels, FB Stories'),
    ('191x1', 1200,  628, '1.91:1 Link',    'FB Link Ad / Marketplace'),
]

LUX_V1 = 'assets/composites/courtney_lux_v1.png'  # 3:4 portrait cover
LUX_V2 = 'assets/composites/courtney_lux_v2.png'  # 16:9 landscape negative-space left
LUX_V3 = 'assets/composites/courtney_lux_v3.png'  # 9:16 vertical

# Photo choice by aspect
def pick_photo(size_key, banner_idx):
    if size_key == '191x1':
        return LUX_V2
    if size_key == '9x16':
        return LUX_V3
    if size_key == '4x5':
        # portrait leaning
        return LUX_V1 if banner_idx % 2 == 0 else LUX_V3
    # 1x1 square
    return LUX_V1 if banner_idx % 2 == 0 else LUX_V3

# Object-position tuned per composite
def obj_pos(photo, size_key):
    if photo == LUX_V2:  # landscape, subject right
        return {
            '191x1': 'center 40%',
            '1x1':   '68% 35%',
            '4x5':   '68% 30%',
            '9x16':  '68% 30%',
        }[size_key]
    if photo == LUX_V3:  # vertical, subject center
        return 'center 25%' if size_key != '191x1' else 'center 15%'
    # LUX_V1 portrait cover
    return {
        '1x1':   'center 22%',
        '4x5':   'center 20%',
        '9x16':  'center 18%',
        '191x1': 'center 25%',
    }[size_key]

BANNERS = [
    {'id': 'c_b1', 'title': 'Live Longer. Learn How.',
     'l1': 'Live Longer.', 'l2': 'Learn How.'},
    {'id': 'c_b2', 'title': 'Your Longevity Protocol. Made Personal.',
     'l1': 'Your Longevity Protocol.', 'l2': 'Made Personal.'},
    {'id': 'c_b3', 'title': 'Decode Your Biomarkers. Extend Your Life.',
     'l1': 'Decode Your Biomarkers.', 'l2': 'Extend Your Life.'},
    {'id': 'c_b4', 'title': 'The Longevity Course, Taught Live.',
     'l1': 'The Longevity Course,', 'l2': 'Taught Live.'},
    {'id': 'c_b5', 'title': 'Age Slower. Starts in Class.',
     'l1': 'Age Slower.', 'l2': 'Starts in Class.'},
    {'id': 'c_b6', 'title': 'Enroll. Live Longer. Live Stronger.',
     'l1': 'Enroll. Live Longer.', 'l2': 'Live Stronger.'},
]


def render_banner(b, size_key, w, h, banner_idx):
    is_landscape = w / h > 1.4
    is_portrait  = h / w > 1.4
    is_vertical  = 1.15 < h / w <= 1.4
    is_square    = not (is_landscape or is_portrait or is_vertical)

    photo = pick_photo(size_key, banner_idx)
    op = obj_pos(photo, size_key)

    # Base scale
    s = min(w, h) / 1000.0
    if is_landscape:
        s = h / 620.0

    # LLA lockup on top — quiet & refined
    logo_h = int(56 * s) if is_landscape else int(74 * s)
    top_pad = int(44 * s) if not is_landscape else int(30 * s)
    side_pad = int(60 * s) if not is_landscape else int(46 * s)

    # Headline sizes — big editorial
    if is_landscape:
        h1_size = int(74 * s)
    elif is_portrait:
        h1_size = int(112 * s)
    elif is_vertical:
        h1_size = int(96 * s)
    else:  # 1:1
        h1_size = int(96 * s)

    # Micro typography above headline (eyebrow) — refined, tiny, warm ivory
    eyebrow_size = max(11, int(h1_size * 0.14))

    # Credential (below headline) — one line, refined italic
    cred_size = max(14, int(h1_size * 0.24))

    # CTA — outlined refined pill, small
    cta_size = max(15, int(h1_size * 0.22))
    cta_pad_v = max(12, int(cta_size * 0.8))
    cta_pad_h = max(24, int(cta_size * 1.9))

    # Trustpilot — tiny, refined
    tp_star_h = max(18, int(cta_size * 1.05))
    tp_text = max(12, int(cta_size * 0.72))

    # Layout: everything anchored bottom-left over vignette
    if is_landscape:
        text_bottom = int(52 * s)
        text_left = side_pad
        text_width = int(w * 0.55)
    elif is_portrait:
        text_bottom = int(76 * s)
        text_left = side_pad
        text_width = w - side_pad * 2
    elif is_vertical:
        text_bottom = int(64 * s)
        text_left = side_pad
        text_width = w - side_pad * 2
    else:  # 1:1
        text_bottom = int(56 * s)
        text_left = side_pad
        text_width = w - side_pad * 2

    # Vignette gradient (deep espresso to transparent, from bottom)
    # Placed as an overlay above photo, below text
    if is_landscape:
        vignette = f"background:linear-gradient(90deg, rgba(20,10,4,.92) 0%, rgba(20,10,4,.75) 32%, rgba(20,10,4,.15) 58%, rgba(20,10,4,0) 78%);"
    else:
        vignette = f"background:linear-gradient(180deg, rgba(20,10,4,0) 0%, rgba(20,10,4,0) 32%, rgba(20,10,4,.35) 52%, rgba(20,10,4,.82) 72%, rgba(15,8,3,.96) 100%);"

    l1 = html.escape(b['l1'])
    l2 = html.escape(b['l2'])

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300;9..144,400;9..144,500;9..144,600;9..144,700;9..144,800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  html,body{{margin:0;padding:0;background:#0a0503;overflow:hidden;font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
  .canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:#0a0503;}}
  .photo{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{op};z-index:1;}}
  .vignette{{position:absolute;inset:0;z-index:2;{vignette}}}
  .grain{{position:absolute;inset:0;z-index:3;pointer-events:none;opacity:.055;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/></svg>");}}
  .brand{{position:absolute;left:{side_pad}px;top:{top_pad}px;z-index:10;display:flex;align-items:center;}}
  .brand img{{height:{logo_h}px;display:block;filter:brightness(1.35) drop-shadow(0 2px 12px rgba(0,0,0,.55));}}
  .text{{position:absolute;left:{text_left}px;bottom:{text_bottom}px;width:{text_width}px;z-index:11;color:#f7ede0;}}
  .eyebrow{{font-family:'Inter',sans-serif;font-weight:500;font-size:{eyebrow_size}px;letter-spacing:.28em;text-transform:uppercase;color:rgba(247,237,224,.72);margin-bottom:{max(14,int(h1_size*0.18))}px;}}
  .h1{{font-family:'Fraunces',serif;font-variation-settings:'opsz' 144, 'SOFT' 30;font-weight:400;font-size:{h1_size}px;line-height:.98;letter-spacing:-.02em;margin:0;color:#fbf3e6;text-shadow:0 4px 24px rgba(0,0,0,.55);}}
  .h1 .a{{font-weight:400;font-style:normal;color:#fbf3e6;}}
  .h1 .b{{font-weight:500;font-style:italic;color:#e4b881;display:block;margin-top:{max(2,int(h1_size*0.03))}px;}}
  .cred{{margin-top:{max(20,int(h1_size*0.28))}px;font-family:'Fraunces',serif;font-variation-settings:'opsz' 14;font-style:italic;font-weight:400;font-size:{cred_size}px;color:rgba(247,237,224,.78);line-height:1.35;letter-spacing:.005em;}}
  .cred .name{{font-style:normal;font-weight:600;color:#f7ede0;}}
  .actions{{margin-top:{max(30,int(h1_size*0.42))}px;display:flex;flex-direction:column;align-items:flex-start;gap:{max(16,int(cta_size*0.85))}px;}}
  .cta{{display:inline-flex;align-items:center;gap:{max(8,int(cta_size*0.5))}px;background:rgba(247,237,224,.06);color:#f7ede0;font-family:'Inter',sans-serif;font-weight:500;font-size:{cta_size}px;padding:{cta_pad_v}px {cta_pad_h}px;border-radius:9999px;border:1px solid rgba(247,237,224,.55);letter-spacing:.14em;text-transform:uppercase;backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);}}
  .cta .arr{{font-family:'Inter',sans-serif;font-weight:300;margin-left:{max(3,int(cta_size*0.15))}px;transform:translateY(-1px);}}
  .tp{{display:flex;align-items:center;gap:{max(10,int(tp_star_h*0.5))}px;color:rgba(247,237,224,.75);}}
  .tp img.stars{{height:{tp_star_h}px;filter:brightness(1.05);}}
  .tp .score{{font-family:'Inter',sans-serif;font-weight:600;font-size:{tp_text}px;letter-spacing:.02em;color:rgba(247,237,224,.88);}}
  .tp .word{{font-family:'Inter',sans-serif;font-weight:400;font-size:{max(10,int(tp_text*0.88))}px;letter-spacing:.04em;color:rgba(247,237,224,.55);}}
</style></head><body>
<div class="canvas">
  <img class="photo" src="../{photo}" alt="">
  <div class="vignette"></div>
  <div class="grain"></div>

  <div class="brand">
    <img src="../assets/lla_logo.png" alt="Longevity Life Academy">
  </div>

  <div class="text">
    <div class="eyebrow">Longevity Life Academy</div>
    <h1 class="h1"><span class="a">{l1}</span><span class="b">{l2}</span></h1>
    <div class="cred">With <span class="name">Courtney</span>, Longevity Life Academy Instructor</div>
    <div class="actions">
      <a class="cta">Enroll Now <span class="arr">→</span></a>
      <div class="tp">
        <img class="stars" src="../assets/tp_stars-5.svg">
        <span class="score">4.6</span>
        <span class="word">Trustpilot &nbsp;&nbsp;600+ verified reviews</span>
      </div>
    </div>
  </div>
</div>
</body></html>"""


def main():
    manifest = {'courtney': []}
    for idx, b in enumerate(BANNERS):
        entry = {'id': b['id'], 'title': b['title'], 'sizes': {}}
        for key, w, h, label, note in SIZES:
            html_out = render_banner(b, key, w, h, idx)
            fn = f"{b['id']}_{key}.html"
            with open(os.path.join(BAN, fn), 'w') as f:
                f.write(html_out)
            entry['sizes'][key] = {
                'html': fn, 'png': fn.replace('.html', '.png'),
                'w': w, 'h': h, 'label': label, 'note': note
            }
        manifest['courtney'].append(entry)
    with open(os.path.join(OUT, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {len(BANNERS) * len(SIZES)} HTML files.")


if __name__ == '__main__':
    main()
