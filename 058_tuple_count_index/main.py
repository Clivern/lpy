# 058. tuple.count and index
#
# Tuples have count and index, like lists, but no mutating methods. index raises
# ValueError on a miss. A tuple can hold mutables; the tuple's identity stays fixed.
#
# Run: python 058_tuple_count_index/main.py

t = (1, 2, 1, 3)
print(t.count(1), t.index(3))
try:
    t.index(9)
except ValueError:
    print("missing")
