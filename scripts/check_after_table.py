with open('blogs/best-online-mba-universities-in-india.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Chandigarh University (CU Onli')
print(c[idx:idx+2500])
