import requests
import sys

def test_api(base_url="http://127.0.0.1:8005"):
    print(f"Testing API at {base_url}")
    
    endpoints = [
        "/api/products/",
        "/api/categories/",
        "/api/stories/",
        "/api/pages/",
        "/api/hero/",
        "/api/navigation/",
        "/api/theme/",
        "/api/policies/",
    ]
    
    all_ok = True
    for ep in endpoints:
        url = f"{base_url}{ep}"
        print(f"\nTesting {url}...")
        try:
            r = requests.get(url, timeout=5)
            print(f"Status: {r.status_code}")
            if r.status_code == 200:
                data = r.json()
                if isinstance(data, list):
                    print(f"SUCCESS: Received {len(data)} items.")
                else:
                    print(f"SUCCESS: Received object: {list(data.keys())}")
            else:
                print(f"ERROR: {r.status_code}")
                print(f"Content: {r.text[:500]}")
                all_ok = False
        except Exception as e:
            print(f"FAILED: {e}")
            all_ok = False
            
    if all_ok:
        print("\nALL PUBLIC ENDPOINTS ARE WORKING!")
    else:
        print("\nSOME ENDPOINTS FAILED.")
        sys.exit(1)

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8005"
    test_api(url)
