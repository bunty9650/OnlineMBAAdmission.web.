with open('universities/amity.html', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find('cs-faq-list')
if idx != -1:
    print("--- AMITY FAQ HTML ---")
    print(c[idx-50:idx+1000])

with open('blogs/online-mba-mumbai.html', 'r', encoding='utf-8') as f:
    c = f.read()
idx2 = c.find('faq-accordion')
if idx2 != -1:
    print("\n--- MUMBAI FAQ HTML ---")
    print(c[idx2-50:idx2+1000])
