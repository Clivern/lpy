# 198. json
#
# json.dumps serializes Python data to a string. loads parses it back. dump/load talk to
# file objects. Keys become str. tuples become lists.
#
# Run: python 198_json_mod/main.py

import json
data = {"name": "Ada", "year": 1815, "ok": True}
s = json.dumps(data)
print(s)
print(json.loads(s)["year"])
