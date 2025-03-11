# 275. inspect
#
# inspect.signature lists parameters. getsource reads the source. isfunction and isclass
# classify objects. Debuggers and frameworks lean on this.
#
# Run: python 275_inspect_mod/main.py

import inspect
def greet(name: str, times: int = 1) -> str:
    return name * times
print(inspect.signature(greet))
print(inspect.isfunction(greet))
