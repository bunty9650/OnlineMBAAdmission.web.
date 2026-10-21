# scripts/test_lead_security.py
"""
Automated Security, Validation & Rate-Limit Verification Suite
Tests the /api/lead endpoint against all P0 & P1 checklist constraints.
SAFE: Does not send leads to production CRM (uses mock dry-run).
"""

import urllib.request
import urllib.error
import json
import time
import sys

# Ensure UTF-8 output on Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_URL = "http://localhost:3000/api/lead"

def make_request(payload, origin="http://localhost:3000", client_ip=None):
    headers = {
        "Content-Type": "application/json",
        "Origin": origin
    }
    if client_ip:
        headers["X-Forwarded-For"] = client_ip

    req = urllib.request.Request(
        BASE_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            return resp.status, body, dict(resp.headers)
    except urllib.error.HTTPError as he:
        try:
            body = json.loads(he.read().decode("utf-8"))
        except Exception:
            body = {"raw": he.reason}
        return he.code, body, dict(he.headers)
    except Exception as e:
        return 0, {"error": str(e)}, {}

def run_tests():
    print("=" * 60)
    print("STARTING LEAD API SECURITY & COMPLIANCE TEST SUITE")
    print("=" * 60)

    results = []

    # Test 1: Valid Unicode Devanagari Name (राहुल शर्मा)
    p1 = {
        "name": "राहुल शर्मा",
        "phone": "9876543210",
        "email": "test.hindi@example.com",
        "program": "Online MBA Marketing",
        "consent": True
    }
    status, body, _ = make_request(p1, client_ip="192.168.10.1")
    pass1 = (status == 200 and body.get("success") is True)
    results.append(("Unicode Devanagari Name ('राहुल शर्मा')", status, pass1, body.get("message")))

    # Test 2: Valid Apostrophe Name (D'Souza)
    p2 = {
        "name": "Francis D'Souza",
        "phone": "9812345678",
        "email": "dsouza@example.com",
        "consent": True
    }
    status, body, _ = make_request(p2, client_ip="192.168.10.2")
    pass2 = (status == 200 and body.get("success") is True)
    results.append(("Name with Apostrophe (\"Francis D'Souza\")", status, pass2, body.get("message")))

    # Test 3: Valid Hyphenated Name (Jean-Luc)
    p3 = {
        "name": "Jean-Luc Picard",
        "phone": "9823456789",
        "email": "picard@example.com",
        "consent": True
    }
    status, body, _ = make_request(p3, client_ip="192.168.10.3")
    pass3 = (status == 200 and body.get("success") is True)
    results.append(("Hyphenated Name ('Jean-Luc Picard')", status, pass3, body.get("message")))

    # Test 4: XSS Script Injection in Name (<script>alert(1)</script>)
    p4 = {
        "name": "<script>alert(1)</script>",
        "phone": "9876543210",
        "email": "xss@example.com",
        "consent": True
    }
    status, body, _ = make_request(p4, client_ip="192.168.10.4")
    pass4 = (status == 400 and "valid full name" in body.get("error", ""))
    results.append(("XSS Injection in Name ('<script>')", status, pass4, body.get("error")))

    # Test 5: Overly Long Name (> 60 characters)
    p5 = {
        "name": "A" * 65,
        "phone": "9876543210",
        "email": "long@example.com",
        "consent": True
    }
    status, body, _ = make_request(p5, client_ip="192.168.10.5")
    pass5 = (status == 400 and "valid full name" in body.get("error", ""))
    results.append(("Overly Long Name (65 chars)", status, pass5, body.get("error")))

    # Test 6: Single-Character Invalid Name ('A')
    p6 = {
        "name": "A",
        "phone": "9876543210",
        "email": "short@example.com",
        "consent": True
    }
    status, body, _ = make_request(p6, client_ip="192.168.10.6")
    pass6 = (status == 400 and "valid full name" in body.get("error", ""))
    results.append(("Too Short Name ('A')", status, pass6, body.get("error")))

    # Test 7: Missing Consent (consent: false or null)
    p7 = {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "email": "noconsent@example.com",
        "consent": False
    }
    status, body, _ = make_request(p7, client_ip="192.168.10.7")
    pass7 = (status == 400 and "Consent is mandatory" in body.get("error", ""))
    results.append(("Missing Consent (consent: false)", status, pass7, body.get("error")))

    # Test 8: Invalid Mobile (e.g. 5 digits or non-Indian prefix)
    p8 = {
        "name": "Rahul Sharma",
        "phone": "1234567890",
        "email": "badphone@example.com",
        "consent": True
    }
    status, body, _ = make_request(p8, client_ip="192.168.10.8")
    pass8 = (status == 400 and "valid 10-digit Indian mobile" in body.get("error", ""))
    results.append(("Invalid Mobile ('1234567890')", status, pass8, body.get("error")))

    # Test 9: Invalid Email
    p9 = {
        "name": "Rahul Sharma",
        "phone": "9876543210",
        "email": "not-an-email",
        "consent": True
    }
    status, body, _ = make_request(p9, client_ip="192.168.10.9")
    pass9 = (status == 400 and "valid email address" in body.get("error", ""))
    results.append(("Invalid Email ('not-an-email')", status, pass9, body.get("error")))

    # Test 10: Anti-Spam Honeypot Detection
    p10 = {
        "name": "Spam Bot",
        "phone": "9876543210",
        "email": "bot@spam.com",
        "website": "http://spamsite.com",  # Honeypot filled!
        "consent": True
    }
    status, body, _ = make_request(p10, client_ip="192.168.10.10")
    pass10 = (status == 200 and body.get("message") == "Lead processed")
    results.append(("Honeypot Trap (Bot filled 'website')", status, pass10, body.get("message")))

    # Test 11: Unauthorized Browser CORS Origin
    p11 = {
        "name": "Hacker Cross-Site",
        "phone": "9876543210",
        "email": "hacker@evil.com",
        "consent": True
    }
    status, body, _ = make_request(p11, origin="https://evil-attacker-website.com", client_ip="192.168.10.11")
    pass11 = (status == 403 and "Origin not allowed" in body.get("error", ""))
    results.append(("Unauthorized CORS Origin ('evil-attacker')", status, pass11, body.get("error")))

    # Test 12: IP Rate Limiting (5 allowed, 6th must get HTTP 429)
    # Use dynamic IP per run to avoid carry-over in local memory
    test_ip = f"10.0.99.{int(time.time()) % 200 + 10}"
    rate_results = []
    for i in range(1, 7):
        payload = {
            "name": f"Lead Student",
            "phone": "9876543210",
            "email": f"rate{i}@example.com",
            "consent": True
        }
        st, b, _ = make_request(payload, client_ip=test_ip)
        rate_results.append(st)

    pass12 = (rate_results[:5] == [200, 200, 200, 200, 200] and rate_results[5] == 429)
    results.append(("IP Rate Limiting (6th request -> 429)", rate_results[5], pass12, f"Sequence: {rate_results}"))

    # Print Report
    print(f"\n{'Test Case':<45} | {'HTTP':<5} | {'Status':<6} | Note")
    print("-" * 90)
    all_passed = True
    for name, st, passed, note in results:
        sym = "PASS" if passed else "FAIL"
        if not passed: all_passed = False
        clean_name = name.encode("ascii", "replace").decode("ascii")
        clean_note = str(note).encode("ascii", "replace").decode("ascii")
        print(f"{clean_name:<45} | {st:<5} | {sym:<6} | {clean_note}")
    print("-" * 90)

    if all_passed:
        print("ALL 12 LEAD API SECURITY & BOUNDARY TESTS PASSED!")
    else:
        print("SOME TESTS FAILED - Please check details above.")

if __name__ == "__main__":
    run_tests()
