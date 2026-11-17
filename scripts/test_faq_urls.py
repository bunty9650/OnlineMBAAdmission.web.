import urllib.request

urls = [
    'http://localhost:8000/blogs/online-mba-faridabad',
    'http://localhost:8000/universities/st-aloysius',
    'http://localhost:8000/blogs/online-mba-mumbai',
    'http://localhost:8000/blogs/is-online-mba-valid-in-india',
    'http://localhost:8000/blogs/online-mba-for-working-professionals',
    'http://localhost:8000/styles.css',
    'http://localhost:8000/script.js'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read()
            print(f"HTTP {resp.status} OK: {u} (size: {len(content)} bytes)")
    except Exception as e:
        print(f"FAILED {u}: {e}")
