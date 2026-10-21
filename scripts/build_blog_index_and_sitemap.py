"""
Script: scripts/build_blog_index_and_sitemap.py
1. Collects all 26 articles in blogs/*.html
2. Rebuilds blogs/index.html (Page 1: Articles 1-9)
3. Rebuilds blogs/page-2.html (Page 2: Articles 10-18)
4. Creates blogs/page-3.html (Page 3: Articles 19-26)
5. Updates sitemap.xml with all 26 articles and pagination pages
"""

import os
import re
import glob

# Ordered list of all 26 articles
ORDERED_SLUGS = [
    # Page 1: Top Core Pillar & Master Guides (9 articles)
    "online-mba",
    "top-online-mba-universities-in-india",
    "online-mba-colleges-in-india",
    "online-mba-in-india",
    "best-online-mba",
    "best-online-mba-in-india",
    "online-mba-universities-in-india",
    "online-mba-colleges",
    "online-mba-programs",

    # Page 2: Specialized Pillars & College/University Guides (9 articles)
    "online-mba-courses",
    "online-mba-degree",
    "online-mba-degree-in-india",
    "online-mba-course-in-india",
    "online-mba-universities",
    "best-online-mba-colleges",
    "best-online-mba-colleges-in-india",
    "best-online-mba-university",
    "best-online-mba-universities-in-india",

    # Page 3: Specialized Regulations, Careers & Finance Guides (8 articles)
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
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Next Page">Next &rarr;</a>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 1 &ndash; 9 of 26 expert articles (Page 1 of 3)</div>
        </div>
      </div>
      </div>
    </section>"""

p1_content = head_part + p1_cards + "\n        </div>\n\n" + p1_pagination + after_grid[after_grid.find('\n\n    <!-- Lead Form Magnet -->'):]

with open("blogs/index.html", "w", encoding="utf-8") as fp:
    fp.write(p1_content)
print("Updated: blogs/index.html (Page 1: 9 articles, pagination 1 of 3)")

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
            <a href="/blogs/page-3" class="blog-page-btn" aria-label="Go to Next Page">Next &rarr;</a>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 10 &ndash; 18 of 26 expert articles (Page 2 of 3)</div>
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

p2_content = p2_head + p2_cards + "\n        </div>\n\n" + p2_pagination + after_grid[after_grid.find('\n\n    <!-- Lead Form Magnet -->'):]

with open("blogs/page-2.html", "w", encoding="utf-8") as fp:
    fp.write(p2_content)
print("Updated: blogs/page-2.html (Page 2: 9 articles, pagination 2 of 3)")

# -------------------------------------------------------------
# 3. BUILD blogs/page-3.html (Page 3: items 18-26)
# -------------------------------------------------------------
p3_slugs = ORDERED_SLUGS[18:26]
p3_cards = "\n".join([render_card(s) for s in p3_slugs])

p3_pagination = """        <!-- Executive Blog Articles Pagination (9 per page) -->
        <div id="blog-pagination" class="blog-pagination-wrapper" aria-label="Blog Articles Pagination">
          <nav class="blog-pagination-nav" aria-label="Blog pages navigation">
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Previous Page">&larr; Prev</a>
            <a href="/blogs" class="blog-page-btn" aria-label="Go to Page 1">1</a>
            <a href="/blogs/page-2" class="blog-page-btn" aria-label="Go to Page 2">2</a>
            <span class="blog-page-btn active" aria-current="page">3</span>
            <span class="blog-page-btn disabled" aria-disabled="true">Next &rarr;</span>
          </nav>
          <div class="blog-pagination-info" id="blog-pagination-info">Showing 19 &ndash; 26 of 26 expert articles (Page 3 of 3)</div>
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

p3_content = p3_head + p3_cards + "\n        </div>\n\n" + p3_pagination + after_grid[after_grid.find('\n\n    <!-- Lead Form Magnet -->'):]

with open("blogs/page-3.html", "w", encoding="utf-8") as fp:
    fp.write(p3_content)
print("Created: blogs/page-3.html (Page 3: 8 articles, pagination 3 of 3)")

# -------------------------------------------------------------
# 4. UPDATE sitemap.xml
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
"""

for slug in ORDERED_SLUGS:
    blog_xml_nodes += f"""  <url>
    <loc>https://www.onlinembaadmission.com/blogs/{slug}</loc>
    <lastmod>2026-10-21</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.80</priority>
  </url>\n"""

# Remove old blogs from sitemap
sitemap_xml = re.sub(
    r'\s*<url>\s*<loc>https://www\.onlinembaadmission\.com/blogs/ugc-deb-approval-guide</loc>.*?</url>\s*<url>\s*<loc>https://www\.onlinembaadmission\.com/blogs/no-cost-emi-guide</loc>.*?</url>',
    "",
    sitemap_xml,
    flags=re.DOTALL
)

# Remove old /blogs node
sitemap_xml = re.sub(
    r'\s*<url>\s*<loc>https://www\.onlinembaadmission\.com/blogs</loc>.*?</url>',
    "",
    sitemap_xml,
    flags=re.DOTALL
)

# Insert after /terms node
terms_pattern = r'(<url>\s*<loc>https://www\.onlinembaadmission\.com/terms</loc>.*?</url>)'
sitemap_xml = re.sub(terms_pattern, r'\1' + blog_xml_nodes, sitemap_xml, count=1, flags=re.DOTALL)

with open("sitemap.xml", "w", encoding="utf-8") as fp:
    fp.write(sitemap_xml)

print("Updated: sitemap.xml with all 26 blogs + pagination routes!")
