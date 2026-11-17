with open('script.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('faq-question')
while idx != -1:
    print(c[idx-50:idx+250])
    print("="*40)
    idx = c.find('faq-question', idx+1)
