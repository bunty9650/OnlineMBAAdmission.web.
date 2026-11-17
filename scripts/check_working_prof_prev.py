with open('blogs/online-mba-for-working-professionals.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Need Expert Admission Guidance?')
idx_sec = c.rfind('<section', 0, idx)
print(c[idx_sec-500:idx_sec])
