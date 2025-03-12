# 278. typing.Union and |
#
# int | None is Optional[int] on 3.10+. Union[A, B] is the older spelling. Type checkers
# use this; runtime isinstance needs a tuple of types or Union unwrapping.
#
# Run: python 278_typing_union/main.py

from typing import get_args, get_origin
T = int | str
print(get_origin(T), get_args(T))
print(isinstance(3, get_args(T)))
