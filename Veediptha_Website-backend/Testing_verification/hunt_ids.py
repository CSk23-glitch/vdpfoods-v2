import pymongo

uri = "mongodb+srv://videepthafoods:1ZDiNL2NGKcvKyp5@cluster0.v6jawym.mongodb.net/ecommerce_db?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)

target_ids = ["58fbd1c7-b94a-4a6a-bff6-de43483f288d", "7d774c7d-b2af-4713-960a-f6c4ff6d959b"]

print(f"Hunting for IDs: {target_ids}")

for db_name in client.list_database_names():
    db = client[db_name]
    for coll_name in db.list_collection_names():
        coll = db[coll_name]
        # Search for any document with _id or id matching our target
        for tid in target_ids:
            # Try searching as string and as UUID (if possible)
            res = coll.find_one({"_id": tid})
            if not res:
                res = coll.find_one({"id": tid})
            
            if res:
                print(f"!!! FOUND {tid} in DB: {db_name} | Collection: {coll_name} !!!")
                print(f"Full doc: {res}")

print("Search complete.")
