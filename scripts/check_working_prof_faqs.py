with open('blogs/online-mba-for-working-professionals.html', 'r', encoding='utf-8') as f:
    c = f.read()

import json, re
m = re.search(r'<script type=\"application/ld\+json\">(.*?)</script>', c, re.DOTALL)
if m:
    data = json.loads(m.group(1))
    graph = data.get('@graph', [data])
    for item in graph:
        if item.get('@type') == 'FAQPage':
            for q in item.get('mainEntity', []):
                print("Q:", q.get('name'))
                print("A:", q.get('acceptedAnswer', {}).get('text')[:100])
