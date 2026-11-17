import re
import build_national_pillars as bnp
from priority2_expansion import (
    get_shared_curriculum_blueprint,
    get_deep_university_profiles,
    get_financial_and_scholarship_guide
)
import national_pillars_expanded as npe

curriculum = get_shared_curriculum_blueprint()
deep_profiles = get_deep_university_profiles()
financial = get_financial_and_scholarship_guide("National Advisory")

slugs = [
    "is-online-mba-valid-in-india",
    "government-online-distance-mba-universities",
    "online-mba-after-bcom",
    "online-mba-finance-vs-marketing-vs-hr",
    "online-mba-vs-regular-mba"
]

print("=== CHECKING PROJECTED WORD COUNTS ===")
for slug in slugs:
    base = bnp.get_content_for_pillar(slug)
    extra = ""
    if slug == "is-online-mba-valid-in-india":
        extra = npe.get_wes_and_international_equivalence() + npe.get_psu_promotion_and_dopt_rules()
    elif slug == "government-online-distance-mba-universities":
        extra = npe.get_psu_promotion_and_dopt_rules() + npe.get_wes_and_international_equivalence()
    elif slug == "online-mba-after-bcom":
        extra = npe.get_bcom_career_transition_matrix() + npe.get_wes_and_international_equivalence()
    elif slug == "online-mba-finance-vs-marketing-vs-hr":
        extra = npe.get_specialization_curriculum_comparison() + npe.get_bcom_career_transition_matrix()
    elif slug == "online-mba-vs-regular-mba":
        extra = npe.get_ten_year_wealth_projection() + npe.get_wes_and_international_equivalence()
        
    combined = base + "\n" + deep_profiles + "\n" + curriculum + "\n" + financial + "\n" + extra
    text = re.sub(r'<[^>]+>', ' ', combined)
    words = re.findall(r'\b[A-Za-z0-9\u0900-\u097F₹%–-]+\b', text)
    print(f"{slug:45} -> {len(words)} words (Pass: {len(words) >= 3000})")
