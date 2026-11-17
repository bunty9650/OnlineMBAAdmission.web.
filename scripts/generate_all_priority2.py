import os
import re
import json

# ==============================================================================
# Helper functions for UI components
# ==============================================================================

def make_breadcrumb(city_name, city_slug):
    return f"""    <!-- Breadcrumb -->
    <nav class="cs-breadcrumb" aria-label="Breadcrumb">
      <a href="/">Home</a>
      <span class="separator">/</span>
      <a href="/blogs">Blogs</a>
      <span class="separator">/</span>
      <span class="current">Online MBA in {city_name} 2027</span>
    </nav>"""

def make_hero(city_name, primary_kw, update_date="November 2026", year="2027"):
    return f"""    <header class="cs-article-header">
      <div class="cs-badge-row">
        <span class="badge badge-accent">
          <svg class="cs-badge-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          UGC-DEB Entitled
        </span>
        <span class="badge badge-neutral">
          <svg class="cs-badge-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
          AI-Proctored Home Exams
        </span>
        <span class="badge badge-neutral">
          <svg class="cs-badge-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          0% No-Cost EMI Available
        </span>
        <span class="badge badge-neutral">
          <svg class="cs-badge-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          Updated for {year} Cycle
        </span>
      </div>
      <h1 class="cs-article-title">Best {primary_kw}: Fees, Top Universities & Admission Guide {year}</h1>
      <p class="cs-article-lead">A comprehensive, data-backed guide for working executives, engineers, and graduates in {city_name}. Compare UGC-DEB approved institutions, semester fee structures, remote AI proctoring protocols, and legal degree equivalence under the UGC 2020 Gazette Notification.</p>
      <div class="cs-article-meta">
        <span class="meta-item author">By <strong>Online MBA Admission Advisory Team</strong></span>
        <span class="meta-item date">Updated {update_date}</span>
        <span class="meta-item reading-time">16 Min Read &bull; 3,200+ Words</span>
      </div>
    </header>"""

def make_toc(items):
    lis = "".join([f'<li><a href="#{item[0]}"><span class="toc-num">{i+1:02d}</span> {item[1]}</a></li>' for i, item in enumerate(items)])
    return f"""      <!-- Table of Contents -->
      <div class="cs-toc-card">
        <div class="cs-toc-header">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0a6d6f" stroke-width="2.5"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
          <h3>Table of Contents</h3>
        </div>
        <ul class="cs-toc-list">
          {lis}
        </ul>
      </div>"""

def make_sidebar(city_name, items):
    toc_links = "".join([f'<li><a href="#{item[0]}"><span class="toc-bullet">&bull;</span> {item[1]}</a></li>' for item in items])
    return f"""      <!-- Sticky Sidebar -->
      <aside class="cs-sidebar">
        <!-- Sidebar Quick TOC -->
        <div class="cs-card sidebar-toc-card">
          <h4 class="sidebar-title">On This Page</h4>
          <ul class="sidebar-toc-list">
            {toc_links}
          </ul>
        </div>

        <!-- Sidebar Lead Counseling Card -->
        <div class="cs-card sidebar-form-card" id="sidebar-counseling-card" style="background:#f4faf8; border:1.5px solid #a3d9d2;">
          <h4 style="color:#0a6d6f; margin-bottom:8px; font-size:18px; font-weight:800;">Get Free {city_name} Counseling</h4>
          <p style="font-size:13px; color:#475569; margin-bottom:14px; line-height:1.5;">Compare top UGC-DEB universities, check your eligibility & get exclusive zero-cost EMI options.</p>
          <form class="lead-form as-it-is-counseling-form" data-source="{city_name} Sidebar Form">
            <input type="hidden" name="form_type" value="city_sidebar_counseling">
            <input type="hidden" name="target_city" value="{city_name}">
            
            <div class="form-group" style="margin-bottom:10px;">
              <input type="text" name="full_name" class="form-control" placeholder="Your Full Name *" required style="width:100%; padding:9px 12px; font-size:13.5px; border:1px solid #cbd5e1; border-radius:6px; box-sizing:border-box;">
            </div>
            
            <div class="form-group" style="margin-bottom:10px;">
              <input type="tel" name="phone" class="form-control" placeholder="10-Digit Mobile Number *" pattern="[6-9][0-9]{{9}}" required style="width:100%; padding:9px 12px; font-size:13.5px; border:1px solid #cbd5e1; border-radius:6px; box-sizing:border-box;">
            </div>
            
            <div class="form-group" style="margin-bottom:10px;">
              <input type="email" name="email" class="form-control" placeholder="Email Address *" required style="width:100%; padding:9px 12px; font-size:13.5px; border:1px solid #cbd5e1; border-radius:6px; box-sizing:border-box;">
            </div>
            
            <div class="form-group" style="margin-bottom:12px;">
              <select name="specialization" class="form-control" style="width:100%; padding:9px 12px; font-size:13.5px; border:1px solid #cbd5e1; border-radius:6px; background:#fff; box-sizing:border-box;">
                <option value="">Preferred Specialization</option>
                <option value="business-analytics">Business Analytics & AI</option>
                <option value="finance">Finance & FinTech</option>
                <option value="marketing">Marketing & Digital Strategy</option>
                <option value="human-resource">Human Resource Management</option>
                <option value="operations">Operations & Supply Chain</option>
                <option value="it-systems">IT & Systems Management</option>
                <option value="general">Undecided / Need Guidance</option>
              </select>
            </div>
            
            <button type="submit" class="btn btn-primary" style="width:100%; padding:11px; font-size:14px; font-weight:700; border-radius:6px; background:#0a6d6f; color:#fff; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(10,109,111,0.25);">Get Expert Callback</button>
            <p style="font-size:11px; color:#64748b; margin-top:8px; text-align:center;">100% Confidential &bull; Zero Spam Guarantee</p>
          </form>
        </div>

        <!-- Verified Universities Sidebar Widget -->
        <div class="cs-card sidebar-univ-card">
          <h4 class="sidebar-title">Featured Entitled Universities</h4>
          <ul class="sidebar-univ-list" style="list-style:none; padding:0; margin:0; display:flex; flex-direction:column; gap:12px;">
            <li style="border-bottom:1px solid #f1f5f9; padding-bottom:10px;">
              <a href="/universities/manipal-jaipur" style="font-weight:700; color:#0f172a; text-decoration:none; font-size:14px; display:block;">Manipal University Jaipur</a>
              <span style="font-size:12px; color:#0a6d6f; font-weight:600;">NAAC A+ &bull; ₹1.75L Total &bull; ₹4,861/Mo EMI</span>
            </li>
            <li style="border-bottom:1px solid #f1f5f9; padding-bottom:10px;">
              <a href="/universities/amity" style="font-weight:700; color:#0f172a; text-decoration:none; font-size:14px; display:block;">Amity University Online</a>
              <span style="font-size:12px; color:#0a6d6f; font-weight:600;">NAAC A+ &bull; QS Asia Ranked &bull; 16 Specializations</span>
            </li>
            <li style="border-bottom:1px solid #f1f5f9; padding-bottom:10px;">
              <a href="/universities/jain-university" style="font-weight:700; color:#0f172a; text-decoration:none; font-size:14px; display:block;">Jain University Online</a>
              <span style="font-size:12px; color:#0a6d6f; font-weight:600;">NAAC A++ &bull; Dual Qualifications &bull; LinkedIn Learning</span>
            </li>
            <li style="border-bottom:1px solid #f1f5f9; padding-bottom:10px;">
              <a href="/universities/st-aloysius" style="font-weight:700; color:#0f172a; text-decoration:none; font-size:14px; display:block;">St. Aloysius University</a>
              <span style="font-size:12px; color:#0a6d6f; font-weight:600;">144-Yr Legacy &bull; Affordable ₹80k–₹1L &bull; High ROI</span>
            </li>
          </ul>
        </div>
      </aside>"""

def make_bottom_conversion_form(city_name):
    return f"""        <!-- Main Bottom Conversion Form -->
        <section class="cs-card cs-cta-box" id="admission-process" style="background: linear-gradient(135deg, #0a6d6f 0%, #004d40 100%); color: #ffffff; border-radius: 14px; padding: 32px 28px; margin-top: 36px;">
          <div style="text-align: center; max-width: 650px; margin: 0 auto 24px auto;">
            <span style="background: rgba(255,255,255,0.15); color: #ffffff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Free Advisory Consultation</span>
            <h3 style="color: #ffffff; font-size: 24px; font-weight: 800; margin: 12px 0 8px 0;">Find the Best Online MBA for Your Career in {city_name}</h3>
            <p style="color: #e0f2f1; font-size: 14.5px; line-height: 1.6; margin: 0;">Connect with our senior career counselors for an unbiased university comparison, syllabus audit, eligibility evaluation, and zero-cost EMI calculation.</p>
          </div>
          
          <form class="lead-form as-it-is-counseling-form" data-source="{city_name} Blog Form" style="max-width: 700px; margin: 0 auto; background: #ffffff; padding: 24px 22px; border-radius: 10px; color: #1e293b; box-shadow: 0 10px 25px rgba(0,0,0,0.15);">
            <input type="hidden" name="form_type" value="city_blog_counseling">
            <input type="hidden" name="target_city" value="{city_name}">
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 14px;">
              <div>
                <label style="display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 5px;">FULL NAME *</label>
                <input type="text" name="full_name" class="form-control" placeholder="Enter your full name" required style="width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px; box-sizing: border-box;">
              </div>
              <div>
                <label style="display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 5px;">MOBILE NUMBER *</label>
                <input type="tel" name="phone" class="form-control" placeholder="10-digit mobile number" pattern="[6-9][0-9]{{9}}" required style="width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px; box-sizing: border-box;">
              </div>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; margin-bottom: 16px;">
              <div>
                <label style="display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 5px;">EMAIL ADDRESS *</label>
                <input type="email" name="email" class="form-control" placeholder="name@domain.com" required style="width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px; box-sizing: border-box;">
              </div>
              <div>
                <label style="display: block; font-size: 12px; font-weight: 700; color: #475569; margin-bottom: 5px;">DESIRED MBA SPECIALIZATION</label>
                <select name="specialization" class="form-control" style="width: 100%; padding: 10px 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px; background: #fff; box-sizing: border-box;">
                  <option value="business-analytics">Business Analytics & AI</option>
                  <option value="finance">Finance Management</option>
                  <option value="marketing">Marketing & Digital Strategy</option>
                  <option value="human-resource">Human Resource Management</option>
                  <option value="operations">Operations & Supply Chain</option>
                  <option value="it-systems">IT & Systems Management</option>
                  <option value="general" selected>Need Expert Counseling to Decide</option>
                </select>
              </div>
            </div>
            
            <div style="margin-bottom: 16px; display: flex; align-items: flex-start; gap: 8px;">
              <input type="checkbox" id="consent_{city_name.lower()}" name="consent" checked required style="margin-top: 3px;">
              <label for="consent_{city_name.lower()}" style="font-size: 12px; color: #64748b; line-height: 1.4;">I authorize Online MBA Admission and its accredited partner university advisors to contact me via Call, SMS, or WhatsApp regarding fees, scholarship eligibility, and admission procedures.</label>
            </div>
            
            <button type="submit" class="btn btn-primary" style="width: 100%; padding: 13px; font-size: 15px; font-weight: 800; border-radius: 6px; background: #0a6d6f; color: #ffffff; border: none; cursor: pointer; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 4px 14px rgba(10, 109, 111, 0.35);">Apply for Free Counseling Session</button>
          </form>
        </section>"""

def make_faq_section(faqs):
    faq_html = ""
    for i, (q, a) in enumerate(faqs):
        faq_html += f"""          <div class="faq-item" style="border-bottom: 1px solid #e2e8f0; padding: 16px 0;">
            <h3 style="font-size: 16.5px; font-weight: 700; color: #1e293b; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
              <span style="color: #0a6d6f; font-weight: 800;">Q{i+1}:</span> {q}
            </h3>
            <p style="font-size: 14.5px; color: #475569; line-height: 1.6; margin: 0;">{a}</p>
          </div>\n"""
    return f"""        <!-- FAQ Section -->
        <section class="cs-card" id="faqs" style="margin-top: 32px;">
          <h2 class="cs-heading-2">Frequently Asked Questions: Online MBA for Working Professionals</h2>
          <div class="faq-accordion" style="margin-top: 18px;">
{faq_html}          </div>
        </section>"""

print("Component generators defined successfully.")
