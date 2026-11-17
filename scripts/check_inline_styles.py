import re

with open('blogs/online-mba-faridabad.html', 'r', encoding='utf-8') as f:
    c = f.read()

styles = re.findall(r'<style[^>]*>(.*?)</style>', c, re.DOTALL)
print(f"Found {len(styles)} style blocks in faridabad.html")
for i, s in enumerate(styles):
    print(f"Block {i} length: {len(s)}")
    if 'faq' in s.lower():
        print(f"Block {i} HAS FAQ STYLES!")
    else:
        print(f"Block {i} has NO faq styles")
