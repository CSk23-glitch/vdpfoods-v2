import os
import django
from pymongo import MongoClient
import environ

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

env = environ.Env()
environ.Env.read_env('.env')
uri = env('MONGODB_URI')
client = MongoClient(uri)
db = client['ecommerce_db']

collections_to_revert = {
    'website_pages': 'pages',
    'website_categories': 'categories',
    'website_products': 'products',
    'website_coupons': 'coupons',
    'website_stories': 'stories',
    'website_heroes': 'heroes',
    'website_navigation': 'navigation',
    'website_policies': 'policies',
    'website_orders': 'orders',
    'website_promotions': 'promotions'
}

existing_colls = db.list_collection_names()
print("Existing collections before revert:")
for c in existing_colls:
    print(" -", c)

for old_col, new_col in collections_to_revert.items():
    if old_col in existing_colls:
        if new_col in existing_colls:
            print(f"Target collection {new_col} already exists. Dropping it first...")
            db[new_col].drop()
        print(f"Reverting {old_col} to {new_col}...")
        db[old_col].rename(new_col)
    else:
        print(f"Collection {old_col} not found, skipping.")

print("Revert complete!")
print("New collections:", db.list_collection_names())
