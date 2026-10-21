import os
import re
import urllib.request

slugs = [
    "top-online-mba-universities-in-india",
    "online-mba-colleges",
    "online-mba-colleges-in-india",
    "online-mba-universities",
    "online-mba-universities-in-india",
    "online-mba-programs",
    "online-mba-courses",
    "online-mba-degree",
    "online-mba-degree-in-india",
    "online-mba-course-in-india"
]

all_passed = True
print("==================================================")
print("AUDIT & VERIFICATION SUITE FOR 10 PILLAR BLOGS")
print("==================================================")

for slug in slugs:
    filepath = os.path.join("blogs", f"{slug}.html")
    if not os.path.exists(filepath):
        print(f"[FAIL] {slug}: File not found at {filepath}")
        all_passed = False
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
    words = 0
    if main_match:
        clean = re.sub(r'<[^>]+>', ' ', main_match.group(1))
        words = len(clean.split())

    checks = {
        "Embedded CSS": '<style id="embedded-template-css">' in content,
        "Progress Bar": 'id="readingProgressBar"' in content,
        "Header Nav": 'class="top-bar"' in content,
        "Breadcrumbs": 'class="breadcrumbs"' in content,
        "Hero 4 Stats": 'class="hero-stat-card"' in content and content.count('class="hero-stat-card"') == 4,
        "Executive Summary": "Executive Summary &amp; Key Takeaways" in content,
        "Collapsible TOC": 'class="blog-toc-card"' in content and 'class="blog-toc-toggle-btn"' in content,
        "Curriculum Table": "Core Modules &amp; Subject Breakdown" in content,
        "Universities Table": "Manipal University Jaipur" in content,
        "Specialization Table": "Business Analytics &amp; Data Science" in content,
        "Online vs Distance Table": "Online MBA vs Distance MBA: Critical Differences" in content,
        "Admission 4 Steps": 'class="admission-step-card"' in content and content.count('class="admission-step-card"') == 4,
        "EMI Table": "12-Month 0% EMI" in content,
        "Lead Form": 'class="lead-form"' in content and 'name="consent"' in content,
        "5 FAQs": 'class="faq-item"' in content and content.count('class="faq-item"') == 5,
        "Author Card": "Rajiv Sharma" in content,
        "4 Related Guides": 'class="related-guide-card"' in content and content.count('class="related-guide-card"') == 4,
        "Luxury Footer": 'class="site-footer"' in content,
        "Lead Modal": 'id="lead-modal"' in content,
        "Interactive Scripts": 'document.addEventListener("DOMContentLoaded"' in content,
        "Word Count >= 2400": words >= 2400
    }

    # Test HTTP server
    url = f"http://localhost:3000/blogs/{slug}"
    http_ok = False
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req) as resp:
            http_ok = (resp.status == 200)
    except Exception as e:
        http_ok = False

    failed_checks = [k for k, v in checks.items() if not v]
    if not failed_checks and http_ok:
        print(f"[PASS] {slug} | Words: {words} | HTTP 200 OK | All 21 checks passed")
    else:
        all_passed = False
        print(f"[FAIL] {slug} | Failed: {failed_checks} | HTTP OK: {http_ok}")

print("==================================================")
if all_passed:
    print("RESULT: ALL 10 PILLAR BLOGS 100% VERIFIED & PASSED!")
else:
    print("RESULT: VERIFICATION FAILED FOR SOME BLOGS!")
print("==================================================")
