with open('styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'cs-faq' in line or 'article-faq-section' in line or 'faq-accordion' in line:
        print(f"Line {i+1}: {line[:120]}")
