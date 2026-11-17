with open('styles.css', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = [m.start() for m in re.finditer(r'cs-faq-item', c)]
print(f"Total cs-faq-item matches: {len(matches)}")
for idx in matches:
    print(c[max(0, idx-20):min(len(c), idx+120)])
    print("=" * 40)
