# scripts/package_for_hostinger.py
"""
OnlineMBAAdmission.com - Hostinger Production Deployment Packager
Creates a clean, production-ready 'hostinger_public_html.zip' ready to upload & extract into Hostinger's public_html folder.
"""

import os
import sys
import zipfile
import shutil
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_ZIP = os.path.join(BASE_DIR, "hostinger_public_html.zip")

# Allowed root files for production
PRODUCTION_ROOT_FILES = {
    ".htaccess",
    "robots.txt",
    "sitemap.xml",
    "index.html",
    "about.html",
    "admission.html",
    "fees.html",
    "eligibility.html",
    "comparison.html",
    "contact.html",
    "thankyou.html",
    "styles.css",
    "script.js",
    "favicon.ico",
    "favicon.png",
    "logo.webp",
    "logo.png",
}

# Production directories to include completely
PRODUCTION_DIRS = {
    "api",
    "blogs",
    "universities",
    "specializations",
    "university",
    "images",
}

# Patterns to skip
EXCLUDE_PATTERNS = {
    ".git",
    ".env",
    "_archive",
    "scripts",
    "__pycache__",
    "hostinger_public_html.zip",
    "blog-template.html",
    ".DS_Store",
    "Thumbs.db",
}

def package_hostinger():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting Hostinger package creation...")
    print(f"Base Directory: {BASE_DIR}")
    
    if os.path.exists(OUTPUT_ZIP):
        try:
            os.remove(OUTPUT_ZIP)
            print("Removed existing hostinger_public_html.zip")
        except Exception as e:
            print(f"Warning: Could not remove old zip: {e}")

    total_files = 0
    total_bytes = 0

    with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        # 1. Add allowed root files
        for fname in sorted(os.listdir(BASE_DIR)):
            fpath = os.path.join(BASE_DIR, fname)
            if os.path.isfile(fpath) and fname in PRODUCTION_ROOT_FILES:
                zipf.write(fpath, arcname=fname)
                size = os.path.getsize(fpath)
                total_files += 1
                total_bytes += size
                print(f"  [+] Added root file: {fname} ({size:,} bytes)")

        # 2. Add production directories
        for dname in sorted(PRODUCTION_DIRS):
            dpath = os.path.join(BASE_DIR, dname)
            if not os.path.isdir(dpath):
                print(f"  [!] Warning: Directory not found: {dname}")
                continue

            for root, dirs, files in os.walk(dpath):
                # Filter out unwanted subdirs
                dirs[:] = [d for d in dirs if d not in EXCLUDE_PATTERNS]

                for file in files:
                    if file in EXCLUDE_PATTERNS or file.endswith(".py") or file.endswith(".pyc"):
                        continue
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, BASE_DIR)
                    zipf.write(full_path, arcname=rel_path)
                    total_files += 1
                    total_bytes += os.path.getsize(full_path)

    zip_size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
    print("\n" + "="*60)
    print("SUCCESS: Hostinger package created successfully!")
    print(f"Location: {OUTPUT_ZIP}")
    print(f"Total Files Packed: {total_files}")
    print(f"Uncompressed Size: {total_bytes / (1024*1024):.2f} MB")
    print(f"Zip Archive Size:   {zip_size_mb:.2f} MB")
    print("="*60)
    print("\nHOW TO DEPLOY ON HOSTINGER:")
    print("1. Log in to Hostinger hPanel -> File Manager.")
    print("2. Navigate into your domain's 'public_html' folder.")
    print("3. Upload 'hostinger_public_html.zip'.")
    print("4. Right-click 'hostinger_public_html.zip' and select 'Extract'.")
    print("5. Delete the zip file after extraction.")
    print("Your website is now 100% LIVE and fully functional!")

if __name__ == "__main__":
    package_hostinger()
