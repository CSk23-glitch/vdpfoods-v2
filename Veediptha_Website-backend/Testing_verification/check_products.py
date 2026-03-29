import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Product
from api.serializers import ProductSerializer

products = Product.objects.all()
print(f"Total products in DB: {products.count()}")

for p in products:
    print(f"- {p.name} (Active: {p.is_active})")

# Simulate API response
serializer = ProductSerializer(products, many=True)
print("\nSerializer Output (Sample):")
if products.count() > 0:
    print(json.dumps(serializer.data[0], indent=2))
else:
    print("No products to serialize")
