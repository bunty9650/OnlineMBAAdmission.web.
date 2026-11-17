with open('blogs/online-mba-bangalore.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="faqs"')
print(c[idx:idx+1500])
