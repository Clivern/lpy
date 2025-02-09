# 199. json defaults and indent
#
# indent pretty-prints. sort_keys makes diffs stable. default= converts types dumps does
# not know, such as datetime, via a hook.
#
# Run: python 199_json_custom/main.py

import json
from datetime import date
def default(o):
    if isinstance(o, date):
        return o.isoformat()
    raise TypeError(type(o))

print(json.dumps({"d": date(2025, 1, 2)}, default=default, indent=2, sort_keys=True))
