import http.server
import socketserver
import os
import urllib.parse
import urllib.request
import urllib.error
import json
import re
import datetime
import gzip
import io

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def load_dotenv():
    env_file = os.path.join(DIRECTORY, ".env")
    if os.path.exists(env_file):
        try:
            with open(env_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip("'\"")
                        if k and k not in os.environ:
                            os.environ[k] = v
        except Exception:
            pass

load_dotenv()

LEGACY_301_MAP = {
    "/compare": "/comparison",
    "/compare.html": "/comparison",
    "/specializations/banking-finance": "/specializations/banking-and-finance",
    "/specializations/business-ai": "/specializations/ai-for-business",
    "/specializations/fintech": "/specializations/fintech-and-financial-services",
    "/specializations/supply-chain": "/specializations/supply-chain-management",
    "/specializations/sustainability-esg": "/specializations/sustainability-and-esg-management",
    "/university-ignou-online": "/universities/ignou",
    "/university-amity-online": "/universities/amity",
    "/university-manipal-online": "/universities/manipal-jaipur",
    "/university-du-sol-online": "/universities/du-sol",
    "/university-gla-online": "/universities/gla",
    "/university-andhra-online": "/universities/andhra-university",
    "/university-ccsu-online": "/universities/ccsu",
    "/university-ddu-online": "/universities/ddu",
    "/university-arka-jain-online": "/universities/arka-jain",
    "/university-parul-online": "/universities/parul",
    "/university-chandigarh-online": "/universities/chandigarh-university",
    "/university-chandigarh-university-online": "/universities/chandigarh-university",
    "/university-niu-online": "/universities/noida-international-university",
    "/university-noida-international-university-online": "/universities/noida-international-university",
    "/universities/niu": "/universities/noida-international-university",
    "/university-dpu-online": "/universities/dpu-online",
    "/university-jain-online": "/universities/jain-university",
    "/universities/dpu": "/universities/dpu-online",
    "/universities/jain": "/universities/jain-university",
    "/university-jain-university-online": "/universities/jain-university",
        "/universities/smu": "/universities/sikkim-manipal-university",
    "/university-smu-online": "/universities/sikkim-manipal-university",
    "/university-sikkim-manipal-online": "/universities/sikkim-manipal-university",
    "/university-sikkim-manipal-university-online": "/universities/sikkim-manipal-university",
    "/universities/uu": "/universities/uttaranchal-university",
    "/universities/uttaranchal": "/universities/uttaranchal-university",
    "/university-uu-online": "/universities/uttaranchal-university",
    "/university-uttaranchal-online": "/universities/uttaranchal-university",
    "/university-uttaranchal-university-online": "/universities/uttaranchal-university",
        "/universities/nmims": "/universities/nmims-online",
    "/university-nmims-online": "/universities/nmims-online",
    "/university-nmims": "/universities/nmims-online",
    "/universities/galgotias": "/universities/galgotias-university",
    "/university-galgotias-online": "/universities/galgotias-university",
    "/university-galgotias": "/universities/galgotias-university",
    "/university-galgotias-university-online": "/universities/galgotias-university",
    "/universities/dbau": "/universities/dbau-online",
    "/universities/dbrau": "/universities/dbau-online",
    "/universities/dbrau-online": "/universities/dbau-online",
    "/universities/dr-bhimrao-ambedkar-university": "/universities/dbau-online",
    "/university-dbau-online": "/universities/dbau-online",
    "/university-dbrau-online": "/universities/dbau-online",
    "/universities/shoolini": "/universities/shoolini-university",
    "/university-shoolini-online": "/universities/shoolini-university",
    "/university-shoolini-university-online": "/universities/shoolini-university",
    "/university/shoolini-university/mba-in-information-technology-management": "/university/shoolini-university/mba-in-it-management",
    "/universities/alliance": "/universities/alliance-university",
    "/university-alliance-online": "/universities/alliance-university",
    "/university-alliance": "/universities/alliance-university",
    "/university-alliance-university-online": "/universities/alliance-university",
    "/universities/bvp": "/universities/bharati-vidyapeeth",
    "/universities/bvdu": "/universities/bharati-vidyapeeth",
    "/universities/bharati": "/universities/bharati-vidyapeeth",
    "/university-bharati-vidyapeeth-online": "/universities/bharati-vidyapeeth",
    "/university-bvdu-online": "/universities/bharati-vidyapeeth",
    "/university-bharati-vidyapeeth": "/universities/bharati-vidyapeeth",
    "/university-dsu-online": "/universities/dsu",
    "/university-dayananda-sagar-online": "/universities/dsu",
    "/university-dayananda-sagar-university-online": "/universities/dsu",
    "/universities/dayananda-sagar": "/universities/dsu",
    "/universities/dayananda-sagar-university": "/universities/dsu",
    "/university-jamia-hamdard-online": "/universities/jamia-hamdard",
    "/universities/jamia": "/universities/jamia-hamdard",
    "/university-jamia-online": "/universities/jamia-hamdard",
    "/universities/vellore": "/universities/vit",
    "/universities/vellore-institute-of-technology": "/universities/vit",
    "/university-vit-online": "/universities/vit",
    "/university-vellore-online": "/universities/vit",
    "/universities/vit-online": "/universities/vit",
    "/university-imt-ghaziabad-online": "/universities/imt-ghaziabad",
    "/university-symbiosis-online": "/universities/symbiosis",
    "/university-kj-somaiya-online": "/universities/kj-somaiya",
    "/university-imi-kolkata-online": "/universities/imi-kolkata",
    "/blog-direct-admission-without-cat": "/blogs/direct-admission-without-cat",
    "/blog-highest-paying-specializations": "/blogs/highest-paying-specializations",
    "/blog-is-online-mba-valid-govt-jobs": "/blogs/is-online-mba-valid-govt-jobs",
    "/blog-no-cost-emi-guide": "/blogs/no-cost-emi-guide",
    "/blog-online-vs-distance-mba": "/blogs/online-vs-distance-mba",
    "/blog-ugc-deb-approval-guide": "/blogs/ugc-deb-approval-guide",
    "/blogs-direct-admission-without-cat": "/blogs/direct-admission-without-cat",
    "/blogs-highest-paying-specializations": "/blogs/highest-paying-specializations",
    "/blogs-is-online-mba-valid-govt-jobs": "/blogs/is-online-mba-valid-govt-jobs",
    "/blogs-no-cost-emi-guide": "/blogs/no-cost-emi-guide",
    "/blogs-online-vs-distance-mba": "/blogs/online-vs-distance-mba",
    "/blogs-ugc-deb-approval-guide": "/blogs/ugc-deb-approval-guide",
    "/blog": "/blogs",
    "/contact": "/admission",
    "/contact.html": "/admission",
    "/sitemap": "/sitemap.xml",
}

class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
    daemon_threads = True

class CleanUrlHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            parts = urllib.parse.urlsplit(self.path)
            if not parts.path.endswith('/'):
                self.send_response(301)
                new_parts = (parts[0], parts[1], parts[2] + '/', parts[3], parts[4])
                new_url = urllib.parse.urlunsplit(new_parts)
                self.send_header("Location", new_url)
                super().end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)

        ctype = self.guess_type(path)
        try:
            with open(path, 'rb') as f:
                data = f.read()
        except OSError:
            self.send_error(404, "File not found")
            return None

        accept_encoding = self.headers.get("Accept-Encoding", "")
        compress_types = ("text/", "application/javascript", "application/json", "image/svg+xml", "application/xml")
        should_compress = "gzip" in accept_encoding and any(ctype.startswith(t) for t in compress_types) and len(data) > 256

        self.send_response(200)
        self.send_header("Content-Type", ctype)

        if should_compress:
            compressed = gzip.compress(data, compresslevel=6)
            self.send_header("Content-Encoding", "gzip")
            self.send_header("Content-Length", str(len(compressed)))
            self.send_header("Vary", "Accept-Encoding")
            out_bytes = compressed
        else:
            self.send_header("Content-Length", str(len(data)))
            out_bytes = data

        if any(path.endswith(ext) for ext in [".css", ".js", ".png", ".webp", ".jpg", ".jpeg", ".ico", ".svg"]):
            self.send_header("Cache-Control", "public, max-age=31536000, immutable")
        else:
            self.send_header("Cache-Control", "public, max-age=0, must-revalidate")

        super().end_headers()
        return io.BytesIO(out_bytes)

    def do_HEAD(self):
        return self.do_GET()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/lead":
            self.handle_lead_api()
            return
        self.send_error(404, "Endpoint not found")

    def handle_lead_api(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length <= 0 or content_length > 65536:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Invalid payload size"}).encode("utf-8"))
                return

            raw_body = self.rfile.read(content_length)
            try:
                data = json.loads(raw_body.decode("utf-8"))
            except Exception:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Invalid JSON format"}).encode("utf-8"))
                return

            name = str(data.get("name") or "").strip()
            mobile_raw = str(data.get("mobile") or data.get("phone") or "").strip()
            email = str(data.get("email") or "").strip()
            detail1 = str(data.get("detail1") or data.get("program") or "Online MBA").strip()
            detail2 = str(data.get("detail2") or "").strip()
            consent = data.get("consent")

            # 1. Mandatory Consent Check
            if consent is not True and str(consent).lower() not in ("true", "1"):
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({
                    "success": False,
                    "error": "Consent is mandatory. User must agree to be contacted by OnlineMBAAdmission counsellors."
                }).encode("utf-8"))
                return

            # 2. Validation
            if len(name) < 2:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Name must be at least 2 characters"}).encode("utf-8"))
                return

            # Normalize phone (digits only, strip +91 or 0 prefix if 12/11 digits)
            mobile_digits = re.sub(r"\D", "", mobile_raw)
            if len(mobile_digits) == 12 and mobile_digits.startswith("91"):
                mobile_digits = mobile_digits[2:]
            elif len(mobile_digits) == 11 and mobile_digits.startswith("0"):
                mobile_digits = mobile_digits[1:]

            if not re.match(r"^[6-9]\d{9}$", mobile_digits):
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Please provide a valid 10-digit Indian mobile number"}).encode("utf-8"))
                return

            if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": "Please provide a valid email address"}).encode("utf-8"))
                return

            # Truncate and sanitize fields
            name = name[:100]
            email = email[:100]
            detail1 = detail1[:200]
            if not detail2:
                detail2 = f'Consent: "I agree that OnlineMBAAdmission counsellors may contact me regarding my enquiry." | Submitted: {datetime.datetime.utcnow().isoformat()}Z'
            else:
                detail2 = detail2[:500]

            # Safe Server Logging (Mask PII and never log secret tokens/URLs)
            masked_mobile = mobile_digits[:2] + "******" + mobile_digits[-2:]
            masked_email = (email[0] + "***@" + email.split("@")[-1]) if "@" in email else "***"
            print(f"[Lead Proxy] Received lead: source={detail1[:30]}, mobile={masked_mobile}, email={masked_email}, consent=VERIFIED")

            # Forward to Neodove CRM if NEODOVE_LEADS_URL is configured
            crm_url = os.environ.get("NEODOVE_LEADS_URL", "").strip()
            crm_forwarded = False
            crm_status_code = None

            if crm_url:
                crm_payload = {
                    "name": name,
                    "mobile": int(mobile_digits),
                    "email": email,
                    "detail1": detail1,
                    "detail2": detail2
                }
                try:
                    req = urllib.request.Request(
                        crm_url,
                        data=json.dumps(crm_payload).encode("utf-8"),
                        headers={
                            "Content-Type": "application/json",
                            "User-Agent": "OnlineMBAAdmission-Proxy/1.0"
                        },
                        method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=10) as crm_resp:
                        crm_status_code = crm_resp.getcode()
                        crm_forwarded = (200 <= crm_status_code < 300)
                except urllib.error.HTTPError as he:
                    crm_status_code = he.code
                    crm_forwarded = False
                    print(f"[Lead Proxy] CRM HTTP Error {he.code}")
                except Exception as ex:
                    crm_forwarded = False
                    print(f"[Lead Proxy] CRM Connection Error: {type(ex).__name__}")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "message": "Lead received successfully",
                "forwarded_to_crm": crm_forwarded,
                "crm_status_code": crm_status_code
            }).encode("utf-8"))

        except Exception:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"success": False, "error": "Internal server error processing lead"}).encode("utf-8"))


    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = f"?{parsed.query}" if parsed.query else ""

        # Remove trailing slash if not root
        clean_slug = path.rstrip("/") if len(path) > 1 else path
        if clean_slug.endswith(".html"):
            clean_slug = clean_slug[:-5]

        # 1. Automatic redirect from /blog or /blog/ to /blogs
        if clean_slug == "/blog":
            self.send_response(301)
            self.send_header("Location", "/blogs" + query)
            self.end_headers()
            return
        if clean_slug.startswith("/blog/"):
            dest = "/blogs/" + clean_slug[6:]
            self.send_response(301)
            self.send_header("Location", dest + query)
            self.end_headers()
            return

        # 2. Check legacy 301 redirects
        if clean_slug in LEGACY_301_MAP:
            dest = LEGACY_301_MAP[clean_slug]
            self.send_response(301)
            self.send_header("Location", dest + query)
            self.end_headers()
            return

        # Redirect /universities/[slug]/mba-in-* to /university/[slug]/mba-in-*
        if clean_slug.startswith("/universities/") and "/mba-in-" in clean_slug:
            dest = "/university/" + clean_slug[len("/universities/"):]
            self.send_response(301)
            self.send_header("Location", dest + query)
            self.end_headers()
            return

        # Redirect /university/[slug] (parent page) to /universities/[slug]
        parts = clean_slug.strip("/").split("/")
        if len(parts) == 2 and parts[0] == "university":
            dest = "/universities/" + parts[1]
            self.send_response(301)
            self.send_header("Location", dest + query)
            self.end_headers()
            return

        # 3. Redirect explicit .html to clean URL
        if path.endswith("/index.html") and path != "/index.html":
            dest_dir = path[:-11]
            dest_dir = dest_dir if dest_dir else "/"
            self.send_response(301)
            self.send_header("Location", dest_dir + query)
            self.end_headers()
            return
        elif path == "/index.html":
            self.send_response(301)
            self.send_header("Location", "/" + query)
            self.end_headers()
            return
        elif path.endswith(".html"):
            self.send_response(301)
            self.send_header("Location", clean_slug + query)
            self.end_headers()
            return

        # 4. Check exact file or directory index
        local_path = self.translate_path(path)
        
        # If path is a directory (e.g. /universities, /specializations, or /blogs), look for index.html
        if os.path.isdir(local_path):
            index_path = os.path.join(local_path, "index.html")
            if os.path.exists(index_path):
                self.path = os.path.join(path, "index.html").replace("\\", "/") + query
                return super().do_GET()

        # If extensionless matches .html
        if not os.path.exists(local_path):
            # Check local_path + .html
            if os.path.exists(local_path + ".html"):
                self.path = path.rstrip("/") + ".html" + query
            # Or if path is /universities or /blogs without trailing slash, check {path}/index.html
            elif os.path.exists(os.path.join(local_path, "index.html")):
                self.path = path.rstrip("/") + "/index.html" + query

        return super().do_GET()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with ThreadedHTTPServer(("", PORT), CleanUrlHTTPRequestHandler) as httpd:
        print(f"Serving Master Prompt hierarchical web server at http://localhost:{PORT} from {DIRECTORY}")
        httpd.serve_forever()
