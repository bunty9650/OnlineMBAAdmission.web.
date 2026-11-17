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
import data_priority2_bangalore as bng
import data_priority2_mumbai as mum
import data_priority2_pune as pun
import data_priority2_hyderabad as hyd
import data_priority2_chennai as chn
import data_priority2_kolkata as kol

# Import expansion modules
from priority2_expansion import (
    get_shared_curriculum_blueprint,
    get_deep_university_profiles,
    get_financial_and_scholarship_guide,
    get_career_matrix
)

career_matrices = {
    "Bangalore": [
        ("Senior Software Engineer / Tech Lead", "Technical Product Manager (TPM)", "4–7 Years", "₹14L – ₹18L", "₹26L – ₹36L"),
        ("QA / Test Automation Architect", "Engineering Program Manager (EPM)", "5–9 Years", "₹12L – ₹16L", "₹22L – ₹30L"),
        ("Data Analyst / BI Developer", "Lead Data Strategist / Head of Analytics", "3–6 Years", "₹9L – ₹14L", "₹18L – ₹26L"),
        ("Cloud Operations / DevOps Lead", "Cloud Solutions Delivery Director", "6–10 Years", "₹11L – ₹15L", "₹24L – ₹32L"),
        ("Startup Growth Associate", "VP of Growth & Product Strategy", "4–8 Years", "₹10L – ₹15L", "₹25L – ₹38L")
    ],
    "Mumbai": [
        ("Credit Risk / Loan Underwriter", "Associate VP - Corporate Lending", "4–7 Years", "₹11L – ₹16L", "₹24L – ₹35L"),
        ("Equity Research Associate", "Portfolio Manager / Investment Strategist", "5–8 Years", "₹14L – ₹20L", "₹28L – ₹42L"),
        ("Chartered Accountant (Audit)", "Finance Controller / Head of Accounts", "3–6 Years", "₹12L – ₹18L", "₹25L – ₹38L"),
        ("Media Planner / Advertising Supervisor", "Vice President - Brand Marketing", "5–9 Years", "₹10L – ₹15L", "₹22L – ₹32L"),
        ("Retail Branch Manager (BFSI)", "Regional Zonal Head - Commercial Banking", "7–12 Years", "₹13L – ₹18L", "₹26L – ₹36L")
    ],
    "Pune": [
        ("Production / Shop-Floor Engineer", "Plant Operations Head / General Manager", "6–10 Years", "₹8L – ₹13L", "₹20L – ₹30L"),
        ("Automotive Tooling / Design Lead", "Strategic Global Sourcing Director", "5–9 Years", "₹10L – ₹15L", "₹22L – ₹32L"),
        ("IT Software Developer (Hinjawadi)", "IT Project Manager / Product Owner", "4–7 Years", "₹11L – ₹16L", "₹22L – ₹30L"),
        ("Supply Chain / Logistics Coordinator", "Head of Global Logistics & Procurement", "5–8 Years", "₹9L – ₹14L", "₹19L – ₹28L"),
        ("Plant Quality Assurance Engineer", "Director - Total Quality Management (TQM)", "6–10 Years", "₹9L – ₹14L", "₹21L – ₹31L")
    ],
    "Hyderabad": [
        ("Cloud / DevOps Engineer", "Technical Product Manager (Cloud Platforms)", "4–7 Years", "₹13L – ₹18L", "₹25L – ₹35L"),
        ("Pharma R&D Scientist (Genome Valley)", "Clinical Project Director / Regulatory Head", "5–9 Years", "₹10L – ₹15L", "₹22L – ₹32L"),
        ("Full-Stack Software Developer", "Director of Software Engineering", "6–10 Years", "₹14L – ₹20L", "₹28L – ₹40L"),
        ("QA / Compliance Lead (Pharma)", "VP - Global Pharma Supply Chain Operations", "6–11 Years", "₹11L – ₹16L", "₹24L – ₹34L"),
        ("IT Business Analyst (HITEC City)", "Strategic Enterprise Management Consultant", "4–7 Years", "₹10L – ₹15L", "₹21L – ₹29L")
    ],
    "Chennai": [
        ("Auto Assembly Engineer (Sriperumbudur)", "General Manager - Plant Manufacturing", "6–10 Years", "₹9L – ₹14L", "₹22L – ₹32L"),
        ("SaaS Customer Success Lead", "Director of Customer Experience & Growth", "4–8 Years", "₹10L – ₹16L", "₹24L – ₹35L"),
        ("Logistics & Freight Officer (Chennai Port)", "VP of Maritime Freight & Global Trade", "5–9 Years", "₹8L – ₹13L", "₹18L – ₹28L"),
        ("Mechanical Tooling Engineer", "Strategic Sourcing & Procurement Head", "5–8 Years", "₹9L – ₹14L", "₹20L – ₹30L"),
        ("Software Engineer (OMR SaaS Corridor)", "SaaS Technical Product Lead", "4–7 Years", "₹11L – ₹16L", "₹23L – ₹32L")
    ],
    "Kolkata": [
        ("Public Sector Officer (Scale 1/2)", "Executive Manager / Scale 3 Promotion", "5–10 Years", "₹8L – ₹12L", "₹15L – ₹22L"),
        ("Senior Software Engineer (Salt Lake)", "IT Program Delivery Manager", "5–8 Years", "₹10L – ₹15L", "₹20L – ₹28L"),
        ("Commercial Bank Credit Manager", "Zonal Credit Head - Eastern Region", "6–10 Years", "₹9L – ₹14L", "₹18L – ₹26L"),
        ("FMCG Distribution Area Manager", "Regional Sales & Marketing Director", "6–11 Years", "₹11L – ₹16L", "₹22L – ₹32L"),
        ("Industrial Plant Supervisor", "Head of Supply Chain & Operations", "5–9 Years", "₹7L – ₹11L", "₹16L – ₹24L")
    ]
}

cities = [
    {
        "meta": bng.get_bangalore_meta(),
        "faqs": bng.get_bangalore_faqs(),
        "content": bng.get_bangalore_content(),
        "city_key": "Bangalore"
    },
    {
        "meta": mum.get_mumbai_meta(),
        "faqs": mum.get_mumbai_faqs(),
        "content": mum.get_mumbai_content(),
        "city_key": "Mumbai"
    },
    {
        "meta": pun.get_pune_meta(),
        "faqs": pun.get_pune_faqs(),
        "content": pun.get_pune_content(),
        "city_key": "Pune"
    },
    {
        "meta": hyd.get_hyderabad_meta(),
        "faqs": hyd.get_hyderabad_faqs(),
        "content": hyd.get_hyderabad_content(),
        "city_key": "Hyderabad"
    },
    {
        "meta": chn.get_chennai_meta(),
        "faqs": chn.get_chennai_faqs(),
        "content": chn.get_chennai_content(),
        "city_key": "Chennai"
    },
    {
        "meta": kol.get_kolkata_meta(),
        "faqs": kol.get_kolkata_faqs(),
        "content": kol.get_kolkata_content(),
        "city_key": "Kolkata"
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
                "datePublished": "2026-11-17T10:00:00+05:30",
                "dateModified": "2026-11-17T13:30:00+05:30",
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

print(f"\nSuccessfully generated {len(generated_files)} Priority 2 expanded city blog files.")
