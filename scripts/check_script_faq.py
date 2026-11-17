with open('script.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('toggleFaq')
if idx != -1:
    print("Found toggleFaq in script.js:")
    print(c[idx-50:idx+800])
else:
    print("toggleFaq NOT FOUND in script.js!")

idx2 = c.find('faq')
if idx2 != -1:
    print("Found faq in script.js around index", idx2)
    print(c[idx2-50:idx2+500])
