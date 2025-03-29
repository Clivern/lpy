# 337. httpx GET
#
# httpx is a requests-like client with HTTP/2 and async. Client is a context manager.
# timeout= is a Timeout object or a float.
#
# Run: python 337_httpx_get/main.py

import httpx
try:
    r = httpx.get("https://example.com", timeout=5.0)
    print(r.status_code, r.http_version)
except httpx.HTTPError as e:
    print(type(e).__name__)
