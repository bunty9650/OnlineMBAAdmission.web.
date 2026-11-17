with open('blogs/online-mba-mumbai.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx_faq = content.find('id="faqs"')
idx_sec_end = content.find('</section>', idx_faq)
faq_section = content[idx_faq:idx_sec_end]

idx_acc = faq_section.find('<div class="faq-accordion"')
print("idx_acc:", idx_acc)
print("From idx_acc to end:")
print(repr(faq_section[idx_acc:]))
