import os
import django
import pymongo
import environ

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import AdminProfile, CustomerProfile, User
from django.conf import settings

env = environ.Env()
client = pymongo.MongoClient(env('MONGODB_URI'))
db = client[env('MONGODB_DB')]

print("=== RAW DATA ENCRYPTION CHECK ===")

def check_collection(name):
    print(f"\nCollection: {name}")
    doc = db[name].find_one({}, {'full_name': 1, 'phone': 1, '_full_name': 1, '_phone': 1, 'plain_email': 1})
    if doc:
        print(f"Sample ID: {doc['_id']}")
        # In Django models, actual encrypted data is usually in _full_name or similar if using properties
        fname = doc.get('full_name') or doc.get('_full_name')
        fphone = doc.get('phone') or doc.get('_phone')
        
        print(f"Full Name (Raw): {str(fname)[:50] if fname else 'N/A'}...")
        print(f"Phone (Raw): {str(fphone)[:50] if fphone else 'N/A'}...")
        
        # Check if it looks encrypted
        raw_val = str(fname or fphone or "")
        if len(raw_val) > 20 and ':' in raw_val:
             print("RESULT: Data appears to be ENCRYPTED (IV:ciphertext format)")
        else:
             print("RESULT: Data appears to be PLAIN TEXT or missing")
    else:
        print("No documents found.")

check_collection('accounts_admin_profile')
check_collection('accounts_customer_profile')

print("\n=== CREATE TEST USER & VERIFY ENCRYPTION ===")
TEST_EMAIL = "test_encrypt@example.com"
User.objects.filter(email=TEST_EMAIL).delete()
test_user = User.objects.create_user(email=TEST_EMAIL, username="testencrypt", password="testpassword123")
test_profile = CustomerProfile.objects.create(user=test_user, full_name="Test User Encryption", phone="+1234567890")

print(f"Created test user: {TEST_EMAIL}")
print(f"Set Full Name: {test_profile.full_name}")

# Check raw mongo for the NEW user
doc = db['accounts_customer_profile'].find_one({'user_id': test_user.id})
if doc:
    print(f"Raw doc keys: {list(doc.keys())}")
    # The db_column is 'full_name', so it should be 'full_name' in Mongo
    raw_val = doc.get('full_name')
    print(f"Raw 'full_name' in DB: {raw_val}")
    
    raw_val_str = str(raw_val)
    if raw_val and len(raw_val_str) > 20 and (':' in raw_val_str or raw_val_str.startswith('v2$')):
        print("RESULT: NEW Data is ENCRYPTED correctly in DB.")
        
        # Verify decryption
        fetched_profile = CustomerProfile.objects.get(user=test_user)
        if fetched_profile.full_name == "Test User Encryption":
            print("RESULT: Decryption SUCCESSFUL for new user.")
        else:
            print(f"RESULT: Decryption FAILED. Got: '{fetched_profile.full_name}'")
    else:
        print(f"RESULT: NEW Data detection FAILED or PLAIN TEXT. Raw was: {raw_val_str[:20]}...")


else:
    print("Failed to find test profile in raw MongoDB.")

# Cleanup
test_user.delete()
print("Test user cleaned up.")


