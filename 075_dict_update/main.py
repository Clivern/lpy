# 075. dict.update
#
# update merges another mapping or an iterable of pairs. Keywords work too: update(a=1).
# Later keys overwrite. It mutates in place and returns None.
#
# Run: python 075_dict_update/main.py

d = {"a": 1, "b": 0}
print(d.update({"b": 2, "c": 3}), d)
d.update(d=4, a=9)
print(d)
d.update([("e", 5)])
print(d)
