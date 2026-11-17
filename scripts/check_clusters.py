import openpyxl

wb = openpyxl.load_workbook('C:/Users/bunty/.gemini/antigravity/brain/3c178001-576a-4b67-9269-bade2c7e2404/.user_uploaded/media_1794900064008_9c2c8438.xlsx')
ws = wb['City Keyword Plan']

header = [cell for cell in next(ws.iter_rows(values_only=True))]
print('Header:', header)

rows = list(ws.iter_rows(min_row=2, values_only=True))

clusters = {}
for r in rows:
    if not any(r): continue
    region = r[0]
    city = r[1]
    prio = r[2]
    title = r[3]
    kw = r[4]
    url = r[7]
    clusters.setdefault(region, []).append({
        'city': city,
        'prio': prio,
        'title': title,
        'kw': kw,
        'url': url
    })

for reg, items in clusters.items():
    print(f"\n=== {reg} ({len(items)} cities) ===")
    for it in items:
        print(f"  City: {it['city']} | Prio: {it['prio']} | URL: {it['url']} | Title: {it['title']}")
