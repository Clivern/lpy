# 063. set.add
#
# add inserts one hashable item. Adding twice is a no-op. A list cannot be added; convert
# to a tuple. add returns None.
#
# Run: python 063_set_add/main.py

s = {1, 2}
print(s.add(3), s)
s.add(2)
print(s)
try:
    s.add([4])
except TypeError:
    s.add((4,))
    print(s)
