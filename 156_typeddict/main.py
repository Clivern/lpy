# 156. TypedDict
#
# TypedDict describes the keys and value types of a dict for checkers. At runtime it is a
# dict. total=False makes keys optional.
#
# Run: python 156_typeddict/main.py

from typing import TypedDict

class User(TypedDict):
    name: str
    year: int

u: User = {"name": "Ada", "year": 1815}
print(u["name"], dict(u))
