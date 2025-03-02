# 253. concurrent.futures
#
# ThreadPoolExecutor runs callables in a pool. map preserves order. with shuts the pool
# down. ProcessPoolExecutor is the CPU twin; arguments must pickle.
#
# Run: python 253_concurrent/main.py

from concurrent.futures import ThreadPoolExecutor
def square(n):
    return n * n
with ThreadPoolExecutor(max_workers=3) as pool:
    print(list(pool.map(square, [1, 2, 3, 4])))
