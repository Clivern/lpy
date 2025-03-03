# 256. asyncio.gather
#
# gather runs several coroutines concurrently and returns their results in order. One
# exception can cancel the rest unless you set return_exceptions.
#
# Run: python 256_asyncio_gather/main.py

import asyncio
async def n(x):
    await asyncio.sleep(0)
    return x
async def main():
    return await asyncio.gather(n(1), n(2), n(3))
print(asyncio.run(main()))
