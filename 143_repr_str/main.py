# 143. __repr__ and __str__
#
# __repr__ is for developers and should be unambiguous. __str__ is for users. print uses
# str, the interactive prompt uses repr. !r in f-strings uses repr.
#
# Run: python 143_repr_str/main.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(repr(p), str(p), f"{p!r}")
