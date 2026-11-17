with open('blogs/online-mba-for-working-professionals.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<h[23][^>]*>.*?(?:faq|frequently|question).*?</h[23]>', c, re.I)
print("Matches in working professionals blog:", matches)
