# 170. any and all
#
# any(it) is True if some item is true. all(it) is True if every item is true. Empty any
# is False; empty all is True. Both short-circuit.
#
# Run: python 170_any_all/main.py

print(any([0, 0, 2]), all([1, 2, 3]), all([]), any([]))
print(all(n > 0 for n in [1, 2, 3]))
