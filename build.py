#!/usr/bin/env python3
"""
Courtney Banners V14
- Logo: one-line wordmark recomposed pixel-exact from the real lla_logo.png
  ("Longevity Life Academy" one line, "by eTeacher Group" beneath).
- No gold anywhere: brand navy/blue/white palette only.
- Course info as a structured graphic block (rule + diamond markers + dividers), no pills.
- "Taught live by Courtney, Longevity Life Academy Instructor" as an on-set
  broadcast lower third placed next to Courtney.
Copywriting unchanged.
"""

import json, os, html

OUT = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(OUT, 'banners')
os.makedirs(BAN, exist_ok=True)

PLATE_SQ = 'assets/composites/courtney_realset_sq.png'
PLATE_45 = 'assets/composites/courtney_realset_45.png'
PLATE_PT = 'assets/composites/courtney_realset_pt.png'
PLATE_LS = 'assets/composites/courtney_realset_ls.png'

BLUE = '#9cc2ee'       # light brand blue (from logo "Longevity" tone)
BLUE_ACC = '#5d92dd'   # accent bar / markers
INK = '#0a1428'

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

SIZES = {
    '1x1':   dict(w=1080, h=1080, label='1:1 Feed',     note='Instagram Post / FB Feed Square',
                  pad=64, logo=640, h1=112, cred=28, cta=21, ctap='20px 40px',
                  tpi=26, tps=22, eyeb=22, mk=8, ltn=24, ltr=19,
                  ltpos='right:64px;bottom:72px;', plate=PLATE_SQ, op='70% 24%'),
    '4x5':   dict(w=1080, h=1350, label='4:5 Vertical', note='Instagram / FB Feed Vertical',
                  pad=68, logo=660, h1=120, cred=29, cta=22, ctap='21px 42px',
                  tpi=27, tps=23, eyeb=23, mk=8, ltn=25, ltr=19,
                  ltpos='right:68px;bottom:76px;', plate=PLATE_45, op='68% 16%'),
    '9x16':  dict(w=1080, h=1920, label='9:16 Story',   note='IG Stories, Reels, FB Stories',
                  pad=72, logo=690, h1=126, cred=30, cta=23, ctap='22px 44px',
                  tpi=28, tps=24, eyeb=24, mk=9, ltn=26, ltr=21,
                  ltpos='right:72px;top:950px;', plate=PLATE_PT, op='50% 20%'),
    '191x1': dict(w=1200, h=628,  label='1.91:1 Link',  note='FB Link Ad / Marketplace',
                  pad=44, logo=350, h1=68,  cred=18, cta=15, ctap='13px 28px',
                  tpi=18, tps=15, eyeb=16, mk=6, ltn=17, ltr=14,
                  ltpos='right:44px;bottom:36px;', plate=PLATE_LS, op='60% 28%'),
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
.scrim-b{{position:absolute;left:0;right:0;bottom:0;height:78%;
  background:linear-gradient(to top,rgba(6,10,20,.96) 0%,rgba(6,10,20,.88) 35%,rgba(6,10,20,.55) 68%,rgba(6,10,20,0) 100%);}}
.scrim-t{{position:absolute;left:0;right:0;top:0;height:26%;
  background:linear-gradient(to bottom,rgba(6,10,20,.80) 0%,rgba(6,10,20,.35) 55%,rgba(6,10,20,0) 100%);}}
.content{{position:absolute;left:{c['pad']}px;right:{c['pad']}px;bottom:{c['pad']}px;}}
.logo{{width:{c['logo']}px;margin-bottom:{int(c['h1'] * 0.26)}px;}}
.logo img{{width:100%;display:block;}}
.eyebrow{{font-family:'Inter',sans-serif;font-weight:500;color:rgba(255,255,255,.82);
  font-size:{c['eyeb']}px;margin-bottom:{int(c['eyeb'] * 0.9)}px;letter-spacing:.02em;white-space:nowrap;}}
h1{{font-family:'Playfair',serif;font-weight:700;color:#fff;
  font-size:{c['h1']}px;line-height:1.04;letter-spacing:-.015em;}}
h1 span{{display:block;white-space:nowrap;}}
h1 .it{{font-family:'PlayfairIt',serif;font-style:italic;font-weight:600;
  color:{BLUE};}}
.facts{{display:inline-block;margin-top:{int(c['cred'] * 1.1)}px;}}
.fact::before{{content:'';width:{c['mk']}px;height:{c['mk']}px;border-radius:50%;
  background:#fff;flex:none;box-shadow:0 0 10px rgba(255,255,255,.35);}}
.fact{{display:flex;align-items:center;gap:{int(c['cred'] * 0.75)}px;
  font-family:'Inter',sans-serif;font-weight:500;color:#f4f7fb;
  font-size:{c['cred']}px;line-height:1;padding:{int(c['cred'] * 0.5)}px 0;
  text-shadow:0 1px 12px rgba(0,0,0,.55);}}
.row{{display:flex;align-items:center;gap:26px;margin-top:{int(c['cred'] * 1.3)}px;flex-wrap:nowrap;}}
.cta{{font-family:'Inter',sans-serif;font-weight:600;color:{INK};background:#f2f6fc;
  font-size:{c['cta']}px;letter-spacing:.10em;padding:{c['ctap']};border-radius:8px;white-space:nowrap;}}
.tp{{display:flex;align-items:center;gap:12px;}}
.tp img{{height:{c['tpi']}px;display:block;}}
.tp span{{font-family:'Inter',sans-serif;color:rgba(255,255,255,.88);font-size:{c['tps']}px;white-space:nowrap;}}
.lt{{position:absolute;{c['ltpos']}display:flex;}}
.lt .tx{{padding:0;text-align:right;}}
.lt .n{{font-family:'Inter',sans-serif;font-weight:600;color:#fff;
  font-size:{c['ltn']}px;letter-spacing:.01em;white-space:nowrap;
  text-shadow:0 2px 16px rgba(0,0,0,.65),0 1px 4px rgba(0,0,0,.55);}}
.lt .r{{font-family:'Inter',sans-serif;font-weight:400;color:rgba(255,255,255,.78);
  font-size:{c['ltr']}px;margin-top:{int(c['ltr'] * 0.35)}px;letter-spacing:.03em;white-space:nowrap;
  text-shadow:0 2px 16px rgba(0,0,0,.65),0 1px 4px rgba(0,0,0,.55);}}
</style></head><body>
<div class="stage">
  <img class="bg" src="../{c['plate']}">
  <div class="scrim-t"></div><div class="scrim-s"></div><div class="scrim-b"></div>
  <div class="lt"><div class="tx">
    <div class="n">Taught live by Courtney</div>
    <div class="r">Longevity Life Academy Instructor</div>
  </div></div>
  <div class="content">
    <div class="logo"><img src="../assets/lla_logo_oneline.png"></div>
    <h1><span class="l1">{l1}</span><span class="it">{l2}</span></h1>
    <div class="facts">
      <div class="fact">Join 18 live sessions. Small groups of 8-15.</div>
      <div class="fact">Master the Six Pillars of longevity.</div>
      <div class="fact">Get your written longevity protocol.</div>
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
