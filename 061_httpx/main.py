# 061. httpx
#
# Client, AsyncClient, and status errors.
#
# Run: python 061_httpx/main.py

# --- httpx get ---
import httpx
try:
    r = httpx.get("https://example.com", timeout=5.0)
    print(r.status_code, r.http_version)
except httpx.HTTPError as e:
    print(type(e).__name__)

# --- httpx client ---
import httpx
with httpx.Client(headers={"User-Agent": "learn-python"}) as client:
    print(client.headers["user-agent"])
    req = client.build_request("GET", "https://example.com")
    print(req.method, req.url.host)

# --- httpx async ---
import asyncio
import httpx
async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://example.com", timeout=5.0)
        return r.status_code
try:
    print(asyncio.run(main()))
except httpx.HTTPError as e:
    print(type(e).__name__)

# --- httpx status ---
import httpx
print(httpx.codes.OK, httpx.codes.NOT_FOUND)
req = httpx.Request("GET", "https://example.com")
r = httpx.Response(404, request=req)
try:
    r.raise_for_status()
except httpx.HTTPStatusError as e:
    print(e.response.status_code)
