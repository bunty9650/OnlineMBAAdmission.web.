"""
Script: scripts/build_academic_duration_blogs.py
Replaced with unified generator in scripts/rebuild_all_30_blogs.py
Maintains get_specialized_matrix_table for compatibility.
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from academic_duration_definitions import BLOGS

def get_specialized_matrix_table(slug):
    # Specialized domain matrix tables
    if slug == "online-mba-2-years":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view 2-year academic roadmap &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Academic Period</th>
        <th>Duration &amp; Timeline</th>
        <th>Curricular Focus</th>
        <th>CBCS Credits</th>
        <th>Key Deliverables</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Year 1: Semester 1</strong></td>
        <td>Months 1 to 6 (July-Dec / Jan-June)</td>
        <td>Foundational Management Principles, Economics, Accounting, Statistics</td>
        <td>24 to 26 Credits</td>
        <td>Continuous quizzes, 2 assignments per subject, proctored TEE exams.</td>
      </tr>
      <tr>
        <td><strong>Year 1: Semester 2</strong></td>
        <td>Months 7 to 12 (Jan-June / July-Dec)</td>
        <td>Functional Domains: Marketing, Corporate Finance, HRM, Operations</td>
        <td>24 to 26 Credits</td>
        <td>Cross-functional business cases, digital lab simulations, specialization selection.</td>
      </tr>
      <tr>
        <td><strong>Year 2: Semester 3</strong></td>
        <td>Months 13 to 18 (July-Dec / Jan-June)</td>
        <td>Domain Electives Track 1, Strategic Management, Research Methodology</td>
        <td>24 to 26 Credits</td>
        <td>Advanced specialization projects, live industry webinars, minor project.</td>
      </tr>
      <tr>
        <td><strong>Year 2: Semester 4</strong></td>
        <td>Months 19 to 24 (Jan-June / July-Dec)</td>
        <td>Advanced Electives Track 2, Business AI, Capstone Dissertation, Viva</td>
        <td>24 to 26 Credits</td>
        <td>Full industry consulting dissertation, viva voce, final degree convocation.</td>
      </tr>
      <tr>
        <td><strong>NEP 2020 Extended Window</strong></td>
        <td>Months 25 to 48 (Up to 4 Years)</td>
        <td>Backlog Clearance, Semester Breaks, Extended Project Submission</td>
        <td>Permanent in ABC ID</td>
        <td>Complete paused terms without re-admission fees or credit loss.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-syllabus":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view complete 4-semester syllabus &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Semester</th>
        <th>Core &amp; Elective Courses Covered</th>
        <th>CBCS Credits</th>
        <th>Evaluation Weightage</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Semester 1 (Core Foundations)</strong></td>
        <td>Principles of Management, Managerial Economics, Financial &amp; Management Accounting, Quantitative Techniques, Organizational Behaviour, Business Communication</td>
        <td>24-26 Credits</td>
        <td>30% Continuous Internal Assessment + 70% Term-End Exam</td>
      </tr>
      <tr>
        <td><strong>Semester 2 (Functional Core)</strong></td>
        <td>Financial Management, Marketing Management, Human Resource Management, Operations &amp; Supply Chain, Business Research Methods, Management Information Systems (MIS)</td>
        <td>24-26 Credits</td>
        <td>30% Continuous Internal Assessment + 70% Term-End Exam</td>
      </tr>
      <tr>
        <td><strong>Semester 3 (Specialization Electives)</strong></td>
        <td>Track Elective I, Track Elective II, Track Elective III, Strategic Management, Corporate Governance &amp; Ethics, Minor Industry Project / Case Folio</td>
        <td>24-26 Credits</td>
        <td>40% Continuous Assignment/Case Study + 60% Term-End Exam</td>
      </tr>
      <tr>
        <td><strong>Semester 4 (Advanced Capstone)</strong></td>
        <td>Advanced Elective IV, Advanced Elective V, Business Analytics &amp; AI for Managers, Master Capstone Dissertation, Comprehensive Viva Voce</td>
        <td>24-26 Credits</td>
        <td>50% Dissertation Defense &amp; Viva + 50% Term-End Exam</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-subjects":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view full subject distribution &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Subject Cluster</th>
        <th>Semester</th>
        <th>Key Practical Topics</th>
        <th>Software / Tools Taught</th>
        <th>Industry Application</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Corporate Finance</strong></td>
        <td>Sem 1 &amp; 2 (Core)</td>
        <td>Working Capital Management, Capital Budgeting, Financial Statement Analysis</td>
        <td>Advanced MS Excel, Financial Modeling</td>
        <td>Equity research, corporate treasury, debt restructuring</td>
      </tr>
      <tr>
        <td><strong>Marketing &amp; Digital Growth</strong></td>
        <td>Sem 2 &amp; 3</td>
        <td>Consumer Behaviour, Brand Strategy, Performance Marketing, Omni-Channel Sales</td>
        <td>Google Ads, Meta Business Suite, SEMrush</td>
        <td>Brand management, growth hacking, product marketing</td>
      </tr>
      <tr>
        <td><strong>Data Science &amp; Business AI</strong></td>
        <td>Sem 2 &amp; 4</td>
        <td>Predictive Modeling, Executive Dashboards, Generative AI for Workplaces</td>
        <td>Power BI, Tableau, Python Basics, ChatGPT Enterprise</td>
        <td>Business intelligence, data-driven revenue optimization</td>
      </tr>
      <tr>
        <td><strong>People Analytics &amp; HRM</strong></td>
        <td>Sem 2 &amp; 3</td>
        <td>Talent Acquisition, Strategic HRM, Compensation Planning, Labor Laws</td>
        <td>Darwinbox, Workday Essentials, BambooHR</td>
        <td>HR business partnering, executive search, compensation design</td>
      </tr>
      <tr>
        <td><strong>Operations &amp; SCM</strong></td>
        <td>Sem 2 &amp; 3</td>
        <td>Logistics Engineering, Total Quality Management (TQM), Six Sigma, Procurement</td>
        <td>SAP ERP Essentials, Arena Simulation</td>
        <td>Supply chain lead, operations transformation manager</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-exams":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view remote exam architecture &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Examination Parameter</th>
        <th>Online Proctored Architecture</th>
        <th>Technical Specifications Required</th>
        <th>Malpractice Mitigation System</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Testing Venue</strong></td>
        <td>100% Home/Office Remote Proctored</td>
        <td>Quiet room, clean desk, adequate lighting</td>
        <td>360-degree webcam room scan before login</td>
      </tr>
      <tr>
        <td><strong>Hardware Needed</strong></td>
        <td>Laptop or Desktop PC (Windows/macOS)</td>
        <td>Min Core i3, 4GB RAM, 720p Webcam, Mic</td>
        <td>Smartphones &amp; Tablets strictly disallowed for TEE</td>
      </tr>
      <tr>
        <td><strong>Browser Environment</strong></td>
        <td>Safe Exam Browser (SEB) Lockdown</td>
        <td>Disables Alt+Tab, function keys, clipboard</td>
        <td>Auto-terminates session on screen recording attempt</td>
      </tr>
      <tr>
        <td><strong>AI Surveillance</strong></td>
        <td>Facial Recognition &amp; Gaze Tracking</td>
        <td>Continuous biometric face matching</td>
        <td>Flags looking away, multiple faces, voice whispering</td>
      </tr>
      <tr>
        <td><strong>Human Proctoring</strong></td>
        <td>Live 1:15 Invigilator Dashboard</td>
        <td>Two-way audio/video monitoring</td>
        <td>Proctor can pause test, issue warnings, or nullify test</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "how-long-is-online-mba":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view duration breakdown &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Degree Type</th>
        <th>Minimum Duration</th>
        <th>Maximum Allowed Duration</th>
        <th>Weekly Study Hours</th>
        <th>Target Aspirant</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>UGC-DEB Online MBA (Standard)</strong></td>
        <td>2 Years (24 Months)</td>
        <td>4 Years (48 Months under NEP)</td>
        <td>8 to 12 Hours/Week</td>
        <td>Fresh graduates &amp; working professionals seeking statutory master degree.</td>
      </tr>
      <tr>
        <td><strong>1-Year Global Executive MBA</strong></td>
        <td>12 Months (Fast-Track)</td>
        <td>2 Years</td>
        <td>18 to 22 Hours/Week</td>
        <td>Senior managers with 5+ years experience (Autonomous/International).</td>
      </tr>
      <tr>
        <td><strong>Part-Time Weekend MBA</strong></td>
        <td>2.5 to 3 Years</td>
        <td>5 Years</td>
        <td>15 Hours/Weekend</td>
        <td>Professionals commuting to physical campus for weekend lectures.</td>
      </tr>
      <tr>
        <td><strong>Full-Time On-Campus MBA</strong></td>
        <td>2 Years (Residential)</td>
        <td>3 Years</td>
        <td>40+ Hours/Week (Full Time)</td>
        <td>Fresh graduates able to take a 2-year full-time career hiatus.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "who-can-do-online-mba":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view eligibility categories &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Candidate Background</th>
        <th>Undergraduate Stream</th>
        <th>Min Marks Required</th>
        <th>Work Experience Required</th>
        <th>Key Motivation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Working Corporate Executives</strong></td>
        <td>B.Tech, B.Com, BBA, B.Sc, BA</td>
        <td>50% (45% Reserved)</td>
        <td>0 to 10+ Years (Flexible)</td>
        <td>Accelerate promotion to General Manager / VP level without job hiatus.</td>
      </tr>
      <tr>
        <td><strong>Fresh Undergraduates</strong></td>
        <td>Any stream (10+2+3 or 10+2+4)</td>
        <td>50% Aggregate</td>
        <td>0 Years (Freshers Welcome)</td>
        <td>Earn a recognized UGC master degree while preparing for competitive exams or jobs.</td>
      </tr>
      <tr>
        <td><strong>Entrepreneurs &amp; Business Owners</strong></td>
        <td>Any recognized degree</td>
        <td>Passing Marks / 50%</td>
        <td>Family business / Startup</td>
        <td>Master corporate scaling, financial structuring, and digital performance marketing.</td>
      </tr>
      <tr>
        <td><strong>Govt &amp; Defense Personnel</strong></td>
        <td>Indian Armed Forces, State/Central Govt</td>
        <td>50% (Relaxation as per norms)</td>
        <td>Serving or Ex-Servicemen</td>
        <td>Corporate transition, post-retirement career growth, defense fee concessions.</td>
      </tr>
      <tr>
        <td><strong>International &amp; NRI Aspirants</strong></td>
        <td>Foreign Bachelor Degree (AIU Equiv)</td>
        <td>Equivalent 50% / Grade C</td>
        <td>Not mandatory</td>
        <td>Globally valid Indian business degree at 80% lower cost than UK/US programs.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "who-is-eligible-for-online-mba":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view statutory eligibility criteria &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Aspirant Cohort</th>
        <th>Qualifying Degree Criteria</th>
        <th>Minimum Cut-Off %</th>
        <th>National Entrance Test</th>
        <th>Mandatory Documentation</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>General / Unreserved</strong></td>
        <td>10+2+3 or 10+2+4 Bachelor's Degree</td>
        <td>50.0% Aggregate</td>
        <td>Exempt (Direct Merit)</td>
        <td>Aadhaar, 10th, 12th, Degree Marksheets, Passing Cert</td>
      </tr>
      <tr>
        <td><strong>SC / ST / PwD Candidates</strong></td>
        <td>Recognized Bachelor's Degree</td>
        <td>45.0% Aggregate (5% Waiver)</td>
        <td>Exempt (Direct Merit)</td>
        <td>Category/Caste Certificate + Standard Academic Records</td>
      </tr>
      <tr>
        <td><strong>Final Semester UG Students</strong></td>
        <td>Awaiting Final Year Bachelor Results</td>
        <td>Min 50% in Sem 1-5 / 1-7</td>
        <td>Exempt (Provisional)</td>
        <td>Provisional Admit Card, undertaking to submit final marksheet</td>
      </tr>
      <tr>
        <td><strong>Technical / Medical Graduates</strong></td>
        <td>B.Tech, B.E., MBBS, BDS, B.Pharm</td>
        <td>50.0% Aggregate</td>
        <td>Exempt (Direct Merit)</td>
        <td>AICTE/NMC/PCI recognized bachelor certificates</td>
      </tr>
      <tr>
        <td><strong>Distance / Open University Grads</strong></td>
        <td>IGNOU, DU SOL, State Open Universities</td>
        <td>50.0% (45% Reserved)</td>
        <td>Exempt (Direct Merit)</td>
        <td>UGC-DEB recognized degree certificate &amp; consolidated marksheet</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "how-to-do-online-mba":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view success strategy roadmap &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Phase</th>
        <th>Operational Action</th>
        <th>Weekly Time Commitment</th>
        <th>Key Milestone</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Month 1: Orientation &amp; LMS Setup</strong></td>
        <td>Login to university LMS, attend live onboarding, set study schedule</td>
        <td>4-6 Hours/Week</td>
        <td>Access student portal, e-library, WhatsApp peer study group</td>
      </tr>
      <tr>
        <td><strong>Months 2-5: Core Term Work</strong></td>
        <td>Watch asynchronous video lectures, attend weekend live classes</td>
        <td>8-10 Hours/Week</td>
        <td>Submit 2 continuous assignments per subject before deadline</td>
      </tr>
      <tr>
        <td><strong>Month 6: Exam Prep &amp; TEE</strong></td>
        <td>System mock test, review case questions, attempt proctored exams</td>
        <td>12-14 Hours/Week (Exam Week)</td>
        <td>Clear Semester 1 term-end proctored exam from home</td>
      </tr>
      <tr>
        <td><strong>Year 2: Elective Specialization</strong></td>
        <td>Select career track (Finance/Marketing/Analytics), start capstone thesis</td>
        <td>10 Hours/Week</td>
        <td>Complete industry project report &amp; virtual corporate internship</td>
      </tr>
      <tr>
        <td><strong>Month 24: Final Degree Convocation</strong></td>
        <td>Defend capstone dissertation via viva, verify credits in ABC portal</td>
        <td>Final viva window</td>
        <td>Receive UGC-DEB master degree certificate &amp; grade sheet</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "how-to-apply-for-online-mba":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view application blueprint &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Step #</th>
        <th>Application Stage</th>
        <th>Estimated Time</th>
        <th>Documents &amp; Actions Required</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Stage 1</strong></td>
        <td>University &amp; Specialization Shortlisting</td>
        <td>Day 1</td>
        <td>Verify UGC-DEB status, compare total fees, check 0% EMI availability</td>
      </tr>
      <tr>
        <td><strong>Stage 2</strong></td>
        <td>Digital Application Submission</td>
        <td>15 Minutes</td>
        <td>Fill basic profile, upload 10th/12th/UG marksheet, Aadhaar card</td>
      </tr>
      <tr>
        <td><strong>Stage 3</strong></td>
        <td>Counselor Document Verification</td>
        <td>12-24 Hours</td>
        <td>Academic team checks eligibility cut-off (50% Gen / 45% Reserved)</td>
      </tr>
      <tr>
        <td><strong>Stage 4</strong></td>
        <td>Fee Payment or EMI Activation</td>
        <td>Same Day</td>
        <td>Pay semester fee or complete paperless Aadhaar e-KYC for 0% EMI</td>
      </tr>
      <tr>
        <td><strong>Stage 5</strong></td>
        <td>Enrollment Number &amp; LMS Activation</td>
        <td>24-48 Hours</td>
        <td>Receive official university student ID, LMS login, and study material</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    elif slug == "online-mba-assignments":
        return """
<div class="mobile-table-swipe-hint">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
  <span>Swipe horizontally to view internal assessment structure &rarr;</span>
</div>
<div class="article-table-wrapper">
  <table class="article-data-table">
    <thead>
      <tr>
        <th>Assignment Component</th>
        <th>Format &amp; Submission Mode</th>
        <th>Weightage in Final Grade</th>
        <th>Evaluation Rubric</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Formative Quizzes (MCQs)</strong></td>
        <td>Online LMS timed quizzes after each module</td>
        <td>10% of total term score</td>
        <td>Automated instant scoring, conceptual clarity testing</td>
      </tr>
      <tr>
        <td><strong>Subject Descriptive Assignments</strong></td>
        <td>Written case analysis / analytical problem sheet (PDF upload)</td>
        <td>15% to 20% of total score</td>
        <td>Plagiarism scan (<10% via Turnitin), structure, domain reasoning</td>
      </tr>
      <tr>
        <td><strong>Discussion Forum Participation</strong></td>
        <td>Faculty-led asynchronous thread discussions</td>
        <td>5% of total score</td>
        <td>Peer interaction, quality of insights, weekly consistency</td>
      </tr>
      <tr>
        <td><strong>Minor Practical Projects</strong></td>
        <td>Data modeling, marketing campaigns, or financial models</td>
        <td>10% in Elective semesters</td>
        <td>Applied practical utility, real company dataset synthesis</td>
      </tr>
      <tr>
        <td><strong>Term-End Examination (TEE)</strong></td>
        <td>AI web-proctored remote 70-mark examination</td>
        <td>70% of total semester score</td>
        <td>Case studies, conceptual essays, quantitative problems</td>
      </tr>
    </tbody>
  </table>
</div>
"""
    return ""

if __name__ == "__main__":
    from rebuild_all_30_blogs import run_rebuild
    run_rebuild()
