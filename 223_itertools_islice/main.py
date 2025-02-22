# 223. itertools.islice
#
# islice(it, start, stop, step) slices an iterator you cannot subscript. It is the lazy
# equivalent of seq[start:stop:step].
#
# Run: python 223_itertools_islice/main.py

from itertools import islice, count
print(list(islice(count(), 5, 12, 2)))
print(list(islice("abcdef", 2, 5)))
