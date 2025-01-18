# 071. dict.get
#
# d[k] raises KeyError on a miss. get(k) returns None. get(k, default) returns default
# without inserting. Use get when absence is normal.
#
# Run: python 071_dict_get/main.py

d = {"name": "Ada"}
print(d.get("name"), d.get("city"), d.get("city", "n/a"))
try:
    d["city"]
except KeyError as e:
    print(type(e).__name__, e)
print({"n": 1}.get("m", 0))
