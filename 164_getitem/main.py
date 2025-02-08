# 164. __getitem__
#
# x[i] calls __getitem__. Slices arrive as slice objects. A class that only implements
# getitem with ints is a sequence enough for for-loops via old iteration.
#
# Run: python 164_getitem/main.py

class FirstLast:
    def __init__(self, items):
        self.items = list(items)

    def __getitem__(self, i):
        if i == 0:
            return self.items[0]
        if i == -1:
            return self.items[-1]
        raise IndexError(i)

fl = FirstLast([10, 20, 30])
print(fl[0], fl[-1])
