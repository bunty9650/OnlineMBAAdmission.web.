# -*- coding: utf-8 -*-
"""
Add 5 New National Pillar clean URLs to sitemap.xml
"""

import re
from data_national_pillars import national_pillars_data

with open("sitemap.xml", "r", encoding="utf-8") as f:
    content = f.read()

entries = []
for slug, data in national_pillars_data.items():
    u = f"https://www.onlinembaadmission.com/blogs/{slug}"
    if f"<loc>{u}</loc>" not in content:
        entry = f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>"""
        entries.append(entry)

if entries:
    new_xml_block = "\n".join(entries) + "\n</urlset>"
    content = content.replace("</urlset>", new_xml_block)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added {len(entries)} National Pillar URLs to sitemap.xml!")
else:
    print("All National Pillar URLs already present in sitemap.xml.")

all_locs = re.findall(r'<loc>(.*?)</loc>', content)
print(f"Total updated sitemap URLs: {len(all_locs)}")
