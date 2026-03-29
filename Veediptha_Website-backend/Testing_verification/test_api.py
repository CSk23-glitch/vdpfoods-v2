import requests
from config import API_URL

def test_api():
    base_url = API_URL
    
    # We need a token. Let's use the one generated for ddevelop776@gmail.com
    # But since it's hard to get the exact JWT here without login flow, 
    # let's assume we can bypass or use a mock if we modify settings temporarily.
    # OR we can just check if headers work or if it's returning 401.
    
    print("Testing /products/ (Publicly available)...")
    try:
        r = requests.get(f"{base_url}/products/")
        print(f"Status: {r.status_code}")
        print(f"Data: {r.json()}")
    except Exception as e:
        print(f"Error: {e}")

    print("\nTesting /orders/ (Requires auth)...")
    # This will likely return 401/403 without a token, but let's see.
    try:
        r = requests.get(f"{base_url}/orders/")
        print(f"Status: {r.status_code}")
        print(f"Data: {r.json() if r.status_code == 200 else 'Unauthorized'}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
