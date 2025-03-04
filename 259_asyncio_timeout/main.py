# 259. asyncio timeout
#
# asyncio.timeout (3.11) cancels work that runs too long. wait_for is the older wrapper.
# CancelledError is BaseException, not Exception.
#
# Run: python 259_asyncio_timeout/main.py

import asyncio
async def main():
    try:
        async with asyncio.timeout(0.01):
            await asyncio.sleep(0)
            return "ok"
    except TimeoutError:
        return "late"
print(asyncio.run(main()))
