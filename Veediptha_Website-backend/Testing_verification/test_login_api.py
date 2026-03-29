import requests
import json

URL = "http://127.0.0.1:8005/api/accounts/login/"
DATA = {
    "email": "customer@example.com",
    "password": "customer123",
    "portal": "website"
}

print(f"Testing login at {URL}")
print(f"Payload: {DATA}")

try:
    response = requests.post(URL, json=DATA)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
    try:
        print(f"Raw Response: {response.text[:500]}")
    except:
        pass
