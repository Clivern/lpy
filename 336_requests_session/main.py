# 336. requests Session
#
# Session reuses TCP connections and cookies. mount() attaches adapters. Always close or
# use with Session(). Cookies persist on the session object.
#
# Run: python 336_requests_session/main.py

import requests
with requests.Session() as s:
    s.cookies.set("n", "1")
    print(s.cookies.get("n"))
    print(s.get("https://example.com", timeout=5).status_code if False else "lazy")
