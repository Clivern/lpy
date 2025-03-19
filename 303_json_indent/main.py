# 303. json lines
#
# JSON Lines is one object per line. dumps each row and join with newlines. loads one line
# at a time. Logs and exports use this more than pretty JSON.
#
# Run: python 303_json_indent/main.py

import json
rows = [{"n": 1}, {"n": 2}]
text = "\n".join(json.dumps(r) for r in rows)
print([json.loads(line)["n"] for line in text.splitlines()])
