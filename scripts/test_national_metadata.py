items = [
    ('Topic 6', 'Government Online MBA Universities in India: Fees 2027', 'Compare top government online MBA universities in India for 2027. Review IGNOU, state open universities, low fees under ₹50,000 & 0% EMI. Check eligibility.'),
    ('Topic 9', 'Online MBA After BCom: Top Universities & Careers 2027', 'Explore the best online MBA after BCom in 2027. Compare top UGC-DEB universities, finance and corporate specializations, fees & 0% EMI. Check eligibility.'),
    ('Topic 10', 'Online MBA Finance vs Marketing vs HR: Which Is Best 2027?', 'Compare Online MBA in Finance vs Marketing vs HR for 2027. Review career scopes, syllabus differences, top UGC-DEB colleges & salaries. Check eligibility.'),
    ('Topic 12', 'Online MBA vs Regular MBA: Fees & Recognition 2027', 'Online MBA vs Regular MBA comparison for 2027. Review total costs, UGC-DEB degree parity under Gazette 2020, ROI and corporate placements. Check eligibility.'),
    ('Topic 4', 'Is an Online MBA Valid in India? UGC-DEB Rules & Law 2027', 'Is an online MBA valid in India? Explore UGC-DEB entitlements, Gazette 2020 Regulation 22 legal parity for govt jobs, PSUs and WES. Check eligibility.')
]
for top, t, m in items:
    tl = len(t)
    ml = len(m)
    t_ok = 50 <= tl <= 60
    m_ok = 150 <= ml <= 160
    cta_ok = m.endswith("Check eligibility.")
    print(f"{top:10} | Title: {tl} chars ({t_ok}) | Meta: {ml} chars ({m_ok}) | CTA: {cta_ok}")
