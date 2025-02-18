# 212. collections.defaultdict
#
# defaultdict(factory) calls factory for missing keys. defaultdict(list) is the usual
# group-by. The factory takes no arguments.
#
# Run: python 212_defaultdict/main.py

from collections import defaultdict
g = defaultdict(list)
for name in ["Ada", "Alan", "Alonzo"]:
    g[name[0]].append(name)
print(dict(g))
