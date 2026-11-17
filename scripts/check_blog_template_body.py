with open('blogs/blog-template.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="faqs"')
if idx != -1:
    print(c[idx:idx+1200])
else:
    print("id faqs not found in body")
