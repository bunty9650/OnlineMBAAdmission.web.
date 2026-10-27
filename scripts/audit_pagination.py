import re

pages = [
    ('blogs/index.html', 1, 1, 9, 76, 9),
    ('blogs/page-2.html', 2, 10, 18, 76, 9),
    ('blogs/page-3.html', 3, 19, 27, 76, 9),
    ('blogs/page-4.html', 4, 28, 36, 76, 9),
    ('blogs/page-5.html', 5, 37, 45, 76, 9),
    ('blogs/page-6.html', 6, 46, 54, 76, 9),
    ('blogs/page-7.html', 7, 55, 63, 76, 9),
    ('blogs/page-8.html', 8, 64, 72, 76, 9),
    ('blogs/page-9.html', 9, 73, 76, 76, 9),
]

for file, p_num, s_num, e_num, total_art, total_p in pages:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    
    expected_info = f"Showing {s_num} &ndash; {e_num} of {total_art} expert articles (Page {p_num} of {total_p})"
    has_info = expected_info in c
    
    expected_active = f'<span class="blog-page-btn active" aria-current="page">{p_num}</span>'
    has_active = expected_active in c
    
    cards = len(re.findall(r'<article class="blog-card"', c))
    expected_cards = e_num - s_num + 1
    
    nav_match = re.search(r'<nav class="blog-pagination-nav"[^>]*>(.*?)</nav>', c, re.DOTALL)
    nav_html = nav_match.group(1) if nav_match else ''
    all_btns_present = all((f">{p}<" in nav_html) for p in range(1, 10))
    
    print(f"{file}: InfoOK={has_info} | ActiveOK={has_active} | Cards={cards}/{expected_cards} | All9BtnsPresent={all_btns_present}")
