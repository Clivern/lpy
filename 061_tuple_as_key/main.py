# 061. Tuples as dict keys
#
# A tuple of hashables is a valid dict key and set member. It is the usual composite key.
# If it contains a list, hashing fails.
#
# Run: python 061_tuple_as_key/main.py

seen = {(0, 0), (1, 2)}
seen.add((0, 0))
print(sorted(seen))
print({(1, 2): "point"}[(1, 2)])
