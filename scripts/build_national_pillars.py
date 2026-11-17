# -*- coding: utf-8 -*-
"""
Builder script for 5 Brand New National Pillar Blog Guides
Generates full 3,100+ word guides with 100% Developer Checklist compliance.
"""

import os
import sys
import json
import re

# Add scripts directory to path
sys.path.append(os.path.dirname(__file__))

from build_priority2_blogs import get_shared_header_and_critical_css, get_shared_footer
from generate_all_priority2 import (
    make_breadcrumb, make_toc, make_sidebar,
    make_bottom_conversion_form, make_faq_section
)
from priority2_expansion import (
    get_shared_curriculum_blueprint,
    get_deep_university_profiles,
    get_financial_and_scholarship_guide
)
import national_pillars_expanded as npe
import enrichment_modules as em
from data_national_pillars import national_pillars_data

def make_national_hero(title, primary_kw, badge):
    return f"""      <!-- Hero Section -->
      <header class="cs-hero" style="background: linear-gradient(135deg, #0a2540 0%, #0a6d6f 100%); color: #ffffff; padding: 48px 24px; border-radius: 12px; margin-bottom: 32px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1);">
        <div style="max-width: 900px; margin: 0 auto; text-align: center;">
          <div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(8px); padding: 6px 16px; border-radius: 30px; font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 20px;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            <span>{badge}</span>
          </div>
          <h1 class="cs-hero-title" style="font-size: clamp(26px, 4vw, 38px); font-weight: 800; line-height: 1.25; margin-bottom: 16px; color: #ffffff;">{title}</h1>
          <p class="cs-hero-subtitle" style="font-size: 16px; line-height: 1.6; color: #e2e8f0; max-width: 780px; margin: 0 auto 24px auto;">
            Comprehensive 2027 national master guide covering verified UGC-DEB regulatory entitlements, university fee comparisons, curriculum architecture, AI-proctored examination rules, and executive career outcomes.
          </p>
          <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; font-size: 13.5px; color: #cbd5e1; border-top: 1px solid rgba(255,255,255,0.15); padding-top: 18px;">
            <span style="display: inline-flex; align-items: center; gap: 6px;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> Last Updated: November 2026</span>
            <span style="display: inline-flex; align-items: center; gap: 6px;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg> UGC-DEB & Gazette 2020 Verified</span>
            <span style="display: inline-flex; align-items: center; gap: 6px;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg> 2027 Admissions Open</span>
          </div>
        </div>
      </header>"""

def build_schema(data):
    faq_schema_items = []
    for q, a in data["faqs"]:
        faq_schema_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        
    canonical_url = f"https://www.onlinembaadmission.com/blogs/{data['slug']}"
    
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
                        "name": data["primary_kw"],
                        "item": canonical_url
                    }
                ]
            },
            {
                "@type": "BlogPosting",
                "headline": data["title"],
                "description": data["meta_desc"],
                "image": "https://www.onlinembaadmission.com/logo.png",
                "datePublished": "2026-11-17T11:00:00+05:30",
                "dateModified": "2026-11-17T15:00:00+05:30",
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

def build_full_toc(slug):
    base_toc = [
        ("executive-summary", "1. Executive Summary & Core Landscape"),
        ("ugc-deb-validity", "2. UGC-DEB Regulatory Approval & Legal Validity"),
        ("top-universities", "3. Top Universities & Fee Comparison 2027"),
        ("university-deep-dives", "4. In-Depth Profiles: Manipal, Jain, Amity, St. Aloysius"),
        ("online-delivery-model", "5. 100% Online Delivery & Academic Rigor"),
        ("specializations", "6. Top In-Demand Specializations & Industry Fit"),
        ("curriculum-blueprint", "7. Detailed 4-Semester AICTE Curriculum Blueprint"),
        ("comparative-analysis", "8. Strategic Comparative Analysis & Global Standing")
    ]
    
    if slug == "is-online-mba-valid-in-india":
        base_toc.extend([
            ("international-recognition", "9. International Credential Evaluation: WES & UK ENIC"),
            ("psu-promotions", "10. DoPT Guidelines & PSU Departmental Promotions")
        ])
    elif slug == "government-online-distance-mba-universities":
        base_toc.extend([
            ("state-open-universities", "9. Directory of State Open Universities in India"),
            ("psu-promotions", "10. DoPT Guidelines & PSU Promotion Norms")
        ])
    elif slug == "online-mba-after-bcom":
        base_toc.extend([
            ("bcom-curriculum-mapping", "9. B.Com Subject Mapping & CFA Comparison"),
            ("bcom-industry-tracks", "10. The 4 High-Growth Commercial Sectors for Commerce MBAs"),
            ("career-matrix", "11. Career Transition Matrix for B.Com Graduates")
        ])
    elif slug == "online-mba-finance-vs-marketing-vs-hr":
        base_toc.extend([
            ("specialization-curricula", "9. In-Depth Elective Suite: Finance vs Marketing vs HR"),
            ("industry-specialization-matrix", "10. Industry-by-Industry Specialization Matrix"),
            ("specialization-case-studies", "11. Real-World Case Studies of 3 Professionals")
        ])
    elif slug == "online-mba-vs-regular-mba":
        base_toc.extend([
            ("wealth-projection", "9. 10-Year Cumulative Net Worth Projection"),
            ("myths-debunked", "10. 5 Critical Misconceptions Debunked"),
            ("recruiter-perception-audit", "11. Recruiter Sentiment Audit Across Top Sectors")
        ])
        
    base_toc.extend([
        ("financial-roadmap", "11. 0% No-Cost EMI & Scholarship Architecture"),
        ("admission-roadmap", "12. Step-by-Step Admission Process & Verification"),
        ("exam-pattern", "13. Examination Pattern & AI Remote Proctoring Protocol"),
        ("career-outcomes", "14. Alumni Career Velocity & Corporate Hiring"),
        ("faqs", "15. Frequently Asked Questions (FAQ)")
    ])
    return base_toc

def assemble_pillar_page(slug, data):
    title = data["title"]
    meta_desc = data["meta_desc"]
    primary_kw = data["primary_kw"]
    secondary_kws = data["secondary_kws"]
    badge = data["badge"]
    faqs = data["faqs"]
    base_content = data["content"]
    
    canonical_url = f"https://www.onlinembaadmission.com/blogs/{slug}"
    schema_json = build_schema(data)
    
    header_html = get_shared_header_and_critical_css(
        title=title,
        meta_desc=meta_desc,
        keywords=", ".join([primary_kw] + secondary_kws),
        canonical_url=canonical_url,
        schema_json=schema_json
    )
    footer_html = get_shared_footer()
    
    breadcrumb_html = make_breadcrumb(primary_kw, slug)
    hero_html = make_national_hero(title, primary_kw, badge)
    
    toc = build_full_toc(slug)
    mobile_toc_html = f"""      <!-- Mobile Table of Contents -->
      <div class="mobile-toc-card">
        {make_toc(toc)}
      </div>"""
    desktop_toc_html = make_toc(toc)
    faq_html = make_faq_section(faqs)
    bottom_form_html = make_bottom_conversion_form("National Advisory")
    sidebar_html = make_sidebar("National Advisory", toc)
    
    # Enhanced rich modules
    curriculum_html = get_shared_curriculum_blueprint()
    deep_profiles_html = get_deep_university_profiles()
    financial_html = get_financial_and_scholarship_guide("National Advisory")
    
    # Select specific expansion module
    specific_module_html = ""
    if slug == "is-online-mba-valid-in-india":
        specific_module_html = npe.get_wes_and_international_equivalence() + "\n\n" + npe.get_psu_promotion_and_dopt_rules()
    elif slug == "government-online-distance-mba-universities":
        specific_module_html = npe.get_state_open_universities_comprehensive() + "\n\n" + npe.get_psu_promotion_and_dopt_rules()
    elif slug == "online-mba-after-bcom":
        specific_module_html = npe.get_bcom_detailed_curriculum_and_cfa_comparison() + "\n\n" + em.get_bcom_industry_tracks() + "\n\n" + npe.get_bcom_career_transition_matrix()
    elif slug == "online-mba-finance-vs-marketing-vs-hr":
        specific_module_html = npe.get_specialization_curriculum_comparison() + "\n\n" + em.get_specialization_industry_matrix() + "\n\n" + npe.get_five_case_studies_specializations()
    elif slug == "online-mba-vs-regular-mba":
        specific_module_html = npe.get_ten_year_wealth_projection() + "\n\n" + em.get_regular_vs_online_myths_debunked() + "\n\n" + npe.get_detailed_recruiter_sentiment_audit()

    # Guaranteed assembly by finding reliable anchor points
    # 1. Insert deep profiles after Section 3
    parts = base_content.split('<!-- Section 4:')
    if len(parts) == 2:
        content_assembled = parts[0] + deep_profiles_html + '\n\n        <!-- Section 4:' + parts[1]
    else:
        content_assembled = base_content + "\n\n" + deep_profiles_html

    # 2. Insert curriculum after Section 5
    parts2 = content_assembled.split('<!-- Section 6:')
    if len(parts2) == 2:
        content_assembled = parts2[0] + curriculum_html + '\n\n        <!-- Section 6:' + parts2[1]
    else:
        content_assembled = content_assembled + "\n\n" + curriculum_html

    # 3. Insert specific modules & financial guide before Section 7
    parts3 = content_assembled.split('<!-- Section 7:')
    if len(parts3) == 2:
        content_assembled = parts3[0] + specific_module_html + '\n\n' + financial_html + '\n\n        <!-- Section 7:' + parts3[1]
    else:
        content_assembled = content_assembled + "\n\n" + specific_module_html + "\n\n" + financial_html

    page_html = f"""{header_html}
  <main class="cs-wrapper">
{breadcrumb_html}
{hero_html}

{mobile_toc_html}

    <div class="cs-layout-container">
      <!-- Main Content Area -->
      <article class="cs-main-content">
{desktop_toc_html}

{content_assembled}

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
    
    for slug, data in national_pillars_data.items():
        filename = f"{slug}.html"
        filepath = os.path.join(output_dir, filename)
        
        print(f"Building Full Expanded National Pillar Guide: {filepath} ({data['title']})...")
        html_content = assemble_pillar_page(slug, data)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        generated_files.append((filepath, data))
        
    print(f"\nAll {len(generated_files)} National Pillar Blog Guides assembled successfully.")

if __name__ == "__main__":
    main()
