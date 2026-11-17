with open('styles.css', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('article-faq-section')
if idx != -1:
    print("Found article-faq-section in styles.css:")
    print(c[idx-50:idx+1200])
else:
    print("article-faq-section NOT FOUND in styles.css")

idx2 = c.find('faq-accordion')
if idx2 != -1:
    print("Found faq-accordion in styles.css:")
    print(c[idx2-50:idx2+1200])
else:
    print("faq-accordion NOT FOUND in styles.css")
