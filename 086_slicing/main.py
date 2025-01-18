# 086. Slicing
#
# s[start:stop:step] selects a subsequence. Defaults are 0, len, 1. Negative step
# reverses. Assignment into a slice can change length.
#
# Run: python 086_slicing/main.py

s = list(range(8))
print(s[2:5], s[:3], s[5:], s[::2], s[::-1])
s[1:3] = [10, 11, 12]
print(s)
