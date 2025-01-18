# 040. list.append
#
# append adds one item at the end in amortized O(1). The item can be any object, including
# another list, which nests rather than concatenates.
#
# Run: python 040_list_append/main.py

xs = [1, 2]
xs.append(3)
print(xs)
xs.append([4, 5])
print(xs)
