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

# V12 — real production set plates (walnut library, leather chair, camera rig)
WIDE_LS = 'assets/composites/courtney_realset_ls.png'  # 16:9 real set, subject right
WIDE_PT = 'assets/composites/courtney_realset_pt.png'  # 9:16 real set, subject center, face high
WIDE_SQ = 'assets/composites/courtney_realset_sq.png'  # 1:1 real set, subject right
WIDE_45 = 'assets/composites/courtney_realset_45.png'  # 3:4 real set, subject right

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

    # Per-aspect wide-set composite so the wooden library fills the frame and Courtney sits small in it.
    fit = 'cover'
    if size_key == '1x1':
        photo = WIDE_SQ
        op = 'center center'
    elif size_key == '4x5':
        photo = WIDE_45
        # push subject right so the left third stays open for copy
        op = '72% center'
    elif size_key == '191x1':
        photo = WIDE_LS
        op = 'center 45%'
    else:  # 9x16
        photo = WIDE_PT
        op = 'center 30%'

    s = min(w, h) / 1000.0
    if w / h > 1.4:
        s = h / 640.0

    logo_h = {'1x1': int(140 * s), '4x5': int(150 * s),
              '9x16': int(170 * s), '191x1': int(90 * s)}[size_key]

    # Per-size photo box: shift subject up on 9x16 (clears face for larger copy),
    # nudge subject right on 1x1 (clears italic headline tail).
    if size_key == '9x16':
        photo_box = 'top:-14%;left:0;width:100%;height:114%;'
    elif size_key == '1x1':
        photo_box = 'top:0;left:0;width:110%;height:100%;'
    else:
        photo_box = 'inset:0;width:100%;height:100%;'

    # 191x1 is too short (628px) for eyebrow + enlarged copy: drop eyebrow there.
    eyebrow_html = '' if size_key == '191x1' else '<div class="eyebrow">Live Online Longevity Course</div>'
    eyebrow_size = {'1x1': int(26 * s), '4x5': int(28 * s),
                    '9x16': int(32 * s), '191x1': int(20 * s)}[size_key]
    side_pad = int(64 * s) if size_key != '191x1' else int(50 * s)
    # 9x16: keep brand block below IG Stories top UI (~14% of 1920 = 269px)
    top_pad = {'1x1': int(52 * s), '4x5': int(52 * s),
               '9x16': int(150 * s), '191x1': int(36 * s)}[size_key]

    if size_key == '191x1':
        h1_size = int(64 * s)
        text_width = int(w * 0.62)
    elif size_key == '1x1':
        h1_size = int(92 * s)
        text_width = int(w * 0.64)
    elif size_key == '4x5':
        h1_size = int(98 * s)
        text_width = int(w * 0.64)
    else:  # 9x16
        h1_size = int(118 * s)
        text_width = w - side_pad * 2

    cred_size = max(20, int(h1_size * 0.24))
    cta_size = max(24, int(h1_size * 0.28))
    cta_pad_v = max(16, int(cta_size * 0.82))
    cta_pad_h = max(34, int(cta_size * 2.0))
    tp_star_h = max(21, int(cta_size * 1.02))
    tp_text = max(13, int(cta_size * 0.74))

    # 9x16: keep CTA/trust above IG Stories bottom UI (~20% of 1920 = 384px -> use 300 scaled)
    text_bottom = {'1x1': int(64 * s), '4x5': int(80 * s),
                   '9x16': int(240 * s), '191x1': int(44 * s)}[size_key]
    offer_size = max(14, int(h1_size * 0.22))
    fact_size = max(22, int(h1_size * 0.30))

    # Lighter, moodier vignette so the wooden library set stays visible.
    # Left side gets a soft dark scrim behind text; top and bottom get gentle fades for logo/CTA legibility.
    if mode == 'side':
        vignette = ("background:"
                    "linear-gradient(97deg, rgba(14,9,5,.92) 0%, rgba(16,11,6,.78) 22%, "
                    "rgba(18,12,7,.42) 40%, rgba(18,12,7,.10) 56%, rgba(18,12,7,0) 66%),"
                    "linear-gradient(180deg, rgba(14,9,5,.68) 0%, rgba(14,9,5,0) 20%),"
                    "linear-gradient(180deg, rgba(14,9,5,0) 55%, rgba(14,9,5,.62) 100%);")
    else:
        vignette = ("background:linear-gradient(180deg, rgba(14,9,5,.68) 0%, rgba(14,9,5,.15) 18%, "
                    "rgba(14,9,5,0) 30%, rgba(14,9,5,.15) 55%, rgba(14,9,5,.78) 74%, rgba(10,6,3,.95) 100%);")

    l1 = html.escape(b['l1'])
    l2 = html.escape(b['l2'])

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  html,body{{margin:0;padding:0;background:#0c0805;overflow:hidden;font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
  .canvas{{position:relative;width:{w}px;height:{h}px;overflow:hidden;background:#0c0805;}}
  .photo{{position:absolute;{photo_box}object-fit:{fit};object-position:{op};z-index:1;filter:saturate(.98) contrast(1.03) brightness(.96);background:#0c0805;}}
  .vignette{{position:absolute;inset:0;z-index:2;{vignette}}}
  .grain{{position:absolute;inset:0;z-index:3;pointer-events:none;opacity:.05;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='240' height='240'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/></filter><rect width='100%25' height='100%25' filter='url(%23n)' opacity='1'/></svg>");}}
  .brand{{position:absolute;left:{side_pad}px;top:{top_pad}px;z-index:10;display:flex;flex-direction:column;gap:{max(12, int(logo_h * 0.16))}px;}}
  .brand img{{height:{logo_h}px;display:block;opacity:.99;filter:drop-shadow(0 4px 18px rgba(2,6,20,.7));}}
  .brand .eyebrow{{font-family:'EB Garamond',serif;font-style:italic;font-weight:500;font-size:{eyebrow_size}px;color:#e9d9be;line-height:1.25;text-shadow:0 2px 12px rgba(10,6,3,.65);}}
  .text{{position:absolute;left:{side_pad}px;bottom:{text_bottom}px;width:{text_width}px;z-index:11;color:#f7f3ec;}}
  .h1{{font-family:'EB Garamond',serif;font-weight:600;font-size:{h1_size}px;line-height:.98;letter-spacing:-.012em;margin:0;color:#f7f3ec;text-shadow:0 5px 34px rgba(10,6,3,.7);}}
  .h1 .b{{font-style:italic;font-weight:500;display:block;margin-top:{max(6, int(h1_size * 0.07))}px;background:linear-gradient(103deg,#f3e3c3 0%,#e6cd9d 45%,#d8b97f 75%,#eedcba 100%);-webkit-background-clip:text;background-clip:text;color:transparent;filter:drop-shadow(0 4px 22px rgba(10,6,3,.6));}}
  .cred{{margin-top:{max(22, int(h1_size * 0.27))}px;font-family:'EB Garamond',serif;font-style:italic;font-weight:500;font-size:{cred_size}px;color:rgba(247,240,228,.92);line-height:1.4;}}
  .cred .name{{font-style:normal;font-weight:700;color:#eddcb8;}}
  .offer{{margin-top:{max(10, int(h1_size * 0.13))}px;font-family:'Inter',sans-serif;font-weight:500;font-size:{offer_size}px;color:rgba(245,248,252,.95);letter-spacing:.01em;}}
  .facts{{margin-top:{max(16, int(h1_size * 0.24))}px;display:flex;flex-direction:column;gap:{max(10, int(fact_size * 0.60))}px;}}
  .facts .f{{display:block;font-family:'Inter',sans-serif;font-weight:600;font-size:{int(fact_size * 1.15)}px;color:#f7f3ec;line-height:1.28;letter-spacing:.008em;text-shadow:0 2px 10px rgba(10,6,3,.75);}}
  .facts .f .ck{{display:none;}}
  .actions{{margin-top:{max(30, int(h1_size * 0.40))}px;display:flex;flex-direction:column;align-items:flex-start;gap:{max(18, int(cta_size * 0.9))}px;}}
  .cta{{display:inline-flex;align-items:center;justify-content:center;background:#f2e9d8;color:#241408;font-family:'Inter',sans-serif;font-weight:700;font-size:{cta_size}px;letter-spacing:.14em;padding:{cta_pad_v}px {cta_pad_h}px;border-radius:9999px;border:0;box-shadow:0 10px 34px rgba(10,6,3,.55);}}
  .tp{{display:flex;align-items:center;gap:{max(10, int(tp_star_h * 0.5))}px;}}
  .tp .stars{{font-size:{tp_star_h}px;color:#00b67a;letter-spacing:.18em;line-height:1;text-shadow:0 2px 8px rgba(10,6,3,.6);}}
  .tp .word{{font-family:'Inter',sans-serif;font-weight:500;font-size:{max(12, int(tp_text * 1.0))}px;color:rgba(247,242,233,.92);}}
</style></head><body>
<div class="canvas">
  <img class="photo" src="../{photo}" alt="">
  <div class="vignette"></div>
  <div class="grain"></div>

  <div class="brand"><img src="../assets/lla_logo_ivory.png" alt="Longevity Life Academy by eTeacher Group">{eyebrow_html}</div>

  <div class="text">
    <h1 class="h1">{l1}<span class="b">{l2}</span></h1>
    <div class="cred">Taught live by <span class="name">Courtney</span>, Longevity Life Academy Instructor</div>
    <div class="facts">
      <div class="f"><span class="ck">✓</span><span>18 live sessions. Cohorts of 8-15.</span></div>
      <div class="f"><span class="ck">✓</span><span>The Six Pillars of longevity.</span></div>
      <div class="f"><span class="ck">✓</span><span>Your written longevity protocol.</span></div>
    </div>
    <div class="actions">
      <a class="cta">ENROLL NOW</a>
      <div class="tp">
        <span class="stars">★★★★★</span>
        <span class="word">4.6 on Trustpilot</span>
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
