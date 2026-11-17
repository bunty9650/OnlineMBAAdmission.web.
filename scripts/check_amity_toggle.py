with open('universities/amity.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('toggleFaq')
while idx != -1:
    print(c[idx-30:idx+60])
    idx = c.find('toggleFaq', idx+1)
