import urllib.request, re, json

urls = [
    ("mba-general-management", "https://staloysiusonline.com/programmes/mba/mba-general-management"),
    ("mba-marketing", "https://staloysiusonline.com/programmes/mba/mba-marketing"),
    ("mba-finance", "https://staloysiusonline.com/programmes/mba/mba-finance"),
    ("mba-human-resource-management", "https://staloysiusonline.com/programmes/mba/mba-human-resource-management"),
    ("mba-data-science-analytics", "https://staloysiusonline.com/programmes/mba/mba-data-science-analytics"),
    ("mba-healthcare-management", "https://staloysiusonline.com/programmes/mba/mba-healthcare-management"),
    ("mba-logistics-supply-chain", "https://staloysiusonline.com/programmes/mba/mba-logistics-supply-chain"),
]

data = {}

for slug, u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        # Extract text
        text = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL)
        text = re.sub(r'<style.*?</style>', ' ', text, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', text)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        
        data[slug] = {
            "url": u,
            "raw_text": " ".join(lines[:200])
        }
        print(f"Fetched {slug} ({len(html)} bytes)")
    except Exception as e:
        print(f"Error fetching {slug}: {e}")

with open('scripts/aloysius_specs_raw.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Saved raw data to scripts/aloysius_specs_raw.json")
