# 178. del
#
# del name unbinds a name. del xs[i] or del d[k] removes an item. It is not a destructor
# call by itself; objects die when nothing refers to them.
#
# Run: python 178_del_stmt/main.py

xs = [1, 2, 3]
del xs[1]
print(xs)
d = {"a": 1, "b": 2}
del d["a"]
print(d)
