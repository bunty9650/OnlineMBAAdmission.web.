import os, re

count = 0
for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['.git', 'node_modules', '_archive']):
        continue
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            # Replace script.js?v=9.1 or script.js?v=9.0 or script.js with script.js?v=9.2
            new_content = re.sub(r'script\.js(?:\?v=[\d\.]+)?', 'script.js?v=9.2', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as fp:
                    fp.write(new_content)
                count += 1

print(f"Bumped script.js version to v=9.2 in {count} HTML files.")
