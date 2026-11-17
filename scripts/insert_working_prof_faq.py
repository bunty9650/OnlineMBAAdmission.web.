with open('blogs/online-mba-for-working-professionals.html', 'r', encoding='utf-8') as f:
    c = f.read()

faq_block = """
        <!-- Section 10: Frequently Asked Questions -->
        <section class="cs-card" id="faqs" style="margin-top: 32px;">
          <h2 class="cs-heading-2">Frequently Asked Questions (Online MBA for Working Professionals)</h2>
          <p>Clear, verified answers to the most frequent queries asked by working executives:</p>
          <div class="cs-faq-wrapper">
          <div class="cs-faq-item">
            <div class="cs-faq-q" onclick="toggleFaq(this)">
              <span>Can working professionals genuinely manage an online MBA alongside a 40-hour workweek?</span>
              <span class="cs-faq-icon">+</span>
            </div>
            <div class="cs-faq-a">
              <p>Yes. The program is built specifically for working executives, demanding only 10 to 14 hours of study per week. Lectures are delivered live on weekends and recorded on the cloud LMS for on-demand playback anytime after work hours.</p>
            </div>
          </div>
          <div class="cs-faq-item">
            <div class="cs-faq-q" onclick="toggleFaq(this)">
              <span>Do top employers in India value an online MBA from accredited universities?</span>
              <span class="cs-faq-icon">+</span>
            </div>
            <div class="cs-faq-a">
              <p>Yes. Leading multinationals (including Deloitte, Amazon, TCS, Infosys, Accenture, ICICI Bank, and EY) actively recruit and promote online MBA graduates from NAAC A+/A++ accredited statutory universities with full parity to regular MBAs.</p>
            </div>
          </div>
          <div class="cs-faq-item">
            <div class="cs-faq-q" onclick="toggleFaq(this)">
              <span>Do I need to submit an Employer NOC (No Objection Certificate) for an online MBA?</span>
              <span class="cs-faq-icon">+</span>
            </div>
            <div class="cs-faq-a">
              <p>Private sector employees do not require an NOC. You can enroll independently without disclosing to your employer. Only select government employees applying for official study allowances need formal departmental clearance.</p>
            </div>
          </div>
          <div class="cs-faq-item">
            <div class="cs-faq-q" onclick="toggleFaq(this)">
              <span>What is the fee range for working professional online MBAs in India?</span>
              <span class="cs-faq-icon">+</span>
            </div>
            <div class="cs-faq-a">
              <p>Total fees range from ₹1,20,000 to ₹2,60,000 across 4 semesters, payable in interest-free monthly EMIs starting from ₹4,500 to ₹8,500 per month without upfront burden.</p>
            </div>
          </div>
          <div class="cs-faq-item">
            <div class="cs-faq-q" onclick="toggleFaq(this)">
              <span>How does an online MBA compare to an Executive MBA (EMBA)?</span>
              <span class="cs-faq-icon">+</span>
            </div>
            <div class="cs-faq-a">
              <p>An Executive MBA is typically a 1-year autonomous diploma or certificate costing ₹8L to ₹25L, while an Online MBA is a full 2-year UGC-entitled Master's degree costing under ₹2.5L, making it far more accessible with identical statutory recognition.</p>
            </div>
          </div>
          </div>
        </section>
"""

marker = "<!-- In-Article Lead Counseling Form -->"
if marker in c:
    c = c.replace(marker, faq_block + "\n        " + marker)
    with open('blogs/online-mba-for-working-professionals.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("SUCCESS: Added FAQ section to online-mba-for-working-professionals.html")
else:
    print("Marker not found in online-mba-for-working-professionals.html")
