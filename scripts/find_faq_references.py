import os

ignore_dirs = {'.git', 'brain', '.user_uploaded', 'dist', 'build'}

results = []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for f in files:
        if f.endswith(('.css', '.js')) or (f.endswith('.html') and 'blog-template' in f):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    txt = fp.read()
                    if 'cs-faq' in txt or 'toggleFaq' in txt or 'faq-item' in txt:
                        results.append(p)
            except Exception as e:
                pass

print("Found in files:", results)
