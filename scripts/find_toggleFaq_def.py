import os

ignore_dirs = {'.git', 'brain', '.user_uploaded', 'dist', 'build'}

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for f in files:
        if f.endswith(('.html', '.js', '.css')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    txt = fp.read()
                    if 'function toggleFaq' in txt or 'toggleFaq =' in txt or 'toggleFaq=' in txt:
                        print("toggleFaq defined in:", p)
            except:
                pass
