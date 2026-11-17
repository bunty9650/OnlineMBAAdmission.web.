import os, re, json

specs = [
    'mba-in-general-management',
    'mba-in-marketing',
    'mba-in-finance',
    'mba-in-human-resource-management',
    'mba-in-data-science-analytics',
    'mba-in-healthcare-management',
    'mba-in-logistics-supply-chain'
]

dir_path = 'university/st-aloysius'
all_passed = True

for slug in specs:
    file_path = os.path.join(dir_path, f"{slug}.html")
    if not os.path.exists(file_path):
        print(f"❌ Missing file: {file_path}")
        all_passed = False
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Title check
    title_m = re.search(r'<title>(.*?)</title>', html)
    title = title_m.group(1) if title_m else ""
    t_len = len(title)
    t_ok = 50 <= t_len <= 60

    # Meta desc check
    meta_m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html)
    meta = meta_m.group(1) if meta_m else ""
    m_len = len(meta)
    m_ok = 150 <= m_len <= 160
    m_cta = meta.endswith("Check eligibility.")

    # Canonical check
    canon_m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html)
    canon = canon_m.group(1) if canon_m else ""
    expected_canon = f"https://www.onlinembaadmission.com/university/st-aloysius/{slug}"
    canon_ok = (canon == expected_canon)

    # Schema JSON check
    schemas = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL)
    schema_ok = False
    types_found = []
    if schemas:
        try:
            s_data = json.loads(schemas[0])
            graph = s_data.get('@graph', [])
            types_found = [g.get('@type') for g in graph]
            if all(t in types_found for t in ['BreadcrumbList', 'Course', 'EducationalOccupationalProgram', 'FAQPage']):
                schema_ok = True
        except Exception as e:
            schema_ok = False

    # Lead form check
    form_count = html.count('as-it-is-counseling-form')
    forms_ok = (form_count >= 2)

    # Word count
    plain_text = re.sub(r'<[^>]+>', ' ', html)
    words = len(plain_text.split())

    # FAQ accordion check
    faq_ok = ('cs-faq-wrapper' in html and 'cs-faq-item' in html and 'toggleFaq' in html)

    print(f"\n--- Checking: {slug} ---")
    print(f"Title ({t_len}c): {'✅' if t_ok else '❌'} '{title}'")
    print(f"Meta ({m_len}c, ends with CTA: {m_cta}): {'✅' if m_ok and m_cta else '❌'} '{meta}'")
    print(f"Canonical: {'✅' if canon_ok else '❌'} '{canon}'")
    print(f"Schema Types ({len(types_found)}): {'✅' if schema_ok else '❌'} {types_found}")
    print(f"Forms count: {'✅' if forms_ok else '❌'} ({form_count} forms)")
    print(f"FAQ Accordion: {'✅' if faq_ok else '❌'}")
    print(f"Word count: {'✅' if words >= 1500 else '❌'} ({words} words)")

    if not (t_ok and m_ok and m_cta and canon_ok and schema_ok and forms_ok and faq_ok):
        all_passed = False

print("\n" + "="*50)
if all_passed:
    print("🎉 ALL 7 ST. ALOYSIUS SPECIALIZATION PAGES 100% COMPLIANT!")
else:
    print("⚠️ SOME CHECKS FAILED! REVIEW OUTPUT ABOVE.")
