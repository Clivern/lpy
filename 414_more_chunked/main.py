# 414. more-itertools window
#
# windowed, pairwise, and padded cover sliding views. spy peeks without consuming.
# always_iterable wraps a scalar.
#
# Run: python 414_more_chunked/main.py

from more_itertools import windowed, pairwise
print(list(windowed([1, 2, 3, 4], 3)))
print(list(pairwise([1, 2, 3])))
