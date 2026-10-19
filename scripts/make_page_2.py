# scripts/make_page_2.py
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "blogs", "index.html")
PAGE2_PATH = os.path.join(BASE_DIR, "blogs", "page-2.html")

with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    txt = f.read()

txt = txt.replace(
    '<title>Online MBA Admission Insights, Regulatory News and Career Guides | Online MBA Admission</title>',
    '<title>Online MBA Admission Insights & Guides - Page 2 | Online MBA Admission</title>'
)
txt = txt.replace(
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs">',
    '<link rel="canonical" href="https://www.onlinembaadmission.com/blogs/page-2">'
)

with open(PAGE2_PATH, 'w', encoding='utf-8') as f:
    f.write(txt)

print("Created blogs/page-2.html successfully.")
