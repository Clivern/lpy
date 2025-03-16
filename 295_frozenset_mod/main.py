# 295. frozenset
#
# frozenset is an immutable set. It can be a dict key or a member of another set.
# Operators | & - still work and return frozenset when both sides are frozen.
#
# Run: python 295_frozenset_mod/main.py

a = frozenset([1, 2, 3])
b = frozenset([3, 4])
print(a | b, {a: "ok"}[a])
