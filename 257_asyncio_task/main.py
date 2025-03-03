# 257. asyncio.create_task
#
# create_task schedules a coroutine on the running loop. Keep a reference. TaskGroup
# (3.11+) cancels siblings when one fails.
#
# Run: python 257_asyncio_task/main.py

import asyncio
async def main():
    t = asyncio.create_task(asyncio.sleep(0, result=7))
    return await t
print(asyncio.run(main()))
