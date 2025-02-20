# 221. permutations and combinations
#
# permutations orders matter. combinations orders do not. combinations_with_replacement
# allows repeats. Length r is optional; default is the full length.
#
# Run: python 221_itertools_perm/main.py

from itertools import permutations, combinations
print(list(permutations("abc", 2)))
print(list(combinations("abc", 2)))
