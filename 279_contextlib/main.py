# 279. contextlib.contextmanager
#
# @contextmanager turns a generator into a with target. Yield the value of __enter__. Code
# after yield is __exit__. Exceptions propagate into the yield.
#
# Run: python 279_contextlib/main.py

from contextlib import contextmanager
@contextmanager
def tag(name):
    print(f"<{name}>")
    try:
        yield name
    finally:
        print(f"</{name}>")
with tag("p") as n:
    print("hi", n)
