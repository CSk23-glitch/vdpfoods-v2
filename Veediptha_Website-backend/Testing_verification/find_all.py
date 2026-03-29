import os
import django
import sys
import pymongo

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings
from django.db import connections

def find_all_collections():
    db_conn = connections['default']
    uri = db_conn.settings_dict['CLIENT']['host']
    client = pymongo.MongoClient(uri)
    
    print(f"Cluster Databases: {client.list_database_names()}")
    
    for db_name in client.list_database_names():
        db = client[db_name]
        print(f"\nScanning Database: {db_name}")
        cols = sorted(db.list_collection_names())
        for c in cols:
            count = db[c].count_documents({})
            print(f"  - {c} ({count} docs)")

if __name__ == "__main__":
    find_all_collections()
