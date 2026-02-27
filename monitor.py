import requests
import sys
import os

SITES_TO_MONITOR = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org"
]

def check_sites(urls):
    failed_sites = []
    # This header tells the website "I am a real browser"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    for url in urls:
        try:
            # Added the headers=headers part here
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"✅ {url} is UP!")
            else:
                print(f"❌ {url} is DOWN! Status: {response.status_code}")
                failed_sites.append(f"{url} ({response.status_code})")
        except Exception as e:
            print(f"💥 Error connecting to {url}: {e}")
            failed_sites.append(f"{url} (Error)")
    
    if failed_sites:
        with open("failed_list.txt", "w") as f:
            f.write(", ".join(failed_sites))
        sys.exit(1)

if __name__ == "__main__":
    check_sites(SITES_TO_MONITOR)