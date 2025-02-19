# 218. itertools.chain
#
# chain(*iters) flattens one level. chain.from_iterable chains an iterable of iterables
# without unpacking a huge argument list.
#
# Run: python 218_itertools_chain/main.py

from itertools import chain
print(list(chain([1, 2], "ab", (9,))))
print(list(chain.from_iterable([[1, 2], [3]])))
