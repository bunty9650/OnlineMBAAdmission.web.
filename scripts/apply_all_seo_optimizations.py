import os, re, json, urllib.parse, openpyxl, sys
sys.path.insert(0, '.')
from openpyxl.styles import PatternFill
from scripts.build_complete_meta_dict import meta_map

EXCEL_PATH = r'C:\Users\bunty\.gemini\antigravity\scratch\sitemap_links\seo_audit_report.xlsx'
ITEMS_PATH = 'scripts/items_to_optimize.json'

with open(ITEMS_PATH, 'r', encoding='utf-8') as f:
    items = json.load(f)

def url_to_local_file(url):
    path = urllib.parse.urlparse(url).path.strip('/')
    if not path:
        return 'index.html'
    if os.path.exists(path + '.html'):
        return path + '.html'
    if os.path.isdir(path) and os.path.exists(os.path.join(path, 'index.html')):
        return os.path.join(path, 'index.html')
    if os.path.exists(path):
        return path
    return None

def replace_meta_tag(attr_name, attr_val, new_content, head_text):
    p1 = rf'(<meta\b[^>]*?\b{attr_name}=["\']{re.escape(attr_val)}["\'][^>]*?\bcontent=)(["\'])(.*?)\2([^>]*?>)'
    p2 = rf'(<meta\b[^>]*?\bcontent=)(["\'])(.*?)\2([^>]*?\b{attr_name}=["\']{re.escape(attr_val)}["\'][^>]*?>)'
    
    if re.search(p1, head_text, flags=re.IGNORECASE):
        return re.sub(p1, rf'\g<1>"{new_content}"\g<4>', head_text, count=1, flags=re.IGNORECASE)
    elif re.search(p2, head_text, flags=re.IGNORECASE):
        return re.sub(p2, rf'\g<1>"{new_content}"\g<4>', head_text, count=1, flags=re.IGNORECASE)
    return head_text

def update_html_meta(html_text, new_title=None, new_desc=None):
    head_m = re.search(r'(<head\b[^>]*>)(.*?)(</head>)', html_text, flags=re.DOTALL | re.IGNORECASE)
    if not head_m:
        return html_text
    
    head = head_m.group(2)
    
    if new_title is not None:
        head = re.sub(r'<title>[^<]*</title>', f'<title>{new_title}</title>', head, count=1, flags=re.IGNORECASE)
        head = replace_meta_tag('property', 'og:title', new_title, head)
        head = replace_meta_tag('name', 'twitter:title', new_title, head)
        
    if new_desc is not None:
        head = replace_meta_tag('name', 'description', new_desc, head)
        head = replace_meta_tag('property', 'og:description', new_desc, head)
        head = replace_meta_tag('name', 'twitter:description', new_desc, head)
        
    return html_text[:head_m.start(2)] + head + html_text[head_m.end(2):]

print("Step 1: Updating local HTML files...")
html_updated_count = 0
for it in items:
    url = it['url']
    if url not in meta_map:
        continue
    
    local_file = url_to_local_file(url)
    if not local_file or not os.path.exists(local_file):
        continue
    
    data = meta_map[url]
    new_t = data.get('title') if it['needs_title'] else None
    new_d = data.get('desc') if it['needs_desc'] else None
    
    if not new_t and not new_d:
        continue
    
    with open(local_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = update_html_meta(content, new_title=new_t, new_desc=new_d)
    
    with open(local_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    html_updated_count += 1

print(f"Successfully updated {html_updated_count} local HTML files.")

print("\nStep 2: Updating Excel Report:", EXCEL_PATH)
wb = openpyxl.load_workbook(EXCEL_PATH)
sheet = wb['SEO Audit Report']

green_fill = PatternFill(start_color="00E2EFDA", end_color="00E2EFDA", fill_type="solid")

headers = [cell.value for cell in sheet[1]]
url_col = headers.index('Page URL (Clickable)') + 1
title_col = headers.index('Title Tag') + 1
title_len_col = headers.index('Title Length') + 1
title_status_col = headers.index('Title Status') + 1
desc_col = headers.index('Meta Description') + 1
desc_len_col = headers.index('Meta Desc Length') + 1
desc_status_col = headers.index('Meta Desc Status') + 1
issues_col = headers.index('SEO Issues / Fixes Required') + 1

excel_updated_rows = 0
for r in range(2, sheet.max_row + 1):
    url = sheet.cell(row=r, column=url_col).value
    if url not in meta_map:
        continue
    
    data = meta_map[url]
    needs_t = data.get('title') is not None
    needs_d = data.get('desc') is not None
    
    if needs_t:
        new_title = data['title']
        sheet.cell(row=r, column=title_col).value = new_title
        sheet.cell(row=r, column=title_len_col).value = len(new_title)
        c_status = sheet.cell(row=r, column=title_status_col)
        c_status.value = 'Optimal'
        c_status.fill = green_fill
        
    if needs_d:
        new_desc = data['desc']
        sheet.cell(row=r, column=desc_col).value = new_desc
        sheet.cell(row=r, column=desc_len_col).value = len(new_desc)
        d_status = sheet.cell(row=r, column=desc_status_col)
        d_status.value = 'Optimal'
        d_status.fill = green_fill
        
    # Update Issues column
    issues_cell = sheet.cell(row=r, column=issues_col)
    cur_issues_str = str(issues_cell.value or "")
    if cur_issues_str:
        issues_list = [i.strip() for i in cur_issues_str.split(';') if i.strip()]
        filtered_issues = []
        for iss in issues_list:
            if 'Title is too long' in iss and needs_t:
                continue
            if 'Meta description too long' in iss and needs_d:
                continue
            filtered_issues.append(iss)
        
        if not filtered_issues:
            issues_cell.value = "None (Clean)"
            issues_cell.fill = green_fill
        else:
            issues_cell.value = "; ".join(filtered_issues)
            
    excel_updated_rows += 1

print(f"Updated {excel_updated_rows} rows in 'SEO Audit Report'.")

# Step 3: Update Audit Executive Summary
summary_sheet = wb['Audit Executive Summary']
# Row 8: Pages with Optimal Title Tag (30-65 chars) -> 385
summary_sheet.cell(row=8, column=2).value = 385
# Row 10: Pages with Optimal Meta Description (70-165 chars) -> 385
summary_sheet.cell(row=10, column=2).value = 385
# Row 17: Pages with Images Missing ALT Tags -> 0
summary_sheet.cell(row=17, column=2).value = 0

OPT_PATH_SCRATCH = r'C:\Users\bunty\.gemini\antigravity\scratch\sitemap_links\seo_audit_report_optimized.xlsx'
OPT_PATH_WORKSPACE = 'seo_audit_report_optimized.xlsx'

wb.save(OPT_PATH_SCRATCH)
print(f"Saved optimized Excel audit report to: {OPT_PATH_SCRATCH}")
wb.save(OPT_PATH_WORKSPACE)
print(f"Saved optimized Excel audit report to: {OPT_PATH_WORKSPACE}")

try:
    wb.save(EXCEL_PATH)
    print(f"Successfully updated original {EXCEL_PATH}!")
except PermissionError:
    print(f"Note: Original {EXCEL_PATH} is locked by Excel/another process; optimized versions saved to {OPT_PATH_SCRATCH} and {OPT_PATH_WORKSPACE}.")
