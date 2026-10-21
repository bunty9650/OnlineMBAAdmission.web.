export default async function handler(req, res) {
  // 1. Strict Security & CORS Headers
  const allowedOrigins = [
    "https://www.onlinembaadmission.com",
    "https://onlinembaadmission.com",
    "https://onlinembaadweb.vercel.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
  ];

  const origin = req.headers.origin;
  if (!origin || allowedOrigins.includes(origin) || origin.endsWith(".vercel.app")) {
    res.setHeader("Access-Control-Allow-Origin", origin || "*");
  } else {
    return res.status(403).json({ success: false, error: "Origin not allowed" });
  }

  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("X-Frame-Options", "DENY");
  res.setHeader("Referrer-Policy", "strict-origin-when-cross-origin");

  if (req.method === "OPTIONS") {
    return res.status(204).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ success: false, error: "Method not allowed" });
  }

  try {
    const data = req.body || {};

    // 2. Anti-Spam Honeypot Check (Invisible to real users, bots fill it)
    if (data.website || data.honeypot || data.company_url || data.fax) {
      return res.status(200).json({ success: true, message: "Lead processed" });
    }

    // Helper: Strip HTML, angle brackets, scripts, and control characters to prevent XSS in CRM
    const sanitizeText = (str, maxLen = 100) => {
      return String(str || "")
        .replace(/<[^>]*>/g, "")
        .replace(/[<>{}\\\/]/g, "")
        .replace(/[\r\n\t]/g, " ")
        .trim()
        .slice(0, maxLen);
    };

    const name = sanitizeText(data.name, 100);
    const mobileRaw = String(data.mobile || data.phone || "").trim();
    const email = String(data.email || "").trim().toLowerCase();
    const detail1 = sanitizeText(data.detail1 || data.program || "Online MBA", 200);
    let detail2 = sanitizeText(data.detail2, 500);
    const consent = data.consent;

    // 3. Mandatory Consent Check (India DPDP Act 2023 compliance)
    if (consent !== true && String(consent).toLowerCase() !== "true" && consent !== 1) {
      return res.status(400).json({
        success: false,
        error: "Consent is mandatory. User must agree to be contacted by OnlineMBAAdmission counsellors."
      });
    }

    // 4. Strict Field Validations
    if (name.length < 2) {
      return res.status(400).json({ success: false, error: "Name must be at least 2 characters" });
    }

    // Normalize phone (strip non-digits, leading 91 or 0)
    let mobileDigits = mobileRaw.replace(/\D/g, "");
    if (mobileDigits.length === 12 && mobileDigits.startsWith("91")) {
      mobileDigits = mobileDigits.slice(2);
    } else if (mobileDigits.length === 11 && mobileDigits.startsWith("0")) {
      mobileDigits = mobileDigits.slice(1);
    }

    if (!/^[6-9]\d{9}$/.test(mobileDigits)) {
      return res.status(400).json({ success: false, error: "Please provide a valid 10-digit Indian mobile number" });
    }

    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || email.length > 100) {
      return res.status(400).json({ success: false, error: "Please provide a valid email address" });
    }

    if (!detail2) {
      detail2 = `Consent: "I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry." | Submitted: ${new Date().toISOString()}`;
    }

    // 5. Forward to NeoDove CRM
    const crmUrl = process.env.NEODOVE_LEADS_URL || "https://3092a01d-31a6-46a0-a092-11aa63948adc.neodove.com/integration/custom/fa17b06f-23c3-4928-8dc3-0ae7fedcd09f/leads";
    let crmForwarded = false;
    let crmStatusCode = null;

    if (crmUrl) {
      const crmPayload = {
        name: name,
        mobile: Number(mobileDigits),
        email: email,
        detail1: detail1,
        detail2: detail2
      };

      try {
        const crmResponse = await fetch(crmUrl, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "User-Agent": "OnlineMBAAdmission-Proxy/1.0"
          },
          body: JSON.stringify(crmPayload)
        });

        crmStatusCode = crmResponse.status;
        crmForwarded = crmResponse.ok;
      } catch (err) {
        console.error("[Vercel Lead Proxy] CRM Fetch Error:", err.message);
      }
    }

    return res.status(200).json({
      success: true,
      message: "Lead received successfully",
      forwarded_to_crm: crmForwarded,
      crm_status_code: crmStatusCode
    });

  } catch (err) {
    console.error("[Vercel Lead Proxy] Internal Error:", err.message);
    return res.status(500).json({ success: false, error: "Internal server error processing lead" });
  }
}
