# 154. Enum
#
# class Color(Enum) names a set of values. Members are unique, hashable, and compare by
# identity. Auto() fills in ints. Iterate the class for members.
#
# Run: python 154_enums/main.py

from enum import Enum, auto

class Status(Enum):
    NEW = auto()
    DONE = auto()

print(Status.NEW, Status.NEW.name, Status.NEW.value)
print(list(Status))
print(Status.NEW is Status.NEW)
