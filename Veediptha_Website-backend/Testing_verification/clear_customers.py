import os
import django
import pymongo
import environ

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from accounts.models import User, CustomerProfile, Address
from django.utils import timezone

def clear_customers():
    print("--- Wiping All Customer Data ---")
    
    # We delete anything that is not staff/superuser
    customers = User.objects.filter(is_staff=False, is_superuser=False)
    count = customers.count()
    customers.delete()
    
    # To be absolutely sure, clean up any dangling profiles or addresses
    # MongoDB direct cleanup for dangling records
    env = environ.Env()
    client = pymongo.MongoClient(env('MONGODB_URI'))
    db = client[env('MONGODB_DB')]
    
    db['accounts_customer_profile'].delete_many({})
    print(f"Deleted {count} customer user records and dropped customer profiles collection.")
    
    # Also clear OTPs and pending signups just in case
    db['accounts_otpstore'].delete_many({})
    db['accounts_pendingsignup'].delete_many({})
    
    print("--- Customer DB Cleaned ---")

if __name__ == "__main__":
    clear_customers()
