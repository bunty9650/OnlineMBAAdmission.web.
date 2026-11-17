with open('blogs/blog-template.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('faqs')
if idx != -1:
    print(c[idx-50:idx+800])
else:
    print("faqs not found in blog-template.html")
