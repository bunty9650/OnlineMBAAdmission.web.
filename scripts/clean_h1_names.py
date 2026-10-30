import glob
import re

subpages = glob.glob('university/*/*.html')
cleaned = 0

for f in subpages:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    h1_m = re.search(r'(<h1[^>]*>)(.*?)(</h1>)', c, re.DOTALL)
    if h1_m:
        h1_text = h1_m.group(2).strip()
        new_h1 = h1_text
        
        # Clean double names
        new_h1 = re.sub(r' - Dr\. Bhimrao Ambedkar University - Dr\. B\.R\. Ambedkar University \(2027\)', ' - Dr. B.R. Ambedkar University (2027)', new_h1)
        new_h1 = re.sub(r' - Vellore Institute of Technology - VIT Online \(2027\)', ' - VIT Online (2027)', new_h1)
        new_h1 = re.sub(r' - Pandit Deendayal Upadhyaya Shekhawati University - DDU Gorakhpur University \(2027\)', ' - DDU Gorakhpur University (2027)', new_h1)
        new_h1 = re.sub(r' - Chaudhary Charan Singh University - CCSU Meerut \(2027\)', ' - CCSU Meerut (2027)', new_h1)
        
        if new_h1 != h1_text:
            c = c[:h1_m.start(2)] + new_h1 + c[h1_m.end(2):]
            with open(f, 'w', encoding='utf-8') as fp:
                fp.write(c)
            cleaned += 1
            print(f"Cleaned {f}: {new_h1}")

print(f"Cleaned {cleaned} subpages.")
