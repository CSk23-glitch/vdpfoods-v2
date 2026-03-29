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

collections_to_rename = {
    'pages': 'website_pages',
    'categories': 'website_categories',
    'products': 'website_products',
    'coupons': 'website_coupons',
    'stories': 'website_stories',
    'heroes': 'website_heroes',
    'navigation': 'website_navigation',
    'policies': 'website_policies',
    'orders': 'website_orders',
    'promotions': 'website_promotions'
}

existing_colls = db.list_collection_names()
print("Existing collections before rename:")
for c in existing_colls:
    print(" -", c)

for old_col, new_col in collections_to_rename.items():
    if old_col in existing_colls:
        if new_col in existing_colls:
            print(f"Target collection {new_col} already exists. Dropping it first...")
            db[new_col].drop()
        print(f"Renaming {old_col} to {new_col}...")
        db[old_col].rename(new_col)
    else:
        print(f"Collection {old_col} not found, skipping.")

print("Rename complete!")
print("New collections:", db.list_collection_names())
