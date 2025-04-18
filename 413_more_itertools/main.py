# 413. more-itertools
#
# more_itertools extends itertools. chunked, collapse, unique_everseen, and first are the
# usual picks. It is the stdlib's missing pieces.
#
# Run: python 413_more_itertools/main.py

from more_itertools import chunked, first, unique_everseen
print(list(chunked([1, 2, 3, 4, 5], 2)))
print(first([], default=0))
print(list(unique_everseen("ABBA")))
