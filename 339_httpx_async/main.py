# 339. httpx AsyncClient
#
# AsyncClient is the awaitable twin. Use it inside asyncio.run. Gather several requests to
# overlap DNS and TLS.
#
# Run: python 339_httpx_async/main.py

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
