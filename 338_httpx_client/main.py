# 338. httpx Client
#
# httpx.Client(base_url=..., headers=...) is the session. follow_redirects defaults to
# False, unlike requests. Read r.text and r.json the same way.
#
# Run: python 338_httpx_client/main.py

import httpx
with httpx.Client(headers={"User-Agent": "learn-python"}) as client:
    print(client.headers["user-agent"])
    req = client.build_request("GET", "https://example.com")
    print(req.method, req.url.host)
