# 141. Dunder methods
#
# Names like __len__ and __add__ hook language syntax. len(x) calls x.__len__(). You
# rarely call dunders directly.
#
# Run: python 141_dunder/main.py

class Bag:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return Bag(self.items + other.items)

print(len(Bag([1, 2])), (Bag([1]) + Bag([2])).items)
