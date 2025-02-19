# 217. itertools.count
#
# count(start, step) is an infinite range. islice cuts it down. cycle repeats an iterable.
# repeat(x, n) yields x n times.
#
# Run: python 217_itertools_count/main.py

from itertools import count, islice, cycle, repeat
print(list(islice(count(10, 2), 4)))
print(list(islice(cycle("ab"), 5)))
print(list(repeat("x", 3)))
