import os
import django
from pymongo import MongoClient
from pathlib import Path
import environ

# Setup environ
env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def list_all_mongodb_info():
    uri = env('MONGODB_URI', default=None)
    if not uri:
        print("MONGODB_URI not found in .env")
        return

    client = MongoClient(uri)
    print("="*50)
    print("FULL MONGODB SERVER AUDIT")
    print("="*50)

    try:
        dbs = client.list_database_names()
        for db_name in dbs:
            if db_name in ['admin', 'local', 'config']: continue
            
            print(f"\n--- Database: {db_name} ---")
            db = client[db_name]
            collections = db.list_collection_names()
            for coll_name in collections:
                count = db[coll_name].count_documents({})
                print(f"  - Collection: {coll_name:20} | Documents: {count}")
                
                if count > 0 and coll_name in ['products', 'categories', 'stories', 'coupons']:
                    sample = db[coll_name].find_one()
                    name_key = 'name' if 'name' in sample else ('title' if 'title' in sample else 'code')
                    print(f"    Sample: {sample.get(name_key)}")

    except Exception as e:
        print(f"Error connecting or listing: {e}")

    print("\n" + "="*50)

if __name__ == "__main__":
    list_all_mongodb_info()
