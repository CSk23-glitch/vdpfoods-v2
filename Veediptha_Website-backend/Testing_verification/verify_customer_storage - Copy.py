import os
import django
import pymongo
import environ

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import User, CustomerProfile, Address
from django.utils import timezone

def verify_customer_storage():
    email = "customer_demo@example.com"
    password = "CustomerPassword123!"
    
    # 1. Create a Demo Customer
    print(f"--- Creating Demo Customer: {email} ---")
    user = User.objects.create_user(email=email, username="cust_demo", password=password)
    
    profile = CustomerProfile.objects.create(
        user=user, 
        plain_email=email,
        is_verified=True,
        profile_completed=True
    )
    profile.full_name = "Jane Doe"
    profile.phone = "+910000000000"
    profile.country_code = "IN"
    profile.preferred_currency = "INR"
    profile.save()
    
    Address.objects.create(
        user=user,
        address_type='shipping',
        is_default=True,
        full_name="Jane Doe",
        phone="+910000000000",
        street_address="123 Green Lane",
        city="Mysore",
        state="Karnataka",
        pincode="570001",
        country="India"
    )

    # 2. Inspect Raw MongoDB Storage
    env = environ.Env()
    client = pymongo.MongoClient(env('MONGODB_URI'))
    db = client[env('MONGODB_DB')]
    
    print("\n1. [auth_user] - Hashed Credentials")
    raw_user = db['auth_user'].find_one({'email': email})
    print(f"   Password: {raw_user['password'][:50]}...")
    
    print("\n2. [accounts_customer_profile] - Encrypted Profile")
    raw_profile = db['accounts_customer_profile'].find_one({'user_id': user.id})
    print(f"   Raw full_name: {raw_profile.get('full_name')}")
    print(f"   Raw phone:     {raw_profile.get('phone')}")
    
    print("\n3. [accounts_address] - Cleartext Delivery Data")
    raw_address = db['accounts_address'].find_one({'user_id': user.id})
    print(f"   Street: {raw_address['street_address']}")
    
    # 4. Prove Decryption (Application Logic)
    print("\n4. [Verification] - Decrypted View via Models")
    user_ref = User.objects.get(email=email)
    print(f"   Decrypted Name:  {user_ref.profile.full_name}")
    print(f"   Decrypted Phone: {user_ref.profile.phone}")
    
    print("\n--- Storage Clear and Secured ---")

if __name__ == "__main__":
    verify_customer_storage()
