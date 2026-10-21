// api/lead.js - Secure Production Lead Proxy for OnlineMBAAdmission.com
// Supports Upstash Redis REST distributed rate limiting with in-memory container fallback

const RATE_LIMIT_WINDOW_SECS = 600; // 10 minutes window
const MAX_REQUESTS_PER_WINDOW = 5;  // max 5 submissions per IP per 10m

// Local container memory fallback
const localIpCounts = new Map();

async function isRateLimited(ip) {
  if (!ip || ip === "unknown") return false;

  const redisUrl = process.env.UPSTASH_REDIS_REST_URL;
  const redisToken = process.env.UPSTASH_REDIS_REST_TOKEN;

  // 1. Distributed Edge Rate Limiter (Upstash Redis REST API)
  if (redisUrl && redisToken) {
    try {
      const cleanIp = ip.replace(/[^a-zA-Z0-9_.-]/g, "_");
      const key = `ratelimit:lead:${cleanIp}`;
      const incrRes = await fetch(`${redisUrl}/incr/${encodeURIComponent(key)}`, {
        headers: { Authorization: `Bearer ${redisToken}` }
      });
      if (incrRes.ok) {
        const data = await incrRes.json();
        const count = data.result;
        if (count === 1) {
          await fetch(`${redisUrl}/expire/${encodeURIComponent(key)}/${RATE_LIMIT_WINDOW_SECS}`, {
            headers: { Authorization: `Bearer ${redisToken}` }
          });
        }
        if (count > MAX_REQUESTS_PER_WINDOW) {
          return true;
        }
        return false;
      }
    } catch (err) {
      console.warn("[RateLimit] Upstash Redis request failed; falling back to in-memory check:", err.message);
    }
  }

  // 2. Local In-Memory Fallback
  const now = Date.now();
  const record = localIpCounts.get(ip);
  if (!record || now > record.resetTime) {
    localIpCounts.set(ip, { count: 1, resetTime: now + RATE_LIMIT_WINDOW_SECS * 1000 });
    return false;
  }
  if (record.count >= MAX_REQUESTS_PER_WINDOW) {
    return true;
  }
  record.count += 1;
  return false;
}

export default async function handler(req, res) {
  // 1. Browser CORS & Security Headers
  const allowedOrigins = [
    "https://www.onlinembaadmission.com",
    "https://onlinembaadmission.com",
    "https://onlinembaadweb.vercel.app",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
  ];

  const origin = req.headers.origin;
  if (origin) {
    if (allowedOrigins.includes(origin) || origin.endsWith(".vercel.app")) {
      res.setHeader("Access-Control-Allow-Origin", origin);
      res.setHeader("Vary", "Origin");
    } else {
      return res.status(403).json({ success: false, error: "Origin not allowed by CORS policy" });
    }
  } else {
    // Direct non-browser request or same-origin direct curl
    res.setHeader("Access-Control-Allow-Origin", "https://www.onlinembaadmission.com");
  }

  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("X-Frame-Options", "SAMEORIGIN");
  res.setHeader("Referrer-Policy", "strict-origin-when-cross-origin");

  if (req.method === "OPTIONS") {
    return res.status(204).end();
  }

  if (req.method !== "POST") {
    return res.status(405).json({ success: false, error: "Method not allowed. Use POST." });
  }

  // 2. Rate Limiting Check (Multi-instance Redis / Local fallback)
  const forwarded = req.headers["x-forwarded-for"];
  const clientIp = forwarded ? forwarded.split(",")[0].trim() : req.socket?.remoteAddress || "unknown";
  
  const limited = await isRateLimited(clientIp);
  if (limited) {
    return res.status(429).json({
      success: false,
      error: "Too many lead submissions from your network. Please wait a few minutes before trying again or contact admissions@onlinembaadmission.com."
    });
  }

  try {
    const data = req.body || {};

    // 3. Anti-Spam Honeypot Verification (Invisible to real users)
    if (data.website || data.honeypot || data.company_url || data.fax) {
      return res.status(200).json({ success: true, message: "Lead processed" });
    }

    // Helper: Ingress Sanitization (Defense-in-depth)
    const sanitizeText = (str, maxLen = 100) => {
      return String(str || "")
        .replace(/<[^>]*>/g, "")
        .replace(/[<>{}\\\/]/g, "")
        .replace(/[\r\n\t]/g, " ")
        .trim()
        .slice(0, maxLen);
    };

    const rawName = String(data.name || "").trim();
    const mobileRaw = String(data.mobile || data.phone || "").trim();
    const email = String(data.email || "").trim().toLowerCase();
    const detail1 = sanitizeText(data.detail1 || data.program || "Online MBA", 200);
    let detail2 = sanitizeText(data.detail2, 500);
    const consent = data.consent;

    // 4. Mandatory Consent Check (DPDP Statutory Principle)
    if (consent !== true && String(consent).toLowerCase() !== "true" && consent !== 1) {
      return res.status(400).json({
        success: false,
        error: "Consent is mandatory. User must agree to be contacted by OnlineMBAAdmission counsellors."
      });
    }

    // 5. Unicode-Aware Name Validation (Supports Indic & International alphabets, dots, hyphens, apostrophes)
    const unicodeNameRegex = /^[\p{L}\p{M}\s\.\'\-]{2,60}$/u;
    if (!unicodeNameRegex.test(rawName)) {
      return res.status(400).json({
        success: false,
        error: "Please provide a valid full name (2 to 60 characters, letters only)."
      });
    }
    const name = sanitizeText(rawName, 60);

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

    // Structured Audit Consent Trail
    if (!detail2) {
      detail2 = `Consent: Granted for University Admission Counselling | Version: 2026.1 | Timestamp: ${new Date().toISOString()}`;
    }

    // Safe Server Logging (Mask PII, never log raw mobile/email or webhook secrets)
    const maskedMobile = mobileDigits.slice(0, 2) + "******" + mobileDigits.slice(-2);
    console.log(`[Lead Proxy] Received lead: source=${detail1.slice(0, 30)}, mobile=${maskedMobile}, consent=VERIFIED`);

    // 6. Forward to CRM strictly via Environment Variable (Zero Hardcoded Secrets)
    const crmUrl = (process.env.NEODOVE_LEADS_URL || "").trim();
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
        console.error("[Lead Proxy] CRM Connection Error (HTTP status:", crmStatusCode, ")");
      }
    } else {
      console.warn("[Lead Proxy] Warning: NEODOVE_LEADS_URL not set in environment. Lead recorded without external CRM forward.");
    }

    return res.status(200).json({
      success: true,
      message: "Lead received successfully",
      forwarded_to_crm: crmForwarded,
      crm_status_code: crmStatusCode
    });

  } catch (err) {
    console.error("[Lead Proxy] Internal Exception:", err.message);
    return res.status(500).json({ success: false, error: "Internal server error processing lead" });
  }
}
