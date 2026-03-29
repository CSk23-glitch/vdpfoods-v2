import os
from pymongo import MongoClient
from pathlib import Path
import environ

# Setup environ
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def migrate_data_to_ecommerce_db():
    uri = env('MONGODB_URI', default=None)
    if not uri:
        print("MONGODB_URI not found in .env")
        return

    client = MongoClient(uri)
    source_db = client['trial1_auth_db']
    target_db = client['ecommerce_db']

    # Collections we want to move
    collections = [
        'products', 'categories', 'stories', 'coupons', 
        'heroes', 'navigation', 'policies', 'promotions',
        'accounts_adminprofile', 'accounts_customerprofile'
    ]

    print("="*50)
    print("MIGRATING DATA TO ECOMMERCE_DB")
    print("="*50)

    for coll_name in collections:
        print(f"\nProcessing: {coll_name}")
        source_coll = source_db[coll_name]
        target_coll = target_db[coll_name]
        
        docs = list(source_coll.find({}))
        if docs:
            print(f"Found {len(docs)} documents in source.")
            # Optional: Clear target first if you want a clean sync
            # target_coll.delete_many({})
            
            # Simple way to avoid duplicates if re-running: 
            # only insert if target is empty OR use update_one with upsert
            for doc in docs:
                target_coll.replace_one({'_id': doc['_id']}, doc, upsert=True)
            
            print(f"Successfully synced documents to ecommerce_db.{coll_name}")
        else:
            print(f"No documents found in source collection {coll_name}.")

    print("\n" + "="*50)
    print("MIGRATION COMPLETE")
    print("="*50)

if __name__ == "__main__":
    migrate_data_to_ecommerce_db()
