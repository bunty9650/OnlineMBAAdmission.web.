with open('blogs/online-mba-for-working-professionals.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', c)
for h in headings:
    print(h)
