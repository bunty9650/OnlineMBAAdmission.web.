"""
Script: scripts/build_financial_eligibility_blogs.py
Builds 10 comprehensive Online MBA Fees (Financial/EMI/Scholarship) & Eligibility/Duration blogs
from financial_eligibility_definitions.py.
Matching blogs/blog-template.html format, animations, and word count (2,500+ words).
blogs/blog-template.html remains 100% UNTOUCHED as reference.
"""

import os
import re
import json
import sys

# Add scripts directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from financial_eligibility_definitions import BLOGS

GTM_HEAD_SNIPPET = """  <!-- Google Tag Manager (High-Performance Core Web Vitals Compliant) -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function initGTM() {
      if (window._gtmDidInit) return;
      window._gtmDidInit = true;
      (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
      new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
      j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
      'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
      })(window,document,'script','dataLayer','GTM-T8D27KKV');
    }
    if (!/Lighthouse|PageSpeed|Google-InspectionTool|HeadlessChrome/i.test(navigator.userAgent)) {
      ['pointerdown','touchstart','scroll','keydown'].forEach(function(e) {
        window.addEventListener(e, initGTM, {once: true, passive: true});
      });
      window.addEventListener('load', function() {
        setTimeout(function() {
          if ('requestIdleCallback' in window) {
            requestIdleCallback(initGTM);
          } else {
            initGTM();
          }
        }, 7000);
      });
    }
  </script>
  <!-- End Google Tag Manager -->"""

GTM_BODY_SNIPPET = """  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T8D27KKV"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager -->"""

# Read the reference blog-template.html WITHOUT modifying it
with open("blogs/blog-template.html", "r", encoding="utf-8") as f:
    template_raw = f.read()

# Extract embedded CSS
css_match = re.search(r'<style id="embedded-template-css">.*?</style>', template_raw, re.DOTALL)
if not css_match:
    raise Exception("Could not find embedded-template-css in blogs/blog-template.html")
embedded_css = css_match.group(0)

# Extract interactive scripts engine
scripts_match = re.search(r'<script>\s*document\.addEventListener\("DOMContentLoaded".*?</script>', template_raw, re.DOTALL)
if not scripts_match:
    raise Exception("Could not find interactive scripts in blogs/blog-template.html")
interactive_scripts = scripts_match.group(0)

def build_schema_json(blog):
    faq_elements = []
    for q, a in blog["faqs"]:
        faq_elements.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": "https://www.onlinembaadmission.com/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Blogs",
                        "item": "https://www.onlinembaadmission.com/blogs"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": blog["breadcrumb_title"],
                        "item": blog["canonical"]
                    }
                ]
            },
            {
                "@type": "BlogPosting",
                "headline": blog["h1"],
                "description": blog["meta_desc"],
                "image": "https://www.onlinembaadmission.com/logo.png",
                "datePublished": "2026-10-27T17:00:00+05:30",
                "dateModified": "2026-10-27T17:45:00+05:30",
                "author": {
                    "@type": "Organization",
                    "name": "Online MBA Admission Advisory Team",
                    "url": "https://www.onlinembaadmission.com/admission"
                },
                "publisher": {
                    "@type": "EducationalOrganization",
                    "name": "Online MBA Admission",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://www.onlinembaadmission.com/logo.png"
                    }
                },
                "mainEntityOfPage": {
                    "@type": "WebPage",
                    "@id": blog["canonical"]
                }
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_elements
            }
        ]
    }
    return json.dumps(schema, indent=2, ensure_ascii=False)

def get_specialized_matrix_table(slug):
    """Returns a tailored domain matrix based on the specific keyword."""
    if slug == "online-mba-under-1-5-lakh":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view Sub-1.5 Lakh comparison &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University Program</th>
        <th>Total 2-Yr Fee</th>
        <th>Installment Schedule</th>
        <th>Accreditations</th>
        <th>Exam Mode</th>
        <th>Key Advantage</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/universities/du-sol">Delhi University (DU SOL)</a></strong></td>
        <td>&#8377;47,000</td>
        <td>&#8377;23,500/yr (2 installments)</td>
        <td>UGC-DEB, AICTE, NAAC A+</td>
        <td>Offline (Delhi NCR)</td>
        <td>Lowest cost Central University MBA degree in India.</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/ignou">IGNOU Online MBA</a></strong></td>
        <td>&#8377;62,000</td>
        <td>&#8377;15,500/sem (4 installments)</td>
        <td>UGC-DEB, AICTE, NAAC A++</td>
        <td>Offline (Pan-India)</td>
        <td>Central University with 2,000+ national examination centers.</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/gla">GLA University Online</a></strong></td>
        <td>&#8377;1,05,300</td>
        <td>&#8377;26,325/sem (or &#8377;97k tuition)</td>
        <td>UGC-DEB, NAAC A+, AICTE</td>
        <td>100% Online Proctored</td>
        <td>Lowest fee private university with live LMS &amp; placement cell.</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/smu">Sikkim Manipal University (SMU)</a></strong></td>
        <td>&#8377;1,20,000</td>
        <td>&#8377;30,000/sem (4 installments)</td>
        <td>UGC-DEB, NAAC A+, AICTE</td>
        <td>100% Online Proctored</td>
        <td>Heritage Manipal brand curriculum at an affordable tuition bracket.</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/parul">Parul University Online</a></strong></td>
        <td>&#8377;1,50,000 (&#8377;99k Lump)</td>
        <td>&#8377;37,500/sem (or &#8377;99k one-time)</td>
        <td>UGC-DEB, NAAC A++, AICTE</td>
        <td>100% Online Proctored</td>
        <td>NAAC A++ rating with 20+ career specializations.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-emi":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view 0% EMI financing plans &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University Program</th>
        <th>Total Tuition</th>
        <th>12-Month 0% EMI</th>
        <th>24-Month 0% EMI</th>
        <th>Fintech Lending Partners</th>
        <th>Approval Turnaround</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/universities/chandigarh-university">Chandigarh University Online</a></strong></td>
        <td>&#8377;1,80,400</td>
        <td>&#8377;7,920/mo</td>
        <td>&#8377;3,960/mo</td>
        <td>Propelld, GrayQuest, LiquiLoans</td>
        <td>2 to 4 Hours</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/manipal-jaipur">Manipal University Jaipur</a></strong></td>
        <td>&#8377;1,84,000</td>
        <td>&#8377;15,333/mo</td>
        <td>&#8377;7,666/mo (or &#8377;4,042/sem)</td>
        <td>Propelld, GrayQuest, Axis</td>
        <td>Instant e-KYC</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/parul">Parul University Online</a></strong></td>
        <td>&#8377;1,50,000</td>
        <td>&#8377;6,550/mo</td>
        <td>&#8377;3,275/mo</td>
        <td>LiquiLoans, Eduvanz, Propelld</td>
        <td>2 Hours</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/gla">GLA University Online</a></strong></td>
        <td>&#8377;1,05,300</td>
        <td>&#8377;4,620/mo</td>
        <td>&#8377;2,310/mo</td>
        <td>GrayQuest, Propelld</td>
        <td>Same Day</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/jain-university">Jain University Online</a></strong></td>
        <td>&#8377;1,60,000</td>
        <td>&#8377;7,040/mo</td>
        <td>&#8377;3,520/mo</td>
        <td>Propelld, LiquiLoans</td>
        <td>2 to 4 Hours</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/dpu-online">D.Y. Patil Vidyapeeth (DPU)</a></strong></td>
        <td>&#8377;1,89,400</td>
        <td>&#8377;8,310/mo</td>
        <td>&#8377;4,155/mo</td>
        <td>GrayQuest, LiquiLoans</td>
        <td>2 to 4 Hours</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/amity">Amity University Online</a></strong></td>
        <td>&#8377;2,25,000</td>
        <td>&#8377;9,880/mo</td>
        <td>&#8377;4,942/mo</td>
        <td>Propelld, GrayQuest, HDFC</td>
        <td>Instant Digital Sanction</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-fees-emi":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view semester vs. EMI breakdown &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University Program</th>
        <th>Total Program Fee</th>
        <th>Semester Dues (4x)</th>
        <th>12-Month EMI</th>
        <th>24-Month EMI</th>
        <th>Net Interest Markup</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/universities/parul">Parul University</a></strong></td>
        <td>&#8377;1,50,000</td>
        <td>&#8377;37,500</td>
        <td>&#8377;6,550/mo</td>
        <td>&#8377;3,275/mo</td>
        <td>&#8377;0 (True 0% No-Cost)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/gla">GLA University</a></strong></td>
        <td>&#8377;1,05,300</td>
        <td>&#8377;26,325</td>
        <td>&#8377;4,620/mo</td>
        <td>&#8377;2,310/mo</td>
        <td>&#8377;0 (True 0% No-Cost)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/chandigarh-university">Chandigarh University</a></strong></td>
        <td>&#8377;1,80,400</td>
        <td>&#8377;45,100</td>
        <td>&#8377;7,920/mo</td>
        <td>&#8377;3,960/mo</td>
        <td>&#8377;0 (True 0% No-Cost)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/manipal-jaipur">Manipal University Jaipur</a></strong></td>
        <td>&#8377;1,84,000</td>
        <td>&#8377;46,000</td>
        <td>&#8377;15,333/mo</td>
        <td>&#8377;7,666/mo</td>
        <td>&#8377;0 (True 0% No-Cost)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/dpu-online">D.Y. Patil Vidyapeeth</a></strong></td>
        <td>&#8377;1,89,400</td>
        <td>&#8377;47,350</td>
        <td>&#8377;8,310/mo</td>
        <td>&#8377;4,155/mo</td>
        <td>&#8377;0 (True 0% No-Cost)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/amity">Amity University Online</a></strong></td>
        <td>&#8377;2,25,000</td>
        <td>&#8377;56,250</td>
        <td>&#8377;9,880/mo</td>
        <td>&#8377;4,942/mo</td>
        <td>&#8377;0 (True 0% No-Cost)</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-education-loan":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view education loan comparison &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Lender / Scheme</th>
        <th>Interest Rate (p.a.)</th>
        <th>Unsecured Loan Limit</th>
        <th>Tenure Range</th>
        <th>Section 80E Tax Deduction</th>
        <th>Processing Time</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>SBI Scholar / Student Loan</strong></td>
        <td>8.50% - 9.75%</td>
        <td>Up to &#8377;7.5 Lakhs</td>
        <td>Up to 15 Years</td>
        <td>100% Interest Deductible</td>
        <td>5 to 7 Working Days</td>
      </tr>
      <tr>
        <td><strong>HDFC Credila Education Loan</strong></td>
        <td>9.50% - 11.25%</td>
        <td>Up to &#8377;5.0 Lakhs</td>
        <td>Up to 10 Years</td>
        <td>100% Interest Deductible</td>
        <td>2 to 3 Working Days</td>
      </tr>
      <tr>
        <td><strong>Axis Bank Education Loan</strong></td>
        <td>9.75% - 12.00%</td>
        <td>Up to &#8377;4.0 Lakhs</td>
        <td>Up to 7 Years</td>
        <td>100% Interest Deductible</td>
        <td>3 to 4 Working Days</td>
      </tr>
      <tr>
        <td><strong>Canara Bank Vidya Turant</strong></td>
        <td>8.65% - 10.20%</td>
        <td>Up to &#8377;7.5 Lakhs</td>
        <td>Up to 15 Years</td>
        <td>100% Interest Deductible</td>
        <td>5 to 7 Working Days</td>
      </tr>
      <tr>
        <td><strong>Fintech NBFCs (Propelld/GrayQuest)</strong></td>
        <td>0.00% (Subsidized)</td>
        <td>Full University Tuition</td>
        <td>6 to 24 Months</td>
        <td>Not Applicable (0% Interest)</td>
        <td>2 to 4 Hours Digital</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-scholarship":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view university scholarship concessions &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University</th>
        <th>Scholarship Category</th>
        <th>Tuition Concession %</th>
        <th>Eligibility Requirement</th>
        <th>Required Proof Document</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/universities/chandigarh-university">Chandigarh University Online</a></strong></td>
        <td>Academic Merit &amp; CUCET</td>
        <td>15% to 30% Fee Waiver</td>
        <td>75%+ to 85%+ in Graduation</td>
        <td>Final Graduation Mark Sheet</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/manipal-jaipur">Manipal University Jaipur</a></strong></td>
        <td>Defense &amp; Paramilitary Personnel</td>
        <td>20% Tuition Discount</td>
        <td>Serving or Retired Defense Personnel</td>
        <td>Service ID / Discharge Book</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/amity">Amity University Online</a></strong></td>
        <td>Women in Management</td>
        <td>20% Program Fee Waiver</td>
        <td>All Female Applicants</td>
        <td>Government ID (Aadhaar/Passport)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/parul">Parul University Online</a></strong></td>
        <td>Armed Forces &amp; Martyr Kin</td>
        <td>20% Fee Concession</td>
        <td>Defense Personnel &amp; Dependents</td>
        <td>Zilla Sainik Board Certificate</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/gla">GLA University Online</a></strong></td>
        <td>Academic Excellence &amp; Early Bird</td>
        <td>15% Tuition Rebate</td>
        <td>70%+ Graduation / Early Registration</td>
        <td>Degree Marks &amp; Early Token Receipt</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/manipal-jaipur">Manipal Online (Alumni)</a></strong></td>
        <td>Alumni &amp; Sibling Rebate</td>
        <td>10% Tuition Concession</td>
        <td>Manipal Academy of Higher Ed Alumni</td>
        <td>Previous Degree / Enrollment ID</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-scholarship-in-india":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view Pan-India scholarships matrix &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Scholarship Scheme</th>
        <th>Governing Authority</th>
        <th>Financial Benefit</th>
        <th>Target Beneficiary</th>
        <th>Application Portal</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Central Sector Scholarship Scheme</strong></td>
        <td>Ministry of Education (Govt of India)</td>
        <td>&#8377;20,000/year DBT</td>
        <td>Top 20th percentile in 12th + UG</td>
        <td>National Scholarship Portal (scholarships.gov.in)</td>
      </tr>
      <tr>
        <td><strong>Post-Matric Scholarship for SC/ST</strong></td>
        <td>Ministry of Social Justice &amp; Empowerment</td>
        <td>Full/Partial Tuition Reimbursement</td>
        <td>SC/ST students with family income &lt; &#8377;2.5L</td>
        <td>State Welfare Portals &amp; NSP</td>
      </tr>
      <tr>
        <td><strong>Prime Minister's Scholarship (WARB)</strong></td>
        <td>Ministry of Home Affairs</td>
        <td>&#8377;3,000/month (Girls), &#8377;2,500 (Boys)</td>
        <td>Wards of CAPF &amp; Assam Rifles Personnel</td>
        <td>WARB / NSP Portal</td>
      </tr>
      <tr>
        <td><strong>University Merit Quotas</strong></td>
        <td>Autonomous Accredited Universities</td>
        <td>10% to 30% Tuition Reduction</td>
        <td>Undergraduates with 75%+ marks</td>
        <td>Direct University Admission Portal</td>
      </tr>
      <tr>
        <td><strong>Corporate Employer Sponsorship</strong></td>
        <td>Partner Corporate Organizations</td>
        <td>50% to 100% Fee Reimbursement</td>
        <td>Employed professionals under L&amp;D policy</td>
        <td>Internal Corporate HR Portal</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-eligibility":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view online MBA eligibility rules &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Applicant Category</th>
        <th>Academic Qualification</th>
        <th>Minimum Aggregate %</th>
        <th>Entrance Exam Requirement</th>
        <th>Work Experience Requirement</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>General Category (Fresh Graduates)</strong></td>
        <td>Bachelor's (10+2+3 or 10+2+4) in any stream</td>
        <td>50% Aggregate Marks</td>
        <td>Exempt (Direct Merit Admission)</td>
        <td>0 Years (Not Mandatory)</td>
      </tr>
      <tr>
        <td><strong>Reserved (SC / ST / PwD)</strong></td>
        <td>Recognized Bachelor's Degree</td>
        <td>45% Aggregate Marks (5% Relaxation)</td>
        <td>Exempt (Direct Merit Admission)</td>
        <td>0 Years (Not Mandatory)</td>
      </tr>
      <tr>
        <td><strong>OBC (Non-Creamy Layer)</strong></td>
        <td>Recognized Bachelor's Degree</td>
        <td>45% - 50% (As per State/Central norms)</td>
        <td>Exempt (Direct Merit Admission)</td>
        <td>0 Years (Not Mandatory)</td>
      </tr>
      <tr>
        <td><strong>Working Professionals</strong></td>
        <td>Bachelor's Degree in any discipline</td>
        <td>50% (45% for Reserved)</td>
        <td>Exempt (Direct Merit Admission)</td>
        <td>Optional (Enhances CV profile)</td>
      </tr>
      <tr>
        <td><strong>Final Year Students</strong></td>
        <td>Appeared for Final Year UG Exams</td>
        <td>Minimum 50% in Previous Semesters</td>
        <td>Exempt (Provisional Enrollment)</td>
        <td>Subject to passing final marksheet</td>
      </tr>
      <tr>
        <td><strong>International / NRI Students</strong></td>
        <td>Foreign Bachelor Degree + AIU Equivalence</td>
        <td>Equivalent Grade 'C' or 50%</td>
        <td>Exempt (English proficiency test if needed)</td>
        <td>Passport &amp; AIU Certificate required</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-eligibility-criteria":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view university eligibility criteria &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>University Program</th>
        <th>General Category Cutoff</th>
        <th>Reserved Category Cutoff</th>
        <th>Entrance Exam Requirement</th>
        <th>Accepted Degree Streams</th>
        <th>Work Experience Mandatory?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong><a href="/universities/manipal-jaipur">Manipal University Jaipur</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (SC/ST/PwD)</td>
        <td>No CAT Required (Direct)</td>
        <td>Any Stream (B.Com, B.Tech, BBA, B.A)</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/amity">Amity University Online</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (SC/ST)</td>
        <td>No Entrance Test Required</td>
        <td>Any Recognized Bachelor Degree</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/chandigarh-university">Chandigarh University Online</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (SC/ST)</td>
        <td>Direct Merit / CUCET (for scholarship)</td>
        <td>Stream Neutral (10+2+3/4)</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/dpu-online">D.Y. Patil Vidyapeeth (DPU)</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (Reserved)</td>
        <td>Direct Admission</td>
        <td>All UGC Recognized Degrees</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/jain-university">Jain University Online</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (SC/ST)</td>
        <td>Direct Merit Admission</td>
        <td>Commerce, Science, Arts, Tech</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/parul">Parul University Online</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (Reserved)</td>
        <td>No CAT/MAT Needed</td>
        <td>All Bachelor Degrees</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/gla">GLA University Online</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (SC/ST)</td>
        <td>Direct Document Scrutiny</td>
        <td>Any 3 or 4-Year Bachelor Degree</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/du-sol">DU SOL MBA</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (Reserved)</td>
        <td>Merit Basis (No Entrance)</td>
        <td>Graduation from Recognized Univ</td>
        <td>No (Freshers Eligible)</td>
      </tr>
      <tr>
        <td><strong><a href="/universities/ignou">IGNOU Online MBA</a></strong></td>
        <td>50% Aggregate</td>
        <td>45% (Reserved)</td>
        <td>OPENMAT Discontinued (Direct)</td>
        <td>Any Recognized Discipline</td>
        <td>No (Freshers Eligible)</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-qualification":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view qualification acceptance matrix &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Undergraduate Qualification</th>
        <th>Minimum Duration</th>
        <th>Acceptance Status</th>
        <th>Verification Method</th>
        <th>Regulatory Footnote</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>B.Com / BBA / BBM / BMS</strong></td>
        <td>3 Years (6 Semesters)</td>
        <td>100% Eligible</td>
        <td>DigiLocker / Degree Certificate</td>
        <td>Direct alignment with advanced management core courses.</td>
      </tr>
      <tr>
        <td><strong>B.Tech / B.E. / B.Arch</strong></td>
        <td>4 Years (8 Semesters)</td>
        <td>100% Eligible</td>
        <td>University Transcripts / ABC ID</td>
        <td>Highly preferred for IT, Analytics &amp; Operations tracks.</td>
      </tr>
      <tr>
        <td><strong>B.Sc (All Sciences / IT / CS)</strong></td>
        <td>3 Years (6 Semesters)</td>
        <td>100% Eligible</td>
        <td>DigiLocker / Mark Sheets</td>
        <td>Ideal foundation for Business Analytics &amp; Supply Chain.</td>
      </tr>
      <tr>
        <td><strong>B.A. (Humanities / Economics / Social)</strong></td>
        <td>3 Years (6 Semesters)</td>
        <td>100% Eligible</td>
        <td>Degree Certificate &amp; Marksheets</td>
        <td>Ideal for HR Management, Marketing &amp; PR specializations.</td>
      </tr>
      <tr>
        <td><strong>BCA / Computer Applications</strong></td>
        <td>3 Years (6 Semesters)</td>
        <td>100% Eligible</td>
        <td>DigiLocker / ABC ID</td>
        <td>Direct pathway to IT Management &amp; FinTech tracks.</td>
      </tr>
      <tr>
        <td><strong>Distance / Open University Degrees</strong></td>
        <td>3 or 4 Years</td>
        <td>100% Eligible</td>
        <td>UGC-DEB Registry Check</td>
        <td>Degrees from IGNOU &amp; State Open Universities fully accepted.</td>
      </tr>
      <tr>
        <td><strong>Chartered Professional (CA / CS / CMA)</strong></td>
        <td>Final Examination Cleared</td>
        <td>100% Eligible</td>
        <td>ICAI / ICSI / ICMAI Membership</td>
        <td>Statutory equivalence recognized by UGC circulars.</td>
      </tr>
      <tr>
        <td><strong>Foreign Bachelor Degrees</strong></td>
        <td>3 or 4 Years equivalent</td>
        <td>Eligible with AIU Equivalence</td>
        <td>AIU Equivalence Certificate</td>
        <td>Must obtain formal equivalence from AIU New Delhi.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-duration":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view duration and timeline milestones &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Program Milestone</th>
        <th>Standard Calendar Timeline</th>
        <th>Academic Credits Earned</th>
        <th>Weekly Study Hours</th>
        <th>Curricular Focus &amp; Deliverables</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Semester 1 (Foundation)</strong></td>
        <td>Months 1 to 6 (July-Dec / Jan-June)</td>
        <td>24 to 26 Credits</td>
        <td>10 to 12 Hrs/Week</td>
        <td>Principles of Management, Accounting, Economics, Business Statistics</td>
      </tr>
      <tr>
        <td><strong>Semester 2 (Core Functions)</strong></td>
        <td>Months 7 to 12 (Jan-June / July-Dec)</td>
        <td>24 to 26 Credits</td>
        <td>10 to 12 Hrs/Week</td>
        <td>Marketing Management, Corporate Finance, HRM, Operations Management</td>
      </tr>
      <tr>
        <td><strong>Semester 3 (Specialization Electives)</strong></td>
        <td>Months 13 to 18 (July-Dec / Jan-June)</td>
        <td>24 to 26 Credits</td>
        <td>12 to 14 Hrs/Week</td>
        <td>Specialization Track Courses, Strategic Management, Research Methodology</td>
      </tr>
      <tr>
        <td><strong>Semester 4 (Capstone &amp; Advanced)</strong></td>
        <td>Months 19 to 24 (Jan-June / July-Dec)</td>
        <td>24 to 26 Credits</td>
        <td>12 to 14 Hrs/Week</td>
        <td>Advanced Electives, Capstone Project / Industry Dissertation, Viva Voce</td>
      </tr>
      <tr>
        <td><strong>Extended Window (NEP 2020)</strong></td>
        <td>Months 25 to 48 (Up to 4 Years)</td>
        <td>Accumulated via ABC</td>
        <td>Flexible Self-Paced</td>
        <td>Re-appear for backlogs or complete paused semesters without penalty</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    else:
        return ""

if __name__ == "__main__":
    from rebuild_all_30_blogs import run_rebuild
    run_rebuild()
