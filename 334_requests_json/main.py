# 334. requests JSON
#
# r.json() parses the body. It raises if the body is not JSON. Combine with
# raise_for_status. httpbin is a public echo; skip if it is down.
#
# Run: python 334_requests_json/main.py

import requests
try:
    r = requests.get("https://httpbin.org/json", timeout=5)
    r.raise_for_status()
    print("slideshow" in r.json() or "author" in str(r.json()))
except requests.RequestException as e:
    print(type(e).__name__)
