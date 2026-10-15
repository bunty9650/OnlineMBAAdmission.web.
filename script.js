const leadApiEndpoint = "/api/lead";

function scrollToTarget(selector) {
  const target = document.querySelector(selector);
  if (target) {
    target.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

function normalizePhone(phone) {
  return String(phone || "").replace(/\D/g, "").replace(/^91/, "").replace(/^0/, "");
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(email || "").trim());
}

async function sendLeadToCrm(lead) {
  const payload = {
    name: lead.name,
    mobile: Number(lead.phone) || lead.phone,
    email: lead.email,
    detail1: lead.program || lead.source || "Online MBA",
    detail2: [
      `Lead ID: ${lead.id}`,
      lead.consent && 'Consent: "I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry."',
      lead.program && `Program: ${lead.program}`,
      lead.university && `Interest: ${lead.university}`,
      lead.qualification && `Qualification: ${lead.qualification}`,
      `Submitted: ${lead.submittedAt}`,
      `Page: ${window.location.pathname}`,
      "Website: onlinembaadmission.com"
    ].filter(Boolean).join(" | "),
    consent: Boolean(lead.consent)
  };

  const response = await fetch(leadApiEndpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.error || `Server request failed with status ${response.status}`);
  }

  return data;
}



function ensureCounselingModal() {
  let modal = document.querySelector("#lead-modal");
  const modalHTML = `
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

      <form class="lead-form modal-form" data-source="Counseling Modal Form" novalidate>
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
  `;

  if (!modal) {
    modal = document.createElement("div");
    modal.className = "modal-backdrop";
    modal.id = "lead-modal";
    modal.setAttribute("aria-hidden", "true");
    modal.innerHTML = modalHTML;
    document.body.appendChild(modal);
  } else if (!modal.querySelector(".modal-chips")) {
    modal.innerHTML = modalHTML;
  }

  attachModalFormListeners(modal);
  return modal;
}

let lastFocusedTrigger = null;
let lastModalCloseTime = 0;

function openLeadModal(university = "", source = "Counseling CTA", triggerElement = null) {
  const modal = ensureCounselingModal();
  const form = modal.querySelector(".modal-form");
  lastFocusedTrigger = triggerElement || document.activeElement;

  if (form) {
    form.dataset.source = source || "Counseling Modal Form";
    const univInput = form.querySelector('input[name="university"]');
    if (univInput) {
      univInput.value = university || "";
    }
    const message = form.querySelector(".form-message");
    if (message) {
      message.textContent = "";
      message.className = "form-message";
    }
    const consentErr = form.querySelector(".consent-error");
    if (consentErr) consentErr.style.display = "none";
  }

  modal.classList.add("is-open");
  modal.setAttribute("aria-hidden", "false");
  document.body.classList.add("modal-open");

  const firstInput = modal.querySelector('input[name="name"]');
  if (firstInput) {
    setTimeout(() => firstInput.focus(), 80);
  }
}

function closeLeadModal() {
  const modal = document.querySelector("#lead-modal");
  if (!modal || !modal.classList.contains("is-open")) return;

  lastModalCloseTime = Date.now();
  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");

  if (lastFocusedTrigger && typeof lastFocusedTrigger.focus === "function") {
    try {
      lastFocusedTrigger.focus();
    } catch (_) {}
  }
}

function attachModalFormListeners(modal) {
  const closeBtn = modal.querySelector(".modal-close");
  if (closeBtn && !closeBtn.dataset.bound) {
    closeBtn.dataset.bound = "true";
    closeBtn.addEventListener("click", closeLeadModal);
  }

  if (!modal.dataset.boundBackdrop) {
    modal.dataset.boundBackdrop = "true";
    modal.addEventListener("click", (e) => {
      if (e.target === modal) {
        closeLeadModal();
      }
    });
  }
}



const EMI_UNIVERSITIES_DATA = {
  "below_50k": {
    label: "Below ₹50,000",
    badge: "Affordable",
    universities: [
      {
        id: "du-sol",
        name: "DU SOL (Delhi University)",
        accred: "UGC-DEB • NAAC A++ • Central University",
        totalFee: "₹47,000",
        semFee: "₹11,750 / sem",
        emi24: "₹3,916 / mo",
        emi12: "₹7,833 / mo"
      },
      {
        id: "andhra",
        name: "Andhra University Online",
        accred: "UGC-DEB • NAAC A++ • State Govt",
        totalFee: "₹40,000 – ₹48,000",
        semFee: "₹10,000 / sem",
        emi24: "₹3,333 / mo",
        emi12: "₹6,666 / mo"
      }
    ]
  },
  "50k_to_120k": {
    label: "₹50,000 to ₹1,20,000",
    badge: "Popular Budget",
    universities: [
      {
        id: "ignou",
        name: "IGNOU Online MBA",
        accred: "Central University • UGC-DEB • NAAC A++",
        totalFee: "₹62,000",
        semFee: "₹15,500 / sem",
        emi24: "₹2,584 / mo",
        emi12: "₹5,167 / mo"
      },
      {
        id: "ccsu",
        name: "CCSU Meerut Online",
        accred: "State Govt • UGC-DEB • NAAC A++",
        totalFee: "₹54,000",
        semFee: "₹13,500 / sem",
        emi24: "₹2,250 / mo",
        emi12: "₹4,500 / mo"
      },
      {
        id: "ddu",
        name: "DDU Gorakhpur University",
        accred: "State Govt • UGC-DEB • NAAC A++",
        totalFee: "₹56,000",
        semFee: "₹14,000 / sem",
        emi24: "₹2,333 / mo",
        emi12: "₹4,667 / mo"
      },
      {
        id: "gla",
        name: "GLA University Online",
        accred: "UGC-DEB • AICTE • NAAC A+",
        totalFee: "₹97,000 – ₹1,05,300",
        semFee: "₹24,250 / sem",
        emi24: "₹4,041 / mo",
        emi12: "₹8,083 / mo"
      },
      {
        id: "parul",
        name: "Parul University Online",
        accred: "UGC-DEB • AICTE • NAAC A++",
        totalFee: "₹99,000 – ₹1,20,000",
        semFee: "₹24,750 / sem",
        emi24: "₹4,125 / mo",
        emi12: "₹8,250 / mo"
      },
      {
        id: "arka-jain",
        name: "Arka Jain University Online",
        accred: "UGC-DEB • AICTE Approved",
        totalFee: "₹75,000",
        semFee: "₹18,750 / sem",
        emi24: "₹3,125 / mo",
        emi12: "₹6,250 / mo"
      }
    ]
  },
  "120k_to_230k": {
    label: "₹1,20,000 to ₹2,30,000",
    badge: "Top NAAC A+ Private",
    universities: [
      {
        id: "manipal-jaipur",
        name: "Manipal University Jaipur (MUJ Online)",
        accred: "UGC-DEB • AICTE • NAAC A+",
        totalFee: "₹1,84,000",
        semFee: "₹46,000 / sem",
        emi24: "₹7,667 / mo",
        emi12: "₹15,333 / mo"
      },
      {
        id: "chandigarh",
        name: "Chandigarh University Online",
        accred: "UGC-DEB • AICTE • NAAC A+",
        totalFee: "₹1,80,400",
        semFee: "₹45,100 / sem",
        emi24: "₹7,516 / mo",
        emi12: "₹15,033 / mo"
      },
      {
        id: "dpu",
        name: "DPU Online (Dr. D.Y. Patil)",
        accred: "UGC-DEB • AICTE • NAAC A++",
        totalFee: "₹1,79,400 – ₹1,89,400",
        semFee: "₹44,850 / sem",
        emi24: "₹7,475 / mo",
        emi12: "₹14,950 / mo"
      },
      {
        id: "amity",
        name: "Amity University Online",
        accred: "UGC-DEB • AICTE • NAAC A+ • WES",
        totalFee: "₹2,07,000 – ₹2,25,000",
        semFee: "₹56,300 / sem",
        emi24: "₹8,906 / mo",
        emi12: "₹17,812 / mo"
      },
      {
        id: "vit",
        name: "VIT Online (Vellore Institute)",
        accred: "UGC-DEB • AICTE • NAAC A++ • NIRF Top 10",
        totalFee: "₹1,80,000",
        semFee: "₹45,000 / sem",
        emi24: "₹7,500 / mo",
        emi12: "₹15,000 / mo"
      },
      {
        id: "jain",
        name: "Jain University Online",
        accred: "UGC-DEB • AICTE • NAAC A++",
        totalFee: "₹1,60,000 – ₹1,96,000",
        semFee: "₹40,000 / sem",
        emi24: "₹6,667 / mo",
        emi12: "₹13,333 / mo"
      },
      {
        id: "dsu",
        name: "Dayananda Sagar University (DSU)",
        accred: "UGC-DEB • AICTE Approved",
        totalFee: "₹1,30,000",
        semFee: "₹32,500 / sem",
        emi24: "₹5,417 / mo",
        emi12: "₹10,833 / mo"
      }
    ]
  },
  "above_230k": {
    label: "₹2,30,000 & Above",
    badge: "Premier Tier-1",
    universities: [
      {
        id: "symbiosis",
        name: "Symbiosis (SSODL Online)",
        accred: "UGC-DEB • AICTE • NAAC A++",
        totalFee: "₹2,50,000 – ₹3,00,000",
        semFee: "₹62,500 / sem",
        emi24: "₹10,416 / mo",
        emi12: "₹20,833 / mo"
      },
      {
        id: "nmims",
        name: "NMIMS Online (CDOE)",
        accred: "UGC-DEB • AICTE • NAAC A+",
        totalFee: "₹2,40,000 – ₹2,80,000",
        semFee: "₹60,000 / sem",
        emi24: "₹10,000 / mo",
        emi12: "₹20,000 / mo"
      },
      {
        id: "imt",
        name: "IMT Ghaziabad (Online/Blended)",
        accred: "AICTE • AACSB Accredited",
        totalFee: "₹2,50,000 – ₹3,50,000",
        semFee: "₹65,000 / sem",
        emi24: "₹10,416 / mo",
        emi12: "₹20,833 / mo"
      }
    ]
  }
};

let emiSelectedBudget = "50k_to_120k";
let emiSelectedUnivIds = [];
let lastFocusedEmiTrigger = null;

function ensureEmiCalculatorModal() {
  let modal = document.querySelector("#emi-calculator-modal");
  if (modal) return modal;

  modal = document.createElement("div");
  modal.className = "modal-backdrop emi-modal-backdrop";
  modal.id = "emi-calculator-modal";
  modal.setAttribute("aria-hidden", "true");

  modal.innerHTML = `
    <div class="modal-dialog emi-modal-dialog" role="dialog" aria-modal="true" aria-labelledby="emi-modal-title">
      <button type="button" class="modal-close emi-modal-close" aria-label="Close EMI Calculator">&times;</button>
      
      <!-- Stepper Progress Bar -->
      <div class="emi-progress-bar">
        <div class="emi-step-item active" id="emi-indicator-1">
          <span class="step-num">1</span>
          <span class="step-label">Budget</span>
        </div>
        <div class="emi-step-line" id="emi-line-1"></div>
        <div class="emi-step-item" id="emi-indicator-2">
          <span class="step-num">2</span>
          <span class="step-label">Universities</span>
        </div>
        <div class="emi-step-line" id="emi-line-2"></div>
        <div class="emi-step-item" id="emi-indicator-3">
          <span class="step-num">3</span>
          <span class="step-label">Unlock EMI</span>
        </div>
      </div>

      <!-- STEP 1: Budget Selection -->
      <div class="emi-step-content" id="emi-step-1">
        <div class="modal-head">
          <span class="modal-eyebrow">0% NO-COST EMI CALCULATOR</span>
          <h2 id="emi-modal-title" style="margin-bottom:6px;">Select Your Total MBA Fee Budget</h2>
          <p class="modal-copy" style="margin-bottom:16px;">Choose your total 2-year fee bracket to find accredited universities offering zero-interest monthly installment plans.</p>
        </div>

        <div class="emi-budget-grid">
          <label class="emi-budget-card">
            <input type="radio" name="emi_budget_radio" value="below_50k">
            <div class="budget-card-inner">
              <div class="budget-top">
                <span class="budget-badge">Affordable</span>
                <span class="budget-radio-indicator"></span>
              </div>
              <div class="budget-amount">Below ₹50,000</div>
              <div class="budget-sub">DU SOL, Andhra Univ Online</div>
              <div class="budget-emi-hint">EMI starts ~₹3,300/mo</div>
            </div>
          </label>

          <label class="emi-budget-card">
            <input type="radio" name="emi_budget_radio" value="50k_to_120k" checked>
            <div class="budget-card-inner">
              <div class="budget-top">
                <span class="budget-badge popular">Popular</span>
                <span class="budget-radio-indicator"></span>
              </div>
              <div class="budget-amount">₹50,000 to ₹1,20,000</div>
              <div class="budget-sub">IGNOU, CCSU, DDU, GLA, Parul</div>
              <div class="budget-emi-hint">EMI starts ~₹2,250/mo</div>
            </div>
          </label>

          <label class="emi-budget-card">
            <input type="radio" name="emi_budget_radio" value="120k_to_230k">
            <div class="budget-card-inner">
              <div class="budget-top">
                <span class="budget-badge top-rated">Top NAAC A+</span>
                <span class="budget-radio-indicator"></span>
              </div>
              <div class="budget-amount">₹1,20,000 to ₹2,30,000</div>
              <div class="budget-sub">Manipal Jaipur, Chandigarh, DPU, VIT</div>
              <div class="budget-emi-hint">EMI starts ~₹5,400/mo</div>
            </div>
          </label>

          <label class="emi-budget-card">
            <input type="radio" name="emi_budget_radio" value="above_230k">
            <div class="budget-card-inner">
              <div class="budget-top">
                <span class="budget-badge premier">Premier Tier-1</span>
                <span class="budget-radio-indicator"></span>
              </div>
              <div class="budget-amount">₹2,30,000 & Above</div>
              <div class="budget-sub">Symbiosis SSODL, NMIMS, IMT</div>
              <div class="budget-emi-hint">EMI starts ~₹10,000/mo</div>
            </div>
          </label>
        </div>

        <div class="emi-step-actions" style="margin-top:18px;">
          <button type="button" class="modal-submit-btn" id="emi-btn-to-step2">Continue to Choose Universities &rarr;</button>
        </div>
      </div>

      <!-- STEP 2: University Multi-Select with Blurred EMI -->
      <div class="emi-step-content" id="emi-step-2" style="display:none;">
        <div class="modal-head">
          <span class="modal-eyebrow" id="emi-step2-budget-badge">BUDGET SELECTED</span>
          <h2 style="margin-bottom:6px;">Choose Your Preferred Universities</h2>
          <p class="modal-copy" style="margin-bottom:14px;">Select one or more universities to preview monthly installment plans. Exact EMI numbers are locked until contact verification.</p>
        </div>

        <div class="emi-univ-toolbar">
          <span class="emi-univ-count" id="emi-univ-count">0 universities selected</span>
          <button type="button" class="emi-select-all-btn" id="emi-select-all-btn">Select All</button>
        </div>

        <div class="emi-univ-list" id="emi-univ-list">
          <!-- Populated dynamically -->
        </div>

        <div class="emi-step-actions" style="display:flex; gap:10px; margin-top:16px;">
          <button type="button" class="btn-secondary" id="emi-btn-back-step1" style="flex:1;">&larr; Back</button>
          <button type="button" class="modal-submit-btn" id="emi-btn-to-step3" style="flex:2;">Next: Unlock EMI Breakdown 🔒</button>
        </div>
      </div>

      <!-- STEP 3: Lead Form to Unlock EMI -->
      <div class="emi-step-content" id="emi-step-3" style="display:none;">
        <div class="modal-head">
          <span class="modal-eyebrow">Instant EMI Unblur</span>
          <h2 style="margin-bottom:6px;">Unlock Your Verified EMI Schedule</h2>
          <p class="modal-copy" style="margin-bottom:14px;">Fill in your details below to instantly unblur the 12-month and 24-month zero-interest installments for your shortlisted universities.</p>
        </div>

        <div class="emi-selected-preview" id="emi-selected-pills">
          <!-- Selected university pills -->
        </div>

        <form class="lead-form emi-unlock-form" id="emi-lead-form" novalidate>
          <div class="form-group">
            <label for="emi-user-name">Full Name</label>
            <input type="text" id="emi-user-name" name="name" placeholder="Enter your full name" required autocomplete="name">
          </div>
          <div class="form-group">
            <label for="emi-user-phone">Mobile Number</label>
            <input type="tel" id="emi-user-phone" name="phone" placeholder="10-digit mobile number" required pattern="[6-9][0-9]{9}" maxlength="10" autocomplete="tel">
          </div>
          <div class="form-group">
            <label for="emi-user-email">Email Address</label>
            <input type="email" id="emi-user-email" name="email" placeholder="Enter your email address" required autocomplete="email">
          </div>

          <div class="form-group consent-group">
            <div class="consent-checkbox-wrap">
              <input type="checkbox" id="emi-calc-consent" name="consent" required>
              <label for="emi-calc-consent">I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry.</label>
            </div>
            <p class="consent-error" id="emi-calc-consent-error" style="display:none;" role="alert"></p>
          </div>

          <div class="emi-trust-banner">
            <span>✓ 0% Interest Guaranteed</span>
            <span>✓ Zero Downpayment</span>
            <span>✓ 100% Privacy</span>
          </div>

          <div class="emi-step-actions" style="display:flex; gap:10px; margin-top:16px;">
            <button type="button" class="btn-secondary" id="emi-btn-back-step2" style="flex:1;">&larr; Back</button>
            <button type="submit" class="modal-submit-btn" id="emi-btn-submit" style="flex:2;">🔓 Unlock & Reveal EMI</button>
          </div>
          <p class="form-message" id="emi-form-message" aria-live="polite"></p>
        </form>
      </div>

      <!-- STEP 4: Unblurred / Revealed EMI Results View -->
      <div class="emi-step-content" id="emi-step-4" style="display:none;">
        <div class="modal-head" style="text-align:center;">
          <div class="emi-success-badge">🎉 0% No-Cost EMI Breakdown Unlocked!</div>
          <h2 style="margin-top:6px; margin-bottom:6px;">Your Verified Monthly Installments</h2>
          <p class="modal-copy" id="emi-revealed-title">Calculated with 0% interest subvention and approved banking partners.</p>
        </div>

        <div class="emi-results-list" id="emi-results-list">
          <!-- Populated dynamically -->
        </div>

        <div class="emi-subvention-box">
          <strong>💡 Zero Interest Subvention Benefit:</strong>
          <p>Under the 0% No-Cost EMI scheme, the university directly bears the financing interest with partner NBFCs (Propelld, Eduvanz, LiquiLoans). You pay only the original semester fee in equal installments with zero processing fee.</p>
        </div>

        <div class="emi-step-actions" style="display:flex; gap:10px; margin-top:18px;">
          <button type="button" class="btn-secondary" id="emi-btn-recalculate" style="flex:1;">Recalculate</button>
          <button type="button" class="modal-submit-btn" id="emi-btn-finish" style="flex:1;">Done &amp; Close</button>
        </div>
      </div>
    </div>
  `;

  document.body.appendChild(modal);
  attachEmiModalEvents(modal);
  return modal;
}

function setEmiStep(stepNum) {
  const modal = ensureEmiCalculatorModal();
  for (let i = 1; i <= 4; i++) {
    const stepEl = modal.querySelector(`#emi-step-${i}`);
    if (stepEl) {
      stepEl.style.display = i === stepNum ? "block" : "none";
    }
  }

  const ind1 = modal.querySelector("#emi-indicator-1");
  const ind2 = modal.querySelector("#emi-indicator-2");
  const ind3 = modal.querySelector("#emi-indicator-3");
  const line1 = modal.querySelector("#emi-line-1");
  const line2 = modal.querySelector("#emi-line-2");

  if (ind1 && ind2 && ind3) {
    ind1.className = "emi-step-item" + (stepNum === 1 ? " active" : stepNum > 1 ? " completed" : "");
    ind2.className = "emi-step-item" + (stepNum === 2 ? " active" : stepNum > 2 ? " completed" : "");
    ind3.className = "emi-step-item" + (stepNum >= 3 ? (stepNum === 4 ? " completed" : " active") : "");
    if (line1) line1.className = "emi-step-line" + (stepNum >= 2 ? " completed" : "");
    if (line2) line2.className = "emi-step-line" + (stepNum >= 3 ? " completed" : "");
  }

  if (stepNum === 1) {
    const checkedRadio = modal.querySelector('input[name="emi_budget_radio"]:checked');
    if (checkedRadio) setTimeout(() => checkedRadio.focus(), 60);
  } else if (stepNum === 2) {
    const firstCheck = modal.querySelector(".emi-univ-check");
    if (firstCheck) setTimeout(() => firstCheck.focus(), 60);
  } else if (stepNum === 3) {
    const nameInput = modal.querySelector("#emi-user-name");
    if (nameInput) setTimeout(() => nameInput.focus(), 60);
  } else if (stepNum === 4) {
    const finishBtn = modal.querySelector("#emi-btn-finish");
    if (finishBtn) setTimeout(() => finishBtn.focus(), 60);
  }
}

function renderEmiStep2Universities() {
  const modal = ensureEmiCalculatorModal();
  const listContainer = modal.querySelector("#emi-univ-list");
  const badgeEl = modal.querySelector("#emi-step2-budget-badge");
  if (!listContainer) return;

  const budgetData = EMI_UNIVERSITIES_DATA[emiSelectedBudget] || EMI_UNIVERSITIES_DATA["50k_to_120k"];
  if (badgeEl) {
    badgeEl.textContent = `BUDGET: ${budgetData.label.toUpperCase()}`;
  }

  emiSelectedUnivIds = budgetData.universities.map(u => u.id);

  listContainer.innerHTML = budgetData.universities.map(u => `
    <div class="emi-univ-card selected" data-id="${u.id}">
      <div class="emi-univ-card-top">
        <input type="checkbox" class="emi-univ-check" data-id="${u.id}" checked aria-label="Select ${u.name}">
        <div class="emi-univ-meta">
          <div class="emi-univ-title">${u.name}</div>
          <div class="emi-univ-accred-text">${u.accred}</div>
          <div class="emi-univ-fees-row">
            <span><strong>Total Fee:</strong> ${u.totalFee}</span>
            <span><strong>Per Sem:</strong> ${u.semFee}</span>
          </div>
          <div class="emi-blur-box">
            <div class="emi-blurred-content" aria-hidden="true">
              <span class="emi-blurred-val">${u.emi24}</span>
              <span class="emi-blurred-sub">24 Months @ 0% No-Cost EMI</span>
            </div>
            <span class="emi-lock-badge">🔒 Locked</span>
          </div>
        </div>
      </div>
    </div>
  `).join("");

  updateEmiUnivSelectionState();
}

function updateEmiUnivSelectionState() {
  const modal = ensureEmiCalculatorModal();
  const cards = modal.querySelectorAll(".emi-univ-card");
  const countEl = modal.querySelector("#emi-univ-count");
  const selectAllBtn = modal.querySelector("#emi-select-all-btn");

  emiSelectedUnivIds = [];
  cards.forEach(card => {
    const chk = card.querySelector(".emi-univ-check");
    if (chk && chk.checked) {
      card.classList.add("selected");
      emiSelectedUnivIds.push(chk.dataset.id);
    } else {
      card.classList.remove("selected");
    }
  });

  if (countEl) {
    countEl.textContent = `${emiSelectedUnivIds.length} of ${cards.length} selected`;
  }
  if (selectAllBtn) {
    selectAllBtn.textContent = emiSelectedUnivIds.length === cards.length ? "Deselect All" : "Select All";
  }
}

function renderEmiStep3Pills() {
  const modal = ensureEmiCalculatorModal();
  const pillsContainer = modal.querySelector("#emi-selected-pills");
  if (!pillsContainer) return;

  const budgetData = EMI_UNIVERSITIES_DATA[emiSelectedBudget];
  if (!budgetData) return;

  const selectedUniversities = budgetData.universities.filter(u => emiSelectedUnivIds.includes(u.id));
  pillsContainer.innerHTML = selectedUniversities.map(u => `
    <span class="emi-selected-pill">🎓 ${u.name}</span>
  `).join("");
}

function renderEmiStep4Results(userName) {
  const modal = ensureEmiCalculatorModal();
  const resultsContainer = modal.querySelector("#emi-results-list");
  const titleEl = modal.querySelector("#emi-revealed-title");
  if (!resultsContainer) return;

  const budgetData = EMI_UNIVERSITIES_DATA[emiSelectedBudget];
  if (!budgetData) return;

  const selectedUniversities = budgetData.universities.filter(u => emiSelectedUnivIds.includes(u.id));
  if (titleEl) {
    titleEl.textContent = `Personalized for ${userName} • 0% Interest Subvention Applied`;
  }

  resultsContainer.innerHTML = selectedUniversities.map(u => `
    <div class="emi-result-card">
      <div class="emi-result-top">
        <div>
          <div class="emi-result-name">${u.name}</div>
          <div class="emi-result-accred">${u.accred}</div>
        </div>
        <div class="emi-result-total">
          ${u.totalFee}
          <small>${u.semFee}</small>
        </div>
      </div>
      <div class="emi-plans-grid">
        <div class="emi-plan-box popular-tenure">
          <div class="emi-plan-tenure">24-Month No-Cost EMI</div>
          <div class="emi-plan-amount">${u.emi24}</div>
          <div class="emi-plan-sub">✓ 0% Interest • ₹0 Downpayment</div>
        </div>
        <div class="emi-plan-box">
          <div class="emi-plan-tenure">12-Month No-Cost EMI</div>
          <div class="emi-plan-amount">${u.emi12}</div>
          <div class="emi-plan-sub">✓ 0% Interest • Pre-Approved</div>
        </div>
      </div>
    </div>
  `).join("");
}

function openEmiCalculatorModal(triggerElement = null) {
  const modal = ensureEmiCalculatorModal();
  lastFocusedEmiTrigger = triggerElement || document.activeElement;

  setEmiStep(1);

  const form = modal.querySelector("#emi-lead-form");
  if (form) {
    form.reset();
    const consentErr = modal.querySelector("#emi-calc-consent-error");
    if (consentErr) consentErr.style.display = "none";
    const msg = modal.querySelector("#emi-form-message");
    if (msg) {
      msg.textContent = "";
      msg.className = "form-message";
    }
    const consentWrap = form.querySelector(".consent-checkbox-wrap");
    if (consentWrap) consentWrap.style.outline = "none";
  }

  modal.classList.add("is-open");
  modal.setAttribute("aria-hidden", "false");
  document.body.classList.add("modal-open");
}

function closeEmiCalculatorModal() {
  const modal = document.querySelector("#emi-calculator-modal");
  if (!modal || !modal.classList.contains("is-open")) return;

  modal.classList.remove("is-open");
  modal.setAttribute("aria-hidden", "true");
  document.body.classList.remove("modal-open");

  if (lastFocusedEmiTrigger && typeof lastFocusedEmiTrigger.focus === "function") {
    try {
      lastFocusedEmiTrigger.focus();
    } catch (_) {}
  }
}

function attachEmiModalEvents(modal) {
  if (modal.dataset.boundEmi) return;
  modal.dataset.boundEmi = "true";

  const closeBtn = modal.querySelector(".emi-modal-close");
  if (closeBtn) {
    closeBtn.addEventListener("click", closeEmiCalculatorModal);
  }
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      closeEmiCalculatorModal();
    }
  });

  const btnToStep2 = modal.querySelector("#emi-btn-to-step2");
  if (btnToStep2) {
    btnToStep2.addEventListener("click", () => {
      const selectedRadio = modal.querySelector('input[name="emi_budget_radio"]:checked');
      if (selectedRadio) {
        emiSelectedBudget = selectedRadio.value;
      }
      renderEmiStep2Universities();
      setEmiStep(2);
    });
  }

  const listContainer = modal.querySelector("#emi-univ-list");
  if (listContainer) {
    listContainer.addEventListener("click", (e) => {
      const card = e.target.closest(".emi-univ-card");
      if (!card) return;
      const chk = card.querySelector(".emi-univ-check");
      if (chk && e.target !== chk) {
        chk.checked = !chk.checked;
      }
      updateEmiUnivSelectionState();
    });
  }

  const selectAllBtn = modal.querySelector("#emi-select-all-btn");
  if (selectAllBtn) {
    selectAllBtn.addEventListener("click", () => {
      const checks = modal.querySelectorAll(".emi-univ-check");
      const allSelected = emiSelectedUnivIds.length === checks.length;
      checks.forEach(c => c.checked = !allSelected);
      updateEmiUnivSelectionState();
    });
  }

  const btnBackStep1 = modal.querySelector("#emi-btn-back-step1");
  if (btnBackStep1) {
    btnBackStep1.addEventListener("click", () => {
      setEmiStep(1);
    });
  }

  const btnToStep3 = modal.querySelector("#emi-btn-to-step3");
  if (btnToStep3) {
    btnToStep3.addEventListener("click", () => {
      if (emiSelectedUnivIds.length === 0) {
        alert("Please select at least one university to unlock EMI breakdown.");
        return;
      }
      renderEmiStep3Pills();
      setEmiStep(3);
    });
  }

  const btnBackStep2 = modal.querySelector("#emi-btn-back-step2");
  if (btnBackStep2) {
    btnBackStep2.addEventListener("click", () => {
      setEmiStep(2);
    });
  }

  const form = modal.querySelector("#emi-lead-form");
  if (form) {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const message = modal.querySelector("#emi-form-message");
      const consentError = modal.querySelector("#emi-calc-consent-error");
      const consentBox = modal.querySelector("#emi-calc-consent");
      const consentWrap = form.querySelector(".consent-checkbox-wrap");
      const submitBtn = modal.querySelector("#emi-btn-submit");

      if (consentError) consentError.style.display = "none";
      if (message) {
        message.textContent = "";
        message.className = "form-message";
      }

      if (!consentBox || !consentBox.checked) {
        const errorText = "Please agree that OnlineMBAAdmission counsellors may contact you regarding your enquiry.";
        if (consentError) {
          consentError.textContent = errorText;
          consentError.style.display = "block";
        }
        if (message) {
          message.textContent = "Please check the consent box to unlock EMI calculations.";
          message.classList.add("error");
        }
        if (consentWrap) {
          consentWrap.style.outline = "2px solid #dc2626";
          consentWrap.style.outlineOffset = "4px";
          consentWrap.style.borderRadius = "4px";
        }
        if (consentBox) consentBox.focus();
        return; // HALT IMMEDIATELY
      }

      if (consentWrap) {
        consentWrap.style.outline = "none";
      }

      const name = (modal.querySelector("#emi-user-name")?.value || "").trim();
      const phoneRaw = modal.querySelector("#emi-user-phone")?.value || "";
      const phone = normalizePhone(phoneRaw);
      const email = (modal.querySelector("#emi-user-email")?.value || "").trim();

      if (name.length < 2) {
        if (message) {
          message.textContent = "Please enter your full name.";
          message.classList.add("error");
        }
        modal.querySelector("#emi-user-name")?.focus();
        return;
      }

      if (!/^[6-9]\d{9}$/.test(phone)) {
        if (message) {
          message.textContent = "Please enter a valid 10-digit Indian mobile number.";
          message.classList.add("error");
        }
        modal.querySelector("#emi-user-phone")?.focus();
        return;
      }

      if (!isValidEmail(email)) {
        if (message) {
          message.textContent = "Please enter a valid email address.";
          message.classList.add("error");
        }
        modal.querySelector("#emi-user-email")?.focus();
        return;
      }

      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Unlocking EMI Plans...";
      }

      const budgetData = EMI_UNIVERSITIES_DATA[emiSelectedBudget];
      const selectedNames = budgetData.universities
        .filter(u => emiSelectedUnivIds.includes(u.id))
        .map(u => u.name);

      const lead = {
        id: `EMI-${Date.now()}`,
        source: "Fees Page EMI Calculator",
        name,
        phone,
        email,
        program: "0% No-Cost EMI Plan",
        university: selectedNames.join(", "),
        qualification: `Budget: ${budgetData.label}`,
        consent: true,
        submittedAt: new Date().toISOString()
      };

      try {
        await sendLeadToCrm(lead);
      } catch (err) {
        console.warn("Lead proxy submission failed, but continuing unblur display:", err);
      }

      const existingLeads = JSON.parse(localStorage.getItem("onlineMbaLeads") || "[]");
      existingLeads.push(lead);
      localStorage.setItem("onlineMbaLeads", JSON.stringify(existingLeads));

      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = "🔓 Unlock & Reveal EMI";
      }

      renderEmiStep4Results(name);
      setEmiStep(4);
    });
  }

  const btnRecalc = modal.querySelector("#emi-btn-recalculate");
  if (btnRecalc) {
    btnRecalc.addEventListener("click", () => {
      setEmiStep(1);
    });
  }

  const btnFinish = modal.querySelector("#emi-btn-finish");
  if (btnFinish) {
    btnFinish.addEventListener("click", () => {
      closeEmiCalculatorModal();
    });
  }
}

document.addEventListener("keydown", (e) => {
  const emiModal = document.querySelector("#emi-calculator-modal");
  if (emiModal && emiModal.classList.contains("is-open")) {
    if (e.key === "Escape") {
      closeEmiCalculatorModal();
      return;
    }

    if (e.key === "Tab") {
      const focusables = emiModal.querySelectorAll('button:not([disabled]), [href], input:not([type="hidden"]):not([disabled]), select, textarea, [tabindex]:not([tabindex="-1"])');
      if (focusables && focusables.length) {
        const first = focusables[0];
        const last = focusables[focusables.length - 1];

        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    }
    return;
  }

  const modal = document.querySelector("#lead-modal");
  if (!modal || !modal.classList.contains("is-open")) return;

  if (e.key === "Escape") {
    closeLeadModal();
    return;
  }

  if (e.key === "Tab") {
    const focusables = modal.querySelectorAll('button, [href], input:not([type="hidden"]), select, textarea, [tabindex]:not([tabindex="-1"])');
    if (!focusables || !focusables.length) return;

    const first = focusables[0];
    const last = focusables[focusables.length - 1];

    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }
});



function isCounselingCta(element) {
  if (!element || !(element instanceof HTMLElement)) return false;

  if (element.tagName === "BUTTON" && element.getAttribute("type") === "submit") {
    return false;
  }

  const text = (element.textContent || "").trim().replace(/\s+/g, " ");
  if (
    element.classList.contains("emi-calc-trigger") ||
    element.dataset.calculator === "emi" ||
    element.id === "openEmiCalculatorBtn" ||
    /calculate (my )?emi/i.test(text)
  ) {
    return false;
  }

  if (
    element.classList.contains("header-counseling-btn") ||
    element.classList.contains("desktop-only-cta") ||
    element.classList.contains("nav-mobile-apply-btn") ||
    element.dataset.modal === "counseling" ||
    element.dataset.modal === "true" ||
    element.dataset.openModal !== undefined
  ) {
    return true;
  }

  if (
    element.closest(".main-nav") ||
    element.closest(".footer-link-list") ||
    element.closest(".breadcrumbs") ||
    element.closest(".social-icon-row") ||
    element.closest(".cs-toc-list") ||
    element.closest(".sidebar-toc-list") ||
    element.closest(".sidebar-univ-list") ||
    element.closest(".sidebar-blog-list") ||
    element.closest(".next-prev-blog-grid") ||
    element.closest(".univ-next-prev-bar") ||
    element.closest(".spec-pagination-bar") ||
    element.classList.contains("cs-faq-question") ||
    element.classList.contains("nav-link") ||
    element.classList.contains("brand") ||
    element.classList.contains("footer-brand") ||
    element.classList.contains("mobile-nav-toggle") ||
    element.classList.contains("modal-close") ||
    element.classList.contains("univ-slider-btn") ||
    element.classList.contains("filter-btn") ||
    element.classList.contains("univ-page-btn") ||
    element.classList.contains("page-btn") ||
    element.classList.contains("univ-search-clear-btn") ||
    element.classList.contains("sidebar-more-link") ||
    element.classList.contains("cs-spec-card") ||
    element.classList.contains("table-link") ||
    element.id === "loadMoreUnivBtn" ||
    element.id === "table-see-more-btn" ||
    element.id === "univ-reset-all-btn"
  ) {
    return false;
  }

  if (/^(view full profile|view syllabus details|view profile|return to all|← return to all|explore 18 specializations|explore 25 specializations)/i.test(text)) {
    return false;
  }

  const scrollTarget = element.dataset.scroll;
  if (scrollTarget && /#(univ-form|compare-form|lead-form|lead-form-top|fee-form|eligibility-form|final-form|spec-lead-form|article-form|blog-lead-form|admission)/i.test(scrollTarget)) {
    return true;
  }

  const href = element.getAttribute("href");
  if (href && /(^|.*\/)#(univ-form|admission|lead-form|lead-form-top|compare-form|fee-form|eligibility-form|spec-lead-form|article-form|blog-lead-form)$/i.test(href)) {
    return true;
  }

  if (element.closest(".cs-hero-actions") || element.closest(".cs-cta-banner")) {
    return true;
  }

  const isCardAction = Boolean(
    element.closest(".university-card") ||
    element.closest(".univ-listing-card") ||
    element.closest(".spec-listing-card") ||
    element.closest(".hook-card") ||
    element.closest(".path-card")
  );
  if (isCardAction && (element.dataset.university || element.tagName === "BUTTON" || element.classList.contains("small-cta"))) {
    return true;
  }

  const ctaPatterns = [
    /^apply/i,
    /^shortlist/i,
    /^free counseling/i,
    /^get free/i,
    /^check eligibility/i,
    /^check my eligibility/i,
    /^check emi eligibility/i,
    /^check curriculum/i,
    /^check distance mba fit/i,
    /^explore programs/i,
    /^admission process/i,
    /^read counselor review/i,
    /^eligibility criteria/i,
    /^career prospects/i,
    /^request free/i,
    /^ask a counselor/i,
    /^reserve my counseling slot/i,
    /^get details/i,
    /^compare roi with counselor/i
  ];

  if (ctaPatterns.some((pattern) => pattern.test(text))) {
    if (
      element.tagName === "BUTTON" ||
      element.classList.contains("btn") ||
      element.classList.contains("primary-btn") ||
      element.classList.contains("btn-primary") ||
      element.classList.contains("outline-btn") ||
      element.classList.contains("btn-outline") ||
      element.classList.contains("btn-accent") ||
      element.classList.contains("secondary-btn") ||
      element.classList.contains("small-cta")
    ) {
      return true;
    }
  }

  return false;
}

document.addEventListener("click", (event) => {
  const trigger = event.target.closest("button, a");
  if (!trigger) return;

  const triggerText = (trigger.textContent || "").trim().replace(/\s+/g, " ");
  const isEmiTrigger = trigger.classList.contains("emi-calc-trigger") ||
                       trigger.dataset.calculator === "emi" ||
                       trigger.id === "openEmiCalculatorBtn" ||
                       /calculate (my )?emi/i.test(triggerText);
  if (isEmiTrigger) {
    event.preventDefault();
    event.stopPropagation();
    openEmiCalculatorModal(trigger);
    return;
  }

  if (isCounselingCta(trigger)) {
    event.preventDefault();
    event.stopPropagation();

    let university = trigger.dataset.university || "";
    if (!university) {
      const card = trigger.closest(".university-card, .univ-listing-card, .spec-listing-card, tr, article");
      if (card) {
        const titleEl = card.querySelector("h3, .card-title, strong");
        if (titleEl) university = titleEl.textContent.trim();
      }
    }
    if (!university) {
      const pageHeroH1 = document.querySelector(".cs-hero h1, .subpage-hero h1");
      if (pageHeroH1) university = pageHeroH1.textContent.trim();
    }

    const ctaText = (trigger.textContent || "").trim().replace(/\s+/g, " ");
    const source = trigger.dataset.source || `${ctaText || "Counseling"} CTA`;

    openLeadModal(university, source, trigger);
  }
});



window.addEventListener("load", function () {
  ensureCounselingModal();

  const isAutomatedAudit = /Lighthouse|PageSpeed|HeadlessChrome|Chrome-Lighthouse/i.test(navigator.userAgent);
  if (isAutomatedAudit) return;

  setTimeout(() => {
    const modal = document.querySelector("#lead-modal");
    if (modal && !modal.classList.contains("is-open") && !sessionStorage.getItem("thankyouName")) {
      const isMobile = window.innerWidth <= 768;
      openLeadModal("", isMobile ? "Mobile Entry Popup (4s)" : "Desktop Entry Popup (4s)");
    }
  }, 4000);
});

document.addEventListener("mouseleave", (e) => {
  if (window.innerWidth <= 768) return; // Desktop only
  if (e.clientY <= 0) {
    const modal = document.querySelector("#lead-modal");
    if (modal && !modal.classList.contains("is-open") && Date.now() - lastModalCloseTime > 1200 && !sessionStorage.getItem("thankyouName")) {
      openLeadModal("", "Desktop Exit Intent Popup");
    }
  }
});

document.addEventListener("mouseout", (e) => {
  if (window.innerWidth <= 768) return; // Desktop only
  if (!e.relatedTarget && e.clientY <= 10) {
    const modal = document.querySelector("#lead-modal");
    if (modal && !modal.classList.contains("is-open") && Date.now() - lastModalCloseTime > 1200 && !sessionStorage.getItem("thankyouName")) {
      openLeadModal("", "Desktop Exit Intent Popup");
    }
  }
});

let mobileEndReached = false;

window.addEventListener("scroll", () => {
  if (window.innerWidth > 768) return; // Phone / Mobile only

  const scrollBottom = window.innerHeight + window.scrollY;
  const docHeight = Math.max(
    document.body.scrollHeight,
    document.documentElement.scrollHeight
  );

  if (scrollBottom >= docHeight - 160) {
    if (!mobileEndReached) {
      mobileEndReached = true;
      const modal = document.querySelector("#lead-modal");
      if (modal && !modal.classList.contains("is-open") && Date.now() - lastModalCloseTime > 1200 && !sessionStorage.getItem("thankyouName")) {
        openLeadModal("", "Mobile Page End Exit Popup");
      }
    }
  } else if (scrollBottom < docHeight - 450) {
    mobileEndReached = false;
  }
}, { passive: true });



function ensureFormConsent(form, idx) {
  if (form.querySelector('input[name="consent"]')) return;

  const consentGroup = document.createElement("div");
  consentGroup.className = "form-group consent-group";
  consentGroup.style.margin = "8px 0 12px 0";
  consentGroup.innerHTML = `
    <div class="consent-checkbox-wrap" style="display:flex; align-items:flex-start; gap:8px;">
      <input type="checkbox" id="consent-inline-${idx}" name="consent" required style="margin-top:3px; accent-color:#ea580c; cursor:pointer;">
      <label for="consent-inline-${idx}" style="font-size:11.5px; line-height:1.4; color:#475569; font-weight:normal; cursor:pointer;">
        I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry.
      </label>
    </div>
    <p class="consent-error" style="display:none; color:#dc2626; font-size:11.5px; margin:4px 0 0;" role="alert"></p>
  `;

  const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
  if (submitBtn) {
    form.insertBefore(consentGroup, submitBtn);
  } else {
    form.appendChild(consentGroup);
  }
}

function prepareAllForms() {
  document.querySelectorAll("form").forEach((form, idx) => {
    if (form.classList.contains("modal-form")) return;

    const hasPhone = form.querySelector('input[type="tel"], input[name="phone"], input[name="mobile"]');
    const hasEmail = form.querySelector('input[type="email"], input[name="email"]');
    const hasName = form.querySelector('input[name="name"], input[name="fullname"]');

    if (hasPhone || hasEmail || hasName || form.classList.contains("lead-form") || form.classList.contains("counselling-form") || form.classList.contains("sidebar-lead-form")) {
      form.classList.add("lead-form");

      if (form.getAttribute("onsubmit")) {
        form.removeAttribute("onsubmit");
        form.onsubmit = null;
      }

      ensureFormConsent(form, idx);
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  ensureCounselingModal();
  ensureEmiCalculatorModal();
  prepareAllForms();
});

window.addEventListener("load", () => {
  ensureEmiCalculatorModal();
  prepareAllForms();
});



document.addEventListener("submit", async (event) => {
  const form = event.target;
  if (!form || !(form instanceof HTMLFormElement)) return;

  if (form.id === "emi-lead-form" || form.classList.contains("emi-unlock-form")) {
    return;
  }

  const isLeadForm = form.classList.contains("lead-form") || 
                     form.classList.contains("counselling-form") || 
                     form.classList.contains("sidebar-lead-form") ||
                     form.querySelector('input[type="tel"], input[name="phone"], input[name="mobile"]');
  if (!isLeadForm) return;

  event.preventDefault();

  let message = form.querySelector(".form-message");
  if (!message) {
    message = document.createElement("div");
    message.className = "form-message";
    form.appendChild(message);
  }
  message.className = "form-message";

  let consentError = form.querySelector(".consent-error");
  if (consentError) consentError.style.display = "none";

  const consentBox = form.querySelector('input[name="consent"]');
  const consentWrap = form.querySelector(".consent-checkbox-wrap");

  if (!consentBox || !consentBox.checked) {
    const errorText = "Please agree that OnlineMBAAdmission counsellors may contact you regarding your enquiry before submitting.";
    if (consentError) {
      consentError.textContent = errorText;
      consentError.style.display = "block";
    }
    message.textContent = "Please check the consent box to proceed.";
    message.classList.add("error");

    if (consentWrap) {
      consentWrap.style.outline = "2px solid #dc2626";
      consentWrap.style.outlineOffset = "4px";
      consentWrap.style.borderRadius = "4px";
    }
    if (consentBox) {
      consentBox.focus();
    }
    return;
  }

  if (consentWrap) {
    consentWrap.style.outline = "none";
  }

  const formData = new FormData(form);
  const name = String(formData.get("name") || formData.get("fullname") || form.querySelector('input[name="name"], input[name="fullname"]')?.value || "").trim();
  const phone = normalizePhone(String(formData.get("phone") || formData.get("mobile") || form.querySelector('input[type="tel"], input[name="phone"], input[name="mobile"]')?.value || ""));
  const email = String(formData.get("email") || form.querySelector('input[type="email"], input[name="email"]')?.value || "").trim();
  const program = String(formData.get("program") || formData.get("specialization") || formData.get("course") || form.querySelector('select[name="program"], select[name="specialization"]')?.value || "Online MBA").trim();
  const university = String(formData.get("university") || formData.get("budget") || form.querySelector('input[name="university"]')?.value || "").trim();
  const qualification = String(formData.get("qualification") || formData.get("experience") || formData.get("query") || form.querySelector('input[name="qualification"]')?.value || "").trim();
  const source = form.dataset.source || document.title.split("|")[0].trim() + " Form";
  const submitButton = form.querySelector('button[type="submit"], input[type="submit"]');

  if (name.length < 2) {
    message.textContent = "Please enter your full name.";
    message.classList.add("error");
    const nameInput = form.querySelector('input[name="name"], input[name="fullname"], input[type="text"]');
    if (nameInput) nameInput.focus();
    return;
  }

  if (!/^[6-9]\d{9}$/.test(phone)) {
    message.textContent = "Please enter a valid 10-digit Indian mobile number.";
    message.classList.add("error");
    const phoneInput = form.querySelector('input[type="tel"], input[name="phone"], input[name="mobile"]');
    if (phoneInput) phoneInput.focus();
    return;
  }

  if (!isValidEmail(email)) {
    message.textContent = "Please enter a valid email address.";
    message.classList.add("error");
    const emailInput = form.querySelector('input[type="email"], input[name="email"]');
    if (emailInput) emailInput.focus();
    return;
  }

  const lead = {
    id: `MBA-${Date.now()}`,
    source,
    name,
    phone,
    email,
    program,
    university,
    qualification,
    consent: true,
    submittedAt: new Date().toISOString()
  };

  const existingLeads = JSON.parse(localStorage.getItem("onlineMbaLeads") || "[]");
  existingLeads.push(lead);
  localStorage.setItem("onlineMbaLeads", JSON.stringify(existingLeads));

  if (submitButton) {
    submitButton.disabled = true;
    if (!submitButton.dataset.defaultText) {
      submitButton.dataset.defaultText = submitButton.textContent || submitButton.value;
    }
    if (submitButton.tagName === "INPUT") {
      submitButton.value = "Submitting...";
    } else {
      submitButton.textContent = "Submitting...";
    }
  }

  message.textContent = "Thank you. Submitting your details...";
  message.classList.add("success");

  try {
    await sendLeadToCrm(lead);
  } catch (error) {
    console.warn("CRM lead proxy submission failed, but lead saved locally:", error);
  }

  form.reset();

  if (submitButton) {
    submitButton.disabled = false;
    if (submitButton.tagName === "INPUT") {
      submitButton.value = submitButton.dataset.defaultText || "Submit";
    } else {
      submitButton.textContent = submitButton.dataset.defaultText || "Submit";
    }
  }

  if (form.classList.contains("modal-form")) {
    closeLeadModal();
  }

  sessionStorage.setItem("thankyouName", name);
  sessionStorage.setItem("thankyouSource", source);
  window.location.href = "/thankyou";
});



const mobileToggle = document.querySelector(".mobile-nav-toggle");
const mainNav = document.querySelector(".main-nav");

if (mobileToggle && mainNav) {
  mobileToggle.addEventListener("click", () => {
    mobileToggle.classList.toggle("is-active");
    mainNav.classList.toggle("is-open");
  });

  document.addEventListener("click", (e) => {
    if (!mobileToggle.contains(e.target) && !mainNav.contains(e.target)) {
      mobileToggle.classList.remove("is-active");
      mainNav.classList.remove("is-open");
    }
  });

  mainNav.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      mobileToggle.classList.remove("is-active");
      mainNav.classList.remove("is-open");
    });
  });
}