import os
import django
from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

def compare_dbs():
    uri = settings.MONGODB_URI
    client = MongoClient(uri)
    
    for db_name in ['ecommerce_db', 'ecommerce_test_db']:
        db = client[db_name]
        print(f"\n--- DB: {db_name} ---")
        
        # Products
        prod_count = db['products'].count_documents({})
        print(f"Products: {prod_count}")
        if prod_count > 0:
            for p in db['products'].find().limit(2):
                print(f"  - Product: {p.get('name')} (ID: {p.get('_id')})")
        
        # Orders
        order_count = db['orders'].count_documents({})
        print(f"Orders: {order_count}")
        if order_count > 0:
            for o in db['orders'].find().limit(2):
                print(f"  - Order: {o.get('order_number')} (Total: {o.get('total_amount')})")

if __name__ == "__main__":
    compare_dbs()
