import urllib.request

urls = [
    "http://localhost:8000/university/st-aloysius/mba-in-general-management",
    "http://localhost:8000/university/st-aloysius/mba-in-marketing",
    "http://localhost:8000/university/st-aloysius/mba-in-finance",
    "http://localhost:8000/university/st-aloysius/mba-in-human-resource-management",
    "http://localhost:8000/university/st-aloysius/mba-in-data-science-analytics",
    "http://localhost:8000/university/st-aloysius/mba-in-healthcare-management",
    "http://localhost:8000/university/st-aloysius/mba-in-logistics-supply-chain",
    "http://localhost:8000/universities/st-aloysius"
]

all_ok = True
for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as res:
            code = res.getcode()
            body = res.read().decode('utf-8')
            print(f"[{code}] {u} (Length: {len(body)} bytes)")
            if code != 200 or len(body) < 1000:
                all_ok = False
    except Exception as e:
        print(f"[ERR] {u}: {e}")
        all_ok = False

if all_ok:
    print("\n✅ All 7 St. Aloysius specialization URLs return HTTP 200 OK on local server!")
else:
    print("\n❌ Errors encountered during HTTP endpoint tests.")
