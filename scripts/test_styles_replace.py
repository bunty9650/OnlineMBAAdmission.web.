with open('styles.css', 'r', encoding='utf-8') as f:
    c = f.read()

target = ".cs-faq-list{display:flex;flex-direction:column;gap:12px;margin-top:20px}.cs-faq-item{border:1px solid var(--line);border-radius:8px;background:#ffffff;overflow:hidden}.cs-faq-question{padding:16px 20px;font-weight:700;font-size:15.5px;color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;background:#ffffff;transition:background 0.2s ease}.cs-faq-question:hover{background:#f8fbfc;color:var(--brand)}.cs-faq-arrow{transition:transform 0.2s ease;font-size:16px;color:var(--muted)}.cs-faq-item.active .cs-faq-arrow{transform:rotate(180deg);color:var(--brand)}.cs-faq-answer{display:none;padding:0 20px 16px;font-size:14.5px;color:var(--text-main);border-top:1px solid #f0f4f3;padding-top:12px;line-height:1.65}.cs-faq-item.active .cs-faq-answer, details.cs-faq-item[open] .cs-faq-answer{display:block}"

if target in c:
    print("Found exact target in styles.css!")
else:
    print("Exact target not found, let's check substring.")
