import xml.etree.ElementTree as ET
import os

tree = ET.parse('sitemap.xml')
root = tree.getroot()

urls = []
for elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if loc is not None and loc.text:
        urls.append(loc.text.strip())

print(f"Total URLs in sitemap.xml: {len(urls)}")

non_www = [u for u in urls if not u.startswith('https://www.onlinembaadmission.com')]
print(f"Non-canonical/Non-www URLs in sitemap: {len(non_www)}")

# Check if every URL exists on disk as a clean route
missing_files = []
for u in urls:
    path = u.replace('https://www.onlinembaadmission.com', '').strip('/')
    if not path:
        # Home
        fpath = 'index.html'
    else:
        # File or directory
        fpath = path + '.html'
        fdir = os.path.join(path, 'index.html')
        if not os.path.exists(fpath) and not os.path.exists(fdir) and not os.path.exists(path):
            missing_files.append((u, fpath))

print(f"URLs in sitemap missing from disk: {len(missing_files)}")
if missing_files:
    for u, f in missing_files:
        print(f"  Missing: {u} (expected {f})")
else:
    print("ALL URLs in sitemap.xml map 100% to valid production files on disk!")
