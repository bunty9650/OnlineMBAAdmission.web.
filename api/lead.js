export default async function handler(req, res) {
  // CORS Headers
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    return res.status(204).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ success: false, error: "Method not allowed" });
  }

  try {
    const data = req.body || {};
    const name = String(data.name || "").trim();
    const mobileRaw = String(data.mobile || data.phone || "").trim();
    const email = String(data.email || "").trim();
    const detail1 = String(data.detail1 || data.program || "Online MBA").trim();
    let detail2 = String(data.detail2 || "").trim();
    const consent = data.consent;

    // 1. Mandatory Consent Check
    if (consent !== true && String(consent).toLowerCase() !== "true" && consent !== 1) {
      return res.status(400).json({
        success: false,
        error: "Consent is mandatory. User must agree to be contacted by OnlineMBAAdmission counsellors."
      });
    }

    // 2. Validation
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

    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      return res.status(400).json({ success: false, error: "Please provide a valid email address" });
    }

    if (!detail2) {
      detail2 = `Consent: "I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry." | Submitted: ${new Date().toISOString()}`;
    }

    // Forward to NeoDove CRM
    const crmUrl = process.env.NEODOVE_LEADS_URL || "https://3092a01d-31a6-46a0-a092-11aa63948adc.neodove.com/integration/custom/fa17b06f-23c3-4928-8dc3-0ae7fedcd09f/leads";
    let crmForwarded = false;
    let crmStatusCode = null;

    if (crmUrl) {
      const crmPayload = {
        name: name.slice(0, 100),
        mobile: Number(mobileDigits),
        email: email.slice(0, 100),
        detail1: detail1.slice(0, 200),
        detail2: detail2.slice(0, 500)
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
    console.error("[Vercel Lead Proxy] Internal Error:", err);
    return res.status(500).json({ success: false, error: "Internal server error processing lead" });
  }
}
