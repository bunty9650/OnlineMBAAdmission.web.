import re

priority3_urls = [
    "https://www.onlinembaadmission.com/blogs/online-mba-jaipur",
    "https://www.onlinembaadmission.com/blogs/online-mba-lucknow",
    "https://www.onlinembaadmission.com/blogs/online-mba-chandigarh",
    "https://www.onlinembaadmission.com/blogs/online-mba-ahmedabad",
    "https://www.onlinembaadmission.com/blogs/online-mba-indore",
    "https://www.onlinembaadmission.com/blogs/online-mba-bhopal",
]

with open("sitemap.xml", "r", encoding="utf-8") as f:
    content = f.read()

entries = []
for u in priority3_urls:
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
    print(f"Added {len(entries)} Priority 3 URLs to sitemap.xml!")
else:
    print("All Priority 3 URLs already present in sitemap.xml.")

# Verify count
all_locs = re.findall(r'<loc>(.*?)</loc>', content)
print(f"Total updated sitemap URLs: {len(all_locs)}")
