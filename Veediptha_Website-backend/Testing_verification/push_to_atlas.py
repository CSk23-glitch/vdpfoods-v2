import pymongo

local_uri = "mongodb://localhost:27017/"
atlas_uri = "mongodb+srv://videepthafoods:1ZDiNL2NGKcvKyp5@cluster0.v6jawym.mongodb.net/ecommerce_db?retryWrites=true&w=majority&appName=Cluster0"

print("Connecting to local...")
local_client = pymongo.MongoClient(local_uri)
local_db = local_client['ecommerce_db']

print("Connecting to Atlas...")
atlas_client = pymongo.MongoClient(atlas_uri)
atlas_db = atlas_client['ecommerce_db']

collections_to_move = ['accounts_admin_profile', 'accounts_customer_profile']

for coll_name in collections_to_move:
    print(f"\nProcessing {coll_name}...")
    local_coll = local_db[coll_name]
    docs = list(local_coll.find({}))
    
    if docs:
        print(f"Found {len(docs)} documents locally. Pushing to Atlas...")
        # Clear Atlas collection first to avoid duplicates
        atlas_db[coll_name].delete_many({})
        atlas_db[coll_name].insert_many(docs)
        print(f"Successfully pushed to Atlas ecommerce_db.{coll_name}")
    else:
        print(f"No documents found in local {coll_name}.")

print("\nCleanup: Removing EncryptedProfile from Atlas (it should be split now)")
atlas_db.accounts_encryptedprofile.drop()
print("Dropped accounts_encryptedprofile from Atlas.")

print("\n--- DONE! Please refresh MongoDB Atlas now. ---")
