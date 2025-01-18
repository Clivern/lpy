# 080. Membership in dicts
#
# k in d tests keys, not values. d.keys() and d are the same for in. k in d.values()
# scans. not in is the inverse. Avoid if d[k]: that KeyErrors on a miss.
#
# Run: python 080_dict_in/main.py

d = {"name": "Ada", "year": 1815}
print("name" in d, "Ada" in d, "Ada" in d.values())
print("city" not in d)
print(d.get("city") is None)
