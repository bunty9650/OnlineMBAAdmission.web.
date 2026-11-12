import json

with open('scripts/items_to_optimize.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

meta_map = {}

# -------------------------------------------------------------
# 1. ROOT PAGES (8)
# -------------------------------------------------------------
meta_map['https://www.onlinembaadmission.com/universities'] = {
    'title': 'Top Online MBA Universities in India 2027: Fees & List', # 54
    'desc': "Compare top UGC-DEB approved Online MBA universities in India for 2027: check fees, NAAC A++ grades, rankings, eligibility, and approvals. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/specializations'] = {
    'title': 'Top Online MBA Specializations 2027: Syllabus & Salary', # 54
    'desc': "Explore top 18 Online MBA specializations in India for 2027: Finance, Marketing, HR, Operations, Analytics & IT. Compare curricula and fees. Check eligibility." # 159
}
meta_map['https://www.onlinembaadmission.com/fees'] = {
    'title': 'Online MBA Fee Structure 2027: Low Cost & No-Cost EMI', # 53
    'desc': "Check Online MBA fees for 200+ Indian universities in 2027. Compare semester fees from ₹15,000, 0% EMI plans, scholarships, and fee structures. Apply now." # 154
}
meta_map['https://www.onlinembaadmission.com/eligibility'] = {
    'title': 'Online MBA Eligibility Criteria 2027: Direct Admission', # 54
    'desc': "Check complete Online MBA eligibility criteria in India for 2027: 50% graduation marks, CAT/MAT exemptions, executive norms, and documents. Check eligibility." # 158
}
meta_map['https://www.onlinembaadmission.com/about'] = {
    'title': "About Us: India's Trusted Online MBA Admission Portal", # 53
    'desc': "About Online MBA Admission: India's premier higher education advisory guiding 50,000+ professionals with 100% unbiased counseling & reviews. Check eligibility." # 159
}
meta_map['https://www.onlinembaadmission.com/privacy'] = {
    'desc': "Official Privacy Policy of Online MBA Admission. Learn how user enquiry details are securely collected and safeguarded under DPDP Act 2023. Check eligibility." # 159
}
meta_map['https://www.onlinembaadmission.com/terms'] = {
    'desc': "Official Terms of Service and legal disclaimer for Online MBA Admission. Understand our independent education advisory scope and user policies. Apply now." # 154
}
meta_map['https://www.onlinembaadmission.com/blogs'] = {
    'title': 'Online MBA Admission Blogs & Guides 2027: Fees and ROI' # 54
}

# -------------------------------------------------------------
# 2. PAGINATION PAGES (10)
# -------------------------------------------------------------
for p in range(2, 12):
    meta_map[f"https://www.onlinembaadmission.com/blogs/page-{p}"] = {
        'title': f"Online MBA Admission Blogs & Guides: Page {p} (2027)" # 51 or 52
    }

# -------------------------------------------------------------
# 3. SPECIALIZATION HUB PAGES (18)
# -------------------------------------------------------------
meta_map['https://www.onlinembaadmission.com/specializations/finance'] = {
    'desc': "Complete 2027 guide to Online MBA in Finance in India. Compare top UGC-DEB universities, syllabus, fees, placement packages & roles. Check eligibility." # 152
}
meta_map['https://www.onlinembaadmission.com/specializations/business-analytics'] = {
    'desc': "Complete 2027 guide to Online MBA in Business Analytics. Compare top UGC-DEB universities, Python syllabus, tools, fees, and top salaries. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/specializations/information-technology'] = {
    'desc': "Complete 2027 guide to Online MBA in IT in India. Compare top UGC-DEB approved universities, cloud architecture syllabus, fees, and top salaries. Apply now." # 156
}
meta_map['https://www.onlinembaadmission.com/specializations/international-business'] = {
    'desc': "Complete 2027 guide to Online MBA in International Business. Compare top UGC-DEB universities, global trade syllabus, fees, and salaries. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/specializations/supply-chain-management'] = {
    'desc': "Complete 2027 guide to Online MBA in Supply Chain Management. Compare top UGC-DEB approved universities, logistics syllabus, fees & scope. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/specializations/healthcare-management'] = {
    'desc': "Complete 2027 guide to Online MBA in Healthcare Management. Compare top UGC-DEB universities, hospital admin syllabus, fees, and salaries. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/specializations/data-science'] = {
    'desc': "Complete 2027 guide to Online MBA in Data Science and AI. Compare top UGC-DEB universities, machine learning syllabus, fees, and salaries. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/specializations/entrepreneurship'] = {
    'desc': "Complete 2027 guide to Online MBA in Entrepreneurship in India. Compare top UGC-DEB universities, venture syllabus, fees, and founder scope. Apply now." # 152
}
meta_map['https://www.onlinembaadmission.com/specializations/logistics-management'] = {
    'desc': "Complete 2027 guide to Online MBA in Logistics Management in India. Compare top UGC-DEB universities, freight syllabus, fees, and salaries. Check eligibility." # 158
}
meta_map['https://www.onlinembaadmission.com/specializations/hospital-administration'] = {
    'desc': "Complete 2027 guide to Online MBA in Hospital Administration. Compare top UGC-DEB universities, clinical syllabus, fees, and salaries. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/specializations/general-management'] = {
    'desc': "Complete 2027 guide to Online MBA in General Management in India. Compare top UGC-DEB universities, corporate syllabus, fees, and salaries. Check eligibility." # 158
}
meta_map['https://www.onlinembaadmission.com/specializations/fintech-and-financial-services'] = {
    'title': 'Online MBA in FinTech & Financial Services 2027: Fees' # 53
}
meta_map['https://www.onlinembaadmission.com/specializations/agribusiness-management'] = {
    'title': 'Online MBA in Agribusiness Management 2027: Fees & Jobs', # 55
    'desc': "Complete 2027 guide to Online MBA in Agribusiness Management. Compare UGC-DEB universities, farm supply chain syllabus, fees, and salaries. Check eligibility." # 158
}
meta_map['https://www.onlinembaadmission.com/specializations/sustainability-and-esg-management'] = {
    'title': 'Online MBA in Sustainability & ESG Management 2027: Scope', # 57
    'desc': "Complete 2027 guide to Online MBA in Sustainability and ESG. Compare UGC-DEB elective tracks, BRSR reporting, climate risk, and fees. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/specializations/international-finance'] = {
    'desc': "Complete 2027 guide to Online MBA in International Finance. Compare UGC-DEB universities, ACCA syllabus, forex risk, fees, and salaries. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/specializations/ai-for-business'] = {
    'title': 'Online MBA in AI for Business 2027: Syllabus & Scope', # 52
    'desc': "Complete 2027 guide to Online MBA in AI for Business in India. Compare top UGC-DEB universities, generative AI syllabus, fees, and salaries. Check eligibility." # 159
}
meta_map['https://www.onlinembaadmission.com/specializations/cybersecurity-management'] = {
    'title': 'Online MBA in Cybersecurity Management 2027: Syllabus', # 53
    'desc': "Complete 2027 guide to Online MBA in Cybersecurity Management. Compare UGC-DEB elective tracks, DPDP compliance, fees, and CISO packages. Check eligibility." # 156
}
meta_map['https://www.onlinembaadmission.com/specializations/e-commerce-management'] = {
    'title': 'Online MBA in E-Commerce Management 2027: Fees & Scope', # 54
    'desc': "Complete 2027 guide to Online MBA in E-Commerce Management. Compare UGC-DEB tracks, D2C retail operations, marketplace funnels, and fees. Check eligibility." # 155
}

# -------------------------------------------------------------
# 4. UNIVERSITY SPECIALIZATIONS (55)
# -------------------------------------------------------------
# IGNOU (3)
meta_map['https://www.onlinembaadmission.com/university/ignou/mba-in-marketing'] = {
    'title': 'Online MBA in Marketing Management 2027: Syllabus | IGNOU' # 57
}
meta_map['https://www.onlinembaadmission.com/university/ignou/mba-in-finance'] = {
    'title': 'Online MBA in Financial Management 2027: Syllabus | IGNOU' # 57
}
meta_map['https://www.onlinembaadmission.com/university/ignou/mba-in-banking-and-finance'] = {
    'title': 'Online MBA in Banking and Finance 2027: Syllabus | IGNOU' # 56
}

# AMITY (13)
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-marketing-and-sales'] = {
    'title': 'Online MBA in Marketing & Sales 2027 | Amity Online', # 51
    'desc': "Explore Online MBA in Marketing and Sales at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and eligibility. Check eligibility." # 152
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-finance-and-accounting'] = {
    'title': 'Online MBA in Finance & Accounting 2027 | Amity Online', # 54
    'desc': "Explore Online MBA in Finance & Accounting at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-human-resource-management'] = {
    'title': 'Online MBA in Human Resource Management 2027 | Amity', # 52
    'desc': "Explore Online MBA in Human Resource Management at Amity University Online. Check UGC-DEB 2027 curriculum, fees, eligibility, and scope. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-digital-marketing'] = {
    'title': 'Online MBA in Digital Marketing 2027 | Amity Online', # 51
    'desc': "Explore Online MBA in Digital Marketing at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and counselor review. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-business-analytics'] = {
    'desc': "Explore Online MBA in Business Analytics at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 151
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-information-technology'] = {
    'title': 'Online MBA in Information Technology 2027 | Amity Online', # 56
    'desc': "Explore Online MBA in Information Technology at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-operations-management'] = {
    'title': 'Online MBA in Operations Management 2027 | Amity Online', # 55
    'desc': "Explore Online MBA in Operations Management at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-international-business'] = {
    'title': 'Online MBA in International Business 2027 | Amity Online', # 56
    'desc': "Explore Online MBA in International Business at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-retail-management'] = {
    'desc': "Explore Online MBA in Retail Management at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, eligibility, and scope. Check eligibility." # 156
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-entrepreneurship-and-leadership'] = {
    'title': 'Online MBA in Entrepreneurship 2027 | Amity Online', # 50
    'desc': "Explore Online MBA in Entrepreneurship & Leadership at Amity University Online. Check UGC-DEB 2027 curriculum, fees, and career scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-hospital-and-healthcare'] = {
    'title': 'Online MBA in Hospital & Healthcare 2027 | Amity Online', # 55
    'desc': "Explore Online MBA in Hospital and Healthcare at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 156
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-international-finance'] = {
    'title': 'Online MBA in International Finance 2027 | Amity Online', # 55
    'desc': "Explore Online MBA in International Finance at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/amity/mba-in-general-management'] = {
    'desc': "Explore Online MBA in General Management at Amity University Online. Check UGC-DEB approved 2027 curriculum, fees, eligibility, and scope. Check eligibility." # 157
}

# MANIPAL JAIPUR (12)
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-marketing'] = {
    'desc': "Explore Online MBA in Marketing at Manipal University Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and admissions guide. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-human-resource-management'] = {
    'title': 'Online MBA in Human Resource Management 2027 | Manipal', # 54
    'desc': "Explore Online MBA in Human Resource Management at Manipal Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-analytics-and-data-science'] = {
    'title': 'Online MBA in Analytics & Data Science 2027 | Manipal', # 53
    'desc': "Explore Online MBA in Analytics & Data Science at Manipal Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-it-and-fintech'] = {
    'title': 'Online MBA in IT & FinTech 2027 | Manipal Jaipur (MUJ)', # 54
    'desc': "Explore Online MBA in IT & FinTech at Manipal University Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-operations-management'] = {
    'title': 'Online MBA in Operations Management 2027 | Manipal MUJ', # 54
    'desc': "Explore Online MBA in Operations Management at Manipal Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-international-business'] = {
    'title': 'Online MBA in International Business 2027 | Manipal MUJ', # 55
    'desc': "Explore Online MBA in International Business at Manipal Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 152
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-information-system-management'] = {
    'title': 'Online MBA in Information Systems 2027 | Manipal MUJ', # 52
    'desc': "Explore Online MBA in Information Systems Management at Manipal Jaipur (MUJ). Check UGC-DEB 2027 curriculum, fees, and career scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-project-management'] = {
    'title': 'Online MBA in Project Management 2027 | Manipal Jaipur', # 54
    'desc': "Explore Online MBA in Project Management at Manipal Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career pathways. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-supply-chain-management'] = {
    'title': 'Online MBA in Supply Chain Management 2027 | Manipal', # 52
    'desc': "Explore Online MBA in Supply Chain Management at Manipal Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-bfsi'] = {
    'title': 'Online MBA in BFSI Management 2027 | Manipal Jaipur MUJ', # 55
    'desc': "Explore Online MBA in BFSI at Manipal University Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, eligibility, and career roles. Apply online." # 152
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-digital-marketing'] = {
    'title': 'Online MBA in Digital Marketing 2027 | Manipal Jaipur', # 53
    'desc': "Explore Online MBA in Digital Marketing at Manipal University Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and admissions. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-retail-management'] = {
    'title': 'Online MBA in Retail Management 2027 | Manipal Jaipur', # 52
    'desc': "Explore Online MBA in Retail Management at Manipal University Jaipur (MUJ). Check UGC-DEB approved 2027 curriculum, fees, and admissions. Check eligibility." # 154
}

# GLA (2)
meta_map['https://www.onlinembaadmission.com/university/gla/mba-in-human-resource-management'] = {
    'desc': "Explore Online MBA in Human Resource Management at GLA University. Check UGC-DEB approved 2027 curriculum, fees, eligibility & scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/gla/mba-in-banking-and-financial-services'] = {
    'title': 'Online MBA in Banking & Finance 2027 | GLA University', # 53
    'desc': "Explore Online MBA in Banking & Financial Services at GLA University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 152
}

# ANDHRA UNIVERSITY (1)
meta_map['https://www.onlinembaadmission.com/university/andhra-university/mba-in-human-resource-management'] = {
    'desc': "Explore Online MBA in Human Resource Management at Andhra University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 153
}

# CCSU (3)
meta_map['https://www.onlinembaadmission.com/university/ccsu/mba-in-marketing'] = {
    'title': 'Online MBA in Marketing Management 2027: Syllabus | CCSU' # 56
}
meta_map['https://www.onlinembaadmission.com/university/ccsu/mba-in-finance'] = {
    'title': 'Online MBA in Financial Management 2027: Syllabus | CCSU' # 56
}
meta_map['https://www.onlinembaadmission.com/university/ccsu/mba-in-operations-management'] = {
    'title': 'Online MBA in Operations Management 2027: Syllabus | CCSU' # 57
}

# ARKA JAIN (5)
meta_map['https://www.onlinembaadmission.com/university/arka-jain/mba-in-human-resource-management'] = {
    'title': 'Online MBA in Human Resource Management 2027 | Arka Jain', # 56
    'desc': "Explore Online MBA in Human Resource Management at Arka Jain University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/arka-jain/mba-in-information-technology'] = {
    'desc': "Explore Online MBA in Information Technology at Arka Jain University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 152
}
meta_map['https://www.onlinembaadmission.com/university/arka-jain/mba-in-operations-supply-chain'] = {
    'title': 'Online MBA in Operations & Supply Chain 2027 | Arka Jain', # 56
    'desc': "Explore Online MBA in Operations & Supply Chain at Arka Jain University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/arka-jain/mba-in-data-analytics-ai'] = {
    'desc': "Explore Online MBA in Data Analytics & AI at Arka Jain University. Check UGC-DEB approved 2027 curriculum, fees, eligibility & scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/arka-jain/mba-in-healthcare-management'] = {
    'desc': "Explore Online MBA in Healthcare Management at Arka Jain University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 151
}

# PARUL (3)
meta_map['https://www.onlinembaadmission.com/university/parul/mba-in-human-resource-management'] = {
    'desc': "Explore Online MBA in Human Resource Management at Parul University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 151
}
meta_map['https://www.onlinembaadmission.com/university/parul/mba-in-digital-marketing-and-sales'] = {
    'desc': "Explore Online MBA in Digital Marketing & Sales at Parul University. Check UGC-DEB approved 2027 curriculum, fees, and career scope. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/parul/mba-in-healthcare-and-hospital'] = {
    'title': 'Online MBA in Healthcare & Hospital 2027 | Parul Univ', # 53
    'desc': "Explore Online MBA in Healthcare & Hospital at Parul University. Check UGC-DEB approved 2027 curriculum, fees, eligibility, and scope. Check eligibility." # 153
}

# DSU (8)
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-financial-management'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in Finance 2027. UGC entitled, NAAC A+ accredited, valuation, risk hedging & admissions. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-human-resource-management'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in HRM 2027. UGC entitled, NAAC A+ accredited, talent acquisition, HR metrics & fees. Check eligibility." # 151
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-marketing-management'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in Marketing 2027. UGC entitled, NAAC A+, brand management, consumer analytics & fees. Check eligibility." # 151
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-it-and-systems-management'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in IT & Systems 2027. UGC entitled, NAAC A+, cloud governance, IT project fees & scope. Check eligibility." # 153
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-supply-chain-management'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in Supply Chain 2027. UGC entitled, NAAC A+, procurement, logistics, curriculum & fees. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-entrepreneurship'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in Entrepreneurship 2027. UGC entitled, NAAC A+, venture funding, startup incubators & fees. Check eligibility." # 157
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-business-analytics'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in Business Analytics 2027. UGC entitled, NAAC A+, predictive models, dashboards & fees. Check eligibility." # 154
}
meta_map['https://www.onlinembaadmission.com/university/dsu/mba-in-artificial-intelligence'] = {
    'desc': "Explore Dayananda Sagar University Online MBA in Artificial Intelligence 2027. UGC entitled, NAAC A+, enterprise AI, curriculum & fees. Check eligibility." # 155
}

# JAMIA HAMDARD (5)
meta_map['https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-marketing-management'] = {
    'desc': "Explore Jamia Hamdard Online MBA in Marketing Management 2027. UGC entitled, NAAC A+ accredited, brand strategy, consumer analytics & fees. Apply now." # 151
}
meta_map['https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-finance-management'] = {
    'desc': "Explore Jamia Hamdard Online MBA in Finance Management 2027. UGC entitled, NAAC A+ accredited, corporate valuation, risk hedging & fees. Check eligibility." # 155
}
meta_map['https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-international-business'] = {
    'desc': "Explore Jamia Hamdard Online MBA in International Business 2027. UGC entitled, NAAC A+ accredited, global market expansion, trade law & fees. Apply now." # 153
}
meta_map['https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-business-ai'] = {
    'desc': "Explore Jamia Hamdard Online MBA in Business AI 2027. UGC entitled, NAAC A+ accredited, enterprise AI strategy, predictive modeling & fees. Apply now." # 150
}
meta_map['https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-logistics-and-supply-chain-management'] = {
    'title': 'Online MBA in Logistics & Supply Chain | Jamia Hamdard', # 54
    'desc': "Explore Jamia Hamdard Online MBA in Logistics & Supply Chain 2027. UGC entitled, NAAC A+ accredited, procurement, warehouse automation & fees. Apply now." # 153
}

# -------------------------------------------------------------
# 5. BLOG ARTICLES (79)
# -------------------------------------------------------------
blog_data = {
    'online-mba': {
        'title': 'Online MBA Guide 2027: Approvals, Top Programs & Fees' # 53
    },
    'online-mba-admission': {
        'title': 'Online MBA Admission 2027: Direct Process & Colleges' # 52
    },
    'online-mba-admission-2026': {
        'title': 'Online MBA Admission 2027: Batch Dates & Apply Online' # 53
    },
    'online-mba-admission-open': {
        'title': 'Online MBA Admission Open 2027: Current Batches & Form' # 54
    },
    'best-online-mba': {
        'title': 'Best Online MBA Programs 2027: 7 Top Selection Factors' # 54
    },
    'online-mba-admission-process': {
        'title': 'Online MBA Admission Process: 5-Step Digital Roadmap' # 52
    },
    'online-mba-in-india': {
        'title': 'Online MBA in India 2027: Approvals & Top Colleges Fee' # 54
    },
    'online-mba-application': {
        'title': 'Online MBA Application Form 2027: How to Apply Online' # 53
    },
    'online-mba-enrollment': {
        'title': 'Online MBA Enrollment Guide 2027: Process & Documents' # 53
    },
    'online-mba-admissions': {
        'title': 'Online MBA Admissions 2027: Top Universities & Portal' # 53
    },
    'online-mba-admission-last-date': {
        'title': 'Online MBA Admission Last Date 2027: All Univ Deadlines' # 55
    },
    'online-mba-admission-deadline': {
        'title': 'Online MBA Admission Deadline 2027: Seats & Dates List' # 54
    },
    'online-mba-admission-2027': {
        'title': 'Online MBA Admission 2027: Early Registration & Fees' # 52
    },
    'best-online-mba-in-india': {
        'title': 'Best Online MBA in India: Top 10 Colleges and Fees 2027' # 55
    },
    'online-mba-colleges': {
        'title': 'Online MBA Colleges 2027: Fees, Eligibility & Direct ROI' # 56
    },
    'online-mba-degree': {
        'title': 'Online MBA Degree 2027: Validity, Certificate & Scope' # 53
    },
    'online-mba-degree-in-india': {
        'title': 'Online MBA Degree in India 2027: Validity & Fee Guide' # 53
    },
    'online-mba-course-in-india': {
        'title': 'Online MBA Course in India 2027: Fees, Scope & Syllabus' # 55
    },
    'best-online-mba-colleges': {
        'title': 'Best Online MBA Colleges 2027: Rankings & Admissions' # 52
    },
    'best-online-mba-colleges-in-india': {
        'title': 'Best Online MBA Colleges in India: Fees and Placements' # 54
    },
    'best-online-mba-university': {
        'title': 'Best Online MBA University 2027: How to Choose Wisely' # 53
    },
    'best-online-mba-universities-in-india': {
        'title': 'Best Online MBA Universities in India: Top Ranked List' # 54
    },
    'top-online-mba-colleges': {
        'title': 'Top Online MBA Colleges 2027: Salaries & Highest Scope' # 54
    },
    'top-online-mba-colleges-in-india': {
        'title': 'Top Online MBA Colleges in India: 2027 Admission Guide' # 54
    },
    'ugc-deb-approval-guide': {
        'title': 'How to Verify UGC-DEB Approval on deb.ugc.ac.in (2027)' # 54
    },
    'direct-admission-without-cat': {
        'title': 'Online MBA Without CAT: Top Direct Admission Colleges' # 53
    },
    'online-vs-distance-mba': {
        'title': 'Online MBA vs Distance MBA: 6 Crucial Differences 2027', # 54
        'desc': "Compare Online MBA vs Distance MBA. Discover critical differences in cloud LMS, weekend live classes, web exams, and recruiter perception. Check eligibility." # 158
    },
    'highest-paying-specializations': {
        'title': 'Highest Paying Online MBA Specializations in India 2027' # 55
    },
    'no-cost-emi-guide': {
        'title': 'Online MBA Fees with 0% No-Cost EMI: 2027 Loan Guide', # 52
        'desc': "Guide to Online MBA No-Cost EMI financing 2027. Learn how to fund your degree from ₹2,258/month with 0% interest and zero down payment. Check eligibility." # 155
    },
    'is-online-mba-valid-govt-jobs': {
        'title': 'Is Online MBA Valid for Govt Jobs, UPSC & PSUs? (2027)' # 54
    },
    'online-mba-admission-requirements': {
        'title': 'Online MBA Admission Requirements 2027: All Documents' # 53
    },
    'online-mba-direct-admission': {
        'title': 'Online MBA Direct Admission 2027: No CAT & Top College' # 54
    },
    'online-mba-college-admission': {
        'title': 'Online MBA College Admission 2027: Top Selection Guide' # 54
    },
    'online-mba-admission-form': {
        'title': 'Online MBA Admission Form 2027: Portal Guide & Upload' # 53
    },
    'online-mba-counselling': {
        'title': 'Online MBA Counselling 2027: Free University Advisory' # 53
    },
    'online-mba-admission-counselling': {
        'title': 'Online MBA Admission Counselling 2027: Expert Guidance' # 54
    },
    'online-mba-fees': {
        'title': 'Online MBA Fees 2027: Top 10 Universities & 0% EMI Plan', # 55
        'desc': "Complete guide to online MBA fees 2027. Compare transparent tuition costs from ₹47,000 to ₹2,25,000 across top UGC-DEB universities. Check eligibility." # 152
    },
    'online-mba-fees-in-india': {
        'title': 'Online MBA Fees in India 2027: Cost Analysis & Checklist' # 56
    },
    'online-mba-course-fees': {
        'title': 'Online MBA Course Fees 2027: Tuition and Exam Installment' # 57
    },
    'online-mba-fees-structure': {
        'title': 'Online MBA Fees Structure 2027: Semester & Annual Breakdown' # 59
    },
    'online-mba-semester-fees': {
        'title': 'Online MBA Semester Fees 2027: Pay-Per-Term Cost Analysis' # 57
    },
    'online-mba-total-fees': {
        'title': 'Online MBA Total Fees 2027: 2-Year Complete Cost Guide' # 54
    },
    'online-mba-fee-structure': {
        'title': 'Online MBA Fee Structure 2027: Compare All Universities' # 55
    },
    'online-mba-admission-fees': {
        'title': 'Online MBA Admission Fees 2027: Registration & Seat EMI' # 55
    },
    'online-mba-affordable-fees': {
        'title': 'Affordable Online MBA Fees 2027: Programs from ₹45,000' # 54
    },
    'affordable-online-mba': {
        'title': 'Affordable Online MBA 2027: Best Low-Cost UGC Programs' # 54
    },
    'affordable-online-mba-in-india': {
        'title': 'Affordable Online MBA in India 2027: Low Budget Guide' # 53
    },
    'low-fee-online-mba': {
        'title': 'Low Fee Online MBA Programs 2027: Accredited Degrees List' # 57
    },
    'cheap-online-mba': {
        'title': 'Cheap Online MBA Programs in India: Avoid Scams 2027' # 52
    },
    'online-mba-under-50000': {
        'title': 'Online MBA Under ₹50,000: Top Govt Universities 2027' # 53
    },
    'online-mba-under-1-lakh': {
        'title': 'Online MBA Under ₹1 Lakh: Best Value UGC Programs 2027' # 54
    },
    'online-mba-scholarship': {
        'desc': "Discover online MBA scholarship schemes for 2027. Explore up to 30% tuition waivers for merit, defense, women, and alumni across top colleges. Apply now." # 154
    },
    'online-mba-scholarship-in-india': {
        'title': 'Online MBA Scholarship in India 2027: Financial Grants' # 54
    },
    'online-mba-eligibility': {
        'desc': "Learn complete online MBA eligibility for 2027. Review graduation cutoffs (50%/45%), stream neutrality, entrance exam waivers & norms. Check eligibility." # 154
    },
    'online-mba-eligibility-criteria': {
        'desc': "Comprehensive review of online MBA eligibility criteria 2027. Compare university cutoffs, AIU equivalence, relaxations, and documents. Check eligibility." # 154
    },
    'online-mba-qualification': {
        'title': 'Online MBA Qualification 2027: Degrees & Academic Norms' # 55
    },
    'online-mba-duration': {
        'title': 'Online MBA Duration in India: 2-Year Program Breakdown', # 54
        'desc': "How long is an online MBA in India? Complete 2027 guide to the 2-year duration, 4 semesters, weekly study hours, and completion rules. Check eligibility." # 154
    },
    'online-mba-2-years': {
        'title': 'Is Online MBA 2 Years Mandatory? UGC Regulations 2027' # 53
    },
    'online-mba-syllabus': {
        'title': 'Online MBA Syllabus 2027: Core & Elective Subjects List', # 55
        'desc': "Explore the complete 4-semester online MBA syllabus for 2027. Review core subjects, elective tracks, credits, and capstone guidelines. Check eligibility." # 155
    },
    'online-mba-subjects': {
        'title': 'Online MBA Subjects List 2027: Core & Elective Modules', # 54
        'desc': "Master list of online MBA subjects for 2027. Discover core foundation courses, functional management papers, and popular elective tracks. Check eligibility." # 156
    },
    'online-mba-exams': {
        'title': 'Online MBA Exams 2027: AI Proctoring & Pattern Rules' # 52
    },
    'how-long-is-online-mba': {
        'title': 'How Long is an Online MBA? 2-Year Timeline & Study Hours', # 56
        'desc': "How long is an online MBA in India? Discover the statutory 24-month duration, 10-12 weekly study hours, batch cycles, and degree rules. Check eligibility." # 154
    },
    'who-can-do-online-mba': {
        'title': 'Who Can Do Online MBA? Ideal Profiles & Eligibility 2027' # 56
    },
    'who-is-eligible-for-online-mba': {
        'title': 'Who is Eligible for Online MBA? Minimum Marks & UGC 2027', # 56
        'desc': "Who is eligible for an online MBA in India 2027? Check UGC statutory marks cutoffs (50%/45%), accepted degrees, CAT waivers, and norms. Check eligibility." # 154
    },
    'how-to-do-online-mba': {
        'title': 'How to Do Online MBA: Routine, LMS & Job Balance 2027', # 53
        'desc': "How to do an online MBA successfully while working? Practical roadmap covering cloud LMS access, live weekend classes, and graduation. Check eligibility." # 154
    },
    'how-to-apply-for-online-mba': {
        'title': 'How to Apply for Online MBA 2027: Step-by-Step Guide' # 52
    },
    'online-mba-assignments': {
        'title': 'Online MBA Assignments 2027: Grading Rubrics & Rules', # 52
        'desc': "Guide to online MBA assignments for 2027. Discover Continuous Internal Assessment (CIA), 30% weightage, Turnitin rules, and scoring tips. Check eligibility." # 157
    },
    'how-are-online-mba-exams-conducted': {
        'title': 'How Are Online MBA Exams Conducted? AI Proctoring 2027' # 54
    },
    'online-mba-for-working-professionals': {
        'title': 'Online MBA for Working Professionals: Top UGC Colleges' # 54
    },
    'online-mba-for-working-people': {
        'title': 'Online MBA for Working People: Earn Degree While Working', # 56
        'desc': "Can working people manage an online MBA? Practical guide to balancing a 40-hour workweek with an accredited MBA, fees, and career growth. Check eligibility." # 157
    },
    'online-mba-for-working-professionals-in-india': {
        'title': 'Online MBA for Working Professionals in India: Top Fees' # 55
    },
    'online-mba-while-working': {
        'title': 'How to Do an Online MBA While Working: Schedule & ROI' # 53
    },
    'mba-while-working-full-time': {
        'title': 'Pursuing an MBA While Working Full Time: Timings & ROI' # 54
    },
    'online-degree-for-working-professionals': {
        'title': 'Online Degree for Working Professionals: UGC Programs', # 53
        'desc': "Discover UGC-entitled online degrees for working professionals in India. Explore Online MBA, MCA, M.Com, validity, and corporate value. Check eligibility." # 155
    },
    'best-online-degree-for-working-professionals': {
        'title': 'Best Online Degree for Working Professionals: 2027 List', # 55
        'desc': "Which is the best online degree for working professionals? Discover top-ranked postgraduate degrees, salary increments, and NAAC A++ grades. Apply now." # 152
    },
    'online-mba-for-employees': {
        'title': 'Online MBA for Employees: Corporate Sponsorship & Fees', # 54
        'desc': "Complete guide to online MBA for corporate employees. Learn about employer tuition assistance, tax savings under Sec 80E, and promotions. Check eligibility." # 157
    },
    'online-mba-for-professionals': {
        'title': 'Online MBA for Professionals: Executive Tracks & Growth', # 55
        'desc': "Comprehensive online MBA guide for seasoned professionals. Explore specializations (FinTech, AI, Analytics), networking, and career ROI. Check eligibility." # 156
    },
    'online-mba-in-bangalore': {
        'title': 'Online MBA in Bangalore 2027: Top Universities & Fees', # 53
        'desc': "Online MBA in Bangalore 2027: compare Jain University, Manipal, IGNOU, NMIMS & more. Check fees, eligibility, EMI plans, and admissions. Check eligibility." # 156
    },
    'ignou-online-mba-admission': {
        'title': 'IGNOU Online MBA Admission 2027: Last Date, Fees & Form', # 55
        'desc': "IGNOU Online MBA Admission 2027: Last date, fees Rs.64,000 total, no entrance exam, UGC approved. Complete guide to apply for IGNOU MBA. Check eligibility." # 156
    }
}

for slug, d in blog_data.items():
    meta_map[f"https://www.onlinembaadmission.com/blogs/{slug}"] = d

print("Total URLs mapped in meta_map:", len(meta_map))
