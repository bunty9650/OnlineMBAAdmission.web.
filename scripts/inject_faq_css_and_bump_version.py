import os, re

faq_css = """
/* --- PREMIUM ANIMATED FAQ ACCORDION ENGINE --- */
.cs-faq-wrapper, .cs-faq-list, .faq-accordion { display: flex !important; flex-direction: column !important; gap: 14px !important; margin: 24px 0 36px !important; width: 100% !important; }
.cs-faq-item, .faq-item { border: 1px solid #e2e8f0 !important; border-radius: 12px !important; background: #ffffff !important; overflow: hidden !important; transition: border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease !important; box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04) !important; margin-bottom: 0 !important; padding: 0 !important; }
.cs-faq-item:hover, .faq-item:hover { border-color: #cbd5e1 !important; box-shadow: 0 4px 14px rgba(15, 23, 42, 0.07) !important; }
.cs-faq-item.active, .faq-item.active { border-color: #0a6d6f !important; box-shadow: 0 6px 20px rgba(10, 109, 111, 0.12) !important; background: #ffffff !important; }
.cs-faq-q, .cs-faq-question, .faq-question { padding: 16px 20px !important; font-weight: 700 !important; font-size: 1.02rem !important; color: #0f172a !important; cursor: pointer !important; display: flex !important; justify-content: space-between !important; align-items: center !important; background: #ffffff !important; user-select: none !important; -webkit-tap-highlight-color: transparent !important; transition: background 0.2s ease, color 0.2s ease !important; gap: 16px !important; line-height: 1.45 !important; margin: 0 !important; outline: none !important; }
.cs-faq-q:hover, .cs-faq-question:hover, .faq-question:hover { background: #f8fafc !important; color: #0a6d6f !important; }
.cs-faq-item.active > .cs-faq-q, .cs-faq-item.active > .cs-faq-question, .faq-item.active > .faq-question { color: #0a6d6f !important; background: #f8fbfb !important; }
.cs-faq-q span:first-child, .cs-faq-question span:first-child, .faq-question span:first-child { flex: 1 !important; }
.cs-faq-icon, .cs-faq-arrow, .faq-chevron { width: 32px !important; height: 32px !important; min-width: 32px !important; border-radius: 50% !important; background: #f1f5f9 !important; color: #0a6d6f !important; display: inline-flex !important; align-items: center !important; justify-content: center !important; font-size: 1.25rem !important; font-weight: 700 !important; line-height: 1 !important; transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), background 0.25s ease, color 0.25s ease !important; flex-shrink: 0 !important; margin-left: 12px !important; }
.cs-faq-q:hover .cs-faq-icon, .cs-faq-question:hover .cs-faq-arrow, .faq-question:hover .faq-chevron { background: #e2e8f0 !important; color: #074e52 !important; }
.cs-faq-item.active .cs-faq-icon { transform: rotate(45deg) !important; background: #0a6d6f !important; color: #ffffff !important; }
.cs-faq-item.active .cs-faq-arrow, .faq-item.active .faq-chevron { transform: rotate(180deg) !important; background: #0a6d6f !important; color: #ffffff !important; }
.cs-faq-a, .cs-faq-answer, .faq-answer { max-height: 0 !important; opacity: 0 !important; overflow: hidden !important; transition: max-height 0.35s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s ease, padding 0.35s ease !important; padding: 0 20px !important; border-top: 1px solid transparent !important; color: #475569 !important; font-size: 0.95rem !important; line-height: 1.7 !important; display: block !important; }
.cs-faq-a p, .cs-faq-answer p, .faq-answer p { margin: 0 !important; line-height: 1.7 !important; color: #475569 !important; }
.cs-faq-item.active > .cs-faq-a, .cs-faq-item.active > .cs-faq-answer, .faq-item.active > .faq-answer { max-height: 1000px !important; opacity: 1 !important; padding: 16px 20px 22px 20px !important; border-top: 1px solid #f1f5f9 !important; background: #ffffff !important; }
@media (max-width: 640px) {
  .cs-faq-q, .cs-faq-question, .faq-question { padding: 14px 16px !important; font-size: 0.96rem !important; gap: 12px !important; }
  .cs-faq-icon, .cs-faq-arrow, .faq-chevron { width: 28px !important; height: 28px !important; min-width: 28px !important; font-size: 1.1rem !important; margin-left: 8px !important; }
  .cs-faq-item.active > .cs-faq-a, .cs-faq-item.active > .cs-faq-answer, .faq-item.active > .faq-answer { padding: 14px 16px 18px 16px !important; }
}
"""

dirs_to_process = ['blogs', 'universities', '.']

updated_files = 0

for d in dirs_to_process:
    for f in os.listdir(d):
        if f.endswith('.html'):
            p = os.path.join(d, f)
            with open(p, 'r', encoding='utf-8') as fp:
                c = fp.read()
            
            modified = False
            # Bump styles and script versions
            if 'styles.css?v=' in c:
                c = re.sub(r'styles\.css\?v=[0-9.]+', 'styles.css?v=9.3', c)
                modified = True
            if 'script.js?v=' in c:
                c = re.sub(r'script\.js\?v=[0-9.]+', 'script.js?v=9.3', c)
                modified = True

            # If page has cs-faq or faq-accordion, ensure the inline style has the FAQ CSS
            if ('cs-faq' in c or 'faq-accordion' in c) and 'PREMIUM ANIMATED FAQ ACCORDION ENGINE' not in c:
                # Find </style> tag in head
                m_style = re.search(r'</style>', c)
                if m_style:
                    c = c[:m_style.start()] + faq_css + c[m_style.start():]
                    modified = True
                else:
                    # Insert a <style> block before </head>
                    m_head = re.search(r'</head>', c, re.I)
                    if m_head:
                        c = c[:m_head.start()] + f"<style>{faq_css}</style>\n" + c[m_head.start():]
                        modified = True

            if modified:
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(c)
                updated_files += 1

print(f"Successfully processed and updated {updated_files} HTML files!")
