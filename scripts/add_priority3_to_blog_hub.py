import re

cards_html = """
          <!-- Priority 3 City Blog 1: Jaipur -->
          <article class="blog-card" id="article-online-mba-jaipur">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fce4ec; color:#c2185b;">Pink City Enterprise Hub</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-jaipur">Online MBA Colleges in Jaipur: Fees &amp; Admission Guide 2027</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive guide for SEZ professionals, engineers, and exporters in Mahindra World City and Sitapura. Review verified UGC-DEB universities &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> 100% online delivery with remote AI-proctored home exams eliminates highway commutes to campuses in Dehmi Kalan or Ajmer Road.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-jaipur" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 3 City Blog 2: Lucknow -->
          <article class="blog-card" id="article-online-mba-lucknow">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2fe; color:#0369a1;">UP Governance &amp; IT Hub</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-lucknow">Online MBA Colleges in Lucknow: Top Universities &amp; Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Authoritative guide for state secretariat officers, PSU engineers, and tech leads in Gomti Nagar &amp; Shaheed Path. Review fees, eligibility &amp; remote exams.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Secure mandatory Master's degree equivalence under the UGC 2020 Gazette for UP state promotions while maintaining full salary.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-lucknow" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 3 City Blog 3: Chandigarh -->
          <article class="blog-card" id="article-online-mba-chandigarh">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#ecfdf5; color:#047857;">Tricity Tech &amp; Global PR</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-chandigarh">Online MBA Colleges in Chandigarh: Fees &amp; Top Options 2027</a></h3>
              <p class="blog-card-excerpt">
                Strategic guide for tech executives in Mohali IT Park and defense veterans in Panchkula. Compare UGC-DEB fees, WES recognized degrees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Gain full 2-year Master's degree WES equivalency for Canadian PR Express Entry points without resigning from your current job.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-chandigarh" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 3 City Blog 4: Ahmedabad -->
          <article class="blog-card" id="article-online-mba-ahmedabad">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fef3c7; color:#b45309;">GIFT City &amp; Industry</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-ahmedabad">Online MBA Colleges in Ahmedabad: Fees &amp; Top Options 2027</a></h3>
              <p class="blog-card-excerpt">
                In-depth guide for finance leads in GIFT City and manufacturing engineers in Sanand &amp; Changodar. Review verified UGC-DEB fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Scale second-generation family enterprises or accelerate to VP of Cross-Border Finance in GIFT City with 100% remote flexibility.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-ahmedabad" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 3 City Blog 5: Indore -->
          <article class="blog-card" id="article-online-mba-indore">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2f1; color:#00695c;">Cleanest City &amp; Pithampur</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-indore">Online MBA Colleges in Indore: Top Universities &amp; Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive guide for IT leads in Super Corridor and manufacturing engineers in Pithampur. Compare UGC-DEB universities, fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Break free from plant shift rotations to become Plant Operations Head or IT Product Lead with an accredited Master's degree.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-indore" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 3 City Blog 6: Bhopal -->
          <article class="blog-card" id="article-online-mba-bhopal">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fff3e0; color:#e65100;">BHEL &amp; Heavy Engineering</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-bhopal">Online MBA Colleges in Bhopal: Fees &amp; Admission Guide 2027</a></h3>
              <p class="blog-card-excerpt">
                Practical guide for engineers at BHEL Bhopal, Mandideep industrial leads, and state secretariat staff. Review verified UGC-DEB fees &amp; PSU validity.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Achieve mandatory Master's degree legal parity for BHEL and MP state utility promotional interviews without taking study leave.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-bhopal" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>
"""

with open("blogs/index.html", "r", encoding="utf-8") as f:
    content = f.read()

target = '          </article>\n\n          <article class="blog-card" id="article-online-mba">'
replacement = f'          </article>\n{cards_html}\n          <article class="blog-card" id="article-online-mba">'

if target in content:
    content = content.replace(target, replacement, 1)
    with open("blogs/index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully added 6 Priority 3 city cards to blogs/index.html!")
else:
    print("Target anchor not found in blogs/index.html")
