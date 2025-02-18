# 211. collections.Counter
#
# Counter counts hashable items. most_common(n) ranks them. Counters add and subtract.
# Missing keys read as 0, not KeyError.
#
# Run: python 211_collections_counter/main.py

from collections import Counter
c = Counter("abracadabra")
print(c["a"], c.most_common(2))
print(Counter("ab") + Counter("bc"))
