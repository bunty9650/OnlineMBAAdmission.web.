import re

cards_html = """
          <!-- Priority 2 City Blog 1: Bangalore -->
          <article class="blog-card" id="article-online-mba-bangalore">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2fe; color:#0369a1;">Silicon Valley Hub</span>
                <span>&bull; 17 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-bangalore">Online MBA Colleges in Bangalore: Fees, Universities &amp; Admission 2027</a></h3>
              <p class="blog-card-excerpt">
                Authoritative guide for tech leads, software engineers, and managers in Electronic City, Whitefield, and ORR. Compare UGC-DEB fees, AI proctored exams, and no-cost EMI plans.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Transition from engineering and coding into Technical Product Management (TPM) and Director roles while avoiding Silk Board traffic and preserving full salary.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-bangalore" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 2 City Blog 2: Mumbai -->
          <article class="blog-card" id="article-online-mba-mumbai">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fef3c7; color:#b45309;">Financial Capital Hub</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-mumbai">Online MBA Colleges in Mumbai: Best Universities &amp; Fee Comparison 2027</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive guide for BFSI executives, financial analysts, and corporate managers across BKC, Nariman Point, and Lower Parel. Review verified UGC-DEB fees and 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> 100% online delivery with home AI-proctored exams eliminates daily local train rush-hour commute while qualifying for senior VP and leadership promotions.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-mumbai" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 2 City Blog 3: Pune -->
          <article class="blog-card" id="article-online-mba-pune">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#ecfdf5; color:#047857;">Auto &amp; IT Powerhouse</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-pune">Online MBA Colleges in Pune: Top Universities, Fees &amp; Admission 2027</a></h3>
              <p class="blog-card-excerpt">
                Strategic guide for IT professionals in Hinjawadi/Kharadi and manufacturing engineers in Chakan/Bhosari. Compare UGC-DEB universities, semester fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Escape shift rotations and plateaued tech salaries to become Plant Operations Head or IT Project Manager with a genuine Master's degree.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-pune" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 2 City Blog 4: Hyderabad -->
          <article class="blog-card" id="article-online-mba-hyderabad">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fce4ec; color:#c2185b;">Cyberabad &amp; Life Sciences</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-hyderabad">Online MBA Colleges in Hyderabad: Top Universities, Fees &amp; Admission 2027</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive guide for tech professionals in HITEC City and pharma leaders in Genome Valley. Compare top UGC-DEB universities, semester fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Advance into Technical Product Leadership or Global Pharma Supply Chain Management with 100% online weekend classes and home exams.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-hyderabad" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 2 City Blog 5: Chennai -->
          <article class="blog-card" id="article-online-mba-chennai">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2f1; color:#00695c;">Detroit of Asia &amp; SaaS Hub</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-chennai">Online MBA Colleges in Chennai: Top Universities, Fees &amp; Admission 2027</a></h3>
              <p class="blog-card-excerpt">
                In-depth guide for automotive engineers in Sriperumbudur/Oragadam and SaaS leads along OMR. Compare UGC-DEB universities, affordable fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Bridge the technical gap to become Plant General Manager or SaaS Director without traveling down congested GST Road or OMR highways.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-chennai" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 2 City Blog 6: Kolkata -->
          <article class="blog-card" id="article-online-mba-kolkata">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fff3e0; color:#e65100;">Commercial Gateway to East</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-kolkata">Online MBA Colleges in Kolkata: Fees, Universities &amp; Admission Guide 2027</a></h3>
              <p class="blog-card-excerpt">
                Practical guide for PSU officers, bank managers, and IT professionals in Salt Lake Sector V and New Town. Review UGC-DEB budget fees under ₹1 Lakh and direct admission.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Achieve mandatory Master's degree legal parity for PSU and banking promotions under the UGC 2020 Gazette while staying in Kolkata.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-kolkata" class="read-more-btn">Read Full Guide &rarr;</a>
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
    print("Successfully added 6 Priority 2 city cards to blogs/index.html!")
else:
    print("Target anchor not found in blogs/index.html")
