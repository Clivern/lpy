# 328. copyreg
#
# copyreg.pickle registers a reduce function for a type so pickle and copy know how to
# rebuild it. Libraries use this for C types.
#
# Run: python 328_copyreg_mod/main.py

import copyreg, copy
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
def reduce_point(p):
    return Point, (p.x, p.y)
copyreg.pickle(Point, reduce_point)
p = copy.copy(Point(1, 2))
print(p.x, p.y)
