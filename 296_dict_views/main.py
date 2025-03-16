# 296. Dict views
#
# keys() and items() are set-like views. They reflect later changes. & | - work between
# key views. values() supports in but not set ops.
#
# Run: python 296_dict_views/main.py

d = {"a": 1, "b": 2}
keys = d.keys()
d["c"] = 3
print("c" in keys, keys & {"a", "x"})
print(list(d.items()))
