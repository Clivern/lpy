# 230. operator
#
# operator.itemgetter and attrgetter build key functions. add, mul, and friends are
# function versions of operators. Useful with map and sorted.
#
# Run: python 230_operator_mod/main.py

from operator import itemgetter, attrgetter, add
print(sorted([("b", 2), ("a", 1)], key=itemgetter(0)))
print(add(3, 4))
class U:
    def __init__(self, name):
        self.name = name
print(attrgetter("name")(U("Ada")))
