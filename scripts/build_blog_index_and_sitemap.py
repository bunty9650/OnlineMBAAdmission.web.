"""
Script: scripts/build_blog_index_and_sitemap.py
1. Collects all 86 articles in blogs/*.html
2. Rebuilds blogs/index.html (Page 1: Articles 1-9, 3-3-3)
3. Rebuilds blogs/page-2.html (Page 2: Articles 10-18, 3-3-3)
4. Rebuilds blogs/page-3.html (Page 3: Articles 19-27, 3-3-3)
5. Rebuilds blogs/page-4.html (Page 4: Articles 28-36, 3-3-3)
6. Rebuilds blogs/page-5.html (Page 5: Articles 37-45, 3-3-3)
7. Rebuilds blogs/page-6.html (Page 6: Articles 46-54, 3-3-3)
8. Rebuilds blogs/page-7.html (Page 7: Articles 55-63, 3-3-3)
9. Rebuilds blogs/page-8.html (Page 8: Articles 64-72, 3-3-3)
10. Rebuilds blogs/page-9.html (Page 9: Articles 73-81, 3-3-3)
11. Creates blogs/page-10.html (Page 10: Articles 82-86)
12. Updates sitemap.xml with all 86 articles and 10 pagination pages (total 372 URLs)
"""

import os
import re
import xml.etree.ElementTree as ET

# Ordered list of all 86 articles
ORDERED_SLUGS = [
    # Page 1: Top Core Pillar & Admission Blueprints (9 articles: 1-9)
    "online-mba",
    "online-mba-admission",
    "online-mba-admission-2026",
    "online-mba-admission-open",
    "top-online-mba-universities-in-india",
    "online-mba-colleges-in-india",
    "best-online-mba",
    "online-mba-admission-process",
    "online-mba-in-india",

    # Page 2: Application, Enrollment & Degree Guides (9 articles: 10-18)
    "online-mba-application",
    "online-mba-enrollment",
    "online-mba-admissions",
    "online-mba-admission-last-date",
    "online-mba-admission-deadline",
    "online-mba-admission-2027",
    "best-online-mba-in-india",
    "online-mba-universities-in-india",
    "online-mba-colleges",

    # Page 3: Curriculum, Programs & Rankings (9 articles: 19-27)
    "online-mba-programs",
    "online-mba-courses",
    "online-mba-degree",
    "online-mba-degree-in-india",
    "online-mba-course-in-india",
    "online-mba-universities",
    "best-online-mba-colleges",
    "best-online-mba-colleges-in-india",
    "best-online-mba-university",

    # Page 4: Regulations, Careers, Fees & ROI Guides (9 articles: 28-36)
    "best-online-mba-universities-in-india",
    "top-online-mba-colleges",
    "top-online-mba-colleges-in-india",
    "ugc-deb-approval-guide",
    "direct-admission-without-cat",
    "online-vs-distance-mba",
    "highest-paying-specializations",
    "no-cost-emi-guide",
    "is-online-mba-valid-govt-jobs",

    # Page 5: Requirements, Eligibility & Direct Enrollment (9 articles: 37-45, 3-3-3)
    "online-mba-admission-eligibility",
    "online-mba-admission-requirements",
    "online-mba-documents-required",
    "online-mba-direct-admission",
    "online-mba-admission-without-entrance",
    "online-mba-admission-without-cat",
    "online-mba-university-admission",
    "online-mba-college-admission",
    "online-mba-enrollment-2027",

    # Page 6: Application Form, Counselling & Fee Structure (9 articles: 46-54, 3-3-3)
    "online-mba-application-form",
    "online-mba-admission-form",
    "online-mba-counselling",
    "online-mba-admission-counselling",
    "online-mba-fees",
    "online-mba-fees-in-india",
    "online-mba-course-fees",
    "online-mba-fees-structure",
    "online-mba-semester-fees",

    # Page 7: Fees, Affordable & Low Fee Guides (9 articles: 55-63, 3-3-3)
    "online-mba-total-fees",
    "online-mba-fee-structure",
    "online-mba-admission-fees",
    "online-mba-affordable-fees",
    "affordable-online-mba",
    "affordable-online-mba-in-india",
    "low-fee-online-mba",
    "cheapest-online-mba-in-india",
    "cheap-online-mba",

    # Page 8: Budget Under 1 Lakh & Financial Aid Guides (9 articles: 64-72, 3-3-3)
    "online-mba-under-50000",
    "online-mba-under-75000",
    "online-mba-under-1-lakh",
    "online-mba-under-1-5-lakh",
    "online-mba-emi",
    "online-mba-fees-emi",
    "online-mba-education-loan",
    "online-mba-scholarship",
    "online-mba-scholarship-in-india",

    # Page 9: Statutory Duration, Academic Subjects & Exams (9 articles: 73-81, 3-3-3)
    "online-mba-eligibility",
    "online-mba-eligibility-criteria",
    "online-mba-qualification",
    "online-mba-duration",
    "online-mba-2-years",
    "online-mba-syllabus",
    "online-mba-subjects",
    "online-mba-exams",
    "how-long-is-online-mba",

    # Page 10: Executive Profiles, Operations & Application Guides (5 articles: 82-86)
    "who-can-do-online-mba",
    "who-is-eligible-for-online-mba",
    "how-to-do-online-mba",
    "how-to-apply-for-online-mba",
    "online-mba-assignments"
]

print(f"Total articles to index: {len(ORDERED_SLUGS)}")

# Extract metadata for each slug
ARTICLE_META = {}
for slug in ORDERED_SLUGS:
    path = os.path.join("blogs", f"{slug}.html")
    if not os.path.exists(path):
        raise Exception(f"File not found: {path}")
    
    with open(path, "r", encoding="utf-8") as fp:
        html = fp.read()

    # Title
    title_m = re.search(r'<h1[^>]*class="article-title"[^>]*>(.*?)</h1>', html, re.DOTALL)
    if not title_m:
        title_m = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    title = re.sub(r'<[^>]+>', '', title_m.group(1)).strip() if title_m else slug
    title = title.split('|')[0].strip()

    # Description
    desc_m = re.search(r'<meta name="description" content="(.*?)"', html)
    desc = desc_m.group(1).strip() if desc_m else ''

    # Badge
    badge_m = re.search(r'class="article-badge-category">(.*?)</span>', html)
    badge = badge_m.group(1).strip() if badge_m else 'Admissions'

    # Read Time
    read_m = re.search(r'(\d+\s*Min\s*Read)', html, re.IGNORECASE)
    read_time = read_m.group(1).strip() if read_m else '8 Min Read'

    # Highlight box text
    highlight_p = re.search(r'<div class="article-callout"[^>]*>.*?<p>(.*?)</p>', html, re.DOTALL)
    if highlight_p and len(re.sub(r'<[^>]+>', '', highlight_p.group(1)).strip()) > 20:
        hl_label = "Key Takeaway"
        hl_text = re.sub(r'<[^>]+>', '', highlight_p.group(1)).strip()
        if len(hl_text) > 120:
            hl_text = hl_text[:117] + "..."
    else:
        highlight_m = re.search(r'<div class="article-callout".*?<strong>(.*?)</strong>(.*?)</div>', html, re.DOTALL)
        if highlight_m and len(re.sub(r'<[^>]+>', '', highlight_m.group(2)).strip()) > 10:
            hl_label = re.sub(r'<[^>]+>', '', highlight_m.group(1)).replace(":", "").strip()
            hl_text = re.sub(r'<[^>]+>', '', highlight_m.group(2)).strip()
            if len(hl_text) > 120:
                hl_text = hl_text[:117] + "..."
        else:
            hl_label = "Key Highlight"
            hl_text = "100% legal equivalence with on-campus MBA under UGC Gazette 2020 Regulation 22."

    ARTICLE_META[slug] = {
        "slug": slug,
        "title": title,
        "desc": desc,
        "badge": badge,
        "read_time": read_time,
        "hl_label": hl_label,
        "hl_text": hl_text
    }

# Color styling for badges
BADGE_COLORS = {
    "Master Guide": "background:#e0f2f1; color:#00695c;",
    "Admission Guide": "background:#e0f2fe; color:#0369a1;",
    "2026 Admissions": "background:#ecfdf5; color:#047857;",
    "2027 Admissions": "background:#ede9fe; color:#6d28d9;",
    "Admissions Directory": "background:#fef3c7; color:#92400e;",
    "Application Guide": "background:#fff7ed; color:#c2410c;",
    "Enrollment Guide": "background:#e0f2f1; color:#00695c;",
    "Live Batches": "background:#fce4ec; color:#c2185b;",
    "Deadlines Tracker": "background:#fee2e2; color:#b91c1c;",
    "Deadline Alert": "background:#fee2e2; color:#b91c1c;",
    "Process Roadmap": "background:#e0f2f1; color:#00695c;",
    "University Rankings": "background:#e0f2fe; color:#0369a1;",
    "Pan-India Rankings": "background:#fce4ec; color:#c2185b;",
    "Higher Education": "background:#ede7f6; color:#512da8;",
    "Selection Framework": "background:#fff3e0; color:#e65100;",
    "Rankings & Reviews": "background:#e8f5e9; color:#2e7d32;",
    "National Directory": "background:#fef3c7; color:#92400e;",
    "College Directory": "background:#e1f5fe; color:#0277bd;",
    "Program Architecture": "background:#ede9fe; color:#6d28d9;",
    "Course Syllabus": "background:#ecfdf5; color:#047857;",
    "Degree Legitimacy": "background:#fdf2f8; color:#be185d;",
    "Statutory Authority": "background:#e0f2f1; color:#00695c;",
    "Student Handbook": "background:#fff7ed; color:#c2410c;",
    "University Directory": "background:#e0f7fa; color:#00838f;",
    "College Comparison": "background:#fce4ec; color:#c2185b;",
    "Evaluation Guide": "background:#e0f7fa; color:#00838f;",
    "University Matrix": "background:#f3e5f5; color:#7b1fa2;",
    "Career & ROI": "background:#e8f5e9; color:#1b5e20;",
    "Direct Admission": "background:#fffde7; color:#f57f17;",
    "UGC Verification": "background:#e0f2f1; color:#00695c;",
    "Distance Comparison": "background:#fbe9e7; color:#d84315;",
    "Salary Report": "background:#e8f5e9; color:#2e7d32;",
    "Education Loans": "background:#ede7f6; color:#512da8;",
    "Government Regulations": "background:#e0f2f1; color:#00695c;",
    "Eligibility Guide": "background:#e0f2fe; color:#0369a1;",
    "Requirements Guide": "background:#e0f2f1; color:#00695c;",
    "Documents Guide": "background:#fef3c7; color:#92400e;",
    "Non-Entrance Guide": "background:#ecfdf5; color:#047857;",
    "Non-CAT Admissions": "background:#fff7ed; color:#c2410c;",
    "University Admissions": "background:#e0f7fa; color:#00838f;",
    "College Admissions": "background:#e1f5fe; color:#0277bd;",
    "2027 Enrollment": "background:#ede9fe; color:#6d28d9;",
    "Application Form": "background:#fce4ec; color:#c2185b;",
    "Admission Form": "background:#fce4ec; color:#c2185b;",
    "Free Counselling": "background:#ede7f6; color:#512da8;",
    "Admission Guidance": "background:#e0f2fe; color:#0369a1;",
    "Fee Comparison": "background:#e8f5e9; color:#1b5e20;",
    "Pan-India Fees": "background:#fff3e0; color:#e65100;",
    "Course Fees": "background:#fef3c7; color:#92400e;",
    "Fee Structure": "background:#e0f2f1; color:#00695c;",
    "Semester Fees": "background:#ede9fe; color:#6d28d9;",
    "Total Fees": "background:#fbe9e7; color:#d84315;",
    "Fee Architecture": "background:#e0f7fa; color:#00838f;",
    "Admission Fees": "background:#e0f2fe; color:#0369a1;",
    "Affordable Fees": "background:#ecfdf5; color:#047857;",
    "Affordable MBA": "background:#e8f5e9; color:#1b5e20;",
    "Budget MBA India": "background:#fff3e0; color:#e65100;",
    "Low Fee MBA": "background:#ede7f6; color:#512da8;",
    "Lowest Cost India": "background:#fef3c7; color:#92400e;",
    "Budget Guide": "background:#fce4ec; color:#c2185b;",
    "Under ₹50,000": "background:#e0f2f1; color:#00695c;",
    "Under ₹75,000": "background:#ede9fe; color:#6d28d9;",
    "Under ₹1 Lakh": "background:#e8f5e9; color:#2e7d32;",
    "Under ₹1.5 Lakh": "background:#e0f2fe; color:#0369a1;",
    "0% EMI Plans": "background:#ecfdf5; color:#047857;",
    "Fees EMI": "background:#e8f5e9; color:#1b5e20;",
    "Scholarships": "background:#fef3c7; color:#92400e;",
    "India Scholarships": "background:#fff3e0; color:#e65100;",
    "Eligibility Criteria": "background:#e0f2f1; color:#00695c;",
    "Qualifications": "background:#fce4ec; color:#c2185b;",
    "Program Duration": "background:#ede9fe; color:#6d28d9;",
    "2-Year Degree": "background:#e0f2f1; color:#00695c;",
    "Syllabus & Curriculum": "background:#ecfdf5; color:#047857;",
    "MBA Subjects": "background:#ede9fe; color:#6d28d9;",
    "Examination Guide": "background:#fef3c7; color:#92400e;",
    "Program Length": "background:#e0f2fe; color:#0369a1;",
    "Who Can Enroll": "background:#fff3e0; color:#e65100;",
    "Eligibility Norms": "background:#e8f5e9; color:#1b5e20;",
    "Student Roadmap": "background:#fce4ec; color:#c2185b;",
    "Academic Assignments": "background:#f3e5f5; color:#7b1fa2;"
}

def render_card(slug):
    m = ARTICLE_META[slug]
    b_style = BADGE_COLORS.get(m["badge"], "background:#e0f2f1; color:#00695c;")
    return f"""          <article class="blog-card" id="article-{slug}">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="{b_style}">{m["badge"]}</span>
                <span>&bull; {m["read_time"]} &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/{slug}">{m["title"]}</a></h3>
              <p class="blog-card-excerpt">
                {m["desc"]}
              </p>
              <div class="blog-highlight-box">
                <strong>{m["hl_label"]}:</strong> {m["hl_text"]}
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Rajiv Sharma</span>
              <a href="/blogs/{slug}" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>\n"""

# Read template base from index.html
with open("blogs/index.html", "r", encoding="utf-8") as fp:
    index_html = fp.read()

# Extract parts from index.html
head_part = index_html[:index_html.find('<div class="blog-grid">') + len('<div class="blog-grid">\n')]
after_grid = index_html[index_html.find('<!-- Executive Blog Articles Pagination'):]
lead_form_part = after_grid[after_grid.find('\n\n    <!-- Lead Form Magnet -->'):]

TOTAL_ARTICLES = len(ORDERED_SLUGS) # 86
TOTAL_PAGES = 10

def get_page_url(page_num):
    if page_num == 1:
        return "/blogs"
    return f"/blogs/page-{page_num}"

# Helper to generate pagination bar
def render_pagination(current_page, start_idx, end_idx):
    prev_html = '<span class="blog-page-btn disabled" aria-disabled="true">&larr; Prev</span>' if current_page == 1 else f'<a href="{get_page_url(current_page - 1)}" class="blog-page-btn" aria-label="Go to Previous Page">&larr; Prev</a>'
    next_html = '<span class="blog-page-btn disabled" aria-disabled="true">Next &rarr;</span>' if current_page == TOTAL_PAGES else f'<a href="{get_page_url(current_page + 1)}" class="blog-page-btn" aria-label="Go to Next Page">Next &rarr;</a>'
    
    page_links = []
    for p in range(1, TOTAL_PAGES + 1):
        if p == current_page:
            page_links.append(f'<span class="blog-page-btn active" aria-current="page">{p}</span>')
        else:
            page_links.append(f'<a href="{get_page_url(p)}" class="blog-page-btn" aria-label="Go to Page {p}">{p}</a>')
    
    pages_str = "\n            ".join(page_links)
    
    return f"""        <!-- Executive Blog Articles Pagination ({end_idx - start_idx} per page) -->
        <div id="blog-pagination" class="blog-pagination-wrapper" aria-label="Blog Articles Pagination">
          <nav class="blog-pagination-nav" aria-label="Blog pages navigation">
            {prev_html}
            {pages_str}
            {next_html}
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing {start_idx + 1} &ndash; {end_idx} of {TOTAL_ARTICLES} expert articles (Page {current_page} of {TOTAL_PAGES})</div>
        </div>
      </div>
      </div>
    </section>"""

# Page slices definition: STRICT 3-3-3 sequence (9 per page on all full pages!)
PAGE_CONFIGS = [
    (1, 0, 9, "blogs/index.html", "Online MBA Admission Blogs and Guides 2026: Approvals, Fees and ROI", "https://www.onlinembaadmission.com/blogs"),
    (2, 9, 18, "blogs/page-2.html", "Online MBA Admission Blogs and Guides (Page 2) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-2"),
    (3, 18, 27, "blogs/page-3.html", "Online MBA Admission Blogs and Guides (Page 3) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-3"),
    (4, 27, 36, "blogs/page-4.html", "Online MBA Admission Blogs and Guides (Page 4) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-4"),
    (5, 36, 45, "blogs/page-5.html", "Online MBA Admission Blogs and Guides (Page 5) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-5"),
    (6, 45, 54, "blogs/page-6.html", "Online MBA Admission Blogs and Guides (Page 6) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-6"),
    (7, 54, 63, "blogs/page-7.html", "Online MBA Admission Blogs and Guides (Page 7) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-7"),
    (8, 63, 72, "blogs/page-8.html", "Online MBA Admission Blogs and Guides (Page 8) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-8"),
    (9, 72, 81, "blogs/page-9.html", "Online MBA Admission Blogs and Guides (Page 9) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-9"),
    (10, 81, 86, "blogs/page-10.html", "Online MBA Admission Blogs and Guides (Page 10) | Online MBA Admission", "https://www.onlinembaadmission.com/blogs/page-10"),
]

for p_num, s_idx, e_idx, filepath, title_text, canonical_url in PAGE_CONFIGS:
    p_slugs = ORDERED_SLUGS[s_idx:e_idx]
    p_cards = "\n".join([render_card(s) for s in p_slugs])
    p_pagination = render_pagination(p_num, s_idx, e_idx)
    
    # Custom head replacement for title and canonical
    custom_head = head_part
    # Replace title
    custom_head = re.sub(r'<title>.*?</title>', f'<title>{title_text}</title>', custom_head, count=1)
    # Replace canonical
    custom_head = re.sub(r'<link rel="canonical" href=".*?"', f'<link rel="canonical" href="{canonical_url}"', custom_head, count=1)
    
    p_content = custom_head + p_cards + "\n        </div>\n\n" + p_pagination + lead_form_part
    
    with open(filepath, "w", encoding="utf-8") as fp:
        fp.write(p_content)
    print(f"Updated: {filepath} (Page {p_num}: {len(p_slugs)} articles [3-3-3 sequence], pagination {p_num} of {TOTAL_PAGES})")

# -------------------------------------------------------------
# UPDATE sitemap.xml
# -------------------------------------------------------------
with open("sitemap.xml", "r", encoding="utf-8") as fp:
    sitemap_xml = fp.read()

# Build all blog XML nodes
blog_xml_nodes = """
  <!-- Online MBA Blogs & Comprehensive Regulatory Guides -->
  <url>
    <loc>https://www.onlinembaadmission.com/blogs</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.90</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-2</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-3</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-4</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-5</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-6</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-7</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-8</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-9</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-10</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
"""

for slug in ORDERED_SLUGS:
    blog_xml_nodes += f"""  <url>
    <loc>https://www.onlinembaadmission.com/blogs/{slug}</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>\n"""

# Remove any existing /blogs nodes from sitemap
sitemap_xml = re.sub(
    r'\s*<!-- Online MBA Blogs & Comprehensive Regulatory Guides -->.*?<url>\s*<loc>https://www\.onlinembaadmission\.com/blogs/[a-z0-9\-]+</loc>.*?</url>',
    "",
    sitemap_xml,
    flags=re.DOTALL
)

# Remove any stray /blogs nodes
sitemap_xml = re.sub(
    r'\s*<url>\s*<loc>https://www\.onlinembaadmission\.com/blogs(?:/[a-z0-9\-]+)?</loc>.*?</url>',
    "",
    sitemap_xml,
    flags=re.DOTALL
)

# Insert after /terms node
terms_pattern = r'(<url>\s*<loc>https://www\.onlinembaadmission\.com/terms</loc>.*?</url>)'
sitemap_xml = re.sub(terms_pattern, r'\1' + blog_xml_nodes, sitemap_xml, count=1, flags=re.DOTALL)

with open("sitemap.xml", "w", encoding="utf-8") as fp:
    fp.write(sitemap_xml)

# Validate sitemap XML structure
try:
    tree = ET.fromstring(sitemap_xml)
    urls = tree.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url')
    print(f"SUCCESS: sitemap.xml is valid! Total URLs: {len(urls)} (expected 372: 276 core/universities/specializations + 86 blogs + 10 pagination)")
except Exception as e:
    print(f"ERROR validating sitemap XML: {e}")
