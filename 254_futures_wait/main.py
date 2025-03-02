# 254. as_completed and wait
#
# submit returns a Future. as_completed yields futures as they finish. result() blocks and
# re-raises the worker's exception.
#
# Run: python 254_futures_wait/main.py

from concurrent.futures import ThreadPoolExecutor, as_completed
def work(n):
    return n * 10
with ThreadPoolExecutor(max_workers=2) as pool:
    futs = [pool.submit(work, n) for n in range(4)]
    print(sorted(f.result() for f in as_completed(futs)))
