import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import User, AdminProfile
from api.models import Product, Category, Story, Hero

def verify_data():
    print("="*50)
    print("DJANGO DATA VERIFICATION")
    print("="*50)

    # 1. Check Users
    print("\n--- USERS ---")
    users = User.objects.all()
    print(f"Total Users: {users.count()}")
    for u in users:
        print(f"User: {u.email} | Staff: {u.is_staff} | Superuser: {u.is_superuser}")
        if u.email == 'ddevelop776@gmail.com':
            print(f"  VERIFIED: Admin user exists.")
            # Verify password if possible (only check if it has a hash)
            if u.password:
                print(f"  VERIFIED: Password hash is present.")
            else:
                print(f"  WARNING: Password hash is MISSING!")

    # 2. Check Profiles
    print("\n--- ADMIN PROFILES ---")
    profiles = AdminProfile.objects.all()
    print(f"Total Admin Profiles: {profiles.count()}")
    for p in profiles:
        print(f"Profile for: {p.user.email} | Type: {p.user_type}")

    # 3. Check Products & Content
    print("\n--- CONTENT ---")
    print(f"Products Count: {Product.objects.count()}")
    print(f"Categories Count: {Category.objects.count()}")
    print(f"Stories Count: {Story.objects.count()}")
    print(f"Heroes Count: {Hero.objects.count()}")

    if Product.objects.count() == 0:
        print("\nDIAGNOSTIC: Product count is 0. Attempting to fetch first raw document...")
        from pymongo import MongoClient
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_DB]
        raw_doc = db['products'].find_one()
        if raw_doc:
            print(f"Found raw doc in 'products': {raw_doc.get('name')} (_id: {raw_doc.get('_id')})")
            print("Possible reason: Django-MongoDB engine ID mismatch or query issues.")

if __name__ == "__main__":
    verify_data()
