import os
import pprint
from data_national_pillars import national_pillars_data
from update_pillars_data import content_map

for s, c in content_map.items():
    if s in national_pillars_data:
        national_pillars_data[s]["content"] = c

with open('scripts/data_national_pillars.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nData and Content Definitions for 5 New National Pillar Blog Guides\n"""\n\n')
    f.write("national_pillars_data = " + pprint.pformat(national_pillars_data, indent=4, width=120) + "\n")

print("scripts/data_national_pillars.py updated with full content!")
