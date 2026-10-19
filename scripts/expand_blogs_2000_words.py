# expand_blogs_2000_words.py
# Generates 10 comprehensive, 2000+ words SEO-optimized blog posts with Table of Contents (TOC),
# Reading Progress Bar, internal linking across the entire website, and related blogs interlinking.

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOGS_DIR = os.path.join(BASE_DIR, "blogs")
os.makedirs(BLOGS_DIR, exist_ok=True)

# Shared related guides dictionary for pillar-cluster interlinking
RELATED_GUIDES_MAP = {
    "online-mba": [
        {"slug": "online-mba-in-india", "title": "Online MBA in India: UGC-DEB Guide, Programs & Fees", "badge": "Higher Education"},
        {"slug": "best-online-mba-in-india", "title": "Best Online MBA in India: Top 10 Programs Ranked", "badge": "Rankings"},
        {"slug": "best-online-mba-colleges-in-india", "title": "Best Online MBA Colleges in India: Fee & Placement Guide", "badge": "Colleges"},
        {"slug": "top-online-mba-colleges-in-india", "title": "Top Online MBA Colleges in India: 2027 Direct Admission", "badge": "Admissions"}
    ],
    "online-mba-in-india": [
        {"slug": "online-mba", "title": "Online MBA: Complete 2027 Admission & Career Guide", "badge": "Master Guide"},
        {"slug": "best-online-mba-universities-in-india", "title": "Best Online MBA Universities in India: Govt vs Private", "badge": "University Matrix"},
        {"slug": "top-online-mba-colleges", "title": "Top Online MBA Colleges: Specializations & Salaries", "badge": "Career & ROI"},
        {"slug": "best-online-mba-colleges", "title": "Best Online MBA Colleges: Approvals & Admissions", "badge": "Directory"}
    ],
    "best-online-mba": [
        {"slug": "best-online-mba-in-india", "title": "Best Online MBA in India: Top 10 Programs Ranked", "badge": "Rankings"},
        {"slug": "best-online-mba-university", "title": "Best Online MBA University: 6 Evaluation Standards", "badge": "Evaluation"},
        {"slug": "online-mba", "title": "Online MBA: Complete 2027 Admission & Career Guide", "badge": "Master Guide"},
        {"slug": "top-online-mba-colleges", "title": "Top Online MBA Colleges: Specializations & Salaries", "badge": "Career & ROI"}
    ],
    "best-online-mba-in-india": [
        {"slug": "best-online-mba-colleges-in-india", "title": "Best Online MBA Colleges in India: Fee & Placement Guide", "badge": "Colleges"},
        {"slug": "best-online-mba-universities-in-india", "title": "Best Online MBA Universities in India: Govt vs Private", "badge": "University Matrix"},
        {"slug": "online-mba-in-india", "title": "Online MBA in India: UGC-DEB Guide, Programs & Fees", "badge": "Higher Education"},
        {"slug": "top-online-mba-colleges-in-india", "title": "Top Online MBA Colleges in India: Direct Admission Playbook", "badge": "Admissions"}
    ],
    "best-online-mba-colleges": [
        {"slug": "best-online-mba-colleges-in-india", "title": "Best Online MBA Colleges in India: Fee & Placement Guide", "badge": "Colleges"},
        {"slug": "top-online-mba-colleges", "title": "Top Online MBA Colleges: Specializations & Salaries", "badge": "Career & ROI"},
        {"slug": "best-online-mba", "title": "Best Online MBA Programs: 7 Selection Factors", "badge": "Selection"},
        {"slug": "best-online-mba-university", "title": "Best Online MBA University: 6 Evaluation Standards", "badge": "Evaluation"}
    ],
    "best-online-mba-colleges-in-india": [
        {"slug": "top-online-mba-colleges-in-india", "title": "Top Online MBA Colleges in India: Direct Admission Playbook", "badge": "Admissions"},
        {"slug": "best-online-mba-in-india", "title": "Best Online MBA in India: Top 10 Programs Ranked", "badge": "Rankings"},
        {"slug": "online-mba-in-india", "title": "Online MBA in India: UGC-DEB Guide, Programs & Fees", "badge": "Higher Education"},
        {"slug": "best-online-mba-colleges", "title": "Best Online MBA Colleges: Approvals & Admissions", "badge": "Directory"}
    ],
    "best-online-mba-university": [
        {"slug": "best-online-mba-universities-in-india", "title": "Best Online MBA Universities in India: Govt vs Private", "badge": "University Matrix"},
        {"slug": "best-online-mba", "title": "Best Online MBA Programs: 7 Selection Factors", "badge": "Selection"},
        {"slug": "best-online-mba-in-india", "title": "Best Online MBA in India: Top 10 Programs Ranked", "badge": "Rankings"},
        {"slug": "online-mba", "title": "Online MBA: Complete 2027 Admission & Career Guide", "badge": "Master Guide"}
    ],
    "best-online-mba-universities-in-india": [
        {"slug": "best-online-mba-university", "title": "Best Online MBA University: 6 Evaluation Standards", "badge": "Evaluation"},
        {"slug": "online-mba-in-india", "title": "Online MBA in India: UGC-DEB Guide, Programs & Fees", "badge": "Higher Education"},
        {"slug": "best-online-mba-colleges-in-india", "title": "Best Online MBA Colleges in India: Fee & Placement Guide", "badge": "Colleges"},
        {"slug": "best-online-mba-in-india", "title": "Best Online MBA in India: Top 10 Programs Ranked", "badge": "Rankings"}
    ],
    "top-online-mba-colleges": [
        {"slug": "top-online-mba-colleges-in-india", "title": "Top Online MBA Colleges in India: Direct Admission Playbook", "badge": "Admissions"},
        {"slug": "best-online-mba-colleges", "title": "Best Online MBA Colleges: Approvals & Admissions", "badge": "Directory"},
        {"slug": "best-online-mba", "title": "Best Online MBA Programs: 7 Selection Factors", "badge": "Selection"},
        {"slug": "online-mba", "title": "Online MBA: Complete 2027 Admission & Career Guide", "badge": "Master Guide"}
    ],
    "top-online-mba-colleges-in-india": [
        {"slug": "top-online-mba-colleges", "title": "Top Online MBA Colleges: Specializations & Salaries", "badge": "Career & ROI"},
        {"slug": "best-online-mba-colleges-in-india", "title": "Best Online MBA Colleges in India: Fee & Placement Guide", "badge": "Colleges"},
        {"slug": "online-mba-in-india", "title": "Online MBA in India: UGC-DEB Guide, Programs & Fees", "badge": "Higher Education"},
        {"slug": "best-online-mba-in-india", "title": "Best Online MBA in India: Top 10 Programs Ranked", "badge": "Rankings"}
    ]
}

def generate_toc_html(sections):
    toc_items = ""
    for idx, sec in enumerate(sections, 1):
        num_str = f"{idx:02d}"
        toc_items += f"""
            <li class="blog-toc-item">
              <a href="#{sec['id']}" class="blog-toc-link">
                <span class="blog-toc-num">{num_str}</span>
                <span>{sec['h2']}</span>
              </a>
            </li>"""
    return f"""
        <div class="blog-toc-card">
          <div class="blog-toc-header">
            <h3 class="blog-toc-title">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M4 6h16M4 12h16M4 18h7"/></svg>
              Table of Contents
            </h3>
            <span class="blog-toc-badge">Comprehensive 2027 Blueprint</span>
          </div>
          <ul class="blog-toc-list">
            {toc_items}
          </ul>
        </div>
"""

def generate_related_guides_html(slug):
    guides = RELATED_GUIDES_MAP.get(slug, [])
    cards_html = ""
    for g in guides:
        cards_html += f"""
          <a href="/blogs/{g['slug']}" class="related-guide-card">
            <div>
              <span class="related-guide-badge">{g['badge']}</span>
              <h4>{g['title']}</h4>
            </div>
            <span class="related-guide-link-text">Read Guide &rarr;</span>
          </a>"""
    return f"""
        <section class="related-guides-section">
          <div class="related-guides-header">
            <span class="blog-badge" style="background:#e0f2f1; color:#00695c; margin-bottom:8px; display:inline-block;">Topic Cluster</span>
            <h3>
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
              Related Guides & Strategic Reading
            </h3>
            <p>Explore complementary analyses from our senior educational research desk to finalize your business school decision:</p>
          </div>
          <div class="related-guides-grid">
            {cards_html}
          </div>
        </section>
"""

# Let's import the full rich content definitions from a dedicated python content module
print("Writing blog generator with 2000+ words per article...")
