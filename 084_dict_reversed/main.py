# 084. reversed(dict)
#
# reversed(d) iterates keys from the last insertion. reversed(d.items()) yields pairs in
# that order. Useful for LIFO walks without popitem.
#
# Run: python 084_dict_reversed/main.py

d = {"a": 1, "b": 2, "c": 3}
print(list(reversed(d)))
print(list(reversed(d.items())))
