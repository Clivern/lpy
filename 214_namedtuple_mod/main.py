# 214. collections.namedtuple recap
#
# namedtuple lives in collections. It is a factory for tuple subclasses. _fields lists
# names. Unlike dataclass, it is always a tuple.
#
# Run: python 214_namedtuple_mod/main.py

from collections import namedtuple
Row = namedtuple("Row", ["id", "name"])
r = Row(1, "Ada")
print(r._fields, r.id, tuple(r))
