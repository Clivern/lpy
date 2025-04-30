# 062. Sets
#
# set is an unordered collection of unique hashable items. add, update, remove, discard,
# pop, and clear mutate. | & - ^ and the named methods are union, intersection,
# difference, symmetric difference. Operators need a set on both sides; methods take any
# iterable. <= is subset, isdisjoint is empty intersection.
#
# Run: python 062_sets/main.py

a = {1, 2, 3, 2}
b = {3, 4}
print(a, a | b, a & b, a - b, a ^ b)
print(2 in a)

s = {1, 2}
s.add(3)
s.update([4, 5], {5})
s.discard(9)
s.remove(1)
print(s)
print(s.union([5, 6]), s.intersection([2, 9]))

acc = {1, 2, 3, 4}
acc.intersection_update([2, 3, 9])
acc.difference_update([3])
print(acc)
print({1, 2} <= {1, 2, 3}, {1, 2}.isdisjoint({9}))

try:
    s.remove(9)
except KeyError:
    print("missing")
s.clear()
print(s)
