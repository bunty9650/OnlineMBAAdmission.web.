# update_blogs_listing.py
import re
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEW_SCHEMA_POSTS = [
    {
        "@type": "BlogPosting",
        "headline": "Online MBA: The Complete 2027 Admission & Career Guide",
        "url": "https://www.onlinembaadmission.com/blogs/online-mba"
    },
    {
        "@type": "BlogPosting",
        "headline": "Online MBA in India: Complete UGC-DEB Guide, Programs & Fees",
        "url": "https://www.onlinembaadmission.com/blogs/online-mba-in-india"
    },
    {
        "@type": "BlogPosting",
        "headline": "Best Online MBA Programs: How to Choose the Right Degree in 2027",
        "url": "https://www.onlinembaadmission.com/blogs/best-online-mba"
    },
    {
        "@type": "BlogPosting",
        "headline": "Best Online MBA in India: Top 10 Programs, Rankings & Fees 2027",
        "url": "https://www.onlinembaadmission.com/blogs/best-online-mba-in-india"
    },
    {
        "@type": "BlogPosting",
        "headline": "Best Online MBA Colleges: Approvals, Specializations & Admissions",
        "url": "https://www.onlinembaadmission.com/blogs/best-online-mba-colleges"
    },
    {
        "@type": "BlogPosting",
        "headline": "Best Online MBA Colleges in India: Comprehensive Fee & Ranking Guide",
        "url": "https://www.onlinembaadmission.com/blogs/best-online-mba-colleges-in-india"
    },
    {
        "@type": "BlogPosting",
        "headline": "Best Online MBA University: 6 Standards to Evaluate Top Universities",
        "url": "https://www.onlinembaadmission.com/blogs/best-online-mba-university"
    },
    {
        "@type": "BlogPosting",
        "headline": "Best Online MBA Universities in India: Central, State & Private Ranked",
        "url": "https://www.onlinembaadmission.com/blogs/best-online-mba-universities-in-india"
    },
    {
        "@type": "BlogPosting",
        "headline": "Top Online MBA Colleges: Specializations, Career Scope & ROI",
        "url": "https://www.onlinembaadmission.com/blogs/top-online-mba-colleges"
    },
    {
        "@type": "BlogPosting",
        "headline": "Top Online MBA Colleges in India: 2027 Direct Admission Playbook",
        "url": "https://www.onlinembaadmission.com/blogs/top-online-mba-colleges-in-india"
    }
]

NEW_CARDS_HTML = """
          <!-- 1. Online MBA -->
          <article class="blog-card" id="article-online-mba">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2f1; color:#00695c;">Master Guide</span>
                <span>&bull; 8 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba">Online MBA: The Complete 2027 Admission & Career Guide</a></h3>
              <p class="blog-card-excerpt">
                Master the essentials of an Online MBA. Explore UGC-DEB approvals, LMS digital learning, syllabus, fees, direct admissions, and corporate career scope in India.
              </p>
              <div class="blog-highlight-box">
                <strong>Core Fact:</strong> 100% legal equivalence with on-campus MBA under UGC Gazette 2020 Regulation 22.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/online-mba" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 2. Online MBA in India -->
          <article class="blog-card" id="article-online-mba-in-india">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#ede7f6; color:#512da8;">Higher Education</span>
                <span>&bull; 8 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-in-india">Online MBA in India: Complete UGC-DEB Guide, Programs & Fees</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive overview of Online MBA in India. Compare UGC-DEB approved public & private programs, fee structures from ₹50k to ₹2.5L, and corporate hiring trends.
              </p>
              <div class="blog-highlight-box">
                <strong>Fee Span:</strong> ₹47,000 (Central Govt) to ₹1,99,000 (Top Private) with 0% No-Cost EMI.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/online-mba-in-india" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 3. Best Online MBA -->
          <article class="blog-card" id="article-best-online-mba">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fff3e0; color:#e65100;">Selection Framework</span>
                <span>&bull; 7 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/best-online-mba">Best Online MBA Programs: How to Choose the Right Degree in 2027</a></h3>
              <p class="blog-card-excerpt">
                Discover how to choose the best Online MBA program. Evaluate UGC-DEB credentials, NAAC grading, LMS interface, elective flexibility, and true placement ROI.
              </p>
              <div class="blog-highlight-box">
                <strong>7-Pillar Check:</strong> Institutional accreditation, live faculty hours, Harvard cases, and corporate tie-ups.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/best-online-mba" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 4. Best Online MBA in India -->
          <article class="blog-card" id="article-best-online-mba-in-india">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e8f5e9; color:#2e7d32;">Rankings & Reviews</span>
                <span>&bull; 9 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/best-online-mba-in-india">Best Online MBA in India: Top 10 Programs, Rankings & Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Compare the best Online MBA in India for working executives. In-depth review of Manipal, Amity, Jain, DPU, and IGNOU with fees, approvals, and career ROI.
              </p>
              <div class="blog-highlight-box">
                <strong>Top Ranked:</strong> Manipal Jaipur, Amity Online, Jain Online, and DPU Online evaluated.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/best-online-mba-in-india" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 5. Best Online MBA Colleges -->
          <article class="blog-card" id="article-best-online-mba-colleges">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e1f5fe; color:#0277bd;">College Directory</span>
                <span>&bull; 8 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/best-online-mba-colleges">Best Online MBA Colleges: Approvals, Specializations & Admissions</a></h3>
              <p class="blog-card-excerpt">
                Explore the best Online MBA colleges. Learn about statutory UGC-DEB approvals, NAAC ratings, entrance test waivers, course specializations, and fee terms.
              </p>
              <div class="blog-highlight-box">
                <strong>Direct Entry:</strong> 50% graduation score criteria with non-CAT direct merit admissions.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/best-online-mba-colleges" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 6. Best Online MBA Colleges in India -->
          <article class="blog-card" id="article-best-online-mba-colleges-in-india">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fce4ec; color:#c2185b;">College Comparison</span>
                <span>&bull; 8 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/best-online-mba-colleges-in-india">Best Online MBA Colleges in India: Comprehensive Fee & Ranking Guide</a></h3>
              <p class="blog-card-excerpt">
                Research the best Online MBA colleges in India. Comprehensive breakdown of NAAC A++ colleges, semester fees, zero-cost EMI plans, and placement records.
              </p>
              <div class="blog-highlight-box">
                <strong>Placements:</strong> Amazon, Deloitte, Infosys, and HDFC hiring graduates at ₹7 to ₹15 LPA.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/best-online-mba-colleges-in-india" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 7. Best Online MBA University -->
          <article class="blog-card" id="article-best-online-mba-university">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f7fa; color:#00838f;">Evaluation Guide</span>
                <span>&bull; 7 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/best-online-mba-university">Best Online MBA University: 6 Standards to Evaluate Top Universities</a></h3>
              <p class="blog-card-excerpt">
                Uncover the benchmarks of the best Online MBA university. Learn how to verify UGC-DEB entitlement, Category-1 status, LMS quality, and curriculum relevance.
              </p>
              <div class="blog-highlight-box">
                <strong>Verification:</strong> Step-by-step entitlement checking on deb.ugc.ac.in government portal.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/best-online-mba-university" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 8. Best Online MBA Universities in India -->
          <article class="blog-card" id="article-best-online-mba-universities-in-india">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#f3e5f5; color:#7b1fa2;">University Matrix</span>
                <span>&bull; 9 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/best-online-mba-universities-in-india">Best Online MBA Universities in India: Central, State & Private Ranked</a></h3>
              <p class="blog-card-excerpt">
                Compare the best Online MBA universities in India. Complete analysis of NAAC A++ central, state, and private institutions, fees, and UGC equivalence.
              </p>
              <div class="blog-highlight-box">
                <strong>Categories:</strong> Central (IGNOU), State (CCSU, Andhra) & Private Autonomous (Manipal, Amity).
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/best-online-mba-universities-in-india" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 9. Top Online MBA Colleges -->
          <article class="blog-card" id="article-top-online-mba-colleges">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e8f5e9; color:#1b5e20;">Career & ROI</span>
                <span>&bull; 8 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/top-online-mba-colleges">Top Online MBA Colleges: Specializations, Career Scope & ROI</a></h3>
              <p class="blog-card-excerpt">
                Discover top Online MBA colleges offering high-growth specializations in Analytics, FinTech, and Marketing. Review average salary hikes and hiring partners.
              </p>
              <div class="blog-highlight-box">
                <strong>ROI Outlook:</strong> 40% to 65% average compensation jump within 12 months of graduation.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/top-online-mba-colleges" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- 10. Top Online MBA Colleges in India -->
          <article class="blog-card" id="article-top-online-mba-colleges-in-india">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fff8e1; color:#f57f17;">Admissions Playbook</span>
                <span>&bull; 8 Min Read &bull; Oct 2026</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/top-online-mba-colleges-in-india">Top Online MBA Colleges in India: 2027 Direct Admission Playbook</a></h3>
              <p class="blog-card-excerpt">
                Step-by-step admission guide for top Online MBA colleges in India. Check eligibility, non-CAT direct admissions, document checklist, and EMI payment options.
              </p>
              <div class="blog-highlight-box">
                <strong>Paperless:</strong> 48-hour digital enrollment, instant NAD verification, and 0% interest EMI.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Dr. Rajiv Sharma</span>
              <a href="/blogs/top-online-mba-colleges-in-india" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>
"""

def update_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already added
    if 'id="article-online-mba"' in content:
        print(f"Already updated: {filepath}")
        return

    # 1. Update Schema blogPost list
    schema_posts_json = ""
    for post in NEW_SCHEMA_POSTS:
        schema_posts_json += f"""        {{
          "@type": "BlogPosting",
          "headline": "{post['headline']}",
          "url": "{post['url']}"
        }},
"""
    # Insert at beginning of "blogPost": [
    target_schema = '"blogPost": [\n'
    if target_schema in content:
        content = content.replace(target_schema, target_schema + schema_posts_json)

    # 2. Insert the cards at the beginning of <div class="blog-grid">
    target_grid = '<div class="blog-grid">\n'
    if target_grid in content:
        content = content.replace(target_grid, target_grid + NEW_CARDS_HTML)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated successfully: {filepath}")

def main():
    update_file(os.path.join(BASE_DIR, "blogs.html"))
    update_file(os.path.join(BASE_DIR, "blogs", "index.html"))

if __name__ == "__main__":
    main()
