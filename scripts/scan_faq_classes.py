import os, re

dirs_to_check = ['.', 'blogs', 'universities']
faq_patterns = {}

for d in dirs_to_check:
    for f in os.listdir(d):
        if f.endswith('.html'):
            p = os.path.join(d, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                classes = set(re.findall(r'class=[\"\']([^\"\']*faq[^\"\']*)[\"\']', c, re.I))
                if classes:
                    faq_patterns[p] = list(classes)

for k, v in list(faq_patterns.items())[:25]:
    print(k, "->", v)
print(f"Total HTML files with FAQ classes: {len(faq_patterns)}")
