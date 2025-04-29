# 438. httpx status errors
#
# raise_for_status() raises HTTPStatusError. Response.has_redirect_location is a redirect.
# codes is a namespace of status numbers.
#
# Run: python 438_httpx_status/main.py

import httpx
print(httpx.codes.OK, httpx.codes.NOT_FOUND)
req = httpx.Request("GET", "https://example.com")
r = httpx.Response(404, request=req)
try:
    r.raise_for_status()
except httpx.HTTPStatusError as e:
    print(e.response.status_code)
