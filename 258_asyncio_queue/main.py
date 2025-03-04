# 258. asyncio.Queue
#
# asyncio.Queue is the async FIFO. put and get are awaitable. join waits until all joined
# tasks call task_done. Use it between producers and consumers.
#
# Run: python 258_asyncio_queue/main.py

import asyncio
async def main():
    q = asyncio.Queue()
    await q.put("a")
    return await q.get()
print(asyncio.run(main()))
