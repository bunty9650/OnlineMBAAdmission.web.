cities = [
    {
        "city": "Jaipur",
        "title": "Online MBA Colleges in Jaipur: Fees & Admission Guide 2027",  # 57 chars
        "meta": "Explore top online MBA colleges in Jaipur for 2027. Review verified UGC-DEB universities, semester fees from ₹20,000 & 0% EMI options. Check eligibility."  # 153 chars
    },
    {
        "city": "Lucknow",
        "title": "Online MBA Colleges in Lucknow: Top Universities & Fees 2027",  # 59 chars
        "meta": "Compare top online MBA colleges in Lucknow for 2027. Review UGC-DEB recognized universities, fees, eligibility & remote AI proctored exams. Check eligibility."  # 158 chars
    },
    {
        "city": "Chandigarh",
        "title": "Online MBA Colleges in Chandigarh: Fees & Top Options 2027",  # 57 chars
        "meta": "Explore best online MBA colleges in Chandigarh Tricity for 2027. Compare UGC-DEB fees, WES recognized degrees & 0% no-cost EMI plans. Check eligibility."  # 153 chars
    },
    {
        "city": "Ahmedabad",
        "title": "Online MBA Colleges in Ahmedabad: Fees & Top Options 2027",  # 57 chars
        "meta": "Compare top online MBA colleges in Ahmedabad & GIFT City for 2027. Review verified UGC-DEB fees, top electives & 0% no-cost EMI plans. Check eligibility."  # 153 chars
    },
    {
        "city": "Indore",
        "title": "Online MBA Colleges in Indore: Top Universities & Fees 2027",  # 58 chars
        "meta": "Explore best online MBA colleges in Indore for 2027. Compare UGC-DEB recognized universities, Pithampur industry tracks & 0% EMI plans. Check eligibility."  # 154 chars
    },
    {
        "city": "Bhopal",
        "title": "Online MBA Colleges in Bhopal: Fees & Admission Guide 2027",  # 57 chars
        "meta": "Compare top online MBA colleges in Bhopal for working executives in 2027. Review verified UGC-DEB fees, PSU promotional validity & EMI. Check eligibility."  # 155 chars
    }
]

for c in cities:
    t_len = len(c['title'])
    m_len = len(c['meta'])
    print(f"{c['city']}: Title={t_len} chars, Meta={m_len} chars")
    assert 50 <= t_len <= 60, f"Title out of range: {t_len}"
    assert 150 <= m_len <= 160, f"Meta out of range: {m_len}"
print("\nAll 6 Priority 3 titles and meta descriptions strictly passed length bounds!")
