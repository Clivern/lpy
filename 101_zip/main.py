# 101. zip
#
# zip pairs items from several iterables until the shortest is exhausted. zip(*rows)
# transposes. strict=True errors on length mismatch (3.10+).
#
# Run: python 101_zip/main.py

names = ["Ada", "Alan"]
years = [1815, 1912]
print(list(zip(names, years)))
pairs = [(1, 2), (3, 4)]
print(list(zip(*pairs)))
