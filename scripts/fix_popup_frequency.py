import re

with open("script.js", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Update closeLeadModal to save dismissal in sessionStorage
old_close = """function closeLeadModal() {
  const modal = document.querySelector("#lead-modal");
  if (!modal || !modal.classList.contains("is-open")) return;

  lastModalCloseTime = Date.now();
  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");"""

new_close = """function closeLeadModal() {
  const modal = document.querySelector("#lead-modal");
  if (!modal || !modal.classList.contains("is-open")) return;

  lastModalCloseTime = Date.now();
  try {
    sessionStorage.setItem("leadModalDismissed", "true");
  } catch (_) {}
  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");"""

if old_close in code:
    code = code.replace(old_close, new_close, 1)
    print("SUCCESS: closeLeadModal updated with sessionStorage dismissal.")
else:
    print("WARNING: old_close not matched directly, trying regex...")
    code = re.sub(
        r'function closeLeadModal\(\)\s*\{\s*const modal = document\.querySelector\("#lead-modal"\);\s*if \(!modal \|\| !modal\.classList\.contains\("is-open"\)\) return;\s*lastModalCloseTime = Date\.now\(\);',
        'function closeLeadModal() {\n  const modal = document.querySelector("#lead-modal");\n  if (!modal || !modal.classList.contains("is-open")) return;\n\n  lastModalCloseTime = Date.now();\n  try {\n    sessionStorage.setItem("leadModalDismissed", "true");\n  } catch (_) {}',
        code
    )

# 2. Replace the aggressive automated popups (lines 1237 to 1308)
# We find the block starting with // 1. Entry Timer Popup and ending before function ensureFormConsent
popup_block_regex = re.compile(
    r'// 1\. Entry Timer Popup.*?(?=function ensureFormConsent)',
    re.DOTALL
)

new_popup_block = """// Automated Popups Policy (User Experience & Zero-Intrusion Standard):
// - NEVER auto-popup on scroll down (Phone or Desktop)
// - NEVER interrupt users reading or scrolling with sudden entry timers
// - Respect user dismissal: once closed, never automatically popup again in the same session
// - Optional subtle desktop-only exit intent (only when mouse leaves browser window at top, max 1 time per session)
if (!isAuditBot) {
  document.addEventListener("mouseleave", (e) => {
    if (window.innerWidth <= 1024) return; // Desktop only
    if (e.clientY <= 0) { // Cursor leaves top of browser viewport
      try {
        if (sessionStorage.getItem("thankyouName")) return;
        if (sessionStorage.getItem("leadModalDismissed")) return;
        if (sessionStorage.getItem("exitIntentTriggered")) return;
        sessionStorage.setItem("exitIntentTriggered", "true");
      } catch (_) {}

      const modal = ensureCounselingModal();
      if (!modal.classList.contains("is-open") && Date.now() - lastModalCloseTime > 3000) {
        openLeadModal("", "Desktop Exit Intent Popup");
      }
    }
  });
}

"""

if popup_block_regex.search(code):
    code = popup_block_regex.sub(new_popup_block, code)
    print("SUCCESS: Automated entry timer and mobile scroll popups removed!")
else:
    print("ERROR: Could not find popup block in script.js!")

with open("script.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated script.js successfully!")
