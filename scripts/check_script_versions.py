import os, re

count = 0
versions = set()
for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['.git', 'node_modules', '_archive']):
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                txt = fp.read()
            found = re.findall(r'script\.js(?:\?v=[\d\.]+)?', txt)
            if found:
                versions.update(found)
                count += 1

print(f"Total HTML files with script.js: {count}")
print(f"Versions found: {versions}")
