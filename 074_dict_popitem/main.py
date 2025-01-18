# 074. dict.popitem
#
# popitem() removes and returns the last inserted (k, v) pair. On an empty dict it raises
# KeyError. Useful to drain a dict in LIFO order.
#
# Run: python 074_dict_popitem/main.py

d = {"a": 1, "b": 2, "c": 3}
print(d.popitem(), d)
print(d.popitem())
empty = {}
try:
    empty.popitem()
except KeyError:
    print("empty")
