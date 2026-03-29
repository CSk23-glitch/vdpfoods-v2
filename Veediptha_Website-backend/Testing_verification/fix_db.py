import pymongo
import os
import django
import sys

# Set up Django (to get settings)
sys.path.append('d:/GoogeAntigravity/FreelanceProjectDirectory/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

def move_collections():
    uri = settings.MONGODB_URI
    client = pymongo.MongoClient(uri)
    
    source_db = client['ecommerce_test_db']
    target_db = client['ecommerce_db']
    
    collections_to_move = ['accounts_admin_profile', 'accounts_customer_profile']
    
    for coll_name in collections_to_move:
        print(f"Moving {coll_name} from ecommerce_test_db to ecommerce_db...")
        source_coll = source_db[coll_name]
        docs = list(source_coll.find({}))
        
        if docs:
            target_db[coll_name].insert_many(docs)
            print(f"Inserted {len(docs)} documents into ecommerce_db.{coll_name}")
            source_coll.drop()
            print(f"Dropped ecommerce_test_db.{coll_name}")
        else:
            print(f"No documents found in ecommerce_test_db.{coll_name}")

if __name__ == "__main__":
    move_collections()
