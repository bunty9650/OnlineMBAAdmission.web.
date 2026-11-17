import urllib.request

urls = [
    'http://localhost:8000/blogs/online-mba-jaipur',
    'http://localhost:8000/blogs/online-mba-lucknow',
    'http://localhost:8000/blogs/online-mba-chandigarh',
    'http://localhost:8000/blogs/online-mba-ahmedabad',
    'http://localhost:8000/blogs/online-mba-indore',
    'http://localhost:8000/blogs/online-mba-bhopal',
]

for u in urls:
    try:
        resp = urllib.request.urlopen(u)
        print(f'{u} -> HTTP {resp.status} (Length: {len(resp.read())} bytes)')
    except Exception as e:
        print(f'{u} -> ERROR: {e}')
