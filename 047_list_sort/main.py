# 047. list.sort
#
# sort orders in place and returns None. reverse=True flips. The list must be homogeneous
# enough to compare. sorted(xs) returns a new list and leaves xs alone.
#
# Run: python 047_list_sort/main.py

xs = [3, 1, 2]
print(xs.sort(), xs)
ys = [3, 1, 2]
print(sorted(ys), ys)
xs.sort(reverse=True)
print(xs)
print(sorted([3, 1, 2], reverse=True))
