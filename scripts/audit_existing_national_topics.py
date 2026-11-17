import os
import re

existing_national_files = [
    ("Topic 1", "blogs/best-online-mba-universities-in-india.html"),
    ("Topic 2", "blogs/online-mba-fees-in-india.html"),
    ("Topic 3", "blogs/online-mba-under-50000.html"),
    ("Topic 5", "blogs/online-vs-distance-mba.html"),
    ("Topic 7", "blogs/online-mba-admission-without-entrance.html"),
    ("Topic 8", "blogs/online-mba-for-working-professionals.html"),
    ("Topic 11", "blogs/online-mba-admission-process.html")
]

print("=== EXISTING NATIONAL BLOG AUDIT ===")

for top, fpath in existing_national_files:
    if not os.path.exists(fpath):
        print(f"{top}: {fpath} does not exist")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Title
    m_title = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    title = m_title.group(1).strip() if m_title else ""
    tl = len(title)
    
    # Meta
    m_meta = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
    if not m_meta:
        m_meta = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.DOTALL | re.IGNORECASE)
    meta = m_meta.group(1).strip() if m_meta else ""
    ml = len(meta)
    
    # Canonical
    m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html, re.DOTALL | re.IGNORECASE)
    canon = m_canon.group(1).strip() if m_canon else ""
    
    # Words
    clean_html = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL | re.IGNORECASE)
    clean_html = re.sub(r'<style.*?</style>', ' ', clean_html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', clean_html)
    words = len(re.findall(r'\b\w+\b', text))
    
    print(f"\n{top} ({fpath}):")
    print(f"  Title ({tl} chars, 50-60): {50<=tl<=60} -> '{title}'")
    print(f"  Meta  ({ml} chars, 150-160): {150<=ml<=160} -> '{meta}'")
    print(f"  Ends with CTA: {meta.endswith('Check eligibility.') or meta.endswith('Apply now.')}")
    print(f"  Canonical: {canon}")
    print(f"  Words: {words}")
