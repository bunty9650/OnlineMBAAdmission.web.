# -*- coding: utf-8 -*-
"""
Additional enrichment modules for the remaining 3 guides to guarantee 3,150+ words
"""

def get_bcom_industry_tracks():
    return """
        <!-- B.Com Industry Tracks Deep Dive -->
        <section class="cs-card" id="bcom-industry-tracks">
          <h2 class="cs-heading-2">The 4 High-Growth Commercial Sectors Hiring B.Com MBAs in 2027</h2>
          <p>Upon completing an Online MBA, commerce graduates can target 4 distinct high-paying corporate industry verticals:</p>

          <div style="display: flex; flex-direction: column; gap: 16px; margin: 20px 0;">
            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 15px; font-weight:700;">1. BFSI & Commercial Banking (HDFC, ICICI, Axis, SBI)</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #475569;">Commerce MBAs enter private and nationalized banking as Credit Risk Analysts, Branch Operations Managers, and Wealth Relationship Heads. Responsibilities include commercial loan appraisals, working capital monitoring, portfolio advisory, and branch profitability management with starting packages of ₹8L to ₹13L.</p>
            </div>

            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 15px; font-weight:700;">2. Big 4 Professional Services & Consulting (Deloitte, EY, PwC, KPMG)</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #475569;">Global advisory and audit practices recruit commerce MBAs for Statutory Audit, Risk Advisory, International Tax Due Diligence, and Mergers & Acquisitions support. Having an MBA enables rapid progression to Assistant Manager and Manager grades without waiting years for internal promotions.</p>
            </div>

            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 15px; font-weight:700;">3. Global Capability Centers (GCCs - JPMorgan, Goldman Sachs, Morgan Stanley)</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #475569;">India's massive GCC ecosystem in Bangalore, Hyderabad, Mumbai, and Gurgaon hires commerce MBAs for global middle-office and front-office analytics, derivative trade settlements, regulatory capital reporting (Basel III), and global liquidity management.</p>
            </div>

            <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; background: #ffffff;">
              <h4 style="margin: 0 0 8px 0; color: #0a6d6f; font-size: 15px; font-weight:700;">4. Corporate Treasury & FP&A in Manufacturing & Tech</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #475569;">Fast-growing technology firms and manufacturing conglomerates hire commerce MBAs for Financial Planning & Analysis (FP&A), annual corporate budgeting, variance analysis, foreign exchange hedging, and investor relations reporting directly to the Chief Financial Officer (CFO).</p>
            </div>
          </div>
        </section>
    """

def get_specialization_industry_matrix():
    return """
        <!-- Industry Specialization Fit Matrix -->
        <section class="cs-card" id="industry-specialization-matrix">
          <h2 class="cs-heading-2">Industry-by-Industry Specialization Selection Matrix</h2>
          <p>Different corporate sectors place vastly different career value on Finance, Marketing, and HR credentials. Align your choice with your target hiring sector:</p>

          <div class="cs-table-wrapper" style="margin: 20px 0; overflow-x: auto;">
            <table class="cs-table" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 13px;">
              <thead>
                <tr style="background: #0f172a; color: #ffffff;">
                  <th style="padding: 10px; border: 1px solid #334155;">Target Sector</th>
                  <th style="padding: 10px; border: 1px solid #334155;">Best Fit Specialization</th>
                  <th style="padding: 10px; border: 1px solid #334155;">Why This Fits</th>
                  <th style="padding: 10px; border: 1px solid #334155;">Secondary Alternative</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px; font-weight: 700;">IT Services & Cloud Tech</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Human Resource Management (HRM)</td>
                  <td style="padding: 10px;">Tech firms battle heavy attrition; People Analytics and global talent sourcing are mission-critical.</td>
                  <td style="padding: 10px;">Marketing (B2B SaaS)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 10px; font-weight: 700;">BFSI & FinTech</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Financial Management</td>
                  <td style="padding: 10px;">Core business is capital management, credit risk, algorithmic trading, and investment modeling.</td>
                  <td style="padding: 10px;">Marketing (Retail Banking)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px; font-weight: 700;">FMCG, Retail & E-Commerce</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Marketing & Digital Business</td>
                  <td style="padding: 10px;">Consumer brands depend on brand positioning, performance marketing, omnichannel sales, and customer CAC/LTV.</td>
                  <td style="padding: 10px;">Finance (Supply Chain Costing)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 10px; font-weight: 700;">Manufacturing & Heavy Engineering</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Operations / Finance</td>
                  <td style="padding: 10px;">Capital expenditure budgets, factory cost accounting, and working capital optimization drive profitability.</td>
                  <td style="padding: 10px;">HR (Industrial Relations)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px; font-weight: 700;">Healthcare & Pharmaceuticals</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Marketing / HR</td>
                  <td style="padding: 10px;">Managing specialized clinical staff and navigating strict pharma marketing compliance regulations.</td>
                  <td style="padding: 10px;">Finance (Pharma R&D Valuation)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0; background: #f8fafc;">
                  <td style="padding: 10px; font-weight: 700;">Management Consulting & Strategy</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Finance / Marketing</td>
                  <td style="padding: 10px;">Strategic advisory requires deep financial modeling, market entry analysis, and client presentation mastery.</td>
                  <td style="padding: 10px;">HR (Organizational Restructuring)</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                  <td style="padding: 10px; font-weight: 700;">Startups & Venture Capital Ecosystem</td>
                  <td style="padding: 10px; color: #0a6d6f; font-weight: 700;">Dual: Marketing + Finance</td>
                  <td style="padding: 10px;">Founders and early employees must simultaneously drive CAC customer acquisition and pitch unit economics to VC investors.</td>
                  <td style="padding: 10px;">HR (Early Stage Culture Building)</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
    """

def get_regular_vs_online_myths_debunked():
    return """
        <!-- 5 Misconceptions Debunked -->
        <section class="cs-card" id="myths-debunked">
          <h2 class="cs-heading-2">5 Critical Misconceptions Debunked: Online vs Regular Campus MBA</h2>
          <p>Prospective management students frequently encounter outdated assertions regarding online business education. Here are the 5 most common misconceptions analyzed against current 2027 statutory and industry evidence:</p>

          <div style="display: flex; flex-direction: column; gap: 14px; margin: 20px 0;">
            <div style="border-left: 4px solid #b91c1c; background: #fef2f2; padding: 16px 20px; border-radius: 0 8px 8px 0;">
              <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 15px; font-weight:700;">Myth 1: "Online MBA degrees are not recognized for government exams or PhD programs."</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #334155;"><strong>The Reality:</strong> Factually incorrect. Under Gazette of India Regulation 22 (September 2020), online degrees granted by UGC-DEB entitled universities possess 100% legal equality with campus degrees. Online MBA graduates are fully eligible for UPSC, State PSCs, banking specialist officer exams, UGC-NET lectureship, and PhD doctoral admissions in India and abroad.</p>
            </div>

            <div style="border-left: 4px solid #b91c1c; background: #fef2f2; padding: 16px 20px; border-radius: 0 8px 8px 0;">
              <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 15px; font-weight:700;">Myth 2: "Online learning lacks peer interaction and corporate networking."</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #334155;"><strong>The Reality:</strong> In reality, peer cohorts in online MBA programs are often far more seasoned than campus cohorts. While campus batches consist mostly of 21–23 year-old freshers, online MBA cohorts comprise software engineers, plant managers, banking officers, and entrepreneurs with an average of 4 to 8 years of industry experience, fostering corporate peer connections across India.</p>
            </div>

            <div style="border-left: 4px solid #b91c1c; background: #fef2f2; padding: 16px 20px; border-radius: 0 8px 8px 0;">
              <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 15px; font-weight:700;">Myth 3: "Online exams are informal and can be easily compromised."</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #334155;"><strong>The Reality:</strong> Top online universities implement dual-camera AI proctoring, secure browser lockdown software, biometric facial authentication, and continuous audio-visual invigilation. Any unauthorized tab switching, background voice, or secondary monitor triggers an immediate violation flag.</p>
            </div>

            <div style="border-left: 4px solid #b91c1c; background: #fef2f2; padding: 16px 20px; border-radius: 0 8px 8px 0;">
              <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 15px; font-weight:700;">Myth 4: "MNCs and private recruiters reject online MBA graduates."</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #334155;"><strong>The Reality:</strong> For experienced working professionals, recruiters evaluate demonstrated project impact, leadership maturity, and domain mastery over classroom attendance format. Over 500+ top corporations (Amazon, Deloitte, Infosys, Tata Motors) actively recruit and sponsor employees for online master's degrees.</p>
            </div>

            <div style="border-left: 4px solid #b91c1c; background: #fef2f2; padding: 16px 20px; border-radius: 0 8px 8px 0;">
              <h4 style="margin: 0 0 6px 0; color: #b91c1c; font-size: 15px; font-weight:700;">Myth 5: "A Tier-3 Regular MBA is better than a premier Online MBA."</h4>
              <p style="margin: 0; font-size: 13.5px; line-height: 1.6; color: #334155;"><strong>The Reality:</strong> Spending ₹10L–₹15L on an unranked, low-tier physical private college with poor placement records and outdated faculty is financially destructive. An accredited Online MBA from a NAAC A++ / NIRF Top-50 university (Manipal, Jain, Amity, St. Aloysius) offers vastly superior curriculum quality, prestigious brand recognition, and 0% EMI affordability.</p>
            </div>
          </div>
        </section>
    """
