# generate_all_10_blogs.py
import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOGS_DIR = os.path.join(BASE_DIR, "blogs")
os.makedirs(BLOGS_DIR, exist_ok=True)

CURRICULUM_TABLE = """
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Academic Semester</th>
        <th>Core Modules & Subject Breakdown</th>
        <th>Workload</th>
        <th>Applied Managerial Competency</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Semester I<br>(Foundations)</strong></td>
        <td>
          &bull; Managerial Economics & Microeconomic Strategy<br>
          &bull; Organizational Behaviour & Leadership Dynamics<br>
          &bull; Accounting for Corporate Decision Makers<br>
          &bull; Quantitative Techniques & Applied Business Statistics<br>
          &bull; Executive Business Communication & Digital Presence
        </td>
        <td>24 Credits</td>
        <td>Develops core business literacy, quantitative reasoning, microeconomic cost analysis, and cross-functional leadership frameworks.</td>
      </tr>
      <tr>
        <td><strong>Semester II<br>(Functional Integration)</strong></td>
        <td>
          &bull; Corporate Financial Management & Valuation<br>
          &bull; Marketing Strategy & Digital Consumer Behaviour<br>
          &bull; Operations Engineering & Supply Chain Dynamics<br>
          &bull; Strategic Human Resource Management<br>
          &bull; Business Research Methodologies & Predictive Analytics
        </td>
        <td>26 Credits</td>
        <td>Bridges departmental silos, synchronizes supply chains with consumer demand, and masters capital budgeting techniques.</td>
      </tr>
      <tr>
        <td><strong>Semester III<br>(Domain Electives)</strong></td>
        <td>
          &bull; Core Specialization Elective Modules I & II<br>
          &bull; Cross-Functional Elective Track I<br>
          &bull; Strategic Management & Competitive Advantage<br>
          &bull; Corporate Governance, Business Ethics & Cyber Law<br>
          &bull; Summer Consulting Internship / Applied Corporate Project
        </td>
        <td>26 Credits</td>
        <td>Deep-dive specialization mastery (Finance, Analytics, Marketing, HR, or IT) with real-world case studies and internship analysis.</td>
      </tr>
      <tr>
        <td><strong>Semester IV<br>(Capstone & Synthesis)</strong></td>
        <td>
          &bull; Advanced Domain Elective Modules III & IV<br>
          &bull; Enterprise Digital Transformation & Generative AI in Business<br>
          &bull; Entrepreneurial Innovation, Venture Capital & Scale-Up Strategy<br>
          &bull; Master Capstone Research Thesis / Live Corporate Strategy Project
        </td>
        <td>26 Credits</td>
        <td>Executive leadership synthesis, AI-powered digital transformation deployment, and strategic defense of a master consulting thesis.</td>
      </tr>
    </tbody>
  </table>
</div>
"""

UNIVERSITIES_TABLE = """
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University</th>
        <th>NAAC Status</th>
        <th>Statutory Entitlement</th>
        <th>Total Program Fee</th>
        <th>Starting 0% EMI</th>
        <th>Corporate Recruitment Partners</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/universities/manipal-jaipur">Manipal University Jaipur</a></strong></td>
        <td>NAAC A+ (3.28)</td>
        <td>UGC-DEB, AICTE Approved</td>
        <td>₹1,75,000</td>
        <td>₹7,292 / month</td>
        <td>Amazon, Accenture, Dell, EY, Deloitte, KPMG</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/amity">Amity University Online</a></strong></td>
        <td>NAAC A+ (3.27)</td>
        <td>UGC-DEB, QS World Ranked</td>
        <td>₹1,99,000</td>
        <td>₹8,290 / month</td>
        <td>Google, Cognizant, TCS, KPMG, HDFC Bank, Infosys</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/jain-university">Jain University Online</a></strong></td>
        <td>NAAC A++ (3.71)</td>
        <td>UGC-DEB, Category-1 Autonomy</td>
        <td>₹1,60,000</td>
        <td>₹6,666 / month</td>
        <td>Capgemini, Infosys, Flipkart, Morgan Stanley, PwC</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/dpu-online">Dr. D.Y. Patil Vidyapeeth (DPU)</a></strong></td>
        <td>NAAC A++ (3.52)</td>
        <td>UGC-DEB, Category-1 Autonomy</td>
        <td>₹1,40,000</td>
        <td>₹5,833 / month</td>
        <td>Apollo Hospitals, Cipla, Reliance, Axis Bank, TechM</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/parul">Parul University Online</a></strong></td>
        <td>NAAC A++ (3.55)</td>
        <td>UGC-DEB, AICTE Approved</td>
        <td>₹90,000</td>
        <td>₹3,750 / month</td>
        <td>L&T, Tata Motors, ICICI Bank, Tech Mahindra, Sun Pharma</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/gla">GLA University Online</a></strong></td>
        <td>NAAC A+ (3.46)</td>
        <td>UGC-DEB, AICTE Approved</td>
        <td>₹60,000</td>
        <td>₹2,500 / month</td>
        <td>Wipro, Paytm, Jindal Steel, Bandhan Bank, Hitachi</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/chandigarh-university">Chandigarh University Online</a></strong></td>
        <td>NAAC A+ (3.28)</td>
        <td>UGC-DEB, NIRF Top 30</td>
        <td>₹1,70,000</td>
        <td>₹7,083 / month</td>
        <td>IBM, Microsoft, Radisson, Federal Bank, ITC</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/ignou">IGNOU Online MBA</a></strong></td>
        <td>NAAC A++</td>
        <td>Central Govt, UGC-DEB</td>
        <td>₹62,000</td>
        <td>₹15,500 / sem</td>
        <td>Public Sector Banks, UPSC, SSC, State PSCs, PSUs</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/du-sol">DU SOL MBA</a></strong></td>
        <td>NAAC A+</td>
        <td>Delhi University, UGC-DEB</td>
        <td>₹47,000</td>
        <td>Annual Basis</td>
        <td>Central Ministries, PSUs, Banking, Corporate North</td>
      </tr>
    </tbody>
  </table>
</div>
"""

SALARY_TABLE = """
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>MBA Specialization Track</th>
        <th>Pre-MBA Average Package</th>
        <th>Post-MBA Starting Package</th>
        <th>5-Year Senior Leadership Package</th>
        <th>Core Executive Job Roles</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/specializations/business-analytics">Business Analytics & Data Science</a></strong></td>
        <td>₹4.5 – ₹6.5 LPA</td>
        <td>₹8.5 – ₹14.5 LPA</td>
        <td>₹22 – ₹38 LPA</td>
        <td>Data Strategy Manager, Analytics Lead, BI Consultant, VP Analytics</td>
      </tr>
      <tr>
        <td><strong><a href="/specializations/finance">Finance & FinTech Services</a></strong></td>
        <td>₹4.2 – ₹6.0 LPA</td>
        <td>₹8.0 – ₹13.5 LPA</td>
        <td>₹20 – ₹35 LPA</td>
        <td>Investment Banker, Risk Controller, Portfolio Manager, CFO Track</td>
      </tr>
      <tr>
        <td><strong><a href="/specializations/marketing">Marketing & Digital Strategy</a></strong></td>
        <td>₹3.8 – ₹5.5 LPA</td>
        <td>₹7.0 – ₹12.0 LPA</td>
        <td>₹18 – ₹30 LPA</td>
        <td>Brand Marketing Director, Growth Strategist, Omnichannel CMO</td>
      </tr>
      <tr>
        <td><strong><a href="/specializations/information-technology">Information Technology Management</a></strong></td>
        <td>₹5.0 – ₹7.5 LPA</td>
        <td>₹9.5 – ₹15.5 LPA</td>
        <td>₹25 – ₹42 LPA</td>
        <td>Enterprise IT Director, Cloud Solutions Architect, Chief Digital Officer</td>
      </tr>
      <tr>
        <td><strong><a href="/specializations/human-resource-management">Human Resource Management</a></strong></td>
        <td>₹3.5 – ₹5.0 LPA</td>
        <td>₹6.5 – ₹10.5 LPA</td>
        <td>₹16 – ₹28 LPA</td>
        <td>HR Business Partner (HRBP), VP Talent Acquisition, Head People Ops</td>
      </tr>
      <tr>
        <td><strong><a href="/specializations/operations-management">Operations & Supply Chain Management</a></strong></td>
        <td>₹4.0 – ₹5.8 LPA</td>
        <td>₹7.5 – ₹12.5 LPA</td>
        <td>₹19 – ₹32 LPA</td>
        <td>Global Supply Chain Head, Chief Operating Officer (COO), Logistics VP</td>
      </tr>
    </tbody>
  </table>
</div>
"""

EMI_TABLE = """
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University Program</th>
        <th>Total Net Tuition</th>
        <th>12-Month 0% EMI</th>
        <th>18-Month 0% EMI</th>
        <th>24-Month 0% EMI</th>
        <th>Fintech Lending Partners</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>GLA University Online</strong></td>
        <td>₹60,000</td>
        <td>₹5,000 / mo</td>
        <td>₹3,333 / mo</td>
        <td>₹2,500 / mo</td>
        <td>Propelld, Eduvanz, LiquiLoans</td>
      </tr>
      <tr>
        <td><strong>Parul University Online</strong></td>
        <td>₹90,000</td>
        <td>₹7,500 / mo</td>
        <td>₹5,000 / mo</td>
        <td>₹3,750 / mo</td>
        <td>LiquiLoans, GrayQuest, HDFC</td>
      </tr>
      <tr>
        <td><strong>Dr. D.Y. Patil (DPU Online)</strong></td>
        <td>₹1,40,000</td>
        <td>₹11,666 / mo</td>
        <td>₹7,777 / mo</td>
        <td>₹5,833 / mo</td>
        <td>Propelld, Eduvanz, Axis Bank</td>
      </tr>
      <tr>
        <td><strong>Jain University Online</strong></td>
        <td>₹1,60,000</td>
        <td>₹13,333 / mo</td>
        <td>₹8,888 / mo</td>
        <td>₹6,666 / mo</td>
        <td>LiquiLoans, ICICI Bank, Propelld</td>
      </tr>
      <tr>
        <td><strong>Manipal University Jaipur</strong></td>
        <td>₹1,75,000</td>
        <td>₹14,583 / mo</td>
        <td>₹9,722 / mo</td>
        <td>₹7,292 / mo</td>
        <td>Eduvanz, Propelld, LiquiLoans</td>
      </tr>
      <tr>
        <td><strong>Amity University Online</strong></td>
        <td>₹1,99,000</td>
        <td>₹16,583 / mo</td>
        <td>₹11,055 / mo</td>
        <td>₹8,290 / mo</td>
        <td>Propelld, LiquiLoans, Credit Cards</td>
      </tr>
    </tbody>
  </table>
</div>
"""

RELATED_MAP = {
    "online-mba": [
        ("online-mba-in-india", "Online MBA in India: UGC-DEB Guide, Programs & Fees", "Higher Education"),
        ("best-online-mba-in-india", "Best Online MBA in India: Top 10 Programs Ranked", "Rankings"),
        ("best-online-mba-colleges-in-india", "Best Online MBA Colleges in India: Fee & Placement Guide", "Colleges"),
        ("top-online-mba-colleges-in-india", "Top Online MBA Colleges in India: 2027 Direct Admission", "Admissions")
    ],
    "online-mba-in-india": [
        ("online-mba", "Online MBA: Complete 2027 Admission & Career Guide", "Master Guide"),
        ("best-online-mba-universities-in-india", "Best Online MBA Universities in India: Govt vs Private", "University Matrix"),
        ("top-online-mba-colleges", "Top Online MBA Colleges: Specializations & Salaries", "Career & ROI"),
        ("best-online-mba-colleges", "Best Online MBA Colleges: Approvals & Admissions", "Directory")
    ],
    "best-online-mba": [
        ("best-online-mba-in-india", "Best Online MBA in India: Top 10 Programs Ranked", "Rankings"),
        ("best-online-mba-university", "Best Online MBA University: 6 Evaluation Standards", "Evaluation"),
        ("online-mba", "Online MBA: Complete 2027 Admission & Career Guide", "Master Guide"),
        ("top-online-mba-colleges", "Top Online MBA Colleges: Specializations & Salaries", "Career & ROI")
    ],
    "best-online-mba-in-india": [
        ("best-online-mba-colleges-in-india", "Best Online MBA Colleges in India: Fee & Placement Guide", "Colleges"),
        ("best-online-mba-universities-in-india", "Best Online MBA Universities in India: Govt vs Private", "University Matrix"),
        ("online-mba-in-india", "Online MBA in India: UGC-DEB Guide, Programs & Fees", "Higher Education"),
        ("top-online-mba-colleges-in-india", "Top Online MBA Colleges in India: Direct Admission Playbook", "Admissions")
    ],
    "best-online-mba-colleges": [
        ("best-online-mba-colleges-in-india", "Best Online MBA Colleges in India: Fee & Placement Guide", "Colleges"),
        ("top-online-mba-colleges", "Top Online MBA Colleges: Specializations & Salaries", "Career & ROI"),
        ("best-online-mba", "Best Online MBA Programs: 7 Selection Factors", "Selection"),
        ("best-online-mba-university", "Best Online MBA University: 6 Evaluation Standards", "Evaluation")
    ],
    "best-online-mba-colleges-in-india": [
        ("top-online-mba-colleges-in-india", "Top Online MBA Colleges in India: Direct Admission Playbook", "Admissions"),
        ("best-online-mba-in-india", "Best Online MBA in India: Top 10 Programs Ranked", "Rankings"),
        ("online-mba-in-india", "Online MBA in India: UGC-DEB Guide, Programs & Fees", "Higher Education"),
        ("best-online-mba-colleges", "Best Online MBA Colleges: Approvals & Admissions", "Directory")
    ],
    "best-online-mba-university": [
        ("best-online-mba-universities-in-india", "Best Online MBA Universities in India: Govt vs Private", "University Matrix"),
        ("best-online-mba", "Best Online MBA Programs: 7 Selection Factors", "Selection"),
        ("best-online-mba-in-india", "Best Online MBA in India: Top 10 Programs Ranked", "Rankings"),
        ("online-mba", "Online MBA: Complete 2027 Admission & Career Guide", "Master Guide")
    ],
    "best-online-mba-universities-in-india": [
        ("best-online-mba-university", "Best Online MBA University: 6 Evaluation Standards", "Evaluation"),
        ("online-mba-in-india", "Online MBA in India: UGC-DEB Guide, Programs & Fees", "Higher Education"),
        ("best-online-mba-colleges-in-india", "Best Online MBA Colleges in India: Fee & Placement Guide", "Colleges"),
        ("best-online-mba-in-india", "Best Online MBA in India: Top 10 Programs Ranked", "Rankings")
    ],
    "top-online-mba-colleges": [
        ("top-online-mba-colleges-in-india", "Top Online MBA Colleges in India: Direct Admission Playbook", "Admissions"),
        ("best-online-mba-colleges", "Best Online MBA Colleges: Approvals & Admissions", "Directory"),
        ("best-online-mba", "Best Online MBA Programs: 7 Selection Factors", "Selection"),
        ("online-mba", "Online MBA: Complete 2027 Admission & Career Guide", "Master Guide")
    ],
    "top-online-mba-colleges-in-india": [
        ("top-online-mba-colleges", "Top Online MBA Colleges: Specializations & Salaries", "Career & ROI"),
        ("best-online-mba-colleges-in-india", "Best Online MBA Colleges in India: Fee & Placement Guide", "Colleges"),
        ("online-mba-in-india", "Online MBA in India: UGC-DEB Guide, Programs & Fees", "Higher Education"),
        ("best-online-mba-in-india", "Best Online MBA in India: Top 10 Programs Ranked", "Rankings")
    ]
}

def render_toc(sections):
    items = ""
    for idx, (sec_id, title) in enumerate(sections, 1):
        num_str = f"{idx:02d}"
        items += f"""
            <li class="blog-toc-item">
              <a href="#{sec_id}" class="blog-toc-link">
                <span class="blog-toc-num">{num_str}</span>
                <span>{title}</span>
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
            {items}
          </ul>
        </div>
"""

def render_related(slug):
    guides = RELATED_MAP.get(slug, [])
    cards = ""
    for s, t, b in guides:
        cards += f"""
          <a href="/blogs/{s}" class="related-guide-card">
            <div>
              <span class="related-guide-badge">{b}</span>
              <h4>{t}</h4>
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
            {cards}
          </div>
        </section>
"""

# Now write each post with full 2000+ words
print("Script scaffolded successfully.")
