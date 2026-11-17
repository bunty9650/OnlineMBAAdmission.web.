with open('blogs/online-mba-for-working-professionals.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Need Expert Admission Guidance?')
print(c[idx-200:idx+300])
