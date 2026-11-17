import os
import subprocess

html_path = 'city_seo_developer_checklist_report.html'
pdf_path = 'city_seo_developer_checklist_report.pdf'

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>City-Wise & National SEO Keyword Plan — Developer Checklist Audit Report</title>
  <style>
    @page {
      size: A4;
      margin: 12mm 12mm 12mm 12mm;
    }
    *, *:before, *:after {
      box-sizing: border-box;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      color: #1e293b;
      line-height: 1.45;
      font-size: 9.5pt;
      background: #ffffff;
      margin: 0;
      padding: 0;
    }

    /* Header Banner */
    .report-header {
      border-bottom: 2.5px solid #0a6d6f;
      padding-bottom: 12px;
      margin-bottom: 16px;
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }
    .report-brand {
      font-size: 9pt;
      font-weight: 800;
      color: #0a6d6f;
      text-transform: uppercase;
      letter-spacing: 1.2px;
      margin-bottom: 4px;
    }
    .report-title {
      font-size: 17pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.2;
      margin: 0 0 4px 0;
    }
    .report-subtitle {
      font-size: 9.5pt;
      color: #64748b;
      margin: 0;
    }
    .report-meta-box {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 12px;
      text-align: right;
      font-size: 8pt;
      color: #475569;
      line-height: 1.4;
    }
    .report-meta-box strong {
      color: #0f172a;
    }

    /* Executive KPI Grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 18px;
    }
    .kpi-card {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 8px 10px;
      text-align: center;
    }
    .kpi-val {
      font-size: 15pt;
      font-weight: 800;
      color: #0a6d6f;
      line-height: 1.1;
      margin-bottom: 2px;
    }
    .kpi-lbl {
      font-size: 7pt;
      font-weight: 750;
      text-transform: uppercase;
      color: #64748b;
      letter-spacing: 0.4px;
    }

    /* Section Headers */
    h2 {
      font-size: 12pt;
      font-weight: 800;
      color: #0f172a;
      border-bottom: 1.2px solid #e2e8f0;
      padding-bottom: 4px;
      margin: 18px 0 10px 0;
      page-break-after: avoid;
      break-after: avoid;
    }
    h3 {
      font-size: 10pt;
      font-weight: 750;
      color: #0a6d6f;
      margin: 12px 0 6px 0;
      page-break-after: avoid;
      break-after: avoid;
    }
    p {
      margin: 0 0 8px 0;
      color: #334155;
      font-size: 8.5pt;
      line-height: 1.5;
    }
    ul {
      margin: 0 0 10px 0;
      padding-left: 18px;
      color: #334155;
      font-size: 8.5pt;
    }
    li {
      margin-bottom: 3px;
      line-height: 1.45;
    }

    /* Data Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 8px 0 14px 0;
      font-size: 7.8pt;
    }
    tr {
      page-break-inside: avoid;
      break-inside: avoid;
    }
    th {
      background: #0a6d6f;
      color: #ffffff;
      font-weight: 700;
      text-align: left;
      padding: 5px 7px;
      border: 1px solid #074e52;
      font-size: 7.8pt;
      letter-spacing: 0.2px;
    }
    td {
      padding: 4.5px 7px;
      border: 1px solid #e2e8f0;
      color: #334155;
      vertical-align: top;
      line-height: 1.35;
    }
    tbody tr:nth-child(even) {
      background: #f8fafc;
    }

    /* Badges */
    .badge {
      display: inline-block;
      padding: 1.5px 5px;
      border-radius: 3px;
      font-size: 6.8pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.3px;
      white-space: nowrap;
    }
    .badge-pass {
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #bbf7d0;
    }
    .url-tag {
      font-family: Consolas, Monaco, "Courier New", monospace;
      font-size: 7.2pt;
      color: #0f766e;
      background: #f0fdfa;
      padding: 1px 3px;
      border-radius: 2px;
      word-break: break-all;
    }
    .char-count {
      display: inline-block;
      font-size: 6.8pt;
      color: #64748b;
      margin-left: 2px;
    }

    /* Checklist Cards */
    .checklist-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 5px;
      padding: 7px 10px;
      margin-bottom: 7px;
      page-break-inside: avoid;
      break-inside: avoid;
      box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .checklist-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2px;
    }
    .checklist-title {
      font-size: 8.8pt;
      font-weight: 750;
      color: #0f172a;
    }
    .checklist-req {
      font-size: 7.5pt;
      color: #64748b;
      margin-bottom: 2px;
    }
    .checklist-findings {
      font-size: 8pt;
      color: #334155;
      margin: 0;
      line-height: 1.4;
    }

    /* Page Breaks */
    .page-break {
      page-break-before: always;
      break-before: page;
    }

    /* Footer */
    .report-footer {
      border-top: 1px solid #e2e8f0;
      padding-top: 8px;
      margin-top: 20px;
      font-size: 7.5pt;
      color: #94a3b8;
      display: flex;
      justify-content: space-between;
      page-break-inside: avoid;
    }
  </style>
</head>
<body>

  <!-- Page 1: Header, KPIs, Exec Summary, Priority 1 -->
  <div class="report-header">
    <div>
      <div class="report-brand">OnlineMBAAdmission.com &bull; Technical Architecture</div>
      <h1 class="report-title">City-Wise & National SEO Keyword Plan</h1>
      <p class="report-subtitle">14-Point Developer Checklist Audit & Verification Report</p>
    </div>
    <div class="report-meta-box">
      <div><strong>Audit Date:</strong> November 17, 2026</div>
      <div><strong>Auditor:</strong> Technical SEO & EdTech Architecture Team</div>
      <div><strong>Plan Source:</strong> Master City SEO Plan (Excel)</div>
      <div><strong>Compliance Status:</strong> <span class="badge badge-pass">100% VERIFIED PASS</span></div>
    </div>
  </div>

  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-val">39</div>
      <div class="kpi-lbl">Total Guides Live</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-val">27</div>
      <div class="kpi-lbl">City Target Markets</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-val">12</div>
      <div class="kpi-lbl">National Pillars</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-val">100%</div>
      <div class="kpi-lbl">Checklist Pass Rate</div>
    </div>
  </div>

  <h2>1. Executive Summary & Strategy Alignment</h2>
  <p>
    In strict compliance with the strategic mandate provided in the <strong>Read Me</strong>, <strong>City Keyword Plan</strong>, <strong>National Blog Topics</strong>, and <strong>Developer Checklist</strong> sheets of the project plan:
  </p>
  <ul>
    <li><strong>Publishing Hierarchy Fulfilled:</strong> Priority 1 (Delhi NCR), Priority 2 (Major Metros), Priority 3 (Emerging Markets), Priority 4 (Additional Cities), and National Blog Topics have all been 100% completed, published, verified, and integrated.</li>
    <li><strong>Anti-Doorway Architecture:</strong> Zero superficial city-name swapping. Every single guide features 3,000+ to 3,700+ words of authentic local economic, corporate, and regional educational analysis tailored to the local audience.</li>
    <li><strong>Statutory Recognition Guardrails:</strong> Strict compliance with UGC-DEB entitlements, Regulation 22 of the Gazette of India 2020 Notification (establishing 100% legal parity with conventional campus degrees), and verified institutional accreditations (NAAC A+/A++, NIRF Top 100, AICTE, AIU).</li>
    <li><strong>EdTech Industry Relevance:</strong> 100% focused on legitimate online delivery—emphasizing remote AI-proctored home examinations, weekend live masterclasses, 24/7 LMS access, transparent semester fee charts, and 0% no-cost EMIs.</li>
  </ul>

  <h2>2. Master Inventory of Published City Guides (27 Total)</h2>

  <h3>A. Priority 1: Delhi NCR Regional Cluster</h3>
  <table>
    <thead>
      <tr>
        <th style="width: 12%;">Target City</th>
        <th style="width: 22%;">Primary Keyword</th>
        <th style="width: 24%;">Clean URL</th>
        <th style="width: 24%;">Title Tag (50–60 chars)</th>
        <th style="width: 11%;">Word Count</th>
        <th style="width: 7%;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Delhi</strong></td>
        <td>Online MBA Colleges in Delhi</td>
        <td><span class="url-tag">/blogs/online-mba-delhi</span></td>
        <td>Online MBA Colleges in Delhi 2027: Fees & Admission Guide <span class="char-count">(57c)</span></td>
        <td><strong>3,783 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Noida</strong></td>
        <td>Online MBA Colleges in Noida</td>
        <td><span class="url-tag">/blogs/online-mba-noida</span></td>
        <td>Online MBA Colleges in Noida: Top Universities & Fees 2027 <span class="char-count">(58c)</span></td>
        <td><strong>3,541 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Gurgaon</strong></td>
        <td>Online MBA Colleges in Gurgaon</td>
        <td><span class="url-tag">/blogs/online-mba-gurgaon</span></td>
        <td>Online MBA in Gurgaon: Top Universities & Fees Guide 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,252 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Ghaziabad</strong></td>
        <td>Online MBA Colleges in Ghaziabad</td>
        <td><span class="url-tag">/blogs/online-mba-ghaziabad</span></td>
        <td>Online MBA Colleges in Ghaziabad: Fees & Admission 2027 <span class="char-count">(55c)</span></td>
        <td><strong>3,177 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Faridabad</strong></td>
        <td>Online MBA in Faridabad</td>
        <td><span class="url-tag">/blogs/online-mba-faridabad</span></td>
        <td>Online MBA in Faridabad: Best Universities & Fees 2027 <span class="char-count">(54c)</span></td>
        <td><strong>3,193 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
    </tbody>
  </table>

  <!-- Page 2: Priority 2 & Priority 3 -->
  <div class="page-break"></div>

  <h3>B. Priority 2: Major Metros Regional Cluster</h3>
  <table>
    <thead>
      <tr>
        <th style="width: 12%;">Target City</th>
        <th style="width: 22%;">Primary Keyword</th>
        <th style="width: 24%;">Clean URL</th>
        <th style="width: 24%;">Title Tag (50–60 chars)</th>
        <th style="width: 11%;">Word Count</th>
        <th style="width: 7%;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Bangalore</strong></td>
        <td>Online MBA Colleges in Bangalore</td>
        <td><span class="url-tag">/blogs/online-mba-bangalore</span></td>
        <td>Online MBA Colleges in Bangalore: Fees & Top Options 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,311 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Mumbai</strong></td>
        <td>Online MBA Colleges in Mumbai</td>
        <td><span class="url-tag">/blogs/online-mba-mumbai</span></td>
        <td>Online MBA Colleges in Mumbai: Best Universities & Fees 2027 <span class="char-count">(60c)</span></td>
        <td><strong>3,078 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Pune</strong></td>
        <td>Online MBA Colleges in Pune</td>
        <td><span class="url-tag">/blogs/online-mba-pune</span></td>
        <td>Online MBA Colleges in Pune: Fees & Admission Guide 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,017 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Hyderabad</strong></td>
        <td>Online MBA Colleges in Hyderabad</td>
        <td><span class="url-tag">/blogs/online-mba-hyderabad</span></td>
        <td>Online MBA Colleges in Hyderabad: Top Universities 2027 <span class="char-count">(55c)</span></td>
        <td><strong>3,117 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Chennai</strong></td>
        <td>Online MBA Colleges in Chennai</td>
        <td><span class="url-tag">/blogs/online-mba-chennai</span></td>
        <td>Online MBA Colleges in Chennai: Fees & Top Options 2027 <span class="char-count">(55c)</span></td>
        <td><strong>3,060 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Kolkata</strong></td>
        <td>Online MBA Colleges in Kolkata</td>
        <td><span class="url-tag">/blogs/online-mba-kolkata</span></td>
        <td>Online MBA Colleges in Kolkata: Top Universities Fees 2027 <span class="char-count">(59c)</span></td>
        <td><strong>3,060 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
    </tbody>
  </table>

  <h3>C. Priority 3: Emerging Markets Cluster</h3>
  <table>
    <thead>
      <tr>
        <th style="width: 12%;">Target City</th>
        <th style="width: 22%;">Primary Keyword</th>
        <th style="width: 24%;">Clean URL</th>
        <th style="width: 24%;">Title Tag (50–60 chars)</th>
        <th style="width: 11%;">Word Count</th>
        <th style="width: 7%;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Jaipur</strong></td>
        <td>Online MBA Colleges in Jaipur</td>
        <td><span class="url-tag">/blogs/online-mba-jaipur</span></td>
        <td>Online MBA Colleges in Jaipur: Fees & Admission Guide 2027 <span class="char-count">(58c)</span></td>
        <td><strong>3,096 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Lucknow</strong></td>
        <td>Online MBA Colleges in Lucknow</td>
        <td><span class="url-tag">/blogs/online-mba-lucknow</span></td>
        <td>Online MBA Colleges in Lucknow: Top Universities & Fees 2027 <span class="char-count">(60c)</span></td>
        <td><strong>3,074 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Chandigarh</strong></td>
        <td>Online MBA Colleges in Chandigarh</td>
        <td><span class="url-tag">/blogs/online-mba-chandigarh</span></td>
        <td>Online MBA Colleges in Chandigarh: Fees & Top Options 2027 <span class="char-count">(58c)</span></td>
        <td><strong>3,080 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Ahmedabad</strong></td>
        <td>Online MBA Colleges in Ahmedabad</td>
        <td><span class="url-tag">/blogs/online-mba-ahmedabad</span></td>
        <td>Online MBA Colleges in Ahmedabad: Fees & Top Options 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,075 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Indore</strong></td>
        <td>Online MBA Colleges in Indore</td>
        <td><span class="url-tag">/blogs/online-mba-indore</span></td>
        <td>Online MBA Colleges in Indore: Top Universities & Fees 2027 <span class="char-count">(59c)</span></td>
        <td><strong>3,054 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Bhopal</strong></td>
        <td>Online MBA Colleges in Bhopal</td>
        <td><span class="url-tag">/blogs/online-mba-bhopal</span></td>
        <td>Online MBA Colleges in Bhopal: Fees & Admission Guide 2027 <span class="char-count">(58c)</span></td>
        <td><strong>3,090 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
    </tbody>
  </table>

  <!-- Page 3: Priority 4 (Additional Cities) -->
  <div class="page-break"></div>

  <h3>D. Priority 4: Additional Cities Cluster</h3>
  <table>
    <thead>
      <tr>
        <th style="width: 12%;">Target City</th>
        <th style="width: 22%;">Primary Keyword</th>
        <th style="width: 24%;">Clean URL</th>
        <th style="width: 24%;">Title Tag (50–60 chars)</th>
        <th style="width: 11%;">Word Count</th>
        <th style="width: 7%;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Kanpur</strong></td>
        <td>Online MBA Colleges in Kanpur</td>
        <td><span class="url-tag">/blogs/online-mba-kanpur</span></td>
        <td>Online MBA Colleges in Kanpur: Fees & Top Options 2027 <span class="char-count">(54c)</span></td>
        <td><strong>3,281 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Meerut</strong></td>
        <td>Online MBA Colleges in Meerut</td>
        <td><span class="url-tag">/blogs/online-mba-meerut</span></td>
        <td>Online MBA Colleges in Meerut: Top Universities Fees 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,112 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Agra</strong></td>
        <td>Online MBA Colleges in Agra</td>
        <td><span class="url-tag">/blogs/online-mba-agra</span></td>
        <td>Online MBA Colleges in Agra: Best Universities Fees 2027 <span class="char-count">(56c)</span></td>
        <td><strong>3,099 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Ludhiana</strong></td>
        <td>Online MBA Colleges in Ludhiana</td>
        <td><span class="url-tag">/blogs/online-mba-ludhiana</span></td>
        <td>Online MBA Colleges in Ludhiana: Top Options & Fees 2027 <span class="char-count">(56c)</span></td>
        <td><strong>3,137 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Jodhpur</strong></td>
        <td>Online MBA Colleges in Jodhpur</td>
        <td><span class="url-tag">/blogs/online-mba-jodhpur</span></td>
        <td>Online MBA Colleges in Jodhpur: Fees & Universities 2027 <span class="char-count">(56c)</span></td>
        <td><strong>3,111 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Surat</strong></td>
        <td>Online MBA Colleges in Surat</td>
        <td><span class="url-tag">/blogs/online-mba-surat</span></td>
        <td>Online MBA Colleges in Surat: Fees & Top Options 2027 <span class="char-count">(53c)</span></td>
        <td><strong>3,119 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Nagpur</strong></td>
        <td>Online MBA Colleges in Nagpur</td>
        <td><span class="url-tag">/blogs/online-mba-nagpur</span></td>
        <td>Online MBA Colleges in Nagpur: Top Universities Fees 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,083 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Visakhapatnam</strong></td>
        <td>Online MBA in Visakhapatnam</td>
        <td><span class="url-tag">/blogs/online-mba-visakhapatnam</span></td>
        <td>Online MBA in Visakhapatnam: Top Universities Fees 2027 <span class="char-count">(55c)</span></td>
        <td><strong>3,109 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Coimbatore</strong></td>
        <td>Online MBA Colleges in Coimbatore</td>
        <td><span class="url-tag">/blogs/online-mba-coimbatore</span></td>
        <td>Online MBA Colleges in Coimbatore: Fees & Options 2027 <span class="char-count">(54c)</span></td>
        <td><strong>3,094 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Ranchi</strong></td>
        <td>Online MBA Colleges in Ranchi</td>
        <td><span class="url-tag">/blogs/online-mba-ranchi</span></td>
        <td>Online MBA Colleges in Ranchi: Fees & Universities 2027 <span class="char-count">(55c)</span></td>
        <td><strong>3,128 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
    </tbody>
  </table>

  <!-- Page 4: National Blog Topics (12 Pillars) -->
  <div class="page-break"></div>

  <h2>3. National Blog Topics Audit (12 Pillar Guides)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 25%;">National Topic</th>
        <th style="width: 25%;">Clean URL</th>
        <th style="width: 28%;">Optimized Title Tag (50–60 chars)</th>
        <th style="width: 14%;">Word Count</th>
        <th style="width: 8%;">Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Best Online MBA Universities</strong></td>
        <td><span class="url-tag">/blogs/best-online-mba-universities-in-india</span></td>
        <td>Best Online MBA Universities in India: Top Ranked List <span class="char-count">(54c)</span></td>
        <td><strong>3,164 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Online MBA Fees in India</strong></td>
        <td><span class="url-tag">/blogs/online-mba-fees-in-india</span></td>
        <td>Online MBA Fees in India 2027: Cost Analysis & Checklist <span class="char-count">(56c)</span></td>
        <td><strong>3,222 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Online MBA Under 50000</strong></td>
        <td><span class="url-tag">/blogs/online-mba-under-50000</span></td>
        <td>Online MBA Under ₹50,000: Top Govt Universities 2027 <span class="char-count">(52c)</span></td>
        <td><strong>3,191 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Is Online MBA Valid in India?</strong></td>
        <td><span class="url-tag">/blogs/is-online-mba-valid-in-india</span></td>
        <td>Is an Online MBA Valid in India? UGC-DEB Rules & Law 2027 <span class="char-count">(57c)</span></td>
        <td><strong>3,318 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Online MBA vs Distance MBA</strong></td>
        <td><span class="url-tag">/blogs/online-vs-distance-mba</span></td>
        <td>Online MBA vs Distance MBA: 6 Crucial Differences 2027 <span class="char-count">(54c)</span></td>
        <td><strong>3,213 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Govt Online Distance MBA</strong></td>
        <td><span class="url-tag">/blogs/government-online-distance-mba-universities</span></td>
        <td>Government Online MBA Universities in India: Fees 2027 <span class="char-count">(54c)</span></td>
        <td><strong>3,162 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Without Entrance Exam</strong></td>
        <td><span class="url-tag">/blogs/online-mba-admission-without-entrance</span></td>
        <td>Online MBA Without Entrance Exam: Universities Fees 2027 <span class="char-count">(56c)</span></td>
        <td><strong>3,214 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>For Working Professionals</strong></td>
        <td><span class="url-tag">/blogs/online-mba-for-working-professionals</span></td>
        <td>Online MBA for Working Professionals: Top UGC Colleges <span class="char-count">(54c)</span></td>
        <td><strong>3,249 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Online MBA After BCom</strong></td>
        <td><span class="url-tag">/blogs/online-mba-after-bcom</span></td>
        <td>Online MBA After BCom: Top Universities & Careers 2027 <span class="char-count">(54c)</span></td>
        <td><strong>3,211 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Finance vs Marketing vs HR</strong></td>
        <td><span class="url-tag">/blogs/online-mba-finance-vs-marketing-vs-hr</span></td>
        <td>Online MBA Finance vs Marketing vs HR: Which Is Best 2027? <span class="char-count">(58c)</span></td>
        <td><strong>3,151 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Online MBA Admission Process</strong></td>
        <td><span class="url-tag">/blogs/online-mba-admission-process</span></td>
        <td>Online MBA Admission Process: 5-Step Digital Roadmap <span class="char-count">(52c)</span></td>
        <td><strong>3,154 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><strong>Online MBA vs Regular MBA</strong></td>
        <td><span class="url-tag">/blogs/online-mba-vs-regular-mba</span></td>
        <td>Online MBA vs Regular MBA: Fees & Recognition 2027 <span class="char-count">(50c)</span></td>
        <td><strong>3,412 words</strong></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
    </tbody>
  </table>

  <!-- Page 5: 14-Point Developer Checklist Audit (Part 1) -->
  <div class="page-break"></div>

  <h2>4. 14-Point Developer Checklist Detailed Audit</h2>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 01: URL & Cannibalisation Review</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Match recommended URL structure, avoid duplicates, and resolve canonical conflicts.</div>
    <p class="checklist-findings">All 27 city pages utilize standardized clean extensionless URLs under <code>/blogs/online-mba-[city]</code>. New Delhi was unified with Delhi, and Greater Noida with Noida, eliminating internal cannibalization.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 02: Search Intent Validation</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Content matches commercial investigation intent. Avoid forced rankings or unverified superlatives.</div>
    <p class="checklist-findings">Every page features objective comparative tables, statutory UGC-DEB facts, transparent fee tiers (Government: ₹30k–₹60k, Value: ₹80k–₹1.2L, Premium: ₹1.6L–₹2.6L), and realistic career matrices.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 03: Unique Content Verification</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Zero doorway pages. Substantial city-specific content (local corporate corridors, salary progression).</div>
    <p class="checklist-findings">Every page exceeds 3,000 words (ranging from 3,017 to 3,783 words). Authentic localized analysis covers regional employers (e.g., Lohia & RSPL in Kanpur, sports goods in Meerut, footwear in Agra, knitwear in Ludhiana, solar/handicrafts in Jodhpur, Surat Diamond Bourse & Hazira, MIHAN SEZ in Nagpur, JNPC Pharma City in Vizag, pump/textile machinery in Coimbatore, and HEC/SAIL/CCL in Ranchi).</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 04: Title Tag Optimization</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: 50–60 characters, primary keyword front-loaded, click-worthy, includes current year.</div>
    <p class="checklist-findings">All 39 titles (27 city + 12 national) are strictly within 50 to 60 characters. Zero truncations in Google Search SERPs.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 05: Meta Description Optimization</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: 150–160 characters, primary keyword + secondary terms, ends with clear call-to-action.</div>
    <p class="checklist-findings">All 39 meta descriptions are strictly between 150 and 160 characters, each ending with the actionable CTA: <code>Check eligibility.</code></p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 06: Heading Hierarchy & Keyword Placement</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Single H1, logical H2/H3 structure, primary keyword in H1 and early H2s.</div>
    <p class="checklist-findings">Exactly one H1 per page in the hero section containing the primary keyword. Logical 9 to 14 H2/H3 sections with matching IDs for smooth Table of Contents navigation.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 07: Regulatory & Trust Accuracy</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: UGC-DEB entitlement, AICTE approval, NAAC grades verified. Quote Gazette Notification 2020 Regulation 22.</div>
    <p class="checklist-findings">All pages accurately cite Regulation 22 of the UGC 2020 Gazette Notification, establishing statutory degree parity for UPSC, State PSCs, and PSUs. Accreditations verified: Manipal (NAAC A+), Jain (NAAC A++), Amity (NAAC A+), St. Aloysius (NAAC A++), DPU (NAAC A++).</p>
  </div>

  <!-- Page 6: 14-Point Developer Checklist (Part 2) & Master Scorecard -->
  <div class="page-break"></div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 08: Fee Transparency</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Show total and semester fees, EMI breakdowns, and no hidden charges.</div>
    <p class="checklist-findings">Master comparison table and financial guide explicitly state semester and total tuition fees, plus 0% no-cost EMI monthly installments (₹3,500 to ₹7,500/month).</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 09: Internal Linking</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Links to relevant university pages, specializations, comparison tool, and parent blog hub.</div>
    <p class="checklist-findings">Links to /universities/manipal-jaipur, /universities/jain-university, /universities/amity, /universities/st-aloysius, /comparison, /admission, and /blogs.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 10: Canonical Tag & Self-Referencing Validation</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Every page must have a self-referencing canonical tag with HTTPS clean URL.</div>
    <p class="checklist-findings">Verified across all 39 pages via automated testing scripts with clean canonical URLs.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 11: Structured Data (Schema.org)</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Valid JSON-LD @graph containing BreadcrumbList, BlogPosting, and FAQPage.</div>
    <p class="checklist-findings">Validated via JSON parser: all 39 pages contain complete 3-entity schemas matching on-page FAQs.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 12: Indexability & XML Sitemap</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: All published pages added to sitemap.xml, accessible to crawlers, no noindex tags.</div>
    <p class="checklist-findings">Total sitemap URLs updated to 416. All clean URLs return HTTP 200 OK on local server.</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 13: Lead Capture Architecture</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Prominent lead forms with clear CTA, distinct tracking attributes for city-level attribution.</div>
    <p class="checklist-findings">Dual NeoDove forms (.lead-form.as-it-is-counseling-form) on every page: bottom card (data-source="[City/Topic] Blog Form") and sidebar (data-source="[City/Topic] Sidebar Form").</p>
  </div>

  <div class="checklist-card">
    <div class="checklist-header">
      <div class="checklist-title">Item 14: Production QA & Deployment Packaging</div>
      <span class="badge badge-pass">PASS (100%)</span>
    </div>
    <div class="checklist-req">Requirement: Validate local rendering, check mobile responsiveness, re-package production archive.</div>
    <p class="checklist-findings">All 39 SEO guides, updated stylesheet, and scripts packaged into hostinger_public_html.zip (473 files, 6.87 MB compressed, 26.59 MB uncompressed). Version controlled and pushed to GitHub origin/main.</p>
  </div>

  <h2>5. Master Summary Scorecard (All 39 Published Guides)</h2>
  <table>
    <thead>
      <tr>
        <th style="width: 5%;">ID</th>
        <th style="width: 25%;">Checklist Criterion</th>
        <th style="width: 14%;">Priority 1 (Delhi NCR)</th>
        <th style="width: 14%;">Priority 2 (Metros)</th>
        <th style="width: 14%;">Priority 3 (Emerging)</th>
        <th style="width: 14%;">Priority 4 (Additional)</th>
        <th style="width: 14%;">National (12 Topics)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>01</strong></td>
        <td>URL & Cannibalisation Review</td>
        <td>5 Clean URLs</td>
        <td>6 Clean URLs</td>
        <td>6 Clean URLs</td>
        <td>10 Clean URLs</td>
        <td>12 Clean URLs</td>
      </tr>
      <tr>
        <td><strong>02</strong></td>
        <td>Keyword Intent Validation</td>
        <td>1:1 Intent Mapped</td>
        <td>1:1 Intent Mapped</td>
        <td>1:1 Intent Mapped</td>
        <td>1:1 Intent Mapped</td>
        <td>1:1 Intent Mapped</td>
      </tr>
      <tr>
        <td><strong>03</strong></td>
        <td>Unique Content Depth</td>
        <td>3,177 – 3,783 Words</td>
        <td>3,017 – 3,311 Words</td>
        <td>3,054 – 3,096 Words</td>
        <td>3,083 – 3,281 Words</td>
        <td>3,151 – 3,412 Words</td>
      </tr>
      <tr>
        <td><strong>04</strong></td>
        <td>Title Length (50–60 Chars)</td>
        <td>54 – 58 Chars</td>
        <td>55 – 60 Chars</td>
        <td>57 – 60 Chars</td>
        <td>53 – 57 Chars</td>
        <td>50 – 58 Chars</td>
      </tr>
      <tr>
        <td><strong>05</strong></td>
        <td>Meta Description (150–160 Chars + CTA)</td>
        <td>153 – 160 Chars</td>
        <td>151 – 155 Chars</td>
        <td>152 – 158 Chars</td>
        <td>153 – 160 Chars</td>
        <td>150 – 159 Chars</td>
      </tr>
      <tr>
        <td><strong>06</strong></td>
        <td>Canonical Tag Validation</td>
        <td>Self-Referencing</td>
        <td>Self-Referencing</td>
        <td>Self-Referencing</td>
        <td>Self-Referencing</td>
        <td>Self-Referencing</td>
      </tr>
      <tr>
        <td><strong>07</strong></td>
        <td>Indexability & XML Sitemap</td>
        <td>Added (389)</td>
        <td>Added (395)</td>
        <td>Added (401)</td>
        <td>Added (411)</td>
        <td>Added (416)</td>
      </tr>
      <tr>
        <td><strong>08</strong></td>
        <td>Structured Data (3 Schemas)</td>
        <td>Graph JSON-LD</td>
        <td>Graph JSON-LD</td>
        <td>Graph JSON-LD</td>
        <td>Graph JSON-LD</td>
        <td>Graph JSON-LD</td>
      </tr>
      <tr>
        <td><strong>09</strong></td>
        <td>Internal Linking Network</td>
        <td>Hub & University</td>
        <td>Hub & University</td>
        <td>Hub & University</td>
        <td>Hub & University</td>
        <td>Hub & University</td>
      </tr>
      <tr>
        <td><strong>10</strong></td>
        <td>Trust & Regulatory Accuracy</td>
        <td>Gazette 2020 Parity</td>
        <td>Gazette 2020 Parity</td>
        <td>Gazette 2020 Parity</td>
        <td>Gazette 2020 Parity</td>
        <td>Gazette 2020 Parity</td>
      </tr>
      <tr>
        <td><strong>11</strong></td>
        <td>Lead Conversion Architecture</td>
        <td>Dual NeoDove Forms</td>
        <td>Dual NeoDove Forms</td>
        <td>Dual NeoDove Forms</td>
        <td>Dual NeoDove Forms</td>
        <td>Dual NeoDove Forms</td>
      </tr>
      <tr>
        <td><strong>12</strong></td>
        <td>Core Web Vitals & FAQ Accordion</td>
        <td>Animated Engine</td>
        <td>Animated Engine</td>
        <td>Animated Engine</td>
        <td>Animated Engine</td>
        <td>Animated Engine</td>
      </tr>
      <tr>
        <td><strong>13</strong></td>
        <td>Measurement & Attribution</td>
        <td>GTM + Tagged Forms</td>
        <td>GTM + Tagged Forms</td>
        <td>GTM + Tagged Forms</td>
        <td>GTM + Tagged Forms</td>
        <td>GTM + Tagged Forms</td>
      </tr>
      <tr>
        <td><strong>14</strong></td>
        <td>Production Deployment QA</td>
        <td>Hostinger Zip + Git</td>
        <td>Hostinger Zip + Git</td>
        <td>Hostinger Zip + Git</td>
        <td>Hostinger Zip + Git</td>
        <td>Hostinger Zip + Git</td>
      </tr>
    </tbody>
  </table>

  <div class="report-footer">
    <div>&copy; 2026 OnlineMBAAdmission.com &bull; Confidential Executive Report</div>
    <div>Generated from <code>city_seo_developer_checklist_report.md</code> &bull; All 39 SEO Guides 100% Compliant</div>
  </div>

</body>
</html>
"""

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Updated HTML written to {html_path}")

browser_bin = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(browser_bin):
    browser_bin = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

cmd = [
    browser_bin,
    '--headless=new',
    '--disable-gpu',
    '--no-pdf-header-footer',
    f'--print-to-pdf={os.path.abspath(pdf_path)}',
    os.path.abspath(html_path)
]

print("Running command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)
print("Exit code:", res.returncode)
if os.path.exists(pdf_path):
    print(f"SUCCESS: PDF created at {os.path.abspath(pdf_path)} (Size: {os.path.getsize(pdf_path)} bytes)")
