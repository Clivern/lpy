# 314. frozen dataclasses
#
# frozen=True makes assignment raise FrozenInstanceError. The instance is hashable if the
# fields are. order=True adds < from the field tuple.
#
# Run: python 314_dataclasses_frozen/main.py

from dataclasses import dataclass
@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int
p = Point(1, 2)
print(p, hash(p) != 0, Point(0, 0) < p)
