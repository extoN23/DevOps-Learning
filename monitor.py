#!/usr/bin/env python3
import requests

def check_site(url):
    try:
        r = requests.get(url, timeout=5)
        print(f"Status for {url}: {r.status_code}")
    except:
        print(f"Error: {url} is unreachable!")

check_site("https://google.com")
check_site("https://this-is-a-fake-site-123456789.com")
