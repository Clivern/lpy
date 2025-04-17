# 411. cachetools TTLCache
#
# TTLCache(maxsize, ttl) is an in-memory LRU with a time-to-live. @cached(cache) memoizes.
# Use Redis for a process-shared cache.
#
# Run: python 411_cachetools_ttl/main.py

from cachetools import TTLCache, cached
cache = TTLCache(maxsize=8, ttl=60)
@cached(cache)
def inc(n):
    inc.calls = getattr(inc, "calls", 0) + 1
    return n + 1
print(inc(1), inc(1), inc.calls)
