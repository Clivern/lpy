# 044. list.remove
#
# remove(x) deletes the first item equal to x. It raises ValueError if missing. It
# compares with ==, so 1 and True collide. To remove all, use a list comprehension.
#
# Run: python 044_list_remove/main.py

xs = [1, 2, 1, 3]
xs.remove(1)
print(xs)
try:
    xs.remove(9)
except ValueError as e:
    print(type(e).__name__)
print([x for x in [1, 2, 1, 3] if x != 1])
