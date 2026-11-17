# -*- coding: utf-8 -*-
"""
Test HTTP 200 OK for all 10 Priority 4 clean URLs on local development server
"""

import urllib.request
from data_priority4_cities import cities_p4

base_url = "http://localhost:8000/blogs"

print("=== TESTING HTTP 200 FOR PRIORITY 4 CITIES ON LOCALHOST:8000 ===\n")

all_ok = True

for key, data in cities_p4.items():
    clean_url = f"{base_url}/{data['slug']}"
    req = urllib.request.Request(clean_url, headers={"User-Agent": "Mozilla/5.0 QA Inspector"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            status = resp.status
            if status == 200:
                print(f"HTTP {status} OK  : {data['name']:15} -> {clean_url}")
            else:
                print(f"HTTP {status} FAIL: {data['name']:15} -> {clean_url}")
                all_ok = False
    except Exception as e:
        print(f"ERROR: {data['name']:15} -> {clean_url}: {e}")
        all_ok = False

print(f"\nResult: {'ALL 10 CLEAN URLS RETURNED HTTP 200 OK' if all_ok else 'SOME URLS FAILED'}")
