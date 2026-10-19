import re

LEAD_MODAL_HTML = """
  <!-- Static Lead Counseling Modal -->
  <div class="modal-backdrop" id="lead-modal" aria-hidden="true">
    <div class="modal-dialog" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <button class="modal-close" type="button" aria-label="Close popup">&times;</button>
      <div class="modal-eyebrow">FREE COUNSELING</div>
      <h3 id="modal-title">Still Confused About Online MBA Admission?</h3>
      <p class="modal-copy">Get a free shortlist of 200+ university options, fees, eligibility, EMI, and MBA without entrance exam choices. Submit your details and our counselor will reach out.</p>
      
      <div class="modal-chips">
        <div class="modal-chip">Free eligibility<br>check</div>
        <div class="modal-chip">Budget-wise<br>university match</div>
        <div class="modal-chip">No entrance<br>options</div>
      </div>

      <form class="lead-form modal-form" data-source="Portal Lead Modal Form" novalidate>
        <div class="form-group">
          <label for="counseling-name">Full Name</label>
          <input type="text" id="counseling-name" name="name" placeholder="Enter your name" required autocomplete="name">
        </div>
        <div class="form-group">
          <label for="counseling-phone">Mobile Number</label>
          <input type="tel" id="counseling-phone" name="phone" placeholder="10-digit mobile number" required pattern="[6-9][0-9]{9}" maxlength="10" autocomplete="tel">
        </div>
        <div class="form-group">
          <label for="counseling-email">Email Address</label>
          <input type="email" id="counseling-email" name="email" placeholder="Enter your email" required autocomplete="email">
        </div>
        <div class="form-group">
          <label for="counseling-program">Preferred MBA Type</label>
          <select id="counseling-program" name="program">
            <option value="Online MBA" selected>Online MBA</option>
            <option value="Distance MBA">Distance MBA</option>
            <option value="MBA without entrance exam">MBA without entrance exam</option>
            <option value="Not sure, need counseling">Not sure, need counseling</option>
          </select>
        </div>

        <input type="hidden" name="university" id="counseling-university" value="">

        <div class="form-group consent-group">
          <div class="consent-checkbox-wrap">
            <input type="checkbox" id="counseling-consent" name="consent" required>
            <label for="counseling-consent">I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry.</label>
          </div>
          <p class="consent-error" id="counseling-consent-error" style="display:none;" role="alert"></p>
        </div>

        <button type="submit" class="modal-submit-btn">Submit &amp; Get Free Counseling</button>
        <p class="form-message" aria-live="polite"></p>
      </form>
    </div>
  </div>
"""

pages = ['index.html', 'about.html', 'admission.html', 'comparison.html', 'blogs/index.html', 'blogs/page-2.html']

for p in pages:
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="lead-modal"' not in content:
        # Insert right before </body
        content = content.replace('</body>', f'{LEAD_MODAL_HTML}\n</body>')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added static lead-modal to {p}")
    else:
        print(f"{p} already has lead-modal")
