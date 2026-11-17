# -*- coding: utf-8 -*-
"""
Add 10 Priority 4 Clean URLs to sitemap.xml
"""

import re
from data_priority4_cities import cities_p4

with open("sitemap.xml", "r", encoding="utf-8") as f:
    content = f.read()

entries = []
for key, data in cities_p4.items():
    u = f"https://www.onlinembaadmission.com/blogs/{data['slug']}"
    if f"<loc>{u}</loc>" not in content:
        entry = f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-11-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>"""
        entries.append(entry)

if entries:
    new_xml_block = "\n".join(entries) + "\n</urlset>"
    content = content.replace("</urlset>", new_xml_block)
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Added {len(entries)} Priority 4 URLs to sitemap.xml!")
else:
    print("All Priority 4 URLs already present in sitemap.xml.")

# Verify count
all_locs = re.findall(r'<loc>(.*?)</loc>', content)
print(f"Total updated sitemap URLs: {len(all_locs)}")
