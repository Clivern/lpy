# 225. functools.lru_cache
#
# @lru_cache(maxsize=n) memoizes a function. Arguments must be hashable. cache_info()
# shows hits. cache_clear() drops the table. Use for pure functions.
#
# Run: python 225_functools_lru/main.py

from functools import lru_cache
@lru_cache(maxsize=32)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(10), fib.cache_info().hits)
