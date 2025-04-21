# 425. aiohttp ClientSession
#
# aiohttp.ClientSession is an async HTTP client. async with session.get as resp. Always
# close the session. httpx.AsyncClient is the other popular choice.
#
# Run: python 425_aiohttp_get/main.py

import asyncio
import aiohttp
async def main():
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get("https://example.com") as resp:
            return resp.status
try:
    print(asyncio.run(main()))
except Exception as e:
    print(type(e).__name__)
