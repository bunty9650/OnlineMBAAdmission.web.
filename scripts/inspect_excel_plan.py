import openpyxl

wb = openpyxl.load_workbook('C:/Users/bunty/.gemini/antigravity/brain/3c178001-576a-4b67-9269-bade2c7e2404/.user_uploaded/media_1794900064008_9c2c8438.xlsx')
print('Sheets in Workbook:', wb.sheetnames)

ws_cities = wb['City Keyword Plan']
print('\n--- City Keyword Plan ---')
header = [cell for cell in next(ws_cities.iter_rows(values_only=True))]
print('Header:', header)
cities_data = []
for row in ws_cities.iter_rows(min_row=2, values_only=True):
    if any(row):
        cities_data.append(row)
print(f'Total cities in plan: {len(cities_data)}')

priority_map = {}
for r in cities_data:
    city = r[0]
    prio = r[1]
    priority_map.setdefault(prio, []).append(city)

for p, c_list in priority_map.items():
    print(f'Priority: {p} ({len(c_list)} cities): {", ".join(c_list)}')

if 'National Blog Topics' in wb.sheetnames:
    ws_nat = wb['National Blog Topics']
    print('\n--- National Blog Topics ---')
    for r in ws_nat.iter_rows(values_only=True):
        if any(r):
            print(r)
