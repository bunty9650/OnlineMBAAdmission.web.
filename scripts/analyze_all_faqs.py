import os, re

blogs = [os.path.join('blogs', f) for f in os.listdir('blogs') if f.endswith('.html')]
univs = [os.path.join('universities', f) for f in os.listdir('universities') if f.endswith('.html')]

print("=== BLOGS FAQ PATTERNS ===")
blog_patterns = {}
for b in blogs:
    with open(b, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'id="faqs"' in c or 'id="faq"' in c or 'Frequently Asked' in c:
        has_cs_q = 'cs-faq-q' in c
        has_cs_question = 'cs-faq-question' in c
        has_faq_item = 'faq-item' in c
        has_details = '<details' in c
        key = f"cs-faq-q:{has_cs_q} | cs-faq-question:{has_cs_question} | faq-item:{has_faq_item} | details:{has_details}"
        blog_patterns.setdefault(key, []).append(b)

for k, v in blog_patterns.items():
    print(f"\n{k} (Count: {len(v)}):")
    print("Sample:", v[:5])

print("\n=== UNIVERSITIES FAQ PATTERNS ===")
univ_patterns = {}
for u in univs:
    with open(u, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'id="faqs"' in c or 'id="faq"' in c or 'Frequently Asked' in c:
        has_cs_q = 'cs-faq-q' in c
        has_cs_question = 'cs-faq-question' in c
        has_faq_item = 'faq-item' in c
        has_details = '<details' in c
        key = f"cs-faq-q:{has_cs_q} | cs-faq-question:{has_cs_question} | faq-item:{has_faq_item} | details:{has_details}"
        univ_patterns.setdefault(key, []).append(u)

for k, v in univ_patterns.items():
    print(f"\n{k} (Count: {len(v)}):")
    print("Sample:", v[:5])
