# 167. is, ==, and None
#
# Use is for None, True, False, and sentinels. Use == for values. Do not rely on
# interning: a is b for equal ints can fail for large values.
#
# Run: python 167_is_vs_eq/main.py

x = None
print(x is None, x == None)
a = 10**10
b = 10**10
print(a == b, a is b)
