import re

target_file = 'blogs/best-online-mba-universities-in-india.html'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

sub_section = """
        <h3>Global Transcript Attestation &amp; WES Degree Credential Verification</h3>
        <p>
          For ambitious working executives planning international mobility—such as Canadian Permanent Residency (Express Entry), US H-1B / EB-2 advanced degree petitions, or European corporate transfers—degree recognition across international credential assessment agencies is a pivotal decision criterion. A common misconception is that degrees earned through online delivery face administrative hurdles during overseas credential evaluations.
        </p>
        <p>
          Under established international credential assessment frameworks, accredited online MBA degrees awarded by Indian statutory universities holding NAAC A+, A++, or Category-1 autonomy status are recognized as full postgraduate Master’s degrees:
        </p>
        <ul style="margin: 16px 0; padding-left: 20px; line-height: 1.8;">
          <li><strong>World Education Services (WES) Canada &amp; USA:</strong> Evaluates UGC-entitled 2-year Online MBA degrees from NAAC-accredited statutory universities as equivalent to a North American 4-year Bachelor's plus a 1-to-2-year Master's Degree, yielding maximum Comprehensive Ranking System (CRS) points for Express Entry.</li>
          <li><strong>Digital National Academic Depository (NAD / DigiLocker):</strong> Entitled universities issue tamper-proof digital transcripts and degree certificates directly anchored to NAD and DigiLocker, enabling instant electronic verification by global background screening agencies like First Advantage, HireRight, and Sterling.</li>
          <li><strong>Association of Indian Universities (AIU) &amp; Commonwealth Recognition:</strong> Because the degree certificate issued by the university does not append restrictive delivery mode labels pursuant to UGC Gazette Regulation 22, it qualifies for Commonwealth university reciprocity and international doctoral (Ph.D./DBA) admissions.</li>
        </ul>
        <p>
          Ensure that your chosen university provides direct registrar-to-evaluator electronic transcript transmission (via Truecopy, Parchment, or official university registrar email) to streamline the overseas attestation lifecycle without requiring physical postal dispatches.
        </p>
"""

marker = "Review complete details in our <a href=\"/fees\">2027 Fee Structure Guide</a> and our <a href=\"/blogs/no-cost-emi-guide\">0% No-Cost EMI Walkthrough</a>.\n        </p>"

if marker in content:
    content = content.replace(marker, marker + "\n" + sub_section)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Enrichment successfully inserted into", target_file)
else:
    print("Marker not found!")
