# 335. requests headers
#
# headers= sets request headers. r.headers is case-insensitive. A User-Agent is polite.
# Session keeps headers for many calls.
#
# Run: python 335_requests_headers/main.py

import requests
s = requests.Session()
s.headers.update({"User-Agent": "learn-python/0.1"})
print(s.headers["User-Agent"])
print("user-agent" in s.headers)
