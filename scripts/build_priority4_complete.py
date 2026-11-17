# -*- coding: utf-8 -*-
"""
Priority 4 Complete Blog Generator
Generates full expanded 3,000+ word guides for:
Kanpur, Meerut, Agra, Ludhiana, Jodhpur, Surat, Nagpur, Visakhapatnam, Coimbatore, Ranchi
"""

import os
import sys
import json
import re

# Add scripts directory to sys.path
sys.path.append(os.path.dirname(__file__))

from build_priority2_blogs import get_shared_header_and_critical_css, get_shared_footer
from generate_all_priority2 import (
    make_breadcrumb, make_hero, make_toc, make_sidebar,
    make_bottom_conversion_form, make_faq_section
)
from priority2_expansion import (
    get_shared_curriculum_blueprint,
    get_deep_university_profiles,
    get_financial_and_scholarship_guide,
    get_career_matrix
)
from data_priority4_cities import cities_p4

def build_full_toc(city_name):
    return [
        ("executive-summary", f"{city_name} Corporate Landscape & Executive Need"),
        ("ugc-deb-validity", "UGC-DEB Regulatory Approval & Legal Validity"),
        ("top-universities", "Top Online MBA Colleges & Fee Comparison 2027"),
        ("university-deep-dives", "In-Depth Profiles: Manipal, Jain, Amity, St. Aloysius"),
        ("online-delivery-model", "100% Online Delivery vs Physical Campus Clarification"),
        ("specializations", f"In-Demand Specializations across {city_name} Hubs"),
        ("curriculum-blueprint", "Detailed 4-Semester AICTE Curriculum Blueprint"),
        ("comparative-analysis", "Online MBA vs Distance MBA vs Full-Time Exec MBA"),
        ("career-matrix", f"Career Transition & Salary Benchmarks in {city_name}"),
        ("financial-roadmap", "0% No-Cost EMI & Scholarship Architecture"),
        ("admission-roadmap", "Step-by-Step Admission Process & Eligibility"),
        ("exam-pattern", "Examination Pattern & AI Remote Proctoring Protocol"),
        ("career-outcomes", f"Alumni Career Growth & Corporate Hiring in {city_name}"),
        ("faqs", "Frequently Asked Questions (FAQ)")
    ]

def build_schema(city_data):
    faq_schema_items = []
    for q, a in city_data["faqs"]:
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    
    canonical_url = f"https://www.onlinembaadmission.com/blogs/{city_data['slug']}"
    
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
                        "name": f"Online MBA in {city_data['name']} 2027",
                        "item": canonical_url
                    }
                ]
            },
            {
                "@type": "BlogPosting",
                "headline": city_data["title"],
                "description": city_data["meta_desc"],
                "image": "https://www.onlinembaadmission.com/logo.png",
                "datePublished": "2026-11-17T11:00:00+05:30",
                "dateModified": "2026-11-17T14:30:00+05:30",
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
                    "@id": canonical_url
                }
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_schema_items
            }
        ]
    }
    return json.dumps(schema, indent=2)

def generate_city_content(city_data):
    city_name = city_data["name"]
    eco_items_html = ""
    for title, desc in city_data["industrial_ecosystem"]:
        eco_items_html += f"""            <li style="padding: 8px 0; display: flex; align-items: flex-start; gap: 10px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>{title}:</strong> {desc}</span>
            </li>\n"""
            
    dist_comp = city_data["local_distance_comp"]
    
    content = f"""
        <!-- Section 1: Executive Summary & Corporate Landscape -->
        <section class="cs-card" id="executive-summary">
          <h2 class="cs-heading-2">1. Executive Summary & The {city_name} Corporate Landscape</h2>
          <p>{city_data['intro_p1']}</p>
          <p>{city_data['intro_p2']}</p>

          <h3 class="cs-heading-3">Major Industrial Belts & Economic Zones in {city_name}</h3>
          <ul class="cs-checklist" style="list-style: none; padding: 0; margin: 16px 0;">
{eco_items_html}
          </ul>

          <div class="cs-callout" style="background: #eef9f8; border-left: 4px solid #0a6d6f; padding: 16px 20px; border-radius: 6px; margin: 20px 0;">
            <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 16px; font-weight: 700;">Executive Realities for {city_name} Working Professionals</h4>
            <p style="margin: 0; font-size: 14.5px; line-height: 1.6; color: #334155;">Working engineers, plant supervisors, export merchandisers, and administrative officers across {city_name} frequently reach career ceilings where technical competence alone no longer drives promotion. An accredited Online MBA equips professionals with cross-functional leadership, financial acumen, strategic marketing frameworks, and modern enterprise analytics required for senior management promotions.</p>
          </div>
        </section>

        <!-- Section 2: UGC-DEB Legal Parity & Regulatory Validation -->
        <section class="cs-card" id="ugc-deb-validity">
          <h2 class="cs-heading-2">2. UGC-DEB Regulatory Approval & Legal Validity in {city_name}</h2>
          <p>For working executives, government employees, and public sector officers across {city_name}, statutory legitimacy is non-negotiable. Indian law provides explicit, unambiguous legal equivalence for online degrees.</p>

          <p>Under <strong>Regulation 22 of the UGC (Open and Distance Learning Programmes and Online Programmes) Regulations, 2020</strong> published in the official Gazette of India:</p>
          <blockquote style="background: #f8fafc; border-left: 4px solid #0a6d6f; margin: 16px 0; padding: 14px 18px; font-style: italic; color: #334155;">
            "Degrees at undergraduate and postgraduate levels... offered through Online mode by Higher Educational Institutions recognised by the Commission... shall be treated as equivalent to the corresponding awards of the Degrees... offered through conventional mode."
          </blockquote>

          <h3 class="cs-heading-3">Key Legal Protections for {city_name} Learners</h3>
          <ul class="cs-checklist" style="list-style: none; padding: 0; margin: 16px 0;">
            <li style="padding: 8px 0; display: flex; align-items: flex-start; gap: 10px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Corporate & MNC Parity:</strong> Top private sector corporations and multinational companies in {city_name} treat UGC-DEB accredited online MBAs with identical weight to full-time degrees for appraisals and leadership hiring.</span>
            </li>
            <li style="padding: 8px 0; display: flex; align-items: flex-start; gap: 10px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Government Jobs & PSU Promotions:</strong> 100% valid for Union Public Service Commission (UPSC), State PSC examinations, national banking recruitments (IBPS, SBI), and departmental promotions in Central & State PSUs.</span>
            </li>
            <li style="padding: 8px 0; display: flex; align-items: flex-start; gap: 10px;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5" style="flex-shrink:0; margin-top:2px;"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Global Credential Recognition (WES Evaluated):</strong> Recognized by World Education Services (WES) for Canadian Express Entry permanent residency applications and international corporate employment abroad.</span>
            </li>
          </ul>
        </section>

        <!-- Section 3: University Comparison Table -->
        <section class="cs-card" id="top-universities">
          <h2 class="cs-heading-2">3. Top Online MBA Colleges for {city_name} Professionals: 2027 Fee Comparison</h2>
          <p>Below is a verified comparison of premier UGC-DEB entitled universities actively chosen by professionals across {city_name}:</p>

          <div class="cs-table-wrapper" style="margin: 20px 0; overflow-x: auto;">
            <table class="cs-table" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13.5px;">
              <thead>
                <tr style="background: #0a6d6f; color: #ffffff;">
                  <th style="padding: 12px; border: 1px solid #d1d5db;">University</th>
                  <th style="padding: 12px; border: 1px solid #d1d5db;">Accreditation</th>
                  <th style="padding: 12px; border: 1px solid #d1d5db;">Semester Fee</th>
                  <th style="padding: 12px; border: 1px solid #d1d5db;">Total Fee</th>
                  <th style="padding: 12px; border: 1px solid #d1d5db;">Key Specializations</th>
                  <th style="padding: 12px; border: 1px solid #d1d5db;">Action</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                  <td style="padding: 12px; font-weight: 700; color: #0f172a;"><a href="/universities/manipal-jaipur" style="color: #0a6d6f; text-decoration: underline;">Manipal University Jaipur</a><br><small style="color: #64748b;">Global Multi-Campus Group</small></td>
                  <td style="padding: 12px;"><span class="badge" style="background:#dcfce7; color:#166534; font-size:11px; padding:2px 6px; border-radius:4px; font-weight:700;">NAAC A+</span><br>NIRF Ranked #64</td>
                  <td style="padding: 12px; font-weight: 600;">₹43,750</td>
                  <td style="padding: 12px; font-weight: 700; color: #0a6d6f;">₹1,75,000</td>
                  <td style="padding: 12px;">Data Science, BFSI, SCM, Marketing, HR, Finance, International Business</td>
                  <td style="padding: 12px;"><a href="#admission-process" class="btn" style="background:#0a6d6f; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; text-decoration:none; display:inline-block; font-weight:700;">Check Plan</a></td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 12px; font-weight: 700; color: #0f172a;"><a href="/universities/st-aloysius" style="color: #0a6d6f; text-decoration: underline;">St. Aloysius University</a><br><small style="color: #64748b;">144-Year Jesuit Heritage</small></td>
                  <td style="padding: 12px;"><span class="badge" style="background:#dbeafe; color:#1e40af; font-size:11px; padding:2px 6px; border-radius:4px; font-weight:700;">NAAC A++</span><br>High Value ROI</td>
                  <td style="padding: 12px; font-weight: 600;">₹20,000 – ₹25,000</td>
                  <td style="padding: 12px; font-weight: 700; color: #0a6d6f;">₹80,000 – ₹1,00,000</td>
                  <td style="padding: 12px;">General Management, Finance, Human Resources, Marketing</td>
                  <td style="padding: 12px;"><a href="#admission-process" class="btn" style="background:#0a6d6f; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; text-decoration:none; display:inline-block; font-weight:700;">Check Plan</a></td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                  <td style="padding: 12px; font-weight: 700; color: #0f172a;"><a href="/universities/jain-university" style="color: #0a6d6f; text-decoration: underline;">Jain University Online</a><br><small style="color: #64748b;">Category-1 Deemed</small></td>
                  <td style="padding: 12px;"><span class="badge" style="background:#dcfce7; color:#166534; font-size:11px; padding:2px 6px; border-radius:4px; font-weight:700;">NAAC A++</span><br>Top NIRF</td>
                  <td style="padding: 12px; font-weight: 600;">₹40,000 – ₹50,000</td>
                  <td style="padding: 12px; font-weight: 700; color: #0a6d6f;">₹1,60,000 – ₹2,00,000</td>
                  <td style="padding: 12px;">Business Analytics, FinTech, Project Management, Systems, AI for Business</td>
                  <td style="padding: 12px;"><a href="#admission-process" class="btn" style="background:#0a6d6f; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; text-decoration:none; display:inline-block; font-weight:700;">Check Plan</a></td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 12px; font-weight: 700; color: #0f172a;"><a href="/universities/amity" style="color: #0a6d6f; text-decoration: underline;">Amity University Online</a><br><small style="color: #64748b;">Global Recognition</small></td>
                  <td style="padding: 12px;"><span class="badge" style="background:#dcfce7; color:#166534; font-size:11px; padding:2px 6px; border-radius:4px; font-weight:700;">NAAC A+</span><br>QS Asia Ranked</td>
                  <td style="padding: 12px; font-weight: 600;">₹49,750</td>
                  <td style="padding: 12px; font-weight: 700; color: #0a6d6f;">₹1,99,000</td>
                  <td style="padding: 12px;">International Business, Digital Marketing, Retail, Supply Chain, HR</td>
                  <td style="padding: 12px;"><a href="#admission-process" class="btn" style="background:#0a6d6f; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; text-decoration:none; display:inline-block; font-weight:700;">Check Plan</a></td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                  <td style="padding: 12px; font-weight: 700; color: #0f172a;">DY Patil Vidyapeeth (DPU-COL)<br><small style="color: #64748b;">Category-1 Deemed</small></td>
                  <td style="padding: 12px;"><span class="badge" style="background:#dcfce7; color:#166534; font-size:11px; padding:2px 6px; border-radius:4px; font-weight:700;">NAAC A++</span><br>NIRF Top 45</td>
                  <td style="padding: 12px; font-weight: 600;">₹42,500</td>
                  <td style="padding: 12px; font-weight: 700; color: #0a6d6f;">₹1,70,000</td>
                  <td style="padding: 12px;">Hospital & Healthcare, IT Management, Project Management, Operations</td>
                  <td style="padding: 12px;"><a href="#admission-process" class="btn" style="background:#0a6d6f; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; text-decoration:none; display:inline-block; font-weight:700;">Check Plan</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- Section 4: 100% Online Delivery vs Physical Campus Clarification -->
        <section class="cs-card" id="online-delivery-model">
          <h2 class="cs-heading-2">4. Crucial Clarification: 100% Online Delivery vs Physical Campus</h2>
          <p>It is vital for {city_name} applicants to understand that an <strong>Online MBA does not require physical campus attendance</strong> in {city_name} or anywhere else in India. The entire academic journey is conducted virtually:</p>

          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin: 20px 0;">
            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 16px;">Weekend Live Interactive Classes</h4>
              <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Faculty lectures and industry guest masterclasses are conducted on Saturdays and Sundays. Students engage via chat, live Q&A, and breakout sessions without compromising weekday work hours.</p>
            </div>
            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 16px;">24/7 Mobile Learning Portal</h4>
              <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.5;">Access high-definition recorded lectures, digital case studies, e-books, and quiz assessments directly on your mobile app or laptop at any hour of the day or night.</p>
            </div>
            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 16px;">Remote Home Proctored Exams</h4>
              <p style="margin: 0; font-size: 13.5px; color: #475569; line-height: 1.5;">No traveling across {city_name}'s traffic corridors or outstation test centers. All semester exams are taken securely from home via AI proctoring and live webcam invigilators.</p>
            </div>
          </div>

          <div class="cs-callout" style="background: #f1f5f9; border-left: 4px solid #475569; padding: 16px 20px; border-radius: 6px; margin: 20px 0;">
            <h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 16px; font-weight: 700;">{dist_comp['title']}</h4>
            <p style="margin: 0; font-size: 14.5px; line-height: 1.6; color: #334155;">{dist_comp['body']}</p>
          </div>
        </section>

        <!-- Section 5: Specialization Demand in City -->
        <section class="cs-card" id="specializations">
          <h2 class="cs-heading-2">5. Top In-Demand MBA Specializations across {city_name} Hubs</h2>
          <p>Aligning your MBA specialization with {city_name}'s commercial and industrial strengths delivers maximum promotional and business growth:</p>

          <h3 class="cs-heading-3">1. <a href="/specializations/operations-management" style="color: #0a6d6f; text-decoration: underline;">Operations & Supply Chain Management</a></h3>
          <p>Essential for manufacturing plants, heavy engineering facilities, port logistics, and export clusters across {city_name} to optimize warehouse throughput, lean production, vendor sourcing, and global freight distribution.</p>

          <h3 class="cs-heading-3">2. <a href="/specializations/finance" style="color: #0a6d6f; text-decoration: underline;">Finance & Banking Management</a></h3>
          <p>Critical for commercial banking officers, NBFC credit managers, and export enterprise treasurers in {city_name} to master working capital financing, foreign exchange hedging, risk modeling, and capital budgeting.</p>

          <h3 class="cs-heading-3">3. <a href="/specializations/business-analytics" style="color: #0a6d6f; text-decoration: underline;">Business Analytics & Data Science</a></h3>
          <p>Equips technical professionals, software engineers, and corporate planners with predictive modeling, SQL, Python for business intelligence, and executive data visualization skills to lead digital transformation.</p>

          <h3 class="cs-heading-3">4. <a href="/specializations/human-resource-management" style="color: #0a6d6f; text-decoration: underline;">Human Resource Management (HRM)</a></h3>
          <p>Empowers HR associates and personnel officers in heavy industries, healthcare institutions, and IT enterprises across {city_name} to manage talent acquisition, labor compliance, industrial relations, and corporate culture.</p>

          <h3 class="cs-heading-3">5. <a href="/specializations/marketing" style="color: #0a6d6f; text-decoration: underline;">Marketing & Digital Business Strategy</a></h3>
          <p>Provides entrepreneurs, retail heads, and FMCG brand managers in {city_name} with omnichannel marketing, performance advertising, D2C brand scaling, and international market entry tactics.</p>
        </section>

        <!-- Section 6: Online MBA vs Distance MBA vs Full-Time Exec MBA -->
        <section class="cs-card" id="comparative-analysis">
          <h2 class="cs-heading-2">6. Comparison: Online MBA vs Traditional Distance vs Full-Time Exec MBA</h2>
          <p>Here is an objective breakdown comparing educational pathways available to {city_name} working professionals:</p>

          <div class="cs-table-wrapper" style="margin: 20px 0; overflow-x: auto;">
            <table class="cs-table" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13.5px;">
              <thead>
                <tr style="background: #0f172a; color: #ffffff;">
                  <th style="padding: 12px; border: 1px solid #334155;">Metric</th>
                  <th style="padding: 12px; border: 1px solid #334155;">UGC-DEB Online MBA</th>
                  <th style="padding: 12px; border: 1px solid #334155;">Regional Distance MBA</th>
                  <th style="padding: 12px; border: 1px solid #334155;">Full-Time Exec MBA</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 12px; font-weight: 700;">Total Tuition Fees</td>
                  <td style="padding: 12px; color: #0a6d6f; font-weight: 700;">₹80,000 – ₹1,75,000</td>
                  <td style="padding: 12px;">₹30,000 – ₹60,000</td>
                  <td style="padding: 12px; color: #b91c1c; font-weight: 700;">₹15,00,000 – ₹30,00,000</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 12px; font-weight: 700;">Opportunity Cost</td>
                  <td style="padding: 12px; color: #166534; font-weight: 700;">Zero (Earn while learning)</td>
                  <td style="padding: 12px; color: #166534; font-weight: 700;">Zero (Earn while learning)</td>
                  <td style="padding: 12px; color: #b91c1c; font-weight: 700;">2 Years Forgone Salary</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 12px; font-weight: 700;">Learning Delivery</td>
                  <td style="padding: 12px;">24/7 Cloud LMS + Live Weekends</td>
                  <td style="padding: 12px;">Printed Booklets / Self-Study</td>
                  <td style="padding: 12px;">Mandatory Physical Lectures</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 12px; font-weight: 700;">Exam Mode</td>
                  <td style="padding: 12px; color: #0a6d6f; font-weight: 700;">100% Home AI Proctored</td>
                  <td style="padding: 12px;">Offline Physical Centers</td>
                  <td style="padding: 12px;">On-Campus Written Exams</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 12px; font-weight: 700;">Statutory Degree Parity</td>
                  <td style="padding: 12px; color: #166534; font-weight: 700;">100% (UGC Gazette 2020)</td>
                  <td style="padding: 12px;">100% (UGC-DEB)</td>
                  <td style="padding: 12px;">100% (Conventional)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 12px; font-weight: 700;">WES & Global Validity</td>
                  <td style="padding: 12px; color: #166534; font-weight: 700;">Accepted (NAAC A+/A++)</td>
                  <td style="padding: 12px;">Varies by Accreditation</td>
                  <td style="padding: 12px;">Accepted</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- Section 7: Admission Roadmap & Eligibility -->
        <section class="cs-card" id="admission-roadmap">
          <h2 class="cs-heading-2">7. Step-by-Step Admission Process & Eligibility for {city_name} Applicants</h2>
          <p>Admission to UGC-DEB recognized online MBA programs is fully streamlined and 100% digital:</p>

          <h3 class="cs-heading-3">Standard Academic Eligibility Criteria</h3>
          <ul class="cs-checklist" style="list-style: none; padding: 0; margin: 16px 0;">
            <li style="padding: 6px 0; display: flex; align-items: center; gap: 8px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Graduation Degree:</strong> Bachelor's degree (B.E., B.Tech, B.Com, B.Sc, BBA, BCA, BA) from any UGC recognized university.</span>
            </li>
            <li style="padding: 6px 0; display: flex; align-items: center; gap: 8px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>Minimum Percentage:</strong> 50% aggregate marks (45% for Reserved categories like SC/ST/OBC).</span>
            </li>
            <li style="padding: 6px 0; display: flex; align-items: center; gap: 8px;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span><strong>No Entrance Exam Required:</strong> Direct admission without mandatory CAT, MAT, or state entrance scores.</span>
            </li>
          </ul>

          <h3 class="cs-heading-3">The 4-Step Application Procedure</h3>
          <ol style="padding-left: 20px; line-height: 1.8; color: #334155;">
            <li><strong>Expert Advisory:</strong> Connect with our {city_name} counseling desk to compare curricula, faculty ratings, and fee structures.</li>
            <li><strong>Document Upload:</strong> Submit scanned graduation degree transcripts, 10th/12th mark sheets, and Aadhaar card online.</li>
            <li><strong>University Verification:</strong> Admissions committee verifies eligibility within 24–48 hours and issues an official admission letter.</li>
            <li><strong>Payment & LMS Access:</strong> Complete semester fee payment or activate 0% interest monthly EMI. Gain instant access to the digital LMS.</li>
          </ol>
        </section>

        <!-- Section 8: Examination Pattern & AI Proctoring -->
        <section class="cs-card" id="exam-pattern">
          <h2 class="cs-heading-2">8. Examination Pattern & AI Remote Proctoring Protocol</h2>
          <p>All entitled online universities follow the standard continuous evaluation framework mandated by UGC:</p>

          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; margin: 18px 0;">
            <h4 style="margin: 0 0 10px 0; color: #0a6d6f; font-size: 16px;">The 30:70 Evaluation Framework</h4>
            <ul style="margin: 0; padding-left: 18px; line-height: 1.7; color: #475569;">
              <li><strong>Continuous Internal Assessment (30%):</strong> Online project reports, mid-term MCQ quizzes, discussion forum participation, and business case submissions.</li>
              <li><strong>End-Semester Examination (70%):</strong> Remote examinations administered from home featuring dual-camera webcam proctoring, browser lockdown, and AI audio-visual monitoring.</li>
            </ul>
          </div>
        </section>

        <!-- Section 9: Career Trajectory & Alumni Outcomes -->
        <section class="cs-card" id="career-outcomes">
          <h2 class="cs-heading-2">9. Career Growth & Major Hiring Corporations in {city_name}</h2>
          <p>Online MBA graduates in {city_name} achieve rapid promotional velocity across leading regional, national, and multinational enterprises. The curriculum equips technical engineers, plant supervisors, financial analysts, and functional team leads with the strategic problem-solving capabilities, executive communication skills, and financial acumen necessary to qualify for managerial promotions.</p>

          <p>According to graduate outcome surveys, working professionals report average salary increments ranging from 40% to 75% within 12 to 24 months of completing their degree. Universities provide comprehensive career advancement services—including 1-on-1 executive resume auditing, LinkedIn profile optimization, AI-powered mock interview sessions, and exclusive access to virtual job fairs featuring over 500+ corporate hiring partners across India.</p>

          <p>Furthermore, learners in {city_name} gain access to vast national alumni networks spanning thousands of corporate managers, consultants, and entrepreneurs. These peer networks serve as invaluable conduits for unadvertised leadership vacancies, strategic business partnerships, and ongoing professional mentorship throughout your executive trajectory.</p>
        </section>
    """
    return content

def assemble_p4_page(city_key, city_data):
    city_name = city_data["name"]
    toc = build_full_toc(city_name)
    
    base_content = generate_city_content(city_data)
    
    # Enhanced rich content assembly
    curriculum_html = get_shared_curriculum_blueprint()
    deep_profiles_html = get_deep_university_profiles()
    financial_html = get_financial_and_scholarship_guide(city_name)
    matrix_html = get_career_matrix(city_name, city_data["career_matrix"])
    
    # Splice rich modules into content
    # 1. Insert deep profiles right after top-universities
    content_spliced = base_content.replace(
        '</section>\n\n        <!-- Section 4: 100% Online Delivery',
        f'</section>\n\n{deep_profiles_html}\n\n        <!-- Section 4: 100% Online Delivery'
    )
    
    # 2. Insert curriculum right after specializations
    content_spliced = content_spliced.replace(
        '</section>\n\n        <!-- Section 6: Comparison:',
        f'</section>\n\n{curriculum_html}\n\n        <!-- Section 6: Comparison:'
    )
    
    # 3. Insert career matrix & financial guide right after comparative-analysis and before admission-roadmap
    content_spliced = content_spliced.replace(
        '</section>\n\n        <!-- Section 7: Admission Roadmap',
        f'</section>\n\n{matrix_html}\n\n{financial_html}\n\n        <!-- Section 7: Admission Roadmap'
    )
    
    schema_json = build_schema(city_data)
    canonical_url = f"https://www.onlinembaadmission.com/blogs/{city_data['slug']}"
    
    header_html = get_shared_header_and_critical_css(
        title=city_data["title"],
        meta_desc=city_data["meta_desc"],
        keywords=", ".join([city_data["primary_kw"]] + city_data["secondary_kws"]),
        canonical_url=canonical_url,
        schema_json=schema_json
    )
    footer_html = get_shared_footer()
    
    breadcrumb_html = make_breadcrumb(city_name, city_data["slug"])
    hero_html = make_hero(city_name, city_data["primary_kw"])
    mobile_toc_html = f"""      <!-- Mobile Table of Contents -->
      <div class="mobile-toc-card">
        {make_toc(toc)}
      </div>"""
    desktop_toc_html = make_toc(toc)
    faq_html = make_faq_section(city_data["faqs"])
    bottom_form_html = make_bottom_conversion_form(city_name)
    sidebar_html = make_sidebar(city_name, toc)
    
    page_html = f"""{header_html}
  <main class="cs-wrapper">
{breadcrumb_html}
{hero_html}

{mobile_toc_html}

    <div class="cs-layout-container">
      <!-- Main Content Area -->
      <article class="cs-main-content">
{desktop_toc_html}

{content_spliced}

{faq_html}

{bottom_form_html}
      </article>

{sidebar_html}
    </div>
  </main>

{footer_html}"""
    return page_html

def main():
    output_dir = "blogs"
    generated_files = []
    
    for city_key, city_data in cities_p4.items():
        filename = f"{city_data['slug']}.html"
        filepath = os.path.join(output_dir, filename)
        
        print(f"Building Priority 4 blog: {filepath} for {city_data['name']}...")
        html_content = assemble_p4_page(city_key, city_data)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        generated_files.append((filepath, city_data))
        
    print(f"\nAll {len(generated_files)} Priority 4 city blog files generated successfully.")

if __name__ == "__main__":
    main()
