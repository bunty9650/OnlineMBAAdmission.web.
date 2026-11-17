with open('universities/amity.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('function toggleFaq')
if idx != -1:
    print(c[idx-50:idx+400])
