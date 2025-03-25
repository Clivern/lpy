# 318. NewType
#
# NewType("UserId", int) is int at runtime and distinct for checkers. It prevents mixing
# ids of different domains without a cast.
#
# Run: python 318_typing_newtype/main.py

from typing import NewType
UserId = NewType("UserId", int)
uid = UserId(7)
print(uid + 1, type(uid) is int)
