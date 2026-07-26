#!/usr/bin/env python3
"""
Courtney banners — 9 hooks from her exact on-camera script, x 4 Meta/IG ad sizes.
Same luxury design system as the Julie gallery (navy/gold/serif, brand bar),
with Courtney's real home footage frames, $289/mo pricing, "Claim Your Seat" CTA.
"""
import os, json
BANNERS_DIR = "/home/user/workspace/courtney-banners/banners"
os.makedirs(BANNERS_DIR, exist_ok=True)

SIZES = {
    "1x1":   {"w":1080, "h":1080, "label":"1:1 Feed",     "note":"Instagram Post / FB Feed Square"},
    "4x5":   {"w":1080, "h":1350, "label":"4:5 Vertical", "note":"Instagram / FB Feed Vertical"},
    "9x16":  {"w":1080, "h":1920, "label":"9:16 Story",   "note":"IG Stories, Reels, FB Stories"},
    "191x1": {"w":1200, "h":628,  "label":"1.91:1 Link",  "note":"FB Link Ad / Marketplace"},
}

# All headlines are Courtney's exact spoken lines (user-verified transcript).
BANNERS = [
    {"id":"c_b1", "title":"Advice Is Everywhere",  "photo":"courtney_2.jpg", "focus":"48% 22%",
     "h1":"\u201cIt seems like longevity advice", "h2":"is everywhere.\u201d", "quote":True,
     "eyebrow":None},
    {"id":"c_b2", "title":"A Clear Path",          "photo":"courtney_1.jpg", "focus":"46% 22%",
     "h1":"\u201cYou didn\u2019t lack willpower \u2014", "h2":"you lacked a clear path.\u201d", "quote":True,
     "eyebrow":None},
    {"id":"c_b3", "title":"Not Your Fault",        "photo":"courtney_3.jpg", "focus":"50% 22%",
     "h1":"\u201cIt wasn\u2019t", "h2":"your fault.\u201d", "quote":False,
     "eyebrow":None},
    {"id":"c_b4", "title":"A Real Curriculum",     "photo":"courtney_4.jpg", "focus":"48% 22%",
     "h1":"\u201cSix pillars, like a real curriculum", "h2":"\u2014 not a pile of tips.\u201d", "quote":True,
     "eyebrow":None},
    {"id":"c_b5", "title":"Harvard \u00b7 14 Years", "photo":"courtney_2.jpg", "focus":"48% 22%",
     "h1":"Five habits by age 40.", "h2":"14 extra years.", "quote":False,
     "eyebrow":"Harvard tracked 120,000 adults"},
    {"id":"c_b6", "title":"Your Blueprint",        "photo":"courtney_1.jpg", "focus":"46% 22%",
     "h1":"\u201c18 lessons, week by week \u2014 your", "h2":"tailored longevity blueprint.\u201d", "quote":True,
     "eyebrow":None},
    {"id":"c_b7", "title":"Buried in Information", "photo":"courtney_3.jpg", "focus":"50% 22%",
     "h1":"\u201cYou don\u2019t need more information.", "h2":"You\u2019re already buried in it.\u201d", "quote":True,
     "eyebrow":None},
    {"id":"c_b8", "title":"Raise Your Hand",       "photo":"courtney_4.jpg", "focus":"48% 22%",
     "h1":"\u201cA guided classroom \u2014 where", "h2":"you can raise your hand.\u201d", "quote":True,
     "eyebrow":None},
    {"id":"c_b9", "title":"Class Is in Session",   "photo":"courtney_1.jpg", "focus":"46% 22%",
     "h1":"\u201cClass is in session, and", "h2":"there\u2019s a seat for you.\u201d", "quote":True,
     "eyebrow":None},
]

DEFAULT_EYEBROW = 'The Longevity Masterclass <b>\u00b7 100% Online</b>'


def html_head(w, h):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html,body {{ width:{w}px; height:{h}px; overflow:hidden; background:#020B1C; }}
.canvas {{ position:relative; width:{w}px; height:{h}px; background:#020B1C; font-family:'Inter',sans-serif; overflow:hidden; }}
.serif {{ font-family:'Instrument Serif',serif; font-weight:400; letter-spacing:-.01em; line-height:1.02; text-shadow:0 4px 24px rgba(0,0,0,.6); }}
.serif i {{ font-style:italic; color:#A9CFFF; }}
</style></head><body>"""


def render(banner, w, h):
    area = w * h
    s = (area / (1080 * 1080)) ** 0.5
    ratio = w / h
    is_landscape = ratio > 1.4
    is_portrait  = ratio < 0.7

    bar_h = int(90 * s * 1.15) if is_landscape else int(148 * s)
    hl_size1 = int(88 * s * (0.85 if is_landscape else 1.0))
    hl_size2 = int(94 * s * (0.85 if is_landscape else 1.0))
    if banner.get("quote"):
        hl_size1 = int(hl_size1 * 0.70)
        hl_size2 = int(hl_size2 * 0.76)
    eyebrow_size = max(12, int(19 * s))
    cred_size    = max(12, int(16 * s))
    logo_h       = int(bar_h * 0.55)
    cta_font     = max(14, int(22 * s))
    cta_pad_v    = max(10, int(17 * s))
    cta_pad_h    = max(20, int(32 * s))
    bar_pad      = int(36 * s)
    bar_gap      = int(20 * s)
    if is_portrait:
        # narrower canvas relative to scale — tighten the bar so CTA + trust fit
        cta_font  = max(14, int(17 * s))
        cta_pad_h = max(16, int(22 * s))
        bar_pad   = int(24 * s)
        bar_gap   = int(12 * s)
        logo_h    = int(bar_h * 0.46)
    edge_pad     = int(56 * s)

    photo_area = f"""
<div class="photo">
  <img src="../assets/{banner['photo']}" style="object-position:{banner['focus']};">
</div>"""

    if is_landscape:
        text_style = f"left:{edge_pad}px; top:50%; transform:translateY(-50%); text-align:left; max-width:62%;"
        scrim_style = "background:linear-gradient(90deg, rgba(2,11,28,.94) 0%, rgba(2,11,28,.62) 40%, rgba(2,11,28,.08) 70%, rgba(2,11,28,0) 100%);"
    elif is_portrait:
        text_style = f"left:{edge_pad}px; right:{edge_pad}px; bottom:{bar_h + int(80*s)}px; text-align:left;"
        scrim_style = "background:linear-gradient(180deg, rgba(2,11,28,.25) 0%, rgba(2,11,28,0) 30%, rgba(2,11,28,0) 45%, rgba(2,11,28,.65) 70%, rgba(2,11,28,.95) 100%);"
    else:
        text_style = f"left:{edge_pad}px; right:{edge_pad}px; bottom:{bar_h + int(52*s)}px; text-align:left;"
        scrim_style = "background:linear-gradient(90deg, rgba(2,11,28,.88) 0%, rgba(2,11,28,.55) 42%, rgba(2,11,28,.12) 72%, rgba(2,11,28,0) 100%), linear-gradient(180deg, rgba(2,11,28,0) 60%, rgba(2,11,28,.5) 100%);"

    eyebrow_txt = banner.get("eyebrow") or DEFAULT_EYEBROW
    if banner.get("eyebrow"):
        eyebrow_txt = f'{banner["eyebrow"]} <b>\u00b7 Harvard Study</b>' if False else banner["eyebrow"]

    credential_block = f"""
<div class="cred" style="font-size:{cred_size}px; margin-top:{int(20*s)}px;">
  <span class="rule"></span>With <b>Courtney</b> \u2014 Longevity Life Academy<br>
  <span class="f">The Longevity Masterclass \u00b7 18 Live Sessions</span>
</div>"""

    tp_h = int(bar_h * 0.20)
    star_h = int(bar_h * 0.16)
    trust_block = f"""
<div class="r1">
  <img class="tpl" src="../assets/tp_logo-white.svg" style="height:{tp_h}px;">
  <img class="tps" src="../assets/tp_stars-5.svg" style="height:{star_h}px;">
  <span style="font-size:{max(10,int(bar_h*0.10))}px; white-space:nowrap;">4.6/5 \u00b7 600+ reviews</span>
</div>"""
    r2_size = max(10, int(bar_h * 0.10))

    return f"""{html_head(w,h)}
<style>
.photo {{ position:absolute; left:0; right:0; top:0; bottom:{bar_h}px; overflow:hidden; }}
.photo img {{ width:100%; height:100%; object-fit:cover; }}
.scrim {{ position:absolute; left:0; right:0; top:0; bottom:{bar_h}px; {scrim_style} }}
.content {{ position:absolute; z-index:5; {text_style} color:#fff; }}
.eyebrow {{ display:flex; align-items:center; gap:{max(6,int(10*s))}px; margin-bottom:{int(18*s)}px; }}
.eyebrow .dot {{ width:{max(6,int(9*s))}px; height:{max(6,int(9*s))}px; border-radius:50%; background:#E8A75A; box-shadow:0 0 12px rgba(232,167,90,.9); }}
.eyebrow .txt {{ font-size:{eyebrow_size}px; font-weight:700; letter-spacing:.22em; text-transform:uppercase; text-shadow:0 1px 8px rgba(0,0,0,.7); }}
.eyebrow .txt b {{ color:#7EC8FF; font-weight:700; }}
.cred {{ color:#fff; font-weight:700; text-transform:uppercase; letter-spacing:.13em; line-height:1.7; text-shadow:0 1px 8px rgba(0,0,0,.8); }}
.cred .rule {{ display:inline-block; width:{int(28*s)}px; height:{max(2,int(3*s))}px; background:#E8A75A; vertical-align:middle; margin-right:{int(12*s)}px; border-radius:2px; }}
.cred b {{ color:#E8A75A; }}
.cred .f {{ color:#A9CFFF; font-weight:600; letter-spacing:.11em; }}
.bar {{ position:absolute; left:0; right:0; bottom:0; height:{bar_h}px; background:linear-gradient(180deg,#03132E 0%,#010B1E 100%); border-top:1px solid rgba(232,167,90,.55); display:flex; align-items:center; padding:0 {bar_pad}px; z-index:20; gap:{bar_gap}px; }}
.bar .logo img {{ height:{logo_h}px; display:block; }}
.bar .mid {{ margin:0 auto; display:flex; flex-direction:column; align-items:center; gap:{max(4,int(6*s))}px; color:#fff; text-align:center; }}
.bar .mid .r1 {{ display:flex; align-items:center; gap:{max(4,int(8*s))}px; color:rgba(255,255,255,.85); font-weight:600; white-space:nowrap; }}
.bar .mid .r2 {{ font-size:{r2_size}px; font-weight:500; color:rgba(255,255,255,.6); letter-spacing:.04em; }}
.cta {{ display:inline-flex; align-items:center; gap:{max(6,int(10*s))}px; background:linear-gradient(135deg,#3A8DFF 0%,#006EFF 100%); color:#fff; font-weight:800; font-size:{cta_font}px; padding:{cta_pad_v}px {cta_pad_h}px; border-radius:999px; border:1px solid rgba(255,255,255,.5); box-shadow:0 6px 24px rgba(0,110,255,.5), inset 0 1px 0 rgba(255,255,255,.3); white-space:nowrap; font-family:'Inter',sans-serif; }}
</style>
<div class="canvas">
  {photo_area}
  <div class="scrim"></div>
  <div class="content">
    <div class="eyebrow"><span class="dot"></span><span class="txt">{eyebrow_txt}</span></div>
    <div class="serif" style="font-size:{hl_size1}px; color:#fff;">{banner['h1']}</div>
    <div class="serif" style="font-size:{hl_size2}px;"><i>{banner['h2']}</i></div>
    {credential_block}
  </div>
  <div class="bar">
    <div class="logo"><img src="../assets/lla_logo.png"></div>
    <div class="mid">
      {trust_block}
      <div class="r2">From $289/mo \u00b7 longevitylifeacademy.com</div>
    </div>
    <span class="cta">Claim Your Seat <span>\u2192</span></span>
  </div>
</div></body></html>"""


manifest = {"courtney": []}
for b in BANNERS:
    item = {"id": b["id"], "title": b["title"], "sizes": {}}
    for size_key, size in SIZES.items():
        fn = f"{b['id']}_{size_key}.html"
        with open(f"{BANNERS_DIR}/{fn}", "w") as f:
            f.write(render(b, size["w"], size["h"]))
        item["sizes"][size_key] = {
            "html": fn, "png": fn.replace(".html", ".png"),
            "w": size["w"], "h": size["h"], "label": size["label"], "note": size["note"],
        }
    manifest["courtney"].append(item)

with open("/home/user/workspace/courtney-banners/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
print(f"Wrote {len(BANNERS)*len(SIZES)} HTML files for {len(BANNERS)} banners.")
