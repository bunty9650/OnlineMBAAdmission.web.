import re

with open('blogs/online-mba-faridabad.html', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<style[^>]*>(.*?)</style>', c, re.DOTALL)
if m:
    print(m.group(1)[:2000])
