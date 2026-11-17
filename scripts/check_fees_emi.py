with open('blogs/best-online-mba-universities-in-india.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('id="fees-emi"')
if idx != -1:
    print(c[idx:idx+2500])
else:
    print("Not found")
