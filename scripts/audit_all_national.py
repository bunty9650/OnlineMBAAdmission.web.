import os, re

topics = [
    'best-online-mba-universities-in-india.html',
    'online-mba-fees-in-india.html',
    'online-mba-under-50000.html',
    'is-online-mba-valid-in-india.html',
    'online-vs-distance-mba.html',
    'government-online-distance-mba-universities.html',
    'online-mba-admission-without-entrance.html',
    'online-mba-for-working-professionals.html',
    'online-mba-after-bcom.html',
    'online-mba-finance-vs-marketing-vs-hr.html',
    'online-mba-admission-process.html',
    'online-mba-vs-regular-mba.html'
]

for t in topics:
    p = os.path.join('blogs', t)
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m_title = re.search(r'<title>(.*?)</title>', c, re.DOTALL)
    m_desc = re.search(r'<meta\s+name=[\"\']description[\"\']\s+content=[\"\'](.*?)[\"\']', c)
    text = re.sub(r'<script.*?</script>', ' ', c, flags=re.DOTALL)
    text = re.sub(r'<style.*?</style>', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = len(re.findall(r'\b[a-zA-Z0-9_\-\u0900-\u097F]+\b', text))
    title = m_title.group(1).strip() if m_title else ''
    desc = m_desc.group(1).strip() if m_desc else ''
    print(f"{t} | {title} ({len(title)} chars) | {desc} ({len(desc)} chars) | {words} words")
