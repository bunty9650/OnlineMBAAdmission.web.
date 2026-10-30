import glob
import os
import xml.etree.ElementTree as ET

tree = ET.parse('sitemap.xml')
sitemap_urls = set(e.text.strip() for e in tree.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'))

# Convert sitemap urls to expected relative filepaths
sitemap_files = set()
for u in sitemap_urls:
    p = u.replace("https://www.onlinembaadmission.com", "").strip()
    if p == "" or p == "/":
        sitemap_files.add("index.html")
    else:
        if p.startswith("/"): p = p[1:]
        if os.path.exists(f"{p}.html"):
            sitemap_files.add(f"{p}.html".replace("/", "\\"))
        elif os.path.exists(f"{p}/index.html"):
            sitemap_files.add(f"{p}/index.html".replace("/", "\\"))
        elif os.path.exists(p):
            sitemap_files.add(p.replace("/", "\\"))

# Check all active html files (excluding _archive, tmp, etc.)
active_html = []
for root_dir, dirs, files in os.walk("."):
    if "_archive" in root_dir or ".git" in root_dir or "node_modules" in root_dir:
        continue
    for f in files:
        if f.endswith(".html"):
            rel = os.path.relpath(os.path.join(root_dir, f), ".").replace("/", "\\")
            active_html.append(rel)

print(f"Total Active HTML files on disk: {len(active_html)}")
print(f"Total HTML files covered in sitemap: {len(sitemap_files)}")

orphans = set(active_html) - sitemap_files
# Exclude known templates or special files
non_template_orphans = [f for f in orphans if "template" not in f and not f.startswith("scripts")]
print(f"\nOrphan HTML files (on disk but NOT in sitemap.xml): {len(non_template_orphans)}")
for f in sorted(non_template_orphans):
    print(f"  - {f}")
