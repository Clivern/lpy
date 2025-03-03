# 255. asyncio hello
#
# async def defines a coroutine. await pauses until a future is ready. asyncio.run is the
# entry point. sleep(0) yields without waiting for the clock.
#
# Run: python 255_asyncio_hello/main.py

import asyncio
async def main():
    await asyncio.sleep(0)
    return "ok"
print(asyncio.run(main()))

async def twice():
    await asyncio.sleep(0)
    await asyncio.sleep(0)
    return "ok"

print(asyncio.run(twice()))
