import glob
import os
import re

UNIV_NAMES = {
    'alliance-university': 'Alliance University',
    'amity': 'Amity University Online',
    'andhra-university': 'Andhra University',
    'arka-jain': 'Arka Jain University',
    'bharati-vidyapeeth': 'Bharati Vidyapeeth',
    'ccsu': 'CCSU Meerut',
    'chandigarh-university': 'Chandigarh University',
    'dbau-online': 'Dr. B.R. Ambedkar University',
    'ddu': 'DDU Gorakhpur University',
    'dpu-online': 'DPU Online',
    'dsu': 'Dayananda Sagar University',
    'du-sol': 'Delhi University (DU SOL)',
    'galgotias-university': 'Galgotias University',
    'gla': 'GLA University Online',
    'ignou': 'IGNOU',
    'jain-university': 'Jain University Online',
    'jamia-hamdard': 'Jamia Hamdard',
    'manipal-jaipur': 'Manipal University Jaipur',
    'nmims-online': 'NMIMS Online (CDOE)',
    'noida-international-university': 'Noida International University',
    'parul': 'Parul University Online',
    'shoolini-university': 'Shoolini University',
    'sikkim-manipal-university': 'Sikkim Manipal University',
    'uttaranchal-university': 'Uttaranchal University',
    'vit': 'VIT Online'
}

subpages = glob.glob('university/*/*.html')
modified_count = 0

for f in subpages:
    univ_dir = os.path.basename(os.path.dirname(f))
    univ_brand = UNIV_NAMES.get(univ_dir, univ_dir.replace('-', ' ').title())
    
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        
    h1_match = re.search(r'(<h1[^>]*>)(.*?)(</h1>)', content, re.DOTALL)
    if h1_match:
        open_tag = h1_match.group(1)
        current_h1 = h1_match.group(2).strip()
        close_tag = h1_match.group(3)
        
        # Check if university brand or recognizable acronym is already in H1
        simple_univ = univ_dir.replace('-', ' ').lower()
        acronym = "".join([w[0] for w in univ_dir.split('-')]).lower()
        
        # Check if already branded
        is_branded = (
            univ_brand.lower() in current_h1.lower() or 
            simple_univ in current_h1.lower() or
            (len(acronym) >= 3 and acronym in current_h1.lower()) or
            "amity" in current_h1.lower() or
            "jain" in current_h1.lower() or
            "dpu" in current_h1.lower() or
            "nmims" in current_h1.lower() or
            "manipal" in current_h1.lower() or
            "galgotias" in current_h1.lower() or
            "smu" in current_h1.lower() or
            "uttaranchal" in current_h1.lower() or
            "bharati" in current_h1.lower() or
            "alliance" in current_h1.lower()
        )
        
        if not is_branded:
            # Clean up current H1
            clean_h1 = re.sub(r'\s*2027\s*', '', current_h1).strip()
            new_h1 = f"{clean_h1} - {univ_brand} (2027)"
            
            # Replace H1 in content
            content = content[:h1_match.start(2)] + new_h1 + content[h1_match.end(2):]
            
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(content)
            modified_count += 1
            print(f"Updated H1 in {f}:\n  Old: '{current_h1}'\n  New: '{new_h1}'")

print(f"\nTotal subpages with H1 branded & fixed: {modified_count}")
