"""
Script: scripts/build_blog_index_and_sitemap.py
1. Collects all 36 articles in blogs/*.html
2. Rebuilds blogs/index.html (Page 1: Articles 1-9)
3. Rebuilds blogs/page-2.html (Page 2: Articles 10-18)
4. Rebuilds blogs/page-3.html (Page 3: Articles 19-27)
5. Creates blogs/page-4.html (Page 4: Articles 28-36)
6. Updates sitemap.xml with all 36 articles and 4 pagination pages (total 40 blog URLs)
"""

import os
import re
import xml.etree.ElementTree as ET

# Ordered list of all 36 articles
ORDERED_SLUGS = [
    # Page 1: Top Core Pillar & Admission Blueprints (9 articles)
    "online-mba",
    "online-mba-admission",
    "online-mba-admission-2026",
    "online-mba-admission-open",
    "top-online-mba-universities-in-india",
    "online-mba-colleges-in-india",
    "best-online-mba",
    "online-mba-admission-process",
    "online-mba-in-india",

    # Page 2: Application, Enrollment & Degree Guides (9 articles)
    "online-mba-application",
    "online-mba-enrollment",
    "online-mba-admissions",
    "online-mba-admission-last-date",
    "online-mba-admission-deadline",
    "online-mba-admission-2027",
    "best-online-mba-in-india",
    "online-mba-universities-in-india",
    "online-mba-colleges",

    # Page 3: Curriculum, Programs & Rankings (9 articles)
    "online-mba-programs",
    "online-mba-courses",
    "online-mba-degree",
    "online-mba-degree-in-india",
    "online-mba-course-in-india",
    "online-mba-universities",
    "best-online-mba-colleges",
    "best-online-mba-colleges-in-india",
    "best-online-mba-university",

    # Page 4: Regulations, Careers, Fees & ROI Guides (9 articles)
    "best-online-mba-universities-in-india",
    "top-online-mba-colleges",
    "top-online-mba-colleges-in-india",
    "ugc-deb-approval-guide",
    "direct-admission-without-cat",
    "online-vs-distance-mba",
    "highest-paying-specializations",
    "no-cost-emi-guide",
    "is-online-mba-valid-govt-jobs"
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
    highlight_m = re.search(r'<div class="article-callout".*?<strong>(.*?)</strong>(.*?)</div>', html, re.DOTALL)
    if highlight_m:
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
    "Government Regulations": "background:#e0f2f1; color:#00695c;"
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

# -------------------------------------------------------------
# 1. BUILD blogs/index.html (Page 1: items 0-9)
# -------------------------------------------------------------
p1_slugs = ORDERED_SLUGS[0:9]
p1_cards = "\n".join([render_card(s) for s in p1_slugs])

p1_pagination = """        <!-- Executive Blog Articles Pagination (9 per page) -->
        <div id="blog-pagination" class="blog-pagination-wrapper" aria-label="Blog Articles Pagination">
          <nav class="blog-pagination-nav" aria-label="Blog pages navigation">
            <span class="blog-page-btn disabled" aria-disabled="true">&larr; Prev</span>
            <span class="blog-page-btn active" aria-current="page">1</span>
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Page 2">2</a>
            <a href="/blogs/page-3" class="blog-page-btn" aria-label="Go to Page 3">3</a>
            <a href="/blogs/page-4" class="blog-page-btn" aria-label="Go to Page 4">4</a>
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Next Page">Next &rarr;</a>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 1 &ndash; 9 of 36 expert articles (Page 1 of 4)</div>
        </div>
      </div>
      </div>
    </section>"""

p1_content = head_part + p1_cards + "\n        </div>\n\n" + p1_pagination + lead_form_part

with open("blogs/index.html", "w", encoding="utf-8") as fp:
    fp.write(p1_content)
print("Updated: blogs/index.html (Page 1: 9 articles, pagination 1 of 4)")

# -------------------------------------------------------------
# 2. BUILD blogs/page-2.html (Page 2: items 9-18)
# -------------------------------------------------------------
p2_slugs = ORDERED_SLUGS[9:18]
p2_cards = "\n".join([render_card(s) for s in p2_slugs])

p2_pagination = """        <!-- Executive Blog Articles Pagination (9 per page) -->
        <div id="blog-pagination" class="blog-pagination-wrapper" aria-label="Blog Articles Pagination">
          <nav class="blog-pagination-nav" aria-label="Blog pages navigation">
            <a href="/blogs" class="blog-page-btn" aria-label="Go to Previous Page">&larr; Prev</a>
            <a href="/blogs" class="blog-page-btn" aria-label="Go to Page 1">1</a>
            <span class="blog-page-btn active" aria-current="page">2</span>
            <a href="/blogs/page-3" class="blog-page-btn" aria-label="Go to Page 3">3</a>
            <a href="/blogs/page-4" class="blog-page-btn" aria-label="Go to Page 4">4</a>
            <a href="/blogs/page-3" class="blog-page-btn" aria-label="Go to Next Page">Next &rarr;</a>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 10 &ndash; 18 of 36 expert articles (Page 2 of 4)</div>
        </div>
      </div>
      </div>
    </section>"""

p2_head = head_part.replace(
    '<title>Online MBA Admission Blogs and Guides 2026: Approvals, Fees and ROI</title>',
    '<title>Online MBA Admission Blogs and Guides (Page 2) | Online MBA Admission</title>'
).replace(
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs">',
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs/page-2">'
)

p2_content = p2_head + p2_cards + "\n        </div>\n\n" + p2_pagination + lead_form_part

with open("blogs/page-2.html", "w", encoding="utf-8") as fp:
    fp.write(p2_content)
print("Updated: blogs/page-2.html (Page 2: 9 articles, pagination 2 of 4)")

# -------------------------------------------------------------
# 3. BUILD blogs/page-3.html (Page 3: items 18-27)
# -------------------------------------------------------------
p3_slugs = ORDERED_SLUGS[18:27]
p3_cards = "\n".join([render_card(s) for s in p3_slugs])

p3_pagination = """        <!-- Executive Blog Articles Pagination (9 per page) -->
        <div id="blog-pagination" class="blog-pagination-wrapper" aria-label="Blog Articles Pagination">
          <nav class="blog-pagination-nav" aria-label="Blog pages navigation">
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Previous Page">&larr; Prev</a>
            <a href="/blogs" class="blog-page-btn" aria-label="Go to Page 1">1</a>
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Page 2">2</a>
            <span class="blog-page-btn active" aria-current="page">3</span>
            <a href="/blogs/page-4" class="blog-page-btn" aria-label="Go to Page 4">4</a>
            <a href="/blogs/page-4" class="blog-page-btn" aria-label="Go to Next Page">Next &rarr;</a>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 19 &ndash; 27 of 36 expert articles (Page 3 of 4)</div>
        </div>
      </div>
      </div>
    </section>"""

p3_head = head_part.replace(
    '<title>Online MBA Admission Blogs and Guides 2026: Approvals, Fees and ROI</title>',
    '<title>Online MBA Admission Blogs and Guides (Page 3) | Online MBA Admission</title>'
).replace(
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs">',
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs/page-3">'
)

p3_content = p3_head + p3_cards + "\n        </div>\n\n" + p3_pagination + lead_form_part

with open("blogs/page-3.html", "w", encoding="utf-8") as fp:
    fp.write(p3_content)
print("Updated: blogs/page-3.html (Page 3: 9 articles, pagination 3 of 4)")

# -------------------------------------------------------------
# 4. BUILD blogs/page-4.html (Page 4: items 27-36)
# -------------------------------------------------------------
p4_slugs = ORDERED_SLUGS[27:36]
p4_cards = "\n".join([render_card(s) for s in p4_slugs])

p4_pagination = """        <!-- Executive Blog Articles Pagination (9 per page) -->
        <div id="blog-pagination" class="blog-pagination-wrapper" aria-label="Blog Articles Pagination">
          <nav class="blog-pagination-nav" aria-label="Blog pages navigation">
            <a href="/blogs/page-3" class="blog-page-btn" aria-label="Go to Previous Page">&larr; Prev</a>
            <a href="/blogs" class="blog-page-btn" aria-label="Go to Page 1">1</a>
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Page 2">2</a>
            <a href="/blogs/page-3" class="blog-page-btn" aria-label="Go to Page 3">3</a>
            <span class="blog-page-btn active" aria-current="page">4</span>
            <span class="blog-page-btn disabled" aria-disabled="true">Next &rarr;</span>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 28 &ndash; 36 of 36 expert articles (Page 4 of 4)</div>
        </div>
      </div>
      </div>
    </section>"""

p4_head = head_part.replace(
    '<title>Online MBA Admission Blogs and Guides 2026: Approvals, Fees and ROI</title>',
    '<title>Online MBA Admission Blogs and Guides (Page 4) | Online MBA Admission</title>'
).replace(
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs">',
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs/page-4">'
)

p4_content = p4_head + p4_cards + "\n        </div>\n\n" + p4_pagination + lead_form_part

with open("blogs/page-4.html", "w", encoding="utf-8") as fp:
    fp.write(p4_content)
print("Created: blogs/page-4.html (Page 4: 9 articles, pagination 4 of 4)")

# -------------------------------------------------------------
# 5. UPDATE sitemap.xml
# -------------------------------------------------------------
with open("sitemap.xml", "r", encoding="utf-8") as fp:
    sitemap_xml = fp.read()

# Build all blog XML nodes
blog_xml_nodes = """
  <!-- Online MBA Blogs & Comprehensive Regulatory Guides -->
  <url>
    <loc>https://www.onlinembaadmission.com/blogs</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.90</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-2</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-3</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
  <url>
    <loc>https://www.onlinembaadmission.com/blogs/page-4</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.70</priority>
  </url>
"""

for slug in ORDERED_SLUGS:
    blog_xml_nodes += f"""  <url>
    <loc>https://www.onlinembaadmission.com/blogs/{slug}</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>\n"""

# Remove any existing /blogs nodes from sitemap
sitemap_xml = re.sub(
    r'\s*<!-- Online MBA Blogs & Comprehensive Regulatory Guides -->.*?<url>\s*<loc>https://www\.onlinembaadmission\.com/blogs/is-online-mba-valid-govt-jobs</loc>.*?</url>',
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
    print(f"SUCCESS: sitemap.xml is valid! Total URLs: {len(urls)} (expected ~315)")
except Exception as e:
    print(f"ERROR validating sitemap XML: {e}")
