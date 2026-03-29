import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Page

PAGE_ID = '699c432702f5d2dbdb91551d'
p = Page.objects.get(id=PAGE_ID)

print(f"Page Name: {p.name}")
print(f"Total Sections: {len(p.sections)}")

for i, s in enumerate(p.sections):
    blocks = s.get('blocks', [])
    print(f"Section {i} (ID: {s.get('id')}): {len(blocks)} blocks")
    for b in blocks:
        print(f"  Block Type: {b.get('type')}, ID: {b.get('id')}")
        content = b.get('content', {})
        for k, v in content.items():
            if isinstance(v, str) and len(v) > 500:
                print(f"    - Property '{k}' is VERY LARGE: {len(v)} chars")
            elif isinstance(v, (list, dict)):
                 v_str = json.dumps(v)
                 if len(v_str) > 500:
                     print(f"    - Property '{k}' (JSON) is LARGE: {len(v_str)} chars")
