# 041. list.extend
#
# extend appends each item from an iterable. xs += ys is extend. Passing a string extends
# character by character. append(list) would nest.
#
# Run: python 041_list_extend/main.py

xs = [1, 2]
xs.extend([3, 4])
xs.extend("ab")
print(xs)
ys = [1]
ys += [2, 3]
print(ys)
