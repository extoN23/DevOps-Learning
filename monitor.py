import requests
import sys

def check_site(url):
    try:
        # Use a real URL here
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"✅ {url} is UP!")
        else:
            print(f"❌ {url} is DOWN! Status: {response.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"💥 Error connecting to {url}: {e}")
        sys.exit(1)

# Monitor a real site now
check_site("https://www.google.com")