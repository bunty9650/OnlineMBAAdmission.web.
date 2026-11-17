import os, re

cities = [
    'bangalore', 'mumbai', 'pune', 'hyderabad', 'chennai', 'kolkata',
    'jaipur', 'lucknow', 'chandigarh', 'ahmedabad', 'indore', 'bhopal',
    'kanpur', 'meerut', 'agra', 'ludhiana', 'jodhpur', 'surat', 'nagpur',
    'visakhapatnam', 'coimbatore', 'ranchi'
]

for city in cities:
    p = f'blogs/online-mba-{city}.html'
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        idx = c.find('id="faqs"')
        if idx != -1:
            snippet = c[idx:idx+350].replace('\n', ' ')
            print(f"{city}: {snippet[:120]}...")
        else:
            print(f"{city}: id='faqs' NOT FOUND")
