# 281. contextlib.ExitStack
#
# ExitStack enters a dynamic number of context managers. callback schedules a function.
# Useful when the set of resources is only known at runtime.
#
# Run: python 281_exitstack/main.py

from contextlib import ExitStack
from io import StringIO
with ExitStack() as stack:
    f = stack.enter_context(StringIO("hi"))
    stack.callback(lambda: print("done"))
    print(f.read())
