import os
import django
from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

def inspect_db():
    uri = settings.MONGODB_URI
    db_name = settings.MONGODB_DB
    
    client = MongoClient(uri)
    db = client[db_name]
    
    print(f"Connected to DB: {db_name}")
    collections = db.list_collection_names()
    print(f"Collections: {collections}")
    
    for coll_name in collections:
        count = db[coll_name].count_documents({})
        print(f" - {coll_name}: {count} documents")
        if count > 0:
            sample = db[coll_name].find_one()
            print(f"   Sample from {coll_name}: {sample}")

if __name__ == "__main__":
    inspect_db()
