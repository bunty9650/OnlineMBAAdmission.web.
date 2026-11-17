with open('blogs/online-mba-faridabad.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('<style>')
if idx != -1:
    idx_end = c.find('</style>', idx)
    inline_css = c[idx:idx_end+8]
    print("Found inline <style> in faridabad.html (length:", len(inline_css), ")")
    if 'faq' in inline_css:
        print("FAQ mentioned in inline <style>:")
        for line in inline_css.split('\n'):
            if 'faq' in line:
                print("  ", line)
    else:
        print("NO FAQ rules in inline <style>")
