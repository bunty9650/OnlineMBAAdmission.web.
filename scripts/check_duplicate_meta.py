import xml.etree.ElementTree as ET
import re
import sys
sys.path.append('scripts')
from audit_site_ranking_readiness import url_to_local_path

tree = ET.parse('sitemap.xml')
urls = [e.text.strip() for e in tree.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

descs = {}
for u in urls:
    p = url_to_local_path(u)
    if p:
        with open(p, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']', html, re.I)
        if m:
            d = re.sub(r'\s+', ' ', m.group(1)).strip()
            descs.setdefault(d, []).append(u)

dup_d = {d: ul for d, ul in descs.items() if len(ul) > 1}
print(f"Total Unique Descriptions: {len(descs)}")
print(f"Duplicate Meta Descriptions Count: {len(dup_d)}")
for d, ul in list(dup_d.items())[:10]:
    print(f"  Desc: '{d[:75]}...' ({len(ul)} URLs)")
    for u in ul[:3]:
        print(f"    - {u}")
