# 060. Packing and unpacking
#
# A comma packs a tuple. Unpacking requires the numbers to match unless you use *rest.
# Nested unpacking pulls from inner sequences.
#
# Run: python 060_tuple_packing/main.py

t = 1, 2, 3
a, b, c = t
print(a, c)
head, *rest = t
print(head, rest)
(x, y), z = (10, 20), 30
print(x, y, z)
