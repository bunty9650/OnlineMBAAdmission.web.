with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html_classes = set(re.findall(r'class=[\'"]([^\'"]+)[\'"]', html))
all_classes = set()
for c in html_classes:
    for cls in c.split():
        all_classes.add(cls)

all_ids = set(re.findall(r'id=[\'"]([^\'"]+)[\'"]', html))

print('Unique classes in index.html:', len(all_classes))
print('Unique ids in index.html:', len(all_ids))

# Let's see some rules in styles.css that belong to other pages
rules = re.findall(r'([^{]+)\{([^}]+)\}', css)
print('Total rules in styles.css:', len(rules))

page_specific = {
    'blog': 0,
    'spec': 0,
    'univ': 0,
    'compare': 0,
    'fee': 0,
    'calc': 0
}

for sel, body in rules:
    s_lower = sel.lower()
    for k in page_specific:
        if k in s_lower:
            page_specific[k] += 1

print('Rules matching keywords:', page_specific)
