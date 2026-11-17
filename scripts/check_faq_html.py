with open('blogs/online-mba-faridabad.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="faqs"')
if idx != -1:
    print("FARIDABAD FAQ SECTION:")
    print(c[idx:idx+2000])
else:
    print("faqs id not found")
