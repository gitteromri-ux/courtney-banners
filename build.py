#!/usr/bin/env python3
"""
Courtney Banners V3.1 — Luxury Editorial, professionally audited.

Fixes from design audit:
- NO text over face, ever: 1x1 / 4x5 / 191x1 use the landscape plate with
  Courtney offset right, copy in a clean left column. 9x16 keeps face high,
  copy low over deep vignette.
- Tiny-caps eyebrow REMOVED (banned pattern + redundant with logo).
- CTA sentence case "Enroll Now" (no spaced uppercase), larger.
- Ivory logo lockup (navy original was illegible on espresso).
- Stronger scrim behind every text zone. Great contrast everywhere.
"""

import json, os, html

OUT = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(OUT, 'banners')
os.makedirs(BAN, exist_ok=True)

SIZES = [
    ('1x1',   1080, 1080, '1:1 Feed',     'Instagram Post / FB Feed Square'),
    ('4x5',   1080, 1350, '4:5 Vertical', 'Instagram / FB Feed Vertical'),
    ('9x16',  1080, 1920, '9:16 Story',   'IG Stories, Reels, FB Stories'),
    ('191x1', 1200,  628, '1.91:1 Link',  'FB Link Ad / Marketplace'),
]

LUX_V1 = 'assets/composites/courtney_lux_v1.png'  # 3:4 portrait, turtleneck
LUX_V2 = 'assets/composites/courtney_lux_v2.png'  # 16:9 subject right
LUX_V3 = 'assets/composites/courtney_lux_v3.png'  # 9:16 vertical

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


def render_banner(b, size_key, w, h, idx):
    # Layout mode:
    #  'side'   — subject right (landscape plate), copy left column  (1x1, 4x5, 191x1)
    #  'bottom' — subject high (vertical plate), copy low            (9x16)
    mode = 'bottom' if size_key == '9x16' else 'side'

    if mode == 'side':
        photo = LUX_V2
        # push subject right in frame; window math tuned per aspect
        op = {'1x1': '58% 32%', '4x5': '58% 25%', '191x1': '72% 38%'}[size_key]
    else:
        photo = LUX_V3 if idx % 2 == 0 else LUX_V1
        op = 'center 20%' if photo == LUX_V3 else 'center 24%'

    s = min(w, h) / 1000.0
    if w / h > 1.4:
        s = h / 640.0

    logo_h = int(64 * s) if size_key != '191x1' else int(56 * s)
    side_pad = int(64 * s) if size_key != '191x1' else int(50 * s)
    top_pad = int(46 * s) if size_key != '191x1' else int(34 * s)

    if size_key == '191x1':
        h1_size = int(72 * s)
        text_width = int(w * 0.56)
    elif size_key == '1x1':
        h1_size = int(88 * s)
        text_width = int(w * 0.66)
    elif size_key == '4x5':
        h1_size = int(92 * s)
        text_width = int(w * 0.70)
    else:  # 9x16
        h1_size = int(96 * s)
        text_width = w - side_pad * 2

    cred_size = max(15, int(h1_size * 0.24))
    cta_size = max(17, int(h1_size * 0.26))
    cta_pad_v = max(14, int(cta_size * 0.72))
    cta_pad_h = max(28, int(cta_size * 1.7))
    tp_star_h = max(20, int(cta_size * 1.0))
    tp_text = max(13, int(cta_size * 0.72))

    text_bottom = {'1x1': int(64 * s), '4x5': int(80 * s),
                   '9x16': int(72 * s), '191x1': int(48 * s)}[size_key]

    if mode == 'side':
        vignette = ("background:"
                    "linear-gradient(97deg, rgba(12,6,2,.96) 0%, rgba(14,7,3,.85) 26%, "
                    "rgba(16,8,3,.45) 48%, rgba(16,8,3,0) 66%),"
                    "linear-gradient(180deg, rgba(12,6,2,0) 55%, rgba(12,6,2,.55) 100%);")
    else:
        vignette = ("background:linear-gradient(180deg, rgba(20,10,4,0) 0%, rgba(20,10,4,0) 30%, "
                    "rgba(18,9,4,.42) 50%, rgba(14,7,3,.88) 70%, rgba(10,5,2,.97) 100%);")

    l1 = html.escape(b['l1'])
    l2 = html.escape(b['l2'])

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  html,body{{margin:0;padding:0;background:#0a0503;overflow:hidden;font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
  .canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:#0a0503;}}
  .photo{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{op};z-index:1;}}
  .vignette{{position:absolute;inset:0;z-index:2;{vignette}}}
  .grain{{position:absolute;inset:0;z-index:3;pointer-events:none;opacity:.05;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/></svg>");}}
  .brand{{position:absolute;left:{side_pad}px;top:{top_pad}px;z-index:10;}}
  .brand img{{height:{logo_h}px;display:block;opacity:.96;filter:drop-shadow(0 2px 10px rgba(0,0,0,.4));}}
  .text{{position:absolute;left:{side_pad}px;bottom:{text_bottom}px;width:{text_width}px;z-index:11;color:#f7ede0;}}
  .h1{{font-family:'Fraunces',serif;font-variation-settings:'opsz' 144;font-weight:500;font-size:{h1_size}px;line-height:1.02;letter-spacing:-.018em;margin:0;color:#fbf3e6;text-shadow:0 4px 28px rgba(0,0,0,.6);}}
  .h1 .b{{font-style:italic;font-weight:500;color:#e4b881;display:block;margin-top:{max(2, int(h1_size * 0.04))}px;}}
  .cred{{margin-top:{max(20, int(h1_size * 0.26))}px;font-family:'Fraunces',serif;font-style:italic;font-weight:400;font-size:{cred_size}px;color:rgba(247,237,224,.85);line-height:1.4;}}
  .cred .name{{font-style:normal;font-weight:600;color:#fbf3e6;}}
  .actions{{margin-top:{max(30, int(h1_size * 0.40))}px;display:flex;flex-direction:column;align-items:flex-start;gap:{max(18, int(cta_size * 0.9))}px;}}
  .cta{{display:inline-flex;align-items:baseline;gap:{max(10, int(cta_size * 0.55))}px;background:rgba(247,237,224,.07);color:#fbf3e6;font-family:'Fraunces',serif;font-weight:500;font-size:{cta_size}px;letter-spacing:.015em;padding:{cta_pad_v}px {cta_pad_h}px;border-radius:9999px;border:1.5px solid rgba(247,237,224,.62);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);}}
  .cta .arr{{font-family:'Inter',sans-serif;font-weight:400;}}
  .tp{{display:flex;align-items:center;gap:{max(10, int(tp_star_h * 0.5))}px;}}
  .tp img.stars{{height:{tp_star_h}px;}}
  .tp .score{{font-family:'Inter',sans-serif;font-weight:600;font-size:{tp_text}px;color:rgba(251,243,230,.92);}}
  .tp .word{{font-family:'Inter',sans-serif;font-weight:400;font-size:{max(11, int(tp_text * 0.9))}px;color:rgba(247,237,224,.62);}}
</style></head><body>
<div class="canvas">
  <img class="photo" src="../{photo}" alt="">
  <div class="vignette"></div>
  <div class="grain"></div>

  <div class="brand"><img src="../assets/lla_logo_ivory.png" alt="Longevity Life Academy by eTeacher Group"></div>

  <div class="text">
    <h1 class="h1">{l1}<span class="b">{l2}</span></h1>
    <div class="cred">With <span class="name">Courtney</span>, Longevity Life Academy Instructor</div>
    <div class="actions">
      <a class="cta">Enroll Now <span class="arr">→</span></a>
      <div class="tp">
        <img class="stars" src="../assets/tp_stars-5.svg">
        <span class="score">4.6</span>
        <span class="word">600+ verified reviews on Trustpilot</span>
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
            out = render_banner(b, key, w, h, idx)
            fn = f"{b['id']}_{key}.html"
            with open(os.path.join(BAN, fn), 'w') as f:
                f.write(out)
            entry['sizes'][key] = {'html': fn, 'png': fn.replace('.html', '.png'),
                                   'w': w, 'h': h, 'label': label, 'note': note}
        manifest['courtney'].append(entry)
    with open(os.path.join(OUT, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {len(BANNERS) * len(SIZES)} HTML files.")


if __name__ == '__main__':
    main()
