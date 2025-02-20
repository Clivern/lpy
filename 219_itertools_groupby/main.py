# 219. itertools.groupby
#
# groupby clusters consecutive items that share a key. Sort first if you want all equal
# keys together. Each group is an iterator that is consumed as you go.
#
# Run: python 219_itertools_groupby/main.py

from itertools import groupby
rows = [("a", 1), ("a", 2), ("b", 3)]
for key, group in groupby(rows, key=lambda r: r[0]):
    print(key, list(group))
