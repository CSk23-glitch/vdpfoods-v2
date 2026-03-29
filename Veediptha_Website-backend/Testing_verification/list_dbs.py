import os
import django
from pymongo import MongoClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

def list_all_dbs():
    uri = settings.MONGODB_URI
    client = MongoClient(uri)
    
    dbs = client.list_database_names()
    print(f"Databases in cluster: {dbs}")
    
    for db_name in dbs:
        db = client[db_name]
        colls = db.list_collection_names()
        print(f"DB: {db_name} -> Collections: {colls}")
        for c in colls:
            count = db[c].count_documents({})
            if count > 0:
                print(f"  - {c}: {count} docs")

if __name__ == "__main__":
    list_all_dbs()
