# 122. Set comprehensions
#
# {expr for x in it} builds a set. Duplicates disappear. A pair of braces with a colon is
# a dict, so a set of tuples uses just a comma.
#
# Run: python 122_set_comp/main.py

print({n % 3 for n in range(10)})
print({(n, n * n) for n in range(4)})
