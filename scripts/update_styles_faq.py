import os

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = ".cs-faq-list{display:flex;flex-direction:column;gap:12px;margin-top:20px}.cs-faq-item{border:1px solid var(--line);border-radius:8px;background:#ffffff;overflow:hidden}.cs-faq-question{padding:16px 20px;font-weight:700;font-size:15.5px;color:var(--ink);cursor:pointer;display:flex;justify-content:space-between;align-items:center;background:#ffffff;transition:background 0.2s ease}.cs-faq-question:hover{background:#f8fbfc;color:var(--brand)}.cs-faq-arrow{transition:transform 0.2s ease;font-size:16px;color:var(--muted)}.cs-faq-item.active .cs-faq-arrow{transform:rotate(180deg);color:var(--brand)}.cs-faq-answer{display:none;padding:0 20px 16px;font-size:14.5px;color:var(--text-main);border-top:1px solid #f0f4f3;padding-top:12px;line-height:1.65}.cs-faq-item.active .cs-faq-answer, details.cs-faq-item[open] .cs-faq-answer{display:block}"

replacement = """/* ==========================================================================
   PREMIUM ANIMATED FAQ & ACCORDION SYSTEM (UNIVERSAL)
   ========================================================================== */

.cs-faq-wrapper,
.cs-faq-list,
.cs-faq-container,
.faq-accordion,
.faq-accordion-list,
.faq-accordion-group {
  display: flex !important;
  flex-direction: column !important;
  gap: 14px !important;
  margin: 24px 0 36px !important;
  width: 100% !important;
}

/* Individual FAQ Card Item */
.cs-faq-item,
.faq-item,
.faq-accordion-item {
  border: 1px solid #e2e8f0 !important;
  border-radius: 12px !important;
  background: #ffffff !important;
  overflow: hidden !important;
  transition: border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease !important;
  box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04) !important;
  margin-bottom: 0 !important;
  padding: 0 !important;
}

.cs-faq-item:hover,
.faq-item:hover,
.faq-accordion-item:hover {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.07) !important;
}

.cs-faq-item.active,
.faq-item.active,
.faq-accordion-item.active,
details.cs-faq-item[open],
details.faq-accordion-item[open] {
  border-color: #0a6d6f !important;
  box-shadow: 0 6px 20px rgba(10, 109, 111, 0.12) !important;
  background: #ffffff !important;
}

/* Question Header Bar */
.cs-faq-q,
.cs-faq-question,
.faq-question,
.faq-header,
.faq-accordion-summary {
  padding: 16px 20px !important;
  font-weight: 700 !important;
  font-size: 1.02rem !important;
  color: #0f172a !important;
  cursor: pointer !important;
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  background: #ffffff !important;
  user-select: none !important;
  -webkit-tap-highlight-color: transparent !important;
  transition: background 0.2s ease, color 0.2s ease !important;
  gap: 16px !important;
  line-height: 1.45 !important;
  margin: 0 !important;
  outline: none !important;
}

.cs-faq-q:hover,
.cs-faq-question:hover,
.faq-question:hover,
.faq-header:hover,
.faq-accordion-summary:hover {
  background: #f8fafc !important;
  color: #0a6d6f !important;
}

.cs-faq-item.active > .cs-faq-q,
.cs-faq-item.active > .cs-faq-question,
.faq-item.active > .faq-question,
.faq-item.active > .faq-header,
.faq-accordion-item[open] > .faq-accordion-summary {
  color: #0a6d6f !important;
  background: #f8fbfb !important;
}

.cs-faq-q span:first-child,
.cs-faq-question span:first-child,
.faq-question span:first-child,
.faq-accordion-summary span:first-child {
  flex: 1 !important;
}

/* Toggle Icon Badge */
.cs-faq-icon,
.cs-faq-arrow,
.faq-chevron,
.faq-accordion-chevron {
  width: 32px !important;
  height: 32px !important;
  min-width: 32px !important;
  border-radius: 50% !important;
  background: #f1f5f9 !important;
  color: #0a6d6f !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 1.25rem !important;
  font-weight: 700 !important;
  line-height: 1 !important;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), background 0.25s ease, color 0.25s ease !important;
  flex-shrink: 0 !important;
  margin-left: 12px !important;
}

.cs-faq-q:hover .cs-faq-icon,
.cs-faq-question:hover .cs-faq-arrow,
.faq-question:hover .faq-chevron {
  background: #e2e8f0 !important;
  color: #074e52 !important;
}

/* Icon Rotation on Active */
.cs-faq-item.active .cs-faq-icon {
  transform: rotate(45deg) !important;
  background: #0a6d6f !important;
  color: #ffffff !important;
}

.cs-faq-item.active .cs-faq-arrow,
.faq-item.active .faq-chevron,
.faq-accordion-item[open] .faq-accordion-chevron {
  transform: rotate(180deg) !important;
  background: #0a6d6f !important;
  color: #ffffff !important;
}

/* Answer Drawer (Smooth Height & Opacity Animation) */
.cs-faq-a,
.cs-faq-answer,
.faq-answer,
.faq-content,
.faq-accordion-body {
  max-height: 0 !important;
  opacity: 0 !important;
  overflow: hidden !important;
  transition: max-height 0.35s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.25s ease, padding 0.35s ease !important;
  padding: 0 20px !important;
  border-top: 1px solid transparent !important;
  color: #475569 !important;
  font-size: 0.95rem !important;
  line-height: 1.7 !important;
  display: block !important;
}

.cs-faq-a p,
.cs-faq-answer p,
.faq-answer p,
.faq-content p,
.faq-accordion-body p {
  margin: 0 !important;
  line-height: 1.7 !important;
  color: #475569 !important;
}

/* Active State: Open Smoothly */
.cs-faq-item.active > .cs-faq-a,
.cs-faq-item.active > .cs-faq-answer,
.faq-item.active > .faq-answer,
.faq-item.active > .faq-content,
.faq-accordion-item[open] > .faq-accordion-body {
  max-height: 1000px !important;
  opacity: 1 !important;
  padding: 16px 20px 22px 20px !important;
  border-top: 1px solid #f1f5f9 !important;
  background: #ffffff !important;
}

@media (max-width: 640px) {
  .cs-faq-q,
  .cs-faq-question,
  .faq-question {
    padding: 14px 16px !important;
    font-size: 0.96rem !important;
    gap: 12px !important;
  }
  .cs-faq-icon,
  .cs-faq-arrow,
  .faq-chevron {
    width: 28px !important;
    height: 28px !important;
    min-width: 28px !important;
    font-size: 1.1rem !important;
    margin-left: 8px !important;
  }
  .cs-faq-item.active > .cs-faq-a,
  .cs-faq-item.active > .cs-faq-answer,
  .faq-item.active > .faq-answer {
    padding: 14px 16px 18px 16px !important;
  }
}
"""

if target in css:
    new_css = css.replace(target, replacement)
    with open('styles.css', 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("SUCCESS: styles.css updated with animated FAQ accordion system!")
else:
    print("ERROR: Target not found in styles.css")
