# 081. Nested dicts
#
# Values can be dicts. Chain get to walk safely. setdefault builds a level. A miss on
# d["a"]["b"] raises at the first missing key.
#
# Run: python 081_dict_nested/main.py

users = {"ada": {"year": 1815, "city": "London"}}
print(users["ada"]["city"])
print(users.get("alan", {}).get("city"))
users.setdefault("alan", {})["year"] = 1912
print(users["alan"])
