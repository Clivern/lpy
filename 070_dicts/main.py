# 070. Dicts
#
# dict maps hashable keys to values. Insertion order is kept. get returns a default. keys,
# values, and items are dynamic views.
#
# Run: python 070_dicts/main.py

d = {"name": "Ada", "year": 1815}
d["year"] = 1815
print(d["name"], d.get("city", "unknown"))
print(list(d), list(d.values()))
for k, v in d.items():
    print(k, v)
