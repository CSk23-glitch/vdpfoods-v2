import os
import django
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

def fix_profile_links():
    uri = settings.MONGODB_URI
    db_name = settings.MONGODB_DB
    client = MongoClient(uri)
    db = client[db_name]

    print(f"Connecting to database: {db_name}")

    # 1. Get all users and their IDs
    users_by_email = {}
    for user in db['auth_user'].find():
        email = user.get('email')
        if email:
            users_by_email[email] = user.get('_id')
            print(f"User: {email} -> {user.get('_id')}")

    # 2. Update Admin Profiles
    print("\n--- UPDATING ADMIN PROFILES ---")
    for profile in db['accounts_admin_profile'].find():
        email = profile.get('plain_email')
        if email in users_by_email:
            new_user_id = users_by_email[email]
            if profile.get('user_id') != new_user_id:
                db['accounts_admin_profile'].update_one(
                    {'_id': profile['_id']},
                    {'$set': {'user_id': new_user_id}}
                )
                print(f"Updated Profile for {email}: user_id set to {new_user_id}")
            else:
                print(f"Profile for {email} already correctly linked.")
        else:
            print(f"WARNING: No user found for admin profile {email}")

    # 3. Update Customer Profiles
    print("\n--- UPDATING CUSTOMER PROFILES ---")
    for profile in db['accounts_customer_profile'].find():
        email = profile.get('plain_email')
        if email in users_by_email:
            new_user_id = users_by_email[email]
            if profile.get('user_id') != new_user_id:
                db['accounts_customer_profile'].update_one(
                    {'_id': profile['_id']},
                    {'$set': {'user_id': new_user_id}}
                )
                print(f"Updated Profile for {email}: user_id set to {new_user_id}")
            else:
                print(f"Profile for {email} already correctly linked.")
        else:
            print(f"WARNING: No user found for customer profile {email}")

    # 4. Cleanup Refresh Tokens (optional but helpful as they store user_id as string sometimes)
    print("\n--- CLEANING UP REFRESH TOKENS ---")
    # We might want to just delete them to force re-login if they are inconsistent
    result = db['accounts_refreshtoken'].delete_many({})
    print(f"Deleted {result.deleted_count} potentially stale refresh tokens.")

if __name__ == "__main__":
    fix_profile_links()
