import os
import re
import json

files = [
    "blogs/online-mba-jaipur.html",
    "blogs/online-mba-lucknow.html",
    "blogs/online-mba-chandigarh.html",
    "blogs/online-mba-ahmedabad.html",
    "blogs/online-mba-indore.html",
    "blogs/online-mba-bhopal.html",
]

all_passed = True

print(f"{'='*80}")
print(f"VERIFYING PRIORITY 3 (EMERGING MARKETS) CITY BLOG GUIDES")
print(f"{'='*80}\n")

for fpath in files:
    if not os.path.exists(fpath):
        print(f"❌ Missing file: {fpath}")
        all_passed = False
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Title
    title_m = re.search(r"<title>(.*?)</title>", content)
    title = title_m.group(1) if title_m else ""
    t_len = len(title)
    t_pass = 50 <= t_len <= 60
    
    # 2. Meta Description
    meta_m = re.search(r'<meta name="description" content="(.*?)">', content)
    meta = meta_m.group(1) if meta_m else ""
    m_len = len(meta)
    m_pass = 150 <= m_len <= 160
    cta_pass = bool(re.search(r'(Check eligibility|Apply now|Check plan)\.?$', meta, re.IGNORECASE))
    
    # 3. Canonical
    canon_m = re.search(r'<link rel="canonical" href="(.*?)">', content)
    canon = canon_m.group(1) if canon_m else ""
    expected_slug = os.path.splitext(os.path.basename(fpath))[0]
    expected_canon = f"https://www.onlinembaadmission.com/blogs/{expected_slug}"
    c_pass = (canon == expected_canon)
    
    # 4. Word Count
    clean_text = re.sub(r'<script.*?</script>', '', content, flags=re.DOTALL)
    clean_text = re.sub(r'<style.*?</style>', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'<.*?>', ' ', clean_text)
    words = clean_text.split()
    word_count = len(words)
    w_pass = word_count >= 3000
    
    # 5. Dual Lead Forms
    lead_forms = re.findall(r'<form\s+class="lead-form as-it-is-counseling-form"', content)
    form_pass = len(lead_forms) == 2
    
    # 6. Schema JSON-LD
    schema_m = re.search(r'<script type="application/ld\+json">(.*?)</script>', content, flags=re.DOTALL)
    schema_pass = False
    schema_types = []
    if schema_m:
        try:
            s_data = json.loads(schema_m.group(1).strip())
            graph = s_data.get("@graph", [])
            schema_types = [item.get("@type") for item in graph]
            if "BreadcrumbList" in schema_types and "BlogPosting" in schema_types and "FAQPage" in schema_types:
                schema_pass = True
        except Exception as e:
            schema_pass = False
            print(f"   Schema error: {e}")
    
    print(f"File: {fpath}")
    print(f"  Title ({t_len} chars): '{title}' -> {'PASS' if t_pass else 'FAIL'}")
    print(f"  Meta Desc ({m_len} chars): '{meta}' -> {'PASS' if (m_pass and cta_pass) else 'FAIL'}")
    print(f"  Canonical: '{canon}' -> {'PASS' if c_pass else 'FAIL'}")
    print(f"  Word Count: {word_count} words -> {'PASS' if w_pass else 'FAIL'}")
    print(f"  Lead Forms: {len(lead_forms)} detected -> {'PASS' if form_pass else 'FAIL'}")
    print(f"  Schema: {schema_types} -> {'PASS' if schema_pass else 'FAIL'}")
    print("-" * 60)
    
    if not (t_pass and m_pass and cta_pass and c_pass and w_pass and form_pass and schema_pass):
        all_passed = False

if all_passed:
    print("\n🎉 ALL PRIORITY 3 CITY BLOGS PASSED 100% OF VERIFICATION CHECKS!")
else:
    print("\n❌ SOME CHECKS FAILED. PLEASE REVIEW LOGS ABOVE.")
