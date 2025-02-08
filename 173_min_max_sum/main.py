# 173. min, max, sum
#
# min and max take an iterable or several arguments. key= works like sorted. sum starts at
# 0; pass start= for other types. sum of strings is wrong; use join.
#
# Run: python 173_min_max_sum/main.py

print(min(3, 1, 2), max([3, 1, 2]))
print(min("abc", "aa", key=len))
print(sum([1, 2, 3], start=10))
