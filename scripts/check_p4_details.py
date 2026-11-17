import openpyxl

wb = openpyxl.load_workbook('C:/Users/bunty/.gemini/antigravity/brain/3c178001-576a-4b67-9269-bade2c7e2404/.user_uploaded/media_1794900064008_9c2c8438.xlsx')
ws = wb['City Keyword Plan']

header = [cell for cell in next(ws.iter_rows(values_only=True))]

rows = list(ws.iter_rows(min_row=2, values_only=True))

print("=== PRIORITY 4 DETAILS ===")
for r in rows:
    if not any(r): continue
    region = r[0]
    city = r[1]
    prio = r[2]
    if prio == 'Priority 4':
        print(f"\n--- {city} ---")
        for col_name, val in zip(header, r):
            print(f"  {col_name}: {val}")
