# 153. dataclasses
#
# @dataclass generates __init__, __repr__, and __eq__ from annotations. frozen=True makes
# instances immutable. slots=True (3.10+) skips __dict__.
#
# Run: python 153_dataclasses/main.py

from dataclasses import dataclass

@dataclass
class User:
    name: str
    id: int = 0

a = User("Ada", 1)
b = User("Ada", 1)
print(a, a == b, a.name)
print(a.name, a.id)
