import requests

def debug_500(url, method='GET', data=None):
    print(f"\nTesting {method} {url}...")
    try:
        if method == 'GET':
            response = requests.get(url)
        else:
            response = requests.post(url, json=data)
        
        print(f"Status Code: {response.status_code}")
        if response.status_code == 500:
            print("ERROR: Received 500 Internal Server Error.")
            # Save the HTML to a file to inspect the traceback
            filename = f"error_{url.split('/')[-2]}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Traceback HTML saved to {filename}")
        else:
            print(f"Response: {response.text[:200]}...")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    BASE_URL = "http://127.0.0.1:8005"
    debug_500(f"{BASE_URL}/api/pages/")
    debug_500(f"{BASE_URL}/api/stories/")
    debug_500(f"{BASE_URL}/api/accounts/login/", method='POST', data={
        "email": "ddevelop776@gmail.com",
        "password": "abcdefgh"
    })
