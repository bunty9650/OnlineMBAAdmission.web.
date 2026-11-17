import os, re

files_to_convert = [
    # Priority 2
    'blogs/online-mba-bangalore.html',
    'blogs/online-mba-mumbai.html',
    'blogs/online-mba-pune.html',
    'blogs/online-mba-hyderabad.html',
    'blogs/online-mba-chennai.html',
    'blogs/online-mba-kolkata.html',
    # Priority 3
    'blogs/online-mba-jaipur.html',
    'blogs/online-mba-lucknow.html',
    'blogs/online-mba-chandigarh.html',
    'blogs/online-mba-ahmedabad.html',
    'blogs/online-mba-indore.html',
    'blogs/online-mba-bhopal.html',
    # Priority 4
    'blogs/online-mba-kanpur.html',
    'blogs/online-mba-meerut.html',
    'blogs/online-mba-agra.html',
    'blogs/online-mba-ludhiana.html',
    'blogs/online-mba-jodhpur.html',
    'blogs/online-mba-surat.html',
    'blogs/online-mba-nagpur.html',
    'blogs/online-mba-visakhapatnam.html',
    'blogs/online-mba-coimbatore.html',
    'blogs/online-mba-ranchi.html',
    # 5 National Blogs
    'blogs/is-online-mba-valid-in-india.html',
    'blogs/government-online-distance-mba-universities.html',
    'blogs/online-mba-after-bcom.html',
    'blogs/online-mba-finance-vs-marketing-vs-hr.html',
    'blogs/online-mba-vs-regular-mba.html'
]

item_pattern = re.compile(
    r'<div\s+class=[\"\']faq-item[\"\'][^>]*>\s*'
    r'<h3[^>]*>.*?<span[^>]*>Q\d+:</span>\s*(.*?)\s*</h3>\s*'
    r'<p[^>]*>(.*?)</p>\s*'
    r'</div>',
    re.DOTALL | re.IGNORECASE
)

updated_count = 0

for file_path in files_to_convert:
    if not os.path.exists(file_path):
        print(f"Skipping {file_path} (does not exist)")
        continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    idx_faq = content.find('id="faqs"')
    if idx_faq == -1:
        print(f"No id='faqs' in {file_path}")
        continue

    idx_sec_end = content.find('</section>', idx_faq)
    if idx_sec_end == -1:
        print(f"No </section> after faqs in {file_path}")
        continue

    faq_section = content[idx_faq:idx_sec_end]

    items = item_pattern.findall(faq_section)
    if not items:
        print(f"Pattern matched 0 items in {file_path}")
        continue

    idx_acc = faq_section.find('<div class="faq-accordion"')
    if idx_acc == -1:
        print(f"No <div class=\"faq-accordion\" in {file_path}")
        continue

    new_faq_html = '<div class="cs-faq-wrapper">\n'
    for q, a in items:
        q_clean = q.strip()
        a_clean = a.strip()
        new_faq_html += f"""          <div class="cs-faq-item">
            <div class="cs-faq-q" onclick="toggleFaq(this)">
              <span>{q_clean}</span>
              <span class="cs-faq-icon">+</span>
            </div>
            <div class="cs-faq-a">
              <p>{a_clean}</p>
            </div>
          </div>\n"""
    new_faq_html += '          </div>\n        '

    new_section = faq_section[:idx_acc] + new_faq_html
    content = content[:idx_faq] + new_section + content[idx_sec_end:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    updated_count += 1
    print(f"SUCCESS ({len(items)} FAQs): {file_path}")

print(f"\nTotal files updated: {updated_count} / {len(files_to_convert)}")
