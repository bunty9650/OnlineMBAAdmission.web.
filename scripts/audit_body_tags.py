import glob
import re

files = sorted(glob.glob('blogs/*.html'))
print(f"Total blog files: {len(files)}")

body_stats = {
    'header_top_bar': [],
    'header_header': [],
    'header_site_header': [],
    'header_other': [],
    'hero_stat_strip': [],
    'article_hero_stats': [],
    'hero_other': [],
    'footer_site_footer': [],
    'footer_footer': [],
    'footer_other': [],
    'canonical_ok': [],
    'canonical_issue': []
}

for fpath in files:
    if fpath == 'blogs\\blog-template.html' or 'page-' in fpath or fpath == 'blogs\\index.html':
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Split head and body
    body_idx = html.find('<body')
    if body_idx == -1:
        continue
    head_content = html[:body_idx]
    body_content = html[body_idx:]

    # Check top header in body
    top_header_match = re.search(r'<header\s+class=["\']([^"\']+)["\']', body_content)
    if top_header_match:
        cls = top_header_match.group(1)
        if 'top-bar' in cls:
            body_stats['header_top_bar'].append(fpath)
        elif 'site-header' in cls:
            body_stats['header_site_header'].append(fpath)
        elif cls == 'header' or 'header ' in cls:
            body_stats['header_header'].append(fpath)
        else:
            body_stats['header_other'].append((fpath, cls))

    # Check hero stats in body
    if 'class="hero-stat-strip"' in body_content or "class='hero-stat-strip'" in body_content:
        body_stats['hero_stat_strip'].append(fpath)
    elif 'class="article-hero-stats"' in body_content or "class='article-hero-stats'" in body_content:
        body_stats['article_hero_stats'].append(fpath)
    else:
        body_stats['hero_other'].append(fpath)

    # Check bottom footer in body
    bottom_footer_match = re.findall(r'<footer\s+class=["\']([^"\']+)["\']', body_content)
    if bottom_footer_match:
        last_footer_cls = bottom_footer_match[-1]
        if 'site-footer' in last_footer_cls:
            body_stats['footer_site_footer'].append(fpath)
        elif 'footer' in last_footer_cls:
            body_stats['footer_footer'].append(fpath)
        else:
            body_stats['footer_other'].append((fpath, last_footer_cls))
    else:
        body_stats['footer_other'].append((fpath, 'NO_FOOTER_TAG'))

    # Canonical
    c_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']+)["\']', head_content)
    if c_match:
        c_url = c_match.group(1)
        expected = f"https://www.onlinembaadmission.com/{fpath.replace(chr(92), '/').replace('.html', '')}"
        if c_url == expected:
            body_stats['canonical_ok'].append(fpath)
        else:
            body_stats['canonical_issue'].append((fpath, c_url, expected))
    else:
        body_stats['canonical_issue'].append((fpath, 'MISSING', ''))

print(f"Total post files evaluated: {len(files) - 12}")
print(f"Headers: top-bar={len(body_stats['header_top_bar'])}, site-header={len(body_stats['header_site_header'])}, header={len(body_stats['header_header'])}, other={len(body_stats['header_other'])}")
print(f"Hero stats: hero-stat-strip={len(body_stats['hero_stat_strip'])}, article-hero-stats={len(body_stats['article_hero_stats'])}, other={len(body_stats['hero_other'])}")
print(f"Footers: site-footer={len(body_stats['footer_site_footer'])}, footer={len(body_stats['footer_footer'])}, other={len(body_stats['footer_other'])}")
print(f"Canonicals: ok={len(body_stats['canonical_ok'])}, issue={len(body_stats['canonical_issue'])}")

if body_stats['canonical_issue']:
    print("\nCanonical issues:")
    for item in body_stats['canonical_issue']:
        print(" ", item)

print("\nFiles with header='header':", len(body_stats['header_header']))
print("Files with footer='footer':", len(body_stats['footer_footer']))
print("Files with article_hero_stats:", len(body_stats['article_hero_stats']))
