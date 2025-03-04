# 262. re
#
# re.search finds the first match. match anchors at the start. findall returns strings or
# tuples of groups. Compile a pattern you use in a loop.
#
# Run: python 262_re_mod/main.py

import re
print(re.search(r"\d+", "id=42").group())
print(re.findall(r"[A-Z][a-z]+", "Ada Alan"))
print(bool(re.match(r"Ada", "Ada Lovelace")))
