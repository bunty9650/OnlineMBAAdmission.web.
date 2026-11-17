# -*- coding: utf-8 -*-
"""
Verification Script for Priority 4 City Blogs
Using Standard Library Only (re, json, os)
"""

import os
import re
import json
from data_priority4_cities import cities_p4

print("=== STARTING PRIORITY 4 CITY BLOG AUDIT ===\n")

all_passed = True

for key, data in cities_p4.items():
    filename = f"blogs/{data['slug']}.html"
    city = data["name"]
    
    if not os.path.exists(filename):
        print(f"FAILED: File {filename} does not exist!")
        all_passed = False
        continue
        
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()
        
    # 1. Title length
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else ""
    t_len = len(title)
    t_ok = 50 <= t_len <= 60
    
    # 2. Meta description
    meta_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
    if not meta_match:
        meta_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.DOTALL | re.IGNORECASE)
    meta = meta_match.group(1).strip() if meta_match else ""
    m_len = len(meta)
    m_ok = 150 <= m_len <= 160
    cta_ok = meta.endswith("Check eligibility.")
    
    # 3. Canonical tag
    canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
    if not canon_match:
        canon_match = re.search(r'<link\s+href=["\'](.*?)["\']\s+rel=["\']canonical["\']', html, re.DOTALL | re.IGNORECASE)
    canon = canon_match.group(1).strip() if canon_match else ""
    expected_canon = f"https://www.onlinembaadmission.com/blogs/{data['slug']}"
    c_ok = (canon == expected_canon)
    
    # 4. Word count (strip script, style, html tags)
    clean_html = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    clean_html = re.sub(r'<style.*?</style>', ' ', clean_html, flags=re.DOTALL | re.IGNORECASE)
    clean_html = re.sub(r'<nav.*?</nav>', ' ', clean_html, flags=re.DOTALL | re.IGNORECASE)
    clean_html = re.sub(r'<footer.*?</footer>', ' ', clean_html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', clean_html)
    words = re.findall(r'\b[A-Za-z0-9\u0900-\u097F₹%–-]+\b', text)
    word_count = len(words)
    w_ok = word_count >= 3000
    
    # 5. Dual lead forms
    bottom_form_match = re.search(rf'data-source=["\']{re.escape(city)} Blog Form["\']', html)
    sidebar_form_match = re.search(rf'data-source=["\']{re.escape(city)} Sidebar Form["\']', html)
    f_ok = (bottom_form_match is not None and sidebar_form_match is not None)
    
    # 6. JSON-LD Schema
    schema_matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL)
    schema_ok = False
    entities = []
    for sm in schema_matches:
        try:
            sd = json.loads(sm.strip())
            if "@graph" in sd:
                types = [item.get("@type") for item in sd["@graph"]]
                entities.extend(types)
                if "BreadcrumbList" in types and "BlogPosting" in types and "FAQPage" in types:
                    schema_ok = True
        except Exception:
            pass
            
    # 7. EdTech regulatory content
    has_ugc = "UGC" in html and "DEB" in html
    has_gazette = "Regulation 22" in html or "Gazette" in html
    has_proctored = "AI" in html and ("proctor" in html.lower() or "proctored" in html.lower())
    reg_ok = has_ugc and has_gazette and has_proctored
    
    city_pass = t_ok and m_ok and cta_ok and c_ok and w_ok and f_ok and schema_ok and reg_ok
    if not city_pass:
        all_passed = False
        print(f"FAILED City: {city}")
        print(f"  Title ({t_len} chars, 50-60): {t_ok} -> '{title}'")
        print(f"  Meta ({m_len} chars, 150-160): {m_ok}, CTA: {cta_ok} -> '{meta}'")
        print(f"  Canonical ({canon}): {c_ok}")
        print(f"  Word Count ({word_count} words >= 3000): {w_ok}")
        print(f"  Dual Forms: {f_ok}")
        print(f"  Schema Entities ({entities}): {schema_ok}")
        print(f"  Regulatory Content: {reg_ok}")
    else:
        print(f"PASS: {city:15} | Words: {word_count:5} | Title: {t_len} chars | Meta: {m_len} chars | Schema: 3 Entities | Forms: Dual")

print(f"\nAudit Summary: {'ALL 10 PRIORITY 4 CITIES PASSED 100%' if all_passed else 'SOME CITIES FAILED'}")
