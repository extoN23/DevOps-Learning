import requests
import sys

def check_site(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"✅ {url} is UP!")
        else:
            print(f"❌ {url} is DOWN! Status: {response.status_code}")
            sys.exit(1) # This tells GitHub Actions to trigger the failure alert!
    except Exception as e:
        print(f"💥 Error connecting to {url}: {e}")
        sys.exit(1) # This also triggers the alert if the site doesn't exist at all

# Test it with your fake URL
check_site("https://this-is-a-fake-site-123456789.com")