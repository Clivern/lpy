# 232. pprint
#
# pprint pretty-prints nested structures. pp is the function form on 3.8+. width and
# sort_dicts control layout. Debug dumps of JSON-like data go here.
#
# Run: python 232_pprint_mod/main.py

from pprint import pprint, pformat
data = {"users": [{"name": "Ada", "ids": list(range(5))}], "ok": True}
print(pformat(data, width=40, sort_dicts=True))
pprint({"b": 1, "a": 2}, sort_dicts=True)
