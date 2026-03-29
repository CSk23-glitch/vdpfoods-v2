import requests
import os

def debug_endpoint(endpoint):
    url = f"http://127.0.0.1:8005{endpoint}"
    print(f"\n--- Debugging {url} ---")
    try:
        r = requests.get(url, timeout=30) # Longer timeout
        print(f"Status: {r.status_code}")
        if r.status_code == 500:
            filename = f"error_{endpoint.replace('/', '_')}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(r.text)
            print(f"500 Error details saved to {filename}")
        else:
            print(f"Response: {str(r.json())[:200]}")
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    debug_endpoint("/api/pages/")
    debug_endpoint("/api/stories/")
