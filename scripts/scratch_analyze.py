with open('script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    l = line.strip()
    if l.startswith('document.addEventListener(') or l.startswith('window.addEventListener('):
        print(f'{i+1}: {l[:80]}')
