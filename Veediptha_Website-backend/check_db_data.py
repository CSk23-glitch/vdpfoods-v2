import os
import django
import json
from decimal import Decimal
from bson import ObjectId

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import *

models = [Page, Product, Category, Coupon, Theme, Story, Hero, Navigation, Policy, Order, Stock, Promotion]

def json_serial(obj):
    if isinstance(obj, (Decimal)):
        return float(obj)
    if isinstance(obj, ObjectId):
        return str(obj)
    return str(obj)

results = {}
for m in models:
    count = m.objects.count()
    sample = m.objects.first()
    results[m.__name__] = {
        'count': count,
        'has_data': count > 0,
        'sample_keys': list(sample.__dict__.keys()) if sample else []
    }

print(json.dumps(results, indent=2, default=json_serial))
