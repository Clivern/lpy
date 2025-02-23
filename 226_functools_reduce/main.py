# 226. functools.reduce
#
# reduce(fn, it, start) folds a binary function over an iterable. sum, all, and any cover
# the common cases. reduce still shows up in data pipelines.
#
# Run: python 226_functools_reduce/main.py

from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3, 4], 0))
print(reduce(lambda a, b: a * b, range(1, 6), 1))
