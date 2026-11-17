import os
import json
import re

# Import base layout helpers
from build_priority2_blogs import get_shared_header_and_critical_css, get_shared_footer
from generate_all_priority2 import (
    make_breadcrumb, make_hero, make_toc, make_sidebar,
    make_bottom_conversion_form, make_faq_section
)

# Import city data modules
import data_priority3_jaipur as jpr
import data_priority3_lucknow as lko
import data_priority3_chandigarh as chd
import data_priority3_ahmedabad as amd
import data_priority3_indore as idr
import data_priority3_bhopal as bpl

# Import expansion modules
from priority2_expansion import (
    get_shared_curriculum_blueprint,
    get_deep_university_profiles,
    get_financial_and_scholarship_guide,
    get_career_matrix
)

career_matrices = {
    "Jaipur": [
        ("Senior Operations Associate (Mahindra World City)", "Operations Director / Delivery Head", "5–8 Years", "₹9L – ₹14L", "₹20L – ₹28L"),
        ("IT Software Engineer (Sitapura SEZ)", "Technical Product Lead / Scrum Manager", "4–7 Years", "₹8L – ₹13L", "₹18L – ₹26L"),
        ("Gemstone & Jewelry Export Executive", "Head of International Trade & Supply Chain", "5–9 Years", "₹8L – ₹14L", "₹22L – ₹32L"),
        ("Banking Assistant Manager", "Branch Head / Credit Risk Manager", "4–7 Years", "₹7L – ₹11L", "₹15L – ₹22L"),
        ("Family Business Second-Gen Leader", "Managing Director / Enterprise Scaler", "3–6 Years", "₹8L – ₹12L", "₹25L – ₹40L")
    ],
    "Lucknow": [
        ("Public Sector Technical Officer (HAL/PSU)", "Executive Manager (E3/E4 Grade Promotion)", "6–10 Years", "₹8L – ₹12L", "₹16L – ₹24L"),
        ("IT Software Engineer (Gomti Nagar)", "Technical Product Manager (TPM)", "4–7 Years", "₹8L – ₹13L", "₹18L – ₹26L"),
        ("Commercial Bank Branch Officer (PNB/SBI)", "Zonal Credit Head / Senior Manager", "5–9 Years", "₹9L – ₹13L", "₹18L – ₹25L"),
        ("Manufacturing Engineer (Tata Motors Chinhat)", "Plant Operations Head / Sourcing Lead", "5–8 Years", "₹8L – ₹12L", "₹18L – ₹26L"),
        ("State Secretariat Administrative Officer", "Senior Administrative Joint Director", "7–12 Years", "₹9L – ₹13L", "₹17L – ₹25L")
    ],
    "Chandigarh": [
        ("Senior Software Engineer (Mohali IT Park)", "Technical Product Manager (TPM)", "4–7 Years", "₹11L – ₹16L", "₹22L – ₹32L"),
        ("QA / Agile Scrum Lead (Quark City)", "Engineering Program Manager (EPM)", "5–8 Years", "₹10L – ₹15L", "₹20L – ₹28L"),
        ("Prospective Canadian PR Applicant", "WES Master's Credential Verified (Max CRS)", "3–7 Years", "₹9L – ₹14L", "International Career ($75k–$110k CAD)"),
        ("Commercial Bank Relationship Manager", "Zonal Wealth Management Head", "5–9 Years", "₹9L – ₹14L", "₹19L – ₹28L"),
        ("Defense Veteran / Armed Forces Officer", "Corporate Security & Operations Director", "8–15 Years", "₹12L – ₹18L", "₹25L – ₹38L")
    ],
    "Ahmedabad": [
        ("Financial Analyst (GIFT City IFSC)", "Associate VP - Cross-Border Capital Markets", "4–7 Years", "₹12L – ₹18L", "₹25L – ₹38L"),
        ("Automotive Plant Engineer (Sanand)", "Plant General Manager - Manufacturing", "6–10 Years", "₹9L – ₹14L", "₹22L – ₹32L"),
        ("Pharma QC & Regulatory Associate (Zydus/Torrent)", "Director - Global Pharma Regulatory Operations", "5–9 Years", "₹10L – ₹15L", "₹22L – ₹32L"),
        ("Family Business Second-Gen Director", "Chief Executive Officer (Enterprise D2C Scale)", "3–7 Years", "₹10L – ₹16L", "₹30L – ₹50L"),
        ("Chemical Plant Shift Supervisor (Vatva)", "Head of Procurement & Plant Sourcing", "5–8 Years", "₹7L – ₹11L", "₹16L – ₹24L")
    ],
    "Indore": [
        ("Automotive Tooling / Production Engineer (Pithampur)", "Plant Operations Head / General Manager", "6–10 Years", "₹8L – ₹13L", "₹20L – ₹30L"),
        ("Pharma Manufacturing Associate (Cipla/Lupin)", "Global Supply Chain & Regulatory Director", "5–9 Years", "₹9L – ₹14L", "₹20L – ₹29L"),
        ("Software Engineer (TCS Super Corridor)", "IT Delivery Manager / Scrum Lead", "4–7 Years", "₹9L – ₹14L", "₹18L – ₹26L"),
        ("FMCG Regional Sales Supervisor", "Central India Zonal Marketing Director", "5–9 Years", "₹8L – ₹12L", "₹18L – ₹26L"),
        ("Banking Operations Officer", "Regional Credit Underwriter / Scale 3 Manager", "5–8 Years", "₹8L – ₹12L", "₹16L – ₹23L")
    ],
    "Bhopal": [
        ("Electrical / Production Engineer (BHEL Bhopal)", "Senior Manager / AGM Executive Promotion (E4)", "7–12 Years", "₹9L – ₹14L", "₹18L – ₹26L"),
        ("Industrial Plant Engineer (Mandideep HEG/P&G)", "Plant Operations Head / Sourcing Director", "6–10 Years", "₹8L – ₹12L", "₹18L – ₹26L"),
        ("State Power Utility Officer (MPPGCL)", "Executive Superintendent Engineer", "6–11 Years", "₹8L – ₹13L", "₹17L – ₹25L"),
        ("Commercial Bank Credit Manager", "Zonal Head - Commercial Lending", "5–9 Years", "₹8L – ₹13L", "₹17L – ₹24L"),
        ("IT / Systems Support Lead", "Enterprise Digital Transformation Strategist", "4–8 Years", "₹7L – ₹11L", "₹16L – ₹23L")
    ]
}

cities = [
    {
        "meta": jpr.get_jaipur_meta(),
        "faqs": jpr.get_jaipur_faqs(),
        "content": jpr.get_jaipur_content(),
        "city_key": "Jaipur"
    },
    {
        "meta": lko.get_lucknow_meta(),
        "faqs": lko.get_lucknow_faqs(),
        "content": lko.get_lucknow_content(),
        "city_key": "Lucknow"
    },
    {
        "meta": chd.get_chandigarh_meta(),
        "faqs": chd.get_chandigarh_faqs(),
        "content": chd.get_chandigarh_content(),
        "city_key": "Chandigarh"
    },
    {
        "meta": amd.get_ahmedabad_meta(),
        "faqs": amd.get_ahmedabad_faqs(),
        "content": amd.get_ahmedabad_content(),
        "city_key": "Ahmedabad"
    },
    {
        "meta": idr.get_indore_meta(),
        "faqs": idr.get_indore_faqs(),
        "content": idr.get_indore_content(),
        "city_key": "Indore"
    },
    {
        "meta": bpl.get_bhopal_meta(),
        "faqs": bpl.get_bhopal_faqs(),
        "content": bpl.get_bhopal_content(),
        "city_key": "Bhopal"
    }
]

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

def build_schema(meta, faqs):
    faq_schema_items = []
    for q, a in faqs:
        faq_schema_items.append({
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
                        "name": f"Online MBA in {meta['city_name']} 2027",
                        "item": meta['canonical_url']
                    }
                ]
            },
            {
                "@type": "BlogPosting",
                "headline": meta['title'],
                "description": meta['meta_desc'],
                "image": "https://www.onlinembaadmission.com/logo.png",
                "datePublished": "2026-11-17T11:00:00+05:30",
                "dateModified": "2026-11-17T13:45:00+05:30",
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
                    "@id": meta['canonical_url']
                }
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_schema_items
            }
        ]
    }
    return json.dumps(schema, indent=2)

def assemble_page(c_data):
    meta = c_data["meta"]
    faqs = c_data["faqs"]
    base_content = c_data["content"]
    city_key = c_data["city_key"]
    
    toc = build_full_toc(meta["city_name"])
    
    # Enhanced rich content assembly
    curriculum_html = get_shared_curriculum_blueprint()
    deep_profiles_html = get_deep_university_profiles()
    financial_html = get_financial_and_scholarship_guide(meta["city_name"])
    matrix_html = get_career_matrix(meta["city_name"], career_matrices[city_key])
    
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
    
    schema_json = build_schema(meta, faqs)
    header_html = get_shared_header_and_critical_css(
        title=meta["title"],
        meta_desc=meta["meta_desc"],
        keywords=meta["keywords"],
        canonical_url=meta["canonical_url"],
        schema_json=schema_json
    )
    footer_html = get_shared_footer()
    
    breadcrumb_html = make_breadcrumb(meta["city_name"], meta["city_slug"])
    hero_html = make_hero(meta["city_name"], meta["primary_kw"])
    mobile_toc_html = f"""      <!-- Mobile Table of Contents -->
      <div class="mobile-toc-card">
        {make_toc(toc)}
      </div>"""
    desktop_toc_html = make_toc(toc)
    faq_html = make_faq_section(faqs)
    bottom_form_html = make_bottom_conversion_form(meta["city_name"])
    sidebar_html = make_sidebar(meta["city_name"], toc)
    
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

# Main execution loop
output_dir = "blogs"
generated_files = []

for c in cities:
    meta = c["meta"]
    filename = f"{meta['city_slug']}.html"
    filepath = os.path.join(output_dir, filename)
    
    print(f"Generating full expanded {filepath} for {meta['city_name']}...")
    html_content = assemble_page(c)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    generated_files.append((filepath, meta))

print(f"\nSuccessfully generated {len(generated_files)} Priority 3 expanded city blog files.")
