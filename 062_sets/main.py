# 062. Sets
#
# set is an unordered collection of unique hashable items. | & - ^ are union,
# intersection, difference, symmetric difference.
#
# Run: python 062_sets/main.py

a = {1, 2, 3, 2}
b = {3, 4}
print(a, a | b, a & b, a - b, a ^ b)
print(2 in a)
