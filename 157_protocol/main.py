# 157. Protocol
#
# Protocol is structural typing: a class matches if it has the methods, without
# inheriting. runtime_checkable allows isinstance.
#
# Run: python 157_protocol/main.py

from typing import Protocol, runtime_checkable

@runtime_checkable
class Closeable(Protocol):
    def close(self) -> None: ...

class Handle:
    def close(self) -> None:
        print("closed")

print(isinstance(Handle(), Closeable))
Handle().close()
