# 412. cachetools LRUCache
#
# LRUCache evicts the least recently used item. __getitem__ and __setitem__ are the
# mapping API. maxsize is the bound.
#
# Run: python 412_cachetools_lru/main.py

from cachetools import LRUCache
c = LRUCache(maxsize=2)
c["a"] = 1
c["b"] = 2
c["c"] = 3
print("a" in c, list(c))
