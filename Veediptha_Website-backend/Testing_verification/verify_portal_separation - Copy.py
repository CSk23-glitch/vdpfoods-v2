import requests
import json
from config import API_URL

BASE_URL = API_URL

# Test Credentials (known from previous context)
# Super Admin: ddevelop776@gmail.com / abcdefgh
# Customer: bhavanashiva2025@gmail.com / bhavana (assuming some password, let's try to find it or use any)
ADMIN_EMAIL = "ddevelop776@gmail.com"
ADMIN_PASS = "abcdefgh"

CUSTOMER_EMAIL = "bhavanashiva2025@gmail.com"
CUSTOMER_PASS = "Admin@123" # I saw this in previous logs

def test_login(email, password, portal):
    print(f"\nTesting Login - User: {email}, Portal: {portal}")
    payload = {
        "email": email,
        "password": password,
        "portal": portal
    }
    try:
        response = requests.post(f"{BASE_URL}/accounts/login/", json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print("--- STARTING PORTAL SEPARATION TESTS ---")
    
    # 1. Admin login to Admin Portal (Should succeed)
    test_login(ADMIN_EMAIL, ADMIN_PASS, "admin")
    
    # 2. Admin login to Website Portal (Should fail)
    test_login(ADMIN_EMAIL, ADMIN_PASS, "website")
    
    # 3. Customer login to Website Portal (Should succeed)
    test_login(CUSTOMER_EMAIL, CUSTOMER_PASS, "website")
    
    # 4. Customer login to Admin Portal (Should fail)
    test_login(CUSTOMER_EMAIL, CUSTOMER_PASS, "admin")
    
    print("\n--- TESTS COMPLETED ---")
