import requests
import sys

# Define your "Watchlist" here
SITES_TO_MONITOR = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org"
]

def check_sites(urls):
    failed_sites = []
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✅ {url} is UP!")
            else:
                print(f"❌ {url} is DOWN! Status: {response.status_code}")
                failed_sites.append(url)
        except Exception as e:
            print(f"💥 Error connecting to {url}: {e}")
            failed_sites.append(url)
    
    # After checking all sites, see if we need to trigger the alarm
    if failed_sites:
        print(f"\n🚨 Failure detected on: {', '.join(failed_sites)}")
        sys.exit(1)
    else:
        print("\n🟢 All sites are healthy!")

if __name__ == "__main__":
    check_sites(SITES_TO_MONITOR)