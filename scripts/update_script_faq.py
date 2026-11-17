with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

faq_js = """
// ==========================================================================
// UNIVERSAL ANIMATED FAQ ACCORDION ENGINE
// ==========================================================================
window.toggleFaq = function(element, evt) {
  if (evt && typeof evt.preventDefault === 'function') {
    evt.preventDefault();
  }
  if (!element) return;
  
  const item = element.closest('.cs-faq-item, .faq-item, .faq-accordion-item');
  if (!item) return;

  // Prevent double-execution within 120ms
  const now = Date.now();
  if (item._faqLastToggled && (now - item._faqLastToggled < 120)) {
    return;
  }
  item._faqLastToggled = now;

  const container = item.closest('.cs-faq-wrapper, .cs-faq-list, .cs-faq-container, .faq-accordion, .faq-accordion-list, .faq-accordion-group, .article-faq-section') || item.parentElement;
  const isCurrentlyActive = item.classList.contains('active');

  // Close sibling items in the same container for clean accordion UX
  if (container) {
    container.querySelectorAll('.cs-faq-item.active, .faq-item.active, .faq-accordion-item.active').forEach(function(el) {
      if (el !== item) {
        el.classList.remove('active');
        const ans = el.querySelector('.cs-faq-a, .cs-faq-answer, .faq-answer, .faq-content, .faq-accordion-body');
        if (ans) {
          ans.style.maxHeight = null;
        }
      }
    });
  }

  // Toggle current item
  const answer = item.querySelector('.cs-faq-a, .cs-faq-answer, .faq-answer, .faq-content, .faq-accordion-body');
  if (isCurrentlyActive) {
    item.classList.remove('active');
    if (answer) {
      answer.style.maxHeight = null;
    }
  } else {
    item.classList.add('active');
    if (answer) {
      answer.style.maxHeight = (answer.scrollHeight + 40) + 'px';
    }
  }
};

// Global click event delegation for any FAQ header
document.addEventListener('click', function(e) {
  const trigger = e.target.closest('.cs-faq-q, .cs-faq-question, .faq-question, .faq-header, .faq-accordion-summary');
  if (trigger) {
    window.toggleFaq(trigger, e);
  }
});

"""

if "window.toggleFaq" not in js:
    # Add at the very top of script.js
    new_js = faq_js + js
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(new_js)
    print("SUCCESS: script.js updated with universal toggleFaq engine!")
else:
    print("INFO: window.toggleFaq already in script.js")
