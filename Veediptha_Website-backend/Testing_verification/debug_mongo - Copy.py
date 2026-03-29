import os
import django
from pymongo import MongoClient
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def debug_connection():
    uri = settings.MONGODB_URI
    db_name = settings.MONGODB_DB
    print(f"DEBUG: URI={uri}")
    print(f"DEBUG: DB Name={db_name}")

    client = MongoClient(uri)
    db = client[db_name]
    
    print("\n--- RAW PYMONGO CHECK ---")
    collections = db.list_collection_names()
    print(f"Collections in {db_name}: {collections}")
    
    for coll in ['products', 'categories', 'stories', 'heroes', 'auth_user', 'accounts_admin_profile']:
        if coll in collections:
            count = db[coll].count_documents({})
            print(f"Raw '{coll}' count: {count}")
            if count > 0:
                sample = db[coll].find_one()
                print(f"  Sample ID: {sample.get('_id')} (Type: {type(sample.get('_id'))})")
        else:
            print(f"Raw '{coll}' collection not found!")

    print("\n--- DJANGO MODEL CHECK ---")
    from api.models import Product, Category, Story, Hero
    print(f"Product table: {Product._meta.db_table}")
    print(f"Product count (Django): {Product.objects.count()}")
    
    # Try raw SQL/Query if possible (though for MongoDB it's different)
    # Let's see if we can get the query
    print(f"Product Query: {Product.objects.all().query}")

if __name__ == "__main__":
    debug_connection()
