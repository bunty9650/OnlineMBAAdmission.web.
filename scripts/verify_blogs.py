import glob, os

files = sorted(glob.glob('blogs/*.html'))
print(f"{'Filename':42} | {'Words':5} | {'TOC':5} | {'Progress':8} | {'Modal':5}")
print("-" * 75)
for f in files:
    name = os.path.basename(f)
    if name in ['index.html', 'page-2.html']:
        continue
    content = open(f, encoding='utf-8').read()
    words = len(content.split())
    has_toc = "blog-toc-card" in content
    has_prog = "reading-progress-bar" in content
    has_modal = "lead-modal" in content
print("\nChecking core portal pages for modal:")
for p in ['index.html', 'about.html', 'admission.html', 'fees.html', 'eligibility.html', 'comparison.html', 'blogs/index.html', 'blogs/page-2.html']:
    txt = open(p, encoding='utf-8').read()
    print(f"{p:30} | Modal: {'lead-modal' in txt}")
