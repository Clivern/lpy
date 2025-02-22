# 222. compress, dropwhile, takewhile
#
# compress keeps items where the selector is true. dropwhile skips until the predicate
# fails, then yields the rest. takewhile is the opposite prefix.
#
# Run: python 222_itertools_comb/main.py

from itertools import compress, dropwhile, takewhile
print(list(compress("abcd", [1, 0, 1, 0])))
print(list(dropwhile(lambda n: n < 3, [1, 2, 3, 1, 4])))
print(list(takewhile(lambda n: n < 3, [1, 2, 3, 1])))
