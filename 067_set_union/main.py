# 067. set.union and intersection
#
# union, intersection, difference, and symmetric_difference take any iterable and return a
# new set. Operators | & - ^ require a set (or frozenset) on both sides.
#
# Run: python 067_set_union/main.py

a = {1, 2, 3}
print(a.union([3, 4]), a.intersection([2, 9]))
print(a.difference([1, 9]), a.symmetric_difference([3, 4]))
print(a | {0}, a)
print({1, 2}.union([2, 3]))
