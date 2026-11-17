# -*- coding: utf-8 -*-
"""
Test HTTP 200 for 5 new national pillar URLs
"""

import urllib.request
from data_national_pillars import national_pillars_data

base_url = "http://localhost:8000/blogs"

print("=== TESTING HTTP 200 FOR 5 NATIONAL PILLAR GUIDES ON LOCALHOST:8000 ===\n")

all_ok = True

for slug, data in national_pillars_data.items():
    clean_url = f"{base_url}/{slug}"
    req = urllib.request.Request(clean_url, headers={"User-Agent": "Mozilla/5.0 QA Inspector"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            status = resp.status
            if status == 200:
                print(f"HTTP {status} OK  : {slug:45} -> {clean_url}")
            else:
                print(f"HTTP {status} FAIL: {slug:45} -> {clean_url}")
                all_ok = False
    except Exception as e:
        print(f"ERROR: {slug:45} -> {clean_url}: {e}")
        all_ok = False

print(f"\nResult: {'ALL 5 NATIONAL PILLAR CLEAN URLS RETURNED HTTP 200 OK' if all_ok else 'SOME URLS FAILED'}")
