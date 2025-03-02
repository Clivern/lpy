# 248. bisect
#
# bisect keeps a list sorted. bisect_left finds an insertion point. insort inserts. Binary
# search over a sorted list without rolling your own.
#
# Run: python 248_bisect/main.py

import bisect
xs = [1, 3, 3, 7]
print(bisect.bisect_left(xs, 3), bisect.bisect_right(xs, 3))
bisect.insort(xs, 5)
print(xs)
