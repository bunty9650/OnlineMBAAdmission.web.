topics = [
    'blogs/is-online-mba-valid-in-india.html',
    'blogs/government-online-distance-mba-universities.html',
    'blogs/online-mba-after-bcom.html',
    'blogs/online-mba-finance-vs-marketing-vs-hr.html',
    'blogs/online-mba-vs-regular-mba.html'
]

for t in topics:
    with open(t, 'r', encoding='utf-8') as f:
        c = f.read()
    idx = c.find('id="faqs"')
    if idx != -1:
        print(t, ":", c[idx:idx+400].replace('\n', ' '))
    else:
        print(t, ": NOT FOUND")
