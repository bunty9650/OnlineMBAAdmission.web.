with open('universities/st-aloysius.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="faqs"')
if idx != -1:
    print(c[idx:idx+3000])
else:
    print("id faqs not found")
