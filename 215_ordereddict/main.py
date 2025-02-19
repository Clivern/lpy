# 215. collections.OrderedDict
#
# dict keeps insertion order since 3.7. OrderedDict still offers move_to_end and equality
# that cares about order. Use it when those matter.
#
# Run: python 215_ordereddict/main.py

from collections import OrderedDict
d = OrderedDict([("a", 1), ("b", 2)])
d.move_to_end("a")
print(list(d))
print(OrderedDict([("a", 1), ("b", 2)]) == OrderedDict([("b", 2), ("a", 1)]))
