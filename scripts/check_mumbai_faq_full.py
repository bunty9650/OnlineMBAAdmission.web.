with open('blogs/online-mba-mumbai.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="faqs"')
idx_end = c.find('</section>', idx)
print(c[idx:idx_end+10])
