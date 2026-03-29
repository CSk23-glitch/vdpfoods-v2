import os
from pymongo import MongoClient

def search_user():
    uri = 'mongodb+srv://videepthafoods:1ZDiNL2NGKcvKyp5@cluster0.v6jawym.mongodb.net/ecommerce_db?retryWrites=true&w=majority&appName=Cluster0'
    client = MongoClient(uri)
    email = 'ddevelop776@gmail.com'
    
    databases = client.list_database_names()
    print(f"Searching for {email} across ALL databases and collections...")
    
    found = False
    for db_name in databases:
        db = client[db_name]
        collections = db.list_collection_names()
        for coll_name in collections:
            count = db[coll_name].count_documents({'email': email})
            if count > 0:
                for u in db[coll_name].find({'email': email}):
                    print("-" * 50)
                    print(f"DATABASE: {db_name}")
                    print(f"COLLECTION: {coll_name}")
                    print(f"DOCUMENT ID: {u.get('_id')} (Type: {type(u.get('_id'))})")
                    print(f"DATA: {u}")
                    found = True
    
    if not found:
        print(f"User {email} not found anywhere in the cluster.")

if __name__ == "__main__":
    search_user()
