import os
import json

def get_shared_header_and_critical_css(title, meta_desc, keywords, canonical_url, schema_json):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- SEO Metadata -->
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <meta name="keywords" content="{keywords}">
  <link rel="canonical" href="{canonical_url}">
  <meta name="theme-color" content="#0a6d6f">
  <meta name="robots" content="index, follow, max-image-preview:large">

  <!-- Open Graph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_desc}">
  <meta property="og:image" content="https://www.onlinembaadmission.com/logo.png">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="/favicon.png">
  <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
  <link rel="apple-touch-icon" href="/favicon.png">

  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-T8D27KKV');</script>

  <!-- Structured Data (Schema.org JSON-LD) -->
  <script type="application/ld+json">
{schema_json}
  </script>

  <link rel="stylesheet" href="/styles.css?v=9.0">
  <style id="critical-nav-css">
    .top-bar {{ position: sticky !important; top: 0 !important; z-index: 1000 !important; background: #ffffff !important; border-bottom: 1px solid #eef2f5 !important; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.04) !important; min-height: 72px !important; display: flex !important; align-items: center !important; justify-content: space-between !important; padding: 0 clamp(16px, 4vw, 42px) !important; box-sizing: border-box !important; }}
    .brand {{ display: flex !important; align-items: center !important; text-decoration: none !important; flex-shrink: 0 !important; }}
    .brand img, .brand-logo {{ height: 42px !important; width: auto !important; display: block !important; }}
    .main-nav {{ display: flex !important; align-items: center !important; justify-content: center !important; flex: 1 !important; margin: 0 24px !important; }}
    .nav-list {{ display: flex !important; flex-direction: row !important; align-items: center !important; gap: 24px !important; list-style: none !important; margin: 0 !important; padding: 0 !important; }}
    .nav-list li {{ list-style: none !important; margin: 0 !important; padding: 0 !important; }}
    .nav-link {{ color: #17202a !important; font-weight: 700 !important; font-size: 14.5px !important; text-decoration: none !important; padding: 8px 2px !important; position: relative !important; display: inline-block !important; transition: color 0.2s ease !important; white-space: nowrap !important; }}
    .nav-link:hover, .nav-link.active {{ color: #0a6d6f !important; }}
    .top-actions {{ display: flex !important; align-items: center !important; gap: 14px !important; flex-shrink: 0 !important; }}
    .desktop-only-cta {{ display: inline-flex !important; }}
    .nav-mobile-cta {{ display: none !important; }}
    .mobile-nav-toggle {{ display: none; background: transparent; border: 0; padding: 6px; cursor: pointer; flex-direction: column; gap: 5px; }}
    .mobile-nav-toggle span {{ display: block; width: 24px; height: 2px; background: #17202a; border-radius: 2px; }}
    .cs-badge-icon, .badge svg {{ width: 14px !important; height: 14px !important; min-width: 14px !important; max-width: 14px !important; flex-shrink: 0 !important; display: inline-block !important; vertical-align: middle !important; margin-right: 5px !important; }}
    .cs-icon-pill svg {{ width: 16px !important; height: 16px !important; min-width: 16px !important; max-width: 16px !important; flex-shrink: 0 !important; display: inline-block !important; vertical-align: middle !important; }}
    .cs-toc-card {{ background: #f8fbfc; border: 1.5px solid #d8e9eb; border-radius: 12px; padding: 22px 26px; margin: 24px 0 28px 0; box-shadow: 0 4px 14px rgba(10, 109, 111, 0.05); }}
    .cs-toc-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 14px; border-bottom: 1px solid #e1eef0; padding-bottom: 10px; }}
    .cs-toc-header h3 {{ margin: 0; font-size: 17.5px; font-weight: 800; color: #0a6d6f; }}
    .cs-toc-list {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 9px 20px; list-style: none; margin: 0; padding: 0; }}
    .cs-toc-list li {{ margin: 0; padding: 0; }}
    .cs-toc-list a {{ color: #1e293b; text-decoration: none; font-size: 13.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 8px; transition: color 0.2s ease, transform 0.2s ease; }}
    .cs-toc-list a:hover {{ color: #0a6d6f; transform: translateX(3px); text-decoration: underline; }}
    .cs-toc-list .toc-num {{ background: #e0f2f1; color: #00695c; font-size: 11px; font-weight: 800; border-radius: 4px; padding: 2px 6px; }}
    .mobile-toc-card {{ display: none !important; }}
    .mobile-bottom-blogs {{ display: none !important; }}

    @media (max-width: 980px) {{
      .desktop-only-cta,
      .top-actions .small-cta,
      .top-actions .header-counseling-btn,
      .top-actions > a {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        width: 0 !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        overflow: hidden !important;
        pointer-events: none !important;
      }}
      .mobile-nav-toggle {{ display: flex !important; }}
      .main-nav {{ display: none !important; position: absolute !important; top: 100% !important; left: 0 !important; right: 0 !important; background: #ffffff !important; border-bottom: 1px solid #e5ebe9 !important; padding: 16px 24px !important; box-shadow: 0 16px 32px rgba(0,0,0,0.12) !important; margin: 0 !important; z-index: 1001 !important; }}
      .main-nav.is-open {{ display: block !important; }}
      .nav-list {{ flex-direction: column !important; align-items: flex-start !important; gap: 12px !important; }}
      .nav-link {{ display: block !important; width: 100% !important; padding: 8px 0 !important; border-bottom: 1px solid #f0f4f3 !important; font-size: 15px !important; }}
      .nav-mobile-cta {{ display: block !important; margin-top: 18px !important; width: 100% !important; padding-top: 12px !important; border-top: 1px solid #e5ebe9 !important; }}
      .nav-mobile-apply-btn {{ display: block !important; width: 100% !important; box-sizing: border-box !important; text-align: center !important; background: #0a6d6f !important; color: #ffffff !important; font-weight: 700 !important; font-size: 15px !important; padding: 12px 18px !important; border-radius: 8px !important; text-decoration: none !important; box-shadow: 0 4px 14px rgba(10, 109, 111, 0.25) !important; }}
    }}

    @media (max-width: 1024px) {{
      .cs-wrapper {{ padding: 16px 14px 48px !important; }}
      .cs-layout-container {{ display: flex !important; flex-direction: column !important; gap: 20px !important; margin-top: 16px !important; }}
      .cs-main-content {{ width: 100% !important; min-width: 0 !important; }}
      .cs-sidebar {{ width: 100% !important; min-width: 0 !important; display: flex !important; flex-direction: column !important; gap: 20px !important; }}
      .cs-card {{ padding: 20px 15px !important; margin-bottom: 20px !important; }}
      .mobile-toc-card {{ display: block !important; margin-bottom: 22px !important; }}
      .sidebar-toc-card {{ display: none !important; }}
      .sidebar-form-card {{ width: 100% !important; box-sizing: border-box !important; }}
      .sidebar-univ-card {{ width: 100% !important; box-sizing: border-box !important; }}
      .sidebar-blogs-card {{ display: none !important; }}
      .mobile-bottom-blogs {{ display: block !important; width: 100% !important; box-sizing: border-box !important; margin-top: 24px !important; margin-bottom: 20px !important; }}
      .next-prev-blog-grid {{ display: flex !important; flex-direction: column !important; gap: 12px !important; }}
      .sidebar-blog-item {{ width: 100% !important; box-sizing: border-box !important; }}
      .cs-table-wrapper {{ overflow-x: auto !important; -webkit-overflow-scrolling: touch !important; width: 100% !important; }}
      .cs-table {{ min-width: 520px !important; }}
    }}
  </style>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-T8D27KKV"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

  <!-- Top Navigation Header -->
  <header class="top-bar">
    <a class="brand" href="/" aria-label="Online MBA Admission Home" style="display:flex; align-items:center; text-decoration:none;">
      <picture>
        <source srcset="/logo.webp?v=5.2" type="image/webp">
        <img src="/logo.png?v=5.2" alt="Online MBA Admission" class="brand-logo" width="199" height="84" fetchpriority="high" decoding="async">
      </picture>
    </a>

    <!-- Main Navigation -->
    <nav class="main-nav" aria-label="Main Navigation">
      <ul class="nav-list">
        <li><a href="/" class="nav-link">Home</a></li>
        <li><a href="/universities" class="nav-link">Universities</a></li>
        <li><a href="/specializations" class="nav-link">Specializations</a></li>
        <li><a href="/fees" class="nav-link">Fee Structure</a></li>
        <li><a href="/eligibility" class="nav-link">Eligibility</a></li>
        <li><a href="/admission" class="nav-link">Admission</a></li>
        <li><a href="/blogs" class="nav-link active">Blog</a></li>
      </ul>
      <div class="nav-mobile-cta">
        <a href="#admission-process" class="btn btn-primary nav-mobile-apply-btn">Apply Now</a>
      </div>
    </nav>

    <div class="top-actions">
      <a href="#admission-process" class="small-cta desktop-only-cta" style="text-decoration:none;">Apply Now</a>
      <button class="mobile-nav-toggle" aria-label="Toggle navigation menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
"""

def get_shared_footer():
    return """  <!-- Global Footer -->
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-col brand-col">
        <picture>
          <source srcset="/logo.webp?v=5.2" type="image/webp">
          <img src="/logo.png?v=5.2" alt="Online MBA Admission" class="footer-logo" width="180" height="76" loading="lazy">
        </picture>
        <p class="footer-desc">Your trusted, unbiased counseling portal for UGC-DEB entitled online MBA programs in India. Compare rankings, verified fees, curriculum & remote AI exams.</p>
        <div class="footer-contact-info">
          <p><strong>Email:</strong> admission@onlinembaadmission.com</p>
          <p><strong>Counseling Helpline:</strong> +91 9999 000 000</p>
          <p><strong>Working Hours:</strong> Mon - Sat: 9:30 AM - 7:00 PM</p>
        </div>
      </div>
      <div class="footer-col">
        <h4>Top Universities</h4>
        <ul class="footer-links">
          <li><a href="/universities/manipal-jaipur">Manipal University Jaipur</a></li>
          <li><a href="/universities/amity">Amity University Online</a></li>
          <li><a href="/universities/jain-university">Jain University Online</a></li>
          <li><a href="/universities/st-aloysius">St. Aloysius University</a></li>
          <li><a href="/universities">View All 25+ Universities</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Trending Specializations</h4>
        <ul class="footer-links">
          <li><a href="/specializations/business-analytics">Business Analytics</a></li>
          <li><a href="/specializations/finance">Finance Management</a></li>
          <li><a href="/specializations/marketing">Marketing Management</a></li>
          <li><a href="/specializations/human-resource-management">Human Resource Management</a></li>
          <li><a href="/specializations/operations-management">Operations & Supply Chain</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Quick Navigation</h4>
        <ul class="footer-links">
          <li><a href="/fees">Complete Fee Comparison</a></li>
          <li><a href="/eligibility">Eligibility & Exemptions</a></li>
          <li><a href="/admission">Admission Roadmap 2027</a></li>
          <li><a href="/blogs">Expert Blog Library</a></li>
          <li><a href="/contact">Free Advisory Support</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-container">
        <p>&copy; 2027 Online MBA Admission. All rights reserved. Disclaimer: We provide neutral counseling and guidance. University logos and trademarks belong to their respective statutory owners.</p>
        <div class="footer-legal-links">
          <a href="/privacy-policy">Privacy Policy</a>
          <a href="/terms-conditions">Terms of Service</a>
          <a href="/sitemap.xml">XML Sitemap</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="/script.js?v=9.0" defer></script>
</body>
</html>
"""

print("Base layout helper functions established.")
