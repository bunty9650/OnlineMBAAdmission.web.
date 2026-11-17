with open('styles.css', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('cs-faq')
if idx != -1:
    print("Found cs-faq in styles.css:")
    print(c[idx-50:idx+1500])
else:
    print("cs-faq NOT FOUND in styles.css!")
