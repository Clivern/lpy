# 054. Slice assignment
#
# xs[i:j] = iterable replaces that span. The length can change. xs[::2] = ... requires the
# replacement to be the same length. del xs[i:j] deletes a span.
#
# Run: python 054_list_slice_assign/main.py

xs = [0, 1, 2, 3, 4]
xs[1:4] = [8, 9]
print(xs)
xs[::2] = [7, 7, 7]
print(xs)
del xs[1:3]
print(xs)
