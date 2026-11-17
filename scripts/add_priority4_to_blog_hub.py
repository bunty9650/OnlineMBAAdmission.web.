# -*- coding: utf-8 -*-
"""
Add 10 Priority 4 City Blog Cards to blogs/index.html
"""

import re

p4_cards_html = """
          <!-- Priority 4 City Blog 1: Kanpur -->
          <article class="blog-card" id="article-online-mba-kanpur">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2fe; color:#0369a1;">Central UP Industrial Hub</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-kanpur">Online MBA Colleges in Kanpur: Fees &amp; Top Options 2027</a></h3>
              <p class="blog-card-excerpt">
                Definitive guide for defense PSU officers, leather exporters, and FMCG engineers across Panki &amp; Jajmau. Review UGC-DEB fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> 100% remote AI exams and cloud LMS eliminate crowded physical test centers of legacy correspondence programs.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-kanpur" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 2: Meerut -->
          <article class="blog-card" id="article-online-mba-meerut">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fce4ec; color:#c2185b;">Western UP Manufacturing</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-meerut">Online MBA Colleges in Meerut: Top Universities Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Tailored guide for sports goods exporters, publishing executives, and Partapur plant leads. Compare UGC-DEB universities &amp; RapidX mobility.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Earn a top NAAC A+/A++ Master's degree entirely online without commuting along Delhi-Meerut highway corridors.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-meerut" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 3: Agra -->
          <article class="blog-card" id="article-online-mba-agra">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fef3c7; color:#b45309;">Footwear Export &amp; Tourism</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-agra">Online MBA Colleges in Agra: Best Universities Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive guide for footwear export directors, luxury hospitality managers, and foundry engineers. Review semester fees &amp; zero-cost EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Study 24/7 on mobile LMS around rotating hotel shifts or export schedules with 100% home AI proctored exams.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-agra" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 4: Ludhiana -->
          <article class="blog-card" id="article-online-mba-ludhiana">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#ecfdf5; color:#047857;">Punjab Industrial Powerhouse</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-ludhiana">Online MBA Colleges in Ludhiana: Top Options &amp; Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Executive analysis for knitwear manufacturers, cycle plant leads, and family business scions. Compare UGC-DEB fees &amp; WES Canada PR validity.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Maximize Express Entry CRS points with WES Master's equivalency while continuing to run your manufacturing business.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-ludhiana" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 5: Jodhpur -->
          <article class="blog-card" id="article-online-mba-jodhpur">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fff3e0; color:#e65100;">Handicrafts &amp; Solar Hub</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-jodhpur">Online MBA Colleges in Jodhpur: Fees &amp; Universities 2027</a></h3>
              <p class="blog-card-excerpt">
                In-depth guide for handicraft exporters in Basni, Bhadla solar engineers, and banking leads. Review accredited fees, flexible LMS &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Secure Rajasthan State PSC (RPSC) and corporate promotion equivalence with zero requirement to visit outstation campuses.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-jodhpur" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 6: Surat -->
          <article class="blog-card" id="article-online-mba-surat">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#dbeafe; color:#1e40af;">Diamond Bourse &amp; Hazira</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-surat">Online MBA Colleges in Surat: Fees &amp; Top Options 2027</a></h3>
              <p class="blog-card-excerpt">
                Strategic guide for diamond traders at Surat Diamond Bourse, petrochemical leads in Hazira &amp; textile barons. Review verified fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Transition into global trade leadership, international finance, or heavy plant general management with 100% remote freedom.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-surat" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 7: Nagpur -->
          <article class="blog-card" id="article-online-mba-nagpur">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#e0f2f1; color:#00695c;">MIHAN SEZ &amp; Logistics</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-nagpur">Online MBA Colleges in Nagpur: Top Universities Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Essential guide for IT engineers at MIHAN (TCS, Infosys), aerospace technicians &amp; mining leads (WCL/MOIL). Compare fees &amp; remote exams.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Qualify for E4/E5 grade promotions in national PSUs and tech leadership roles in MIHAN without relocating to Mumbai.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-nagpur" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 8: Visakhapatnam -->
          <article class="blog-card" id="article-online-mba-visakhapatnam">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#ede9fe; color:#6d28d9;">Pharma City &amp; Maritime</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-visakhapatnam">Online MBA in Visakhapatnam: Top Universities Fees 2027</a></h3>
              <p class="blog-card-excerpt">
                Actionable guide for pharma leads in JNPC Parawada, steel engineers at RINL, naval veterans &amp; port operators. Review verified fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Secure full statutory degree equivalence under Gazette Regulation 22 for APPSC, central PSUs, and defense transitions.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-visakhapatnam" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 9: Coimbatore -->
          <article class="blog-card" id="article-online-mba-coimbatore">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#fee2e2; color:#b91c1c;">Kongu Engineering Capital</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-coimbatore">Online MBA Colleges in Coimbatore: Fees &amp; Options 2027</a></h3>
              <p class="blog-card-excerpt">
                Comprehensive guide for auto-component engineers, pump manufacturers, textile managers &amp; TIDEL Park tech leads. Compare fees &amp; 0% EMIs.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Upskill into Plant Operations Head or Technical Product Manager with AICTE-benchmarked digital business coursework.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-coimbatore" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>

          <!-- Priority 4 City Blog 10: Ranchi -->
          <article class="blog-card" id="article-online-mba-ranchi">
            <div class="blog-card-body">
              <div class="blog-meta">
                <span class="blog-badge" style="background:#f1f5f9; color:#334155;">Mineral &amp; PSU Capital</span>
                <span>&bull; 16 Min Read &bull; 2027 Guide</span>
              </div>
              <h3 class="blog-card-title"><a href="/blogs/online-mba-ranchi">Online MBA Colleges in Ranchi: Fees &amp; Universities 2027</a></h3>
              <p class="blog-card-excerpt">
                Authoritative guide for public sector executives at HEC, SAIL, CCL, CMPDI &amp; Mecon. Compare verified UGC-DEB fees &amp; PSU promotion criteria.
              </p>
              <div class="blog-highlight-box">
                <strong>Key Takeaway:</strong> Fulfill mandatory post-graduate qualification requirements for executive grade promotions while maintaining continuous service.
              </div>
            </div>
            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-ranchi" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>
"""

with open("blogs/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Locate the end of article-online-mba-bhopal
target = """            <div class="blog-card-footer">
              <span class="author-pill"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:-2px; margin-right:4px;"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg> Advisory Team</span>
              <a href="/blogs/online-mba-bhopal" class="read-more-btn">Read Full Guide &rarr;</a>
            </div>
          </article>"""

replacement = f"""{target}
{p4_cards_html}"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open("blogs/index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully added all 10 Priority 4 city cards to blogs/index.html!")
else:
    print("Target anchor not found in blogs/index.html")
