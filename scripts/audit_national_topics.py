import os
import openpyxl

wb = openpyxl.load_workbook('C:/Users/bunty/.gemini/antigravity/brain/3c178001-576a-4b67-9269-bade2c7e2404/.user_uploaded/media_1794900064008_9c2c8438.xlsx')
ws = wb['National Blog Topics']
rows = list(ws.iter_rows(values_only=True))
header = rows[0]

existing_files = set(os.listdir('blogs'))

print("=== NATIONAL BLOG TOPICS AUDIT & MAPPING ===")

for i, r in enumerate(rows[1:], 1):
    title = r[0]
    p_kw = r[1]
    s_kws = r[2]
    intent = r[3]
    sugg_url = r[4]
    brief = r[5]
    
    # suggested slug without /blog/ and trailing slash
    slug = sugg_url.strip('/').split('/')[-1]
    html_name = f"{slug}.html"
    
    # Check if exact file exists
    exact_exists = html_name in existing_files
    
    # Check close matches
    close_matches = [f for f in existing_files if any(part in f for part in slug.split('-') if len(part) > 3)]
    
    print(f"\n[Topic {i}] {title}")
    print(f"  Target Slug: {slug} ({html_name})")
    print(f"  Exact file exists: {exact_exists}")
    if not exact_exists:
        print(f"  Close matches in blogs/: {close_matches[:4]}")
