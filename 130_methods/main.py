# 130. Methods
#
# A function on a class becomes a method. The instance is passed as self. Calling p.dist()
# is Point.dist(p).
#
# Run: python 130_methods/main.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

print(Point(3, 4).dist())
