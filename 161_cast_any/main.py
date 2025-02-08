# 161. cast and Any
#
# Any turns off checking for a name. cast(T, x) tells the checker x is a T without
# changing the value. Use both sparingly at boundaries.
#
# Run: python 161_cast_any/main.py

from typing import Any, cast

def read() -> Any:
    return "42"

n = cast(int, int(read()))
print(n, n + 1)
