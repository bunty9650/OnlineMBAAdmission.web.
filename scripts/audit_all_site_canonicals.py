import os
import re

dirs_to_check = ['.', 'blogs', 'universities', 'specializations', 'university']
all_html = []

for d in dirs_to_check:
    for root, dirs, files in os.walk(d):
        if any(x in root for x in ['.git', '__pycache__', 'node_modules']):
            continue
        for f in files:
            if f.endswith('.html'):
                all_html.append(os.path.normpath(os.path.join(root, f)))

all_html = sorted(list(set(all_html)))
print(f"Total HTML files found in repo: {len(all_html)}", flush=True)

missing_canonical = []
non_www_canonical = []
wrong_canonical = []
valid_canonical = []

for fpath in all_html:
    if fpath in [os.path.normpath('blogs/blog-template.html'), os.path.normpath('scripts/blog-template.html')]:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    m = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', content)
    if not m:
        m = re.search(r'<link\s+href=["\']([^"\']+)["\']\s+rel=["\']canonical["\']', content)

    if not m:
        missing_canonical.append(fpath)
    else:
        url = m.group(1)
        if url.startswith('https://onlinembaadmission.com'):
            non_www_canonical.append((fpath, url))
        elif not url.startswith('https://www.onlinembaadmission.com'):
            wrong_canonical.append((fpath, url))
        else:
            valid_canonical.append((fpath, url))

print(f"Valid canonicals: {len(valid_canonical)}", flush=True)
print(f"Missing canonicals: {len(missing_canonical)}", flush=True)
print(f"Non-www canonicals: {len(non_www_canonical)}", flush=True)
print(f"Wrong/Other canonicals: {len(wrong_canonical)}", flush=True)

if missing_canonical:
    print("\nFiles MISSING canonical:", flush=True)
    for f in missing_canonical:
        print(" ", f, flush=True)

if non_www_canonical:
    print("\nFiles with NON-WWW canonical:", flush=True)
    for f, u in non_www_canonical:
        print(f"  {f} -> {u}", flush=True)

if wrong_canonical:
    print("\nFiles with WRONG/OTHER canonical:", flush=True)
    for f, u in wrong_canonical:
        print(f"  {f} -> {u}", flush=True)
