# 140. __slots__
#
# __slots__ lists allowed attribute names and skips the instance __dict__. It saves memory
# and catches typos. Subclasses need their own slots to add fields.
#
# Run: python 140_slots/main.py

class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)
print(hasattr(p, "__dict__"))
