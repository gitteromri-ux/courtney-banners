#!/usr/bin/env python3
"""
Courtney Banners V13 — ported 1:1 from the approved Julie on-set system
(julie-onset-banners): Playfair Display headlines, real LLA logo,
champagne accents, boxed Trustpilot stars inline with CTA.
Copywriting unchanged from V11/V12.
"""

import json, os, html

OUT = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(OUT, 'banners')
os.makedirs(BAN, exist_ok=True)

# Real production-set plates (V12, Nano Banana Pro)
PLATE_SQ = 'assets/composites/courtney_realset_sq.png'   # 1:1  subject right
PLATE_45 = 'assets/composites/courtney_realset_45.png'   # 3:4  subject right
PLATE_PT = 'assets/composites/courtney_realset_pt.png'   # 9:16 subject center, face high
PLATE_LS = 'assets/composites/courtney_realset_ls.png'   # 16:9 subject right

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

# Per-size metrics lifted from the approved Julie on-set system,
# headline sizes raised for a wider, more prominent serif presence.
SIZES = {
    '1x1':   dict(w=1080, h=1080, label='1:1 Feed',     note='Instagram Post / FB Feed Square',
                  pad=64, logo=250, h1=100, sub=27, cred=23, cta=21, ctap='20px 40px',
                  tpi=26, tps=22, eyeb=22, plate=PLATE_SQ, op='70% 24%'),
    '4x5':   dict(w=1080, h=1350, label='4:5 Vertical', note='Instagram / FB Feed Vertical',
                  pad=68, logo=260, h1=106, sub=28, cred=24, cta=22, ctap='21px 42px',
                  tpi=27, tps=23, eyeb=23, plate=PLATE_45, op='68% 16%'),
    '9x16':  dict(w=1080, h=1920, label='9:16 Story',   note='IG Stories, Reels, FB Stories',
                  pad=72, logo=270, h1=112, sub=30, cred=25, cta=23, ctap='22px 44px',
                  tpi=28, tps=24, eyeb=24, plate=PLATE_PT, op='50% 20%'),
    '191x1': dict(w=1200, h=628,  label='1.91:1 Link',  note='FB Link Ad / Marketplace',
                  pad=44, logo=190, h1=64,  sub=19, cred=16, cta=15, ctap='13px 28px',
                  tpi=18, tps=15, eyeb=16, plate=PLATE_LS, op='60% 28%'),
}


def render_banner(b, key):
    c = SIZES[key]
    l1, l2 = html.escape(b['l1']), html.escape(b['l2'])
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
@font-face{{font-family:'Playfair';src:url('../assets/fonts/PlayfairDisplay.ttf');font-weight:400 900;}}
@font-face{{font-family:'PlayfairIt';src:url('../assets/fonts/PlayfairDisplay-Italic.ttf');font-weight:400 900;font-style:italic;}}
@font-face{{font-family:'Inter';src:url('../assets/fonts/Inter.ttf');font-weight:100 900;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html,body{{width:{c['w']}px;height:{c['h']}px;overflow:hidden;background:#0a1020;}}
.stage{{position:relative;width:{c['w']}px;height:{c['h']}px;overflow:hidden;}}
.stage img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{c['op']};}}
.scrim-s{{position:absolute;inset:0;background:linear-gradient(to right,rgba(6,10,20,0.55) 0%,rgba(6,10,20,0.2) 46%,rgba(6,10,20,0) 78%);}}
.scrim-b{{position:absolute;left:0;right:0;bottom:0;height:70%;
  background:linear-gradient(to top,rgba(6,10,20,.96) 0%,rgba(6,10,20,.88) 35%,rgba(6,10,20,.55) 68%,rgba(6,10,20,0) 100%);}}
.scrim-t{{position:absolute;left:0;right:0;top:0;height:26%;
  background:linear-gradient(to bottom,rgba(6,10,20,.80) 0%,rgba(6,10,20,.35) 55%,rgba(6,10,20,0) 100%);}}
.logo{{position:absolute;top:{c['pad']}px;left:{c['pad']}px;width:{c['logo']}px;}}
.logo img{{width:100%;display:block;}}
.eyebrow{{font-family:'Inter',sans-serif;font-weight:500;color:rgba(255,255,255,.82);
  font-size:{c['eyeb']}px;margin-top:{int(c['eyeb'] * 0.8)}px;letter-spacing:.02em;white-space:nowrap;}}
.content{{position:absolute;left:{c['pad']}px;right:{c['pad']}px;bottom:{c['pad']}px;}}
h1{{font-family:'Playfair',serif;font-weight:700;color:#fff;
  font-size:{c['h1']}px;line-height:1.04;letter-spacing:-.015em;}}
h1 span{{display:block;white-space:nowrap;}}
h1 .it{{font-family:'PlayfairIt',serif;font-style:italic;font-weight:600;
  color:#d8c39a;}}
.sub{{font-family:'Inter',sans-serif;font-weight:400;color:rgba(255,255,255,.86);
  font-size:{c['sub']}px;line-height:1.35;margin-top:{int(c['sub'] * 0.82)}px;max-width:88%;}}
.cred{{font-family:'Inter',sans-serif;margin-top:{int(c['sub'] * 0.82)}px;}}
.cred div{{color:#d8c39a;font-size:{c['cred']}px;line-height:1.45;font-weight:500;letter-spacing:.01em;}}
.row{{display:flex;align-items:center;gap:26px;margin-top:{int(c['sub'] * 1.25)}px;flex-wrap:nowrap;}}
.cta{{font-family:'Inter',sans-serif;font-weight:600;color:#0a1020;background:#e8d9b5;
  font-size:{c['cta']}px;letter-spacing:.10em;padding:{c['ctap']};border-radius:999px;white-space:nowrap;}}
.tp{{display:flex;align-items:center;gap:12px;}}
.tp img{{height:{c['tpi']}px;display:block;}}
.tp span{{font-family:'Inter',sans-serif;color:rgba(255,255,255,.88);font-size:{c['tps']}px;white-space:nowrap;}}
</style></head><body>
<div class="stage">
  <img class="bg" src="../{c['plate']}">
  <div class="scrim-t"></div><div class="scrim-s"></div><div class="scrim-b"></div>
  <div class="logo"><img src="../assets/lla_logo.png"><div class="eyebrow">Live Online Longevity Course</div></div>
  <div class="content">
    <h1><span class="l1">{l1}</span><span class="it">{l2}</span></h1>
    <div class="sub">Taught live by Courtney, Longevity Life Academy Instructor</div>
    <div class="cred">
      <div>18 live sessions. Cohorts of 8-15.</div>
      <div>The Six Pillars of longevity.</div>
      <div>Your written longevity protocol.</div>
    </div>
    <div class="row">
      <div class="cta">ENROLL NOW</div>
      <div class="tp"><img src="../assets/tp_stars-5.svg"><span>4.6 on Trustpilot</span></div>
    </div>
  </div>
</div>
<script>
(function(){{
  var h1=document.querySelector('h1');
  var box=document.querySelector('.content');
  var max=box.clientWidth;
  var size=parseFloat(getComputedStyle(h1).fontSize);
  while(size>18){{
    var fits=true;
    h1.querySelectorAll('span').forEach(function(s){{ if(s.scrollWidth>max) fits=false; }});
    if(fits) break;
    size-=1; h1.style.fontSize=size+'px';
  }}
}})();
</script>
</body></html>"""


def main():
    manifest = {'courtney': []}
    for b in BANNERS:
        entry = {'id': b['id'], 'title': b['title'], 'sizes': {}}
        for key, c in SIZES.items():
            out = render_banner(b, key)
            fn = f"{b['id']}_{key}.html"
            with open(os.path.join(BAN, fn), 'w') as f:
                f.write(out)
            entry['sizes'][key] = {'html': fn, 'png': fn.replace('.html', '.png'),
                                   'w': c['w'], 'h': c['h'], 'label': c['label'], 'note': c['note']}
        manifest['courtney'].append(entry)
    with open(os.path.join(OUT, 'manifest.json'), 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {len(BANNERS) * len(SIZES)} HTML files.")


if __name__ == '__main__':
    main()
