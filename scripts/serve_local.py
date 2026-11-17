# scripts/serve_local.py
import http.server
import socketserver
import os
import urllib.parse
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def translate_path(self, path):
        parsed = urllib.parse.urlsplit(path)
        clean_path = parsed.path
        parts = clean_path.strip("/").split("/")
        
        if not parts or parts == [""]:
            local_path = os.path.join(BASE_DIR, "index.html")
            if os.path.exists(local_path):
                return local_path

        target = os.path.join(BASE_DIR, *parts)
        if os.path.exists(target):
            if os.path.isdir(target):
                index_file = os.path.join(target, "index.html")
                if os.path.exists(index_file):
                    return index_file
            return target

        html_target = target + ".html"
        if os.path.exists(html_target):
            return html_target

        return target

    def do_POST(self):
        if self.path.startswith("/api/lead") or self.path.startswith("/php/lead"):
            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"success": True, "message": "Lead received successfully (local test server)"}).encode("utf-8"))
            return
        super().do_POST()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    for port in [8000, 8080, 8088, 3000, 5000]:
        try:
            httpd = socketserver.TCPServer(("", port), CleanUrlHandler)
            print(f"Local server started successfully at http://localhost:{port}/", flush=True)
            httpd.serve_forever()
            break
        except OSError as e:
            continue

if __name__ == "__main__":
    run_server()
