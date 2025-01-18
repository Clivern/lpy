# 050. list.copy
#
# copy() is a shallow copy, same as xs[:] or list(xs). Nested objects are shared. Changing
# an inner list shows up in both.
#
# Run: python 050_list_copy/main.py

xs = [[1], [2]]
ys = xs.copy()
ys.append([3])
xs[0].append(9)
print(xs, ys)
print(xs is ys, xs[0] is ys[0])
