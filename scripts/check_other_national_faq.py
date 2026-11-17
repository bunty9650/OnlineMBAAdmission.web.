topics = [
    'blogs/best-online-mba-universities-in-india.html',
    'blogs/online-mba-fees-in-india.html',
    'blogs/online-mba-under-50000.html',
    'blogs/online-vs-distance-mba.html',
    'blogs/online-mba-admission-without-entrance.html',
    'blogs/online-mba-for-working-professionals.html',
    'blogs/online-mba-admission-process.html'
]

for t in topics:
    with open(t, 'r', encoding='utf-8') as f:
        c = f.read()
    idx = c.find('id="faqs"')
    if idx == -1:
        idx = c.find('id="faq"')
    if idx != -1:
        print(t, ":", c[idx:idx+300].replace('\n', ' '))
    else:
        print(t, ": NOT FOUND")
