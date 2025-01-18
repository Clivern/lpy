# 087. Unpacking
#
# *rest captures leftover items. Nested unpacking works on sequences. * in a call splats a
# sequence into positional arguments.
#
# Run: python 087_unpacking/main.py

first, *mid, last = [1, 2, 3, 4, 5]
print(first, mid, last)
print([*mid, last])
print("{x} {y}".format(**{"x": 1, "y": 2}))
