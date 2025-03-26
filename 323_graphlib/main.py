# 323. graphlib.TopologicalSorter
#
# TopologicalSorter orders nodes so edges go forward. CycleError means a cycle. Build
# systems and task graphs use this (3.9+).
#
# Run: python 323_graphlib/main.py

from graphlib import TopologicalSorter
ts = TopologicalSorter({"compile": {"parse"}, "parse": set(), "link": {"compile"}})
print(list(ts.static_order()))
