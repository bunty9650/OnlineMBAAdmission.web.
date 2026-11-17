p4_metadata = [
    {
        "city": "Kanpur",
        "title": "Online MBA Colleges in Kanpur: Fees & Top Options 2027",
        "meta": "Explore top online MBA colleges in Kanpur for 2027. Compare UGC-DEB accredited universities, fees under ₹1 Lakh, 0% EMI & AI proctored exams. Check eligibility."
    },
    {
        "city": "Meerut",
        "title": "Online MBA Colleges in Meerut: Top Universities Fees 2027",
        "meta": "Compare best online MBA colleges in Meerut for working executives in 2027. Review verified UGC-DEB fees, top electives, zero-cost EMI plans. Check eligibility."
    },
    {
        "city": "Agra",
        "title": "Online MBA Colleges in Agra: Best Universities Fees 2027",
        "meta": "Discover top online MBA colleges in Agra for 2027. Compare recognized UGC-DEB universities, semester fee structures, no-cost EMI & AI exams. Check eligibility."
    },
    {
        "city": "Ludhiana",
        "title": "Online MBA Colleges in Ludhiana: Top Options & Fees 2027",
        "meta": "Best online MBA colleges in Ludhiana for business leaders in 2027. Compare top UGC-DEB universities, fees from ₹50,000 & 0% EMI plans. Check eligibility."
    },
    {
        "city": "Jodhpur",
        "title": "Online MBA Colleges in Jodhpur: Fees & Universities 2027",
        "meta": "Review top online MBA colleges in Jodhpur for 2027. Compare accredited UGC-DEB universities, affordable fees, flexible schedules & 0% EMI. Check eligibility."
    },
    {
        "city": "Surat",
        "title": "Online MBA Colleges in Surat: Fees & Top Options 2027",
        "meta": "Top online MBA colleges in Surat for corporate executives in 2027. Review verified UGC-DEB fees, export & supply chain electives with 0% EMI. Check eligibility."
    },
    {
        "city": "Nagpur",
        "title": "Online MBA Colleges in Nagpur: Top Universities Fees 2027",
        "meta": "Explore top online MBA colleges in Nagpur for working professionals in 2027. Compare UGC-DEB fees, AI proctored home exams & zero-cost EMI. Check eligibility."
    },
    {
        "city": "Visakhapatnam",
        "title": "Online MBA in Visakhapatnam: Top Universities Fees 2027",
        "meta": "Best online MBA colleges in Visakhapatnam for 2027. Compare UGC-DEB approved universities, semester fee charts, port logistics MBA & 0% EMI. Check eligibility."
    },
    {
        "city": "Coimbatore",
        "title": "Online MBA Colleges in Coimbatore: Fees & Options 2027",
        "meta": "Top online MBA colleges in Coimbatore for engineering & textile leads in 2027. Compare UGC-DEB fees, AI proctored exams & no-cost EMI plans. Check eligibility."
    },
    {
        "city": "Ranchi",
        "title": "Online MBA Colleges in Ranchi: Fees & Universities 2027",
        "meta": "Compare top online MBA colleges in Ranchi for PSU & mining professionals in 2027. Review verified UGC-DEB fees, flexible LMS & zero-cost EMI. Check eligibility."
    }
]

print("=== PRIORITY 4 METADATA VERIFICATION ===")
all_pass = True
for item in p4_metadata:
    t_len = len(item["title"])
    m_len = len(item["meta"])
    t_ok = 50 <= t_len <= 60
    m_ok = 150 <= m_len <= 160
    cta_ok = item["meta"].endswith("Check eligibility.")
    if not (t_ok and m_ok and cta_ok):
        all_pass = False
        print(f"FAILED: {item['city']} -> Title: {t_len} ({t_ok}), Meta: {m_len} ({m_ok}), CTA: {cta_ok}")
    else:
        print(f"PASS: {item['city']:15} | Title: {t_len} chars | Meta: {m_len} chars | Ends with CTA")

print("Overall:", "ALL PASSED (10/10)" if all_pass else "SOME FAILED")
