#!/usr/bin/env python3
"""Render banner HTML files to PNG with headless Chromium."""
import os, sys, json
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
BAN = os.path.join(ROOT, 'banners')

only = sys.argv[1:] if len(sys.argv) > 1 else None

with open(os.path.join(ROOT, 'manifest.json')) as f:
    manifest = json.load(f)

jobs = []
for entry in manifest['courtney']:
    for key, meta in entry['sizes'].items():
        if only and not any(entry['id'] == o or meta['html'].startswith(o) for o in only):
            continue
        jobs.append((meta['html'], meta['png'], meta['w'], meta['h']))

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for html_fn, png_fn, w, h in jobs:
        page.set_viewport_size({'width': w, 'height': h})
        page.goto('file://' + os.path.join(BAN, html_fn))
        page.wait_for_load_state('networkidle')
        page.wait_for_timeout(400)  # font settle
        page.screenshot(path=os.path.join(BAN, png_fn), clip={'x': 0, 'y': 0, 'width': w, 'height': h})
        print('rendered', png_fn)
    browser.close()
print(f'{len(jobs)} PNGs rendered.')
