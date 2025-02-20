# 220. itertools.product
#
# product is a nested for over several iterables. repeat=n is the cartesian power. It is
# lazy; list it only when the product is small.
#
# Run: python 220_itertools_product/main.py

from itertools import product
print(list(product("ab", "12")))
print(list(product("ab", repeat=2)))
