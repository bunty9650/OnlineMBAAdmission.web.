import re

files = ['blogs/online-mba-faridabad.html', 'universities/st-aloysius.html']
for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    links = re.findall(r'<link[^>]*rel=[\"\']stylesheet[\"\'][^>]*>', c)
    scripts = re.findall(r'<script[^>]*src=[\"\'][^\"\']*[\"\'][^>]*>', c)
    print(fn)
    print("  CSS:", links)
    print("  JS :", scripts)
