# Update Pune Meta with 154 characters
from data_priority2_pune import get_pune_meta, get_pune_faqs, get_pune_content, get_pune_toc_items

def get_pune_meta_fixed():
    meta = get_pune_meta()
    # 154 characters exactly ending with "Check eligibility."
    meta["meta_desc"] = "Compare top online MBA colleges in Pune for IT & manufacturing executives in 2027. Review UGC-DEB universities, semester fees & 0% EMIs. Check eligibility."
    return meta
