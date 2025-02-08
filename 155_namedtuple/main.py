# 155. namedtuple
#
# namedtuple builds a tuple subclass with named fields and a small memory layout. It is
# immutable. _replace returns a copy with some fields changed.
#
# Run: python 155_namedtuple/main.py

from collections import namedtuple

Point = namedtuple("Point", "x y")
p = Point(3, 4)
print(p.x, p[1], p._asdict())
print(p._replace(y=5))
