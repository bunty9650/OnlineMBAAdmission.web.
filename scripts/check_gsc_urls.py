import os

raw_urls = """https://onlinembaadmission.com/blogs/ignou-online-mba-admission-2027
https://www.onlinembaadmission.com/blogs/online-mba-college-admission
https://www.onlinembaadmission.com/blogs/online-mba-university-admission
https://www.onlinembaadmission.com/universities/dsu
https://www.onlinembaadmission.com/university/dsu/mba-in-financial-management
https://www.onlinembaadmission.com/university/dsu/mba-in-it-and-systems-management
https://www.onlinembaadmission.com/university/dsu/mba-in-marketing-management
https://www.onlinembaadmission.com/university/chandigarh-university/mba-in-digital-marketing
https://www.onlinembaadmission.com/fees
https://www.onlinembaadmission.com/university/gla/mba-in-human-resource-management
https://www.onlinembaadmission.com/university/dsu/mba-in-human-resource-management
https://www.onlinembaadmission.com/universities/imi-kolkata
https://www.onlinembaadmission.com/university/jain-university/mba-in-human-resource-management-and-finance
https://www.onlinembaadmission.com/blogs/no-cost-emi-guide
https://www.onlinembaadmission.com/university/jain-university/mba-in-finance-and-marketing
https://www.onlinembaadmission.com/university/jain-university/mba-in-business-intelligence-and-analytics
https://www.onlinembaadmission.com/universities/dbau-online
https://www.onlinembaadmission.com/specializations/data-science
https://www.onlinembaadmission.com/universities
https://www.onlinembaadmission.com/blogs/best-online-mba
https://www.onlinembaadmission.com/university/gla/mba-in-marketing
https://www.onlinembaadmission.com/university/sikkim-manipal-university/mba-in-finance
https://www.onlinembaadmission.com/blogs/page-3
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-healthcare-management
https://www.onlinembaadmission.com/universities/sikkim-manipal-university
https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-marketing-management
https://www.onlinembaadmission.com/university/chandigarh-university/mba-in-hospital-management
https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-international-business
https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-operations-management
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-human-resource-management
https://www.onlinembaadmission.com/universities/imt-ghaziabad
https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-logistics-and-supply-chain-management
https://www.onlinembaadmission.com/university/arka-jain/mba-in-human-resource-management
https://www.onlinembaadmission.com/universities/nmims-online
https://www.onlinembaadmission.com/university/jain-university/mba-in-human-resource-management
https://www.onlinembaadmission.com/specializations/international-finance
https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-business-ai
https://www.onlinembaadmission.com/university/sikkim-manipal-university/mba-in-marketing
https://www.onlinembaadmission.com/university/jamia-hamdard/mba-in-human-resource-management
https://onlinembaadmission.com/university/jamia-hamdard/mba-in-marketing-management
https://www.onlinembaadmission.com/universities/uttaranchal-university
https://www.onlinembaadmission.com/universities/jamia-hamdard
https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-information-system-management
https://www.onlinembaadmission.com/blogs/best-online-mba-in-india
https://www.onlinembaadmission.com/university/dbau-online/mba-in-marketing
https://www.onlinembaadmission.com/university/sikkim-manipal-university/mba-in-healthcare
https://www.onlinembaadmission.com/blogs/online-vs-distance-mba
https://www.onlinembaadmission.com/specializations/retail-management
https://www.onlinembaadmission.com/university/jain-university/mba-in-human-resource-and-business-analytics
https://onlinembaadmission.com/university/jamia-hamdard/mba-in-human-resource-management
https://www.onlinembaadmission.com/universities/gla
https://www.onlinembaadmission.com/privacy
https://www.onlinembaadmission.com/university/jain-university/mba-in-ai-for-finance
https://www.onlinembaadmission.com/universities/ccsu
https://www.onlinembaadmission.com/universities/jain-university
https://www.onlinembaadmission.com/universities/manipal-jaipur
https://www.onlinembaadmission.com/blogs/best-online-mba-colleges
https://www.onlinembaadmission.com/specializations/business-analytics
https://www.onlinembaadmission.com/universities/parul
https://www.onlinembaadmission.com/universities/amity
https://www.onlinembaadmission.com/specializations/project-management
https://www.onlinembaadmission.com/specializations/cybersecurity-management
https://www.onlinembaadmission.com/universities/vit
https://www.onlinembaadmission.com/specializations/supply-chain-management
https://www.onlinembaadmission.com/university/chandigarh-university/mba-in-information-technology
https://onlinembaadmission.com/universities/dbau-online
https://www.onlinembaadmission.com/specializations/healthcare-management
https://www.onlinembaadmission.com/specializations/agribusiness-management
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-pharmaceutical-management
https://www.onlinembaadmission.com/specializations/e-commerce-management
https://www.onlinembaadmission.com/specializations/digital-marketing
https://onlinembaadmission.com/university/jamia-hamdard/mba-in-operations-management
https://onlinembaadmission.com/university-andhra-online
https://www.onlinembaadmission.com/university/ccsu/mba-in-information-technology
https://www.onlinembaadmission.com/blogs/direct-admission-without-cat
https://www.onlinembaadmission.com/specializations/human-resource-management
https://www.onlinembaadmission.com/universities/noida-international-university
https://www.onlinembaadmission.com/specializations/finance
https://www.onlinembaadmission.com/comparison
https://www.onlinembaadmission.com/university/chandigarh-university/mba-in-banking-and-insurance
https://www.onlinembaadmission.com/blogs/online-mba
https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-digital-marketing
https://onlinembaadmission.com/university-imi-kolkata-online
https://www.onlinembaadmission.com/blogs/online-mba-in-india
https://www.onlinembaadmission.com/admission
https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-international-business
https://onlinembaadmission.com/university-amity-online
https://onlinembaadmission.com/university-gla-online
https://onlinembaadmission.com/university-kj-somaiya-online
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-marketing
https://www.onlinembaadmission.com/about
https://www.onlinembaadmission.com/blogs/highest-paying-specializations
https://www.onlinembaadmission.com/university/ccsu/mba-in-finance
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-data-analytics
https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-human-resource-management
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-retail-management
https://www.onlinembaadmission.com/university/chandigarh-university/mba-in-disaster-management
https://www.onlinembaadmission.com/university/amity/mba-in-human-resource-management
https://www.onlinembaadmission.com/blogs/is-online-mba-valid-govt-jobs
https://www.onlinembaadmission.com/university/chandigarh-university/mba-in-human-resource-management
https://www.onlinembaadmission.com/university/parul/mba-in-healthcare-and-hospital
https://www.onlinembaadmission.com/universities/du-sol
https://www.onlinembaadmission.com/university/du-sol/mba-in-human-resource-management
https://www.onlinembaadmission.com/university/du-sol/mba-in-operations-management
https://onlinembaadmission.com/blogs/ignou-online-mba-admission-2026
https://www.onlinembaadmission.com/university/du-sol/mba-in-financial-management
https://www.onlinembaadmission.com/blogs/ugc-deb-approval-guide
https://www.onlinembaadmission.com/specializations/information-technology
https://www.onlinembaadmission.com/specializations/sustainability-and-esg-management
https://www.onlinembaadmission.com/university/ccsu/mba-in-human-resource-management
https://www.onlinembaadmission.com/blogs/best-online-mba-universities-in-india
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-international-business
https://www.onlinembaadmission.com/university/du-sol/mba-in-international-business
https://www.onlinembaadmission.com/university/noida-international-university/mba-in-operations-management
https://www.onlinembaadmission.com/specializations/marketing
https://www.onlinembaadmission.com/universities/arka-jain
https://www.onlinembaadmission.com/specializations/operations-management
https://www.onlinembaadmission.com/universities/chandigarh-university
https://www.onlinembaadmission.com/universities/symbiosis
https://www.onlinembaadmission.com/universities/kj-somaiya
https://www.onlinembaadmission.com/universities/andhra-university
https://www.onlinembaadmission.com/blogs/top-online-mba-colleges
https://www.onlinembaadmission.com/university/ccsu/mba-in-marketing
https://www.onlinembaadmission.com/university/manipal-jaipur/mba-in-project-management
https://www.onlinembaadmission.com/specializations/ai-for-business
https://www.onlinembaadmission.com/blogs/best-online-mba-university
https://www.onlinembaadmission.com/universities/galgotias-university
https://onlinembaadmission.com/university/jamia-hamdard/mba-in-logistics-and-supply-chain-management
https://onlinembaadmission.com/university-parul-online
https://www.onlinembaadmission.com/specializations/international-business
https://www.onlinembaadmission.com/specializations/fintech-and-financial-services
https://www.onlinembaadmission.com/specializations/general-management
https://www.onlinembaadmission.com/specializations/hospital-administration
https://onlinembaadmission.com/university/jamia-hamdard/mba-in-international-business
https://onlinembaadmission.com/university/jamia-hamdard/mba-in-business-ai
https://onlinembaadmission.com/universities
https://onlinembaadmission.com/university-ccsu-online
https://onlinembaadmission.com/university-imt-ghaziabad-online
https://www.onlinembaadmission.com/universities?q=%7Bsearch_term_string%7D
https://www.onlinembaadmission.com/specializations
https://www.onlinembaadmission.com/blogs/top-online-mba-colleges-in-india
https://onlinembaadmission.com/university-manipal-online"""

urls = [line.strip() for line in raw_urls.strip().split('\n') if line.strip()]
print(f"Total URLs in GSC report: {len(urls)}")

missing_on_disk = []
exists_on_disk = []

for u in urls:
    # normalize path
    path = u.replace("https://www.onlinembaadmission.com", "").replace("https://onlinembaadmission.com", "")
    if path.startswith("/"): path = path[1:]
    if "?" in path: path = path.split("?")[0]
    
    # check candidates
    cand1 = path + ".html"
    cand2 = os.path.join(path, "index.html")
    cand3 = path
    
    found = None
    if os.path.exists(cand1): found = cand1
    elif os.path.exists(cand2): found = cand2
    elif os.path.exists(cand3) and os.path.isfile(cand3): found = cand3
    
    if found:
        exists_on_disk.append((u, path, found))
    else:
        missing_on_disk.append((u, path))

print(f"\nURLs that ACTUALLY EXIST on disk: {len(exists_on_disk)}")
print(f"URLs that DO NOT exist on disk: {len(missing_on_disk)}")

print("\n--- MISSING ON DISK ---")
for u, p in missing_on_disk:
    print(f"  {u} -> path: '{p}'")
