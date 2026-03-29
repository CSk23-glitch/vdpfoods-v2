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
from accounts.models import AdminProfile

def debug_db():
    print("--- Django Connection Debug ---")
    db_conn = connections['default']
    print(f"DATABASE NAME in settings: {db_conn.settings_dict['NAME']}")
    print(f"CLIENT HOST in settings: {db_conn.settings_dict['CLIENT']['host']}")
    
    first_admin = AdminProfile.objects.first()
    print(f"First Admin Object: {first_admin}")
    
    # Try to find exactly where this object came from
    if first_admin:
        # Check the collection name and database
        print(f"Model DB Table: {AdminProfile._meta.db_table}")
        
    print("\n--- Manual Pymongo Verification ---")
    uri = db_conn.settings_dict['CLIENT']['host']
    client = pymongo.MongoClient(uri)
    dbs = client.list_database_names()
    print(f"Available Databases: {dbs}")
    
    for dname in dbs:
        db = client[dname]
        cols = db.list_collection_names()
        if 'accounts_admin_profile' in cols:
            print(f"!!! FOUND in {dname} !!!")
            print(f"Document count: {db['accounts_admin_profile'].count_documents({})}")
        elif 'accounts_customer_profile' in cols:
             print(f"!!! FOUND in {dname} (customer only) !!!")

if __name__ == "__main__":
    debug_db()
