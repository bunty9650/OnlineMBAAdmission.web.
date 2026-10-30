import glob
import os
import re

subpages = glob.glob('university/*/*.html')
print(f"Total University Subpages: {len(subpages)}")

word_counts = []
no_faq = []
h1s = {}
titles = {}

for f in subpages:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        html = fp.read()
    clean = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.I|re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    words = len(clean.split())
    word_counts.append(words)
    
    if 'FAQPage' not in html:
        no_faq.append(f)
        
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if h1:
        h1_text = re.sub(r'<[^>]+>', '', h1.group(1)).strip()
        h1_text = re.sub(r'\s+', ' ', h1_text)
        h1s.setdefault(h1_text, []).append(f)
        
    title = re.search(r'<title>(.*?)</title>', html)
    if title:
        t_text = re.sub(r'\s+', ' ', title.group(1)).strip()
        titles.setdefault(t_text, []).append(f)

print(f"Min Words: {min(word_counts)}, Max Words: {max(word_counts)}, Avg Words: {sum(word_counts)/len(word_counts):.0f}")
print(f"Subpages under 1000 words: {len([w for w in word_counts if w < 1000])}")
print(f"Subpages 1000-2000 words: {len([w for w in word_counts if 1000 <= w < 2000])}")
print(f"Subpages 2000+ words: {len([w for w in word_counts if w >= 2000])}")
print(f"Subpages without FAQ schema: {len(no_faq)}")

dup_h1s = {h: flist for h, flist in h1s.items() if len(flist) > 1}
print(f"\nDuplicate H1s across subpages: {len(dup_h1s)}")
for h, flist in dup_h1s.items():
    print(f"  H1: '{h}' ({len(flist)} pages)")
    for f in flist[:4]:
        print(f"    - {f}")

dup_titles = {t: flist for t, flist in titles.items() if len(flist) > 1}
print(f"\nDuplicate Titles across subpages: {len(dup_titles)}")
