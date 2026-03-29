import requests
import json

def test_super_admin_login():
    url = "http://127.0.0.1:8005/api/accounts/login/"
    payload = {
        "email": "ddevelop776@gmail.com",
        "password": "admin123",
        "portal": "admin"
    }
    
    print(f"Testing Login for: {payload['email']}...")
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n[SUCCESS] Login Successful.")
            print(f"User ID: {data['user']['id']}")
            print(f"Username: {data['user']['username']}")
            print(f"Full Name (Decrypted): {data['profile'].get('full_name')}")
            
            # Check for tokens
            if 'access_token' in data:
                print("✓ Access Token Received")
        else:
            print(f"[FAILED] Error: {response.text}")
            
    except Exception as e:
        print(f"[ERROR] Connection Failed: {e}")

if __name__ == "__main__":
    test_super_admin_login()
