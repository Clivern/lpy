# 247. heapq
#
# heapq implements a min-heap on a list. heappush, heappop, nsmallest, and merge are the
# API. For a max-heap, negate the values.
#
# Run: python 247_heapq/main.py

import heapq
h = []
for n in [5, 1, 3]:
    heapq.heappush(h, n)
print(heapq.heappop(h), h)
print(heapq.nsmallest(2, [9, 1, 5, 3]))
