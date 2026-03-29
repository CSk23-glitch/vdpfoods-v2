import os
import django
import sys
import pymongo

# Set up Django
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

def find_it():
    client = pymongo.MongoClient(settings.MONGODB_URI)
    print(f"Connecting to cluster...")
    
    dbs = client.list_database_names()
    print(f"Databases found: {dbs}")
    
    for db_name in dbs:
        db = client[db_name]
        cols = db.list_collection_names()
        if 'accounts_admin_profile' in cols:
            print(f"!!! FOUND 'accounts_admin_profile' in database: {db_name} !!!")
            print(f"Total docs in it: {db.accounts_admin_profile.count_documents({})}")
        if 'accounts_customer_profile' in cols:
            print(f"!!! FOUND 'accounts_customer_profile' in database: {db_name} !!!")

if __name__ == "__main__":
    find_it()
