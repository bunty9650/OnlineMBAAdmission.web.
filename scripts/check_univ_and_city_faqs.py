import os, re

print("--- UNIVERSITIES ---")
for f in os.listdir('universities'):
    if f.endswith('.html'):
        p = os.path.join('universities', f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            c = fp.read()
            classes = set(re.findall(r'class=[\"\']([^\"\']*faq[^\"\']*)[\"\']', c, re.I))
            print(f, "->", classes)

print("\n--- SAMPLE CITY BLOGS ---")
city_samples = ['blogs/online-mba-delhi.html', 'blogs/online-mba-faridabad.html', 'blogs/online-mba-mumbai.html', 'blogs/online-mba-ranchi.html']
for p in city_samples:
    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
        classes = set(re.findall(r'class=[\"\']([^\"\']*faq[^\"\']*)[\"\']', c, re.I))
        print(p, "->", classes)
