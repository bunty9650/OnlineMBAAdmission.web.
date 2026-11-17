with open('universities/st-aloysius.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('faq')
if idx != -1:
    print("Found 'faq' in st-aloysius.html around index", idx)
    print(c[idx-100:idx+1500])
else:
    print("No 'faq' in st-aloysius.html")

# Also search for 'Frequently Asked Questions'
idx2 = c.find('Frequently Asked')
if idx2 != -1:
    print("Found 'Frequently Asked' in st-aloysius.html around index", idx2)
    print(c[idx2-100:idx2+1500])
else:
    print("No 'Frequently Asked' in st-aloysius.html")
