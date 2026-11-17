import os
import re

files_to_check = [
    ('Topic 1', 'best-online-mba-universities-in-india.html', 'best-online-mba-universities-india.html'),
    ('Topic 2', 'online-mba-fees-in-india.html', 'online-mba-fees-india.html'),
    ('Topic 3', 'online-mba-under-50000.html', 'online-mba-under-50000.html'),
    ('Topic 4', 'is-online-mba-valid-govt-jobs.html', 'is-online-mba-valid-in-india.html'),
    ('Topic 5', 'online-vs-distance-mba.html', 'online-mba-vs-distance-mba.html'),
    ('Topic 6', 'government-online-distance-mba-universities.html', 'government-online-distance-mba-universities.html'),
    ('Topic 7', 'online-mba-admission-without-entrance.html', 'online-mba-without-entrance-exam.html'),
    ('Topic 8', 'online-mba-for-working-professionals.html', 'online-mba-working-professionals.html'),
    ('Topic 9', 'online-mba-after-bcom.html', 'online-mba-after-bcom.html'),
    ('Topic 10', 'highest-paying-specializations.html', 'online-mba-finance-vs-marketing-vs-hr.html'),
    ('Topic 11', 'online-mba-admission-process.html', 'online-mba-admission-process.html'),
    ('Topic 12', 'online-mba-vs-regular-mba.html', 'online-mba-vs-regular-mba.html'),
]

for topic, existing, suggested in files_to_check:
    print(f"\n{topic}:")
    print(f"  Existing candidate: {existing}")
    print(f"  Suggested target  : {suggested}")
    ex_path = os.path.join('blogs', existing)
    if os.path.exists(ex_path):
        size = os.path.getsize(ex_path)
        with open(ex_path, 'r', encoding='utf-8') as f:
            html = f.read()
        text = re.sub(r'<[^>]+>', ' ', html)
        words = len(re.findall(r'\b\w+\b', text))
        print(f"  Existing file: {existing} | Size: {size:,} bytes | Words: {words}")
    else:
        print(f"  Existing file: {existing} does NOT exist.")
        
    sugg_path = os.path.join('blogs', suggested)
    if os.path.exists(sugg_path) and sugg_path != ex_path:
        size = os.path.getsize(sugg_path)
        with open(sugg_path, 'r', encoding='utf-8') as f:
            html = f.read()
        text = re.sub(r'<[^>]+>', ' ', html)
        words = len(re.findall(r'\b\w+\b', text))
        print(f"  Suggested file: {suggested} exists | Size: {size:,} bytes | Words: {words}")
