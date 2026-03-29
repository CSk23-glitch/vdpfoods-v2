import pymongo

uri = "mongodb+srv://videepthafoods:1ZDiNL2NGKcvKyp5@cluster0.v6jawym.mongodb.net/ecommerce_db?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(uri)

print(f"Scanning cluster...")
for db_name in client.list_database_names():
    db = client[db_name]
    for coll_name in db.list_collection_names():
        if "profile" in coll_name:
            count = db[coll_name].count_documents({})
            print(f"Database: {db_name} | Collection: {coll_name} | Count: {count}")
