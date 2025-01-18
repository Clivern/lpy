# 046. list.index and count
#
# index(x) returns the first index of x, or ValueError. start and stop bound the search.
# count(x) counts == matches, including True for 1.
#
# Run: python 046_list_index_count/main.py

xs = ["a", "b", "a", "c"]
print(xs.index("a"), xs.index("a", 1), xs.count("a"))
print([1, True, 0].count(1))
try:
    xs.index("z")
except ValueError as e:
    print(type(e).__name__)
