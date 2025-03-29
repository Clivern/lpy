# 332. requests GET
#
# requests.get(url) performs HTTP. raise_for_status() errors on 4xx/5xx. A timeout is
# required in production. This lesson talks to example.com if the network is up.
#
# Run: python 332_requests_get/main.py

import requests
try:
    r = requests.get("https://example.com", timeout=5)
    print(r.status_code, "text/html" in r.headers.get("content-type", ""))
except requests.RequestException as e:
    print(type(e).__name__)
