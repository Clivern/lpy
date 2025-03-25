# 319. collections.abc
#
# Sequence, Mapping, Iterable, Callable are ABCs. isinstance(x, Mapping) is the right way
# to detect a dict-like. Subclassing them gets mixin methods.
#
# Run: python 319_collections_abc/main.py

from collections.abc import Mapping, Sequence, Iterable
print(isinstance({"a": 1}, Mapping))
print(isinstance([1], Sequence) and isinstance(range(3), Iterable))
