# 042. list.insert
#
# insert(i, x) places x at index i and shifts the tail. insert(0, x) is O(n). Negative
# indices count from the end, like elsewhere.
#
# Run: python 042_list_insert/main.py

xs = [1, 2, 3]
xs.insert(0, 0)
xs.insert(-1, 99)
print(xs)
xs.insert(len(xs), 4)
print(xs)
