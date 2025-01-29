# 115. Decorators
#
# @deco above a def is the same as f = deco(f). A decorator takes a function and returns a
# callable, often a wrapper that logs or times.
#
# Run: python 115_decorators/main.py

def trace(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(fn.__name__, args, result)
        return result
    return wrapper

@trace
def add(a, b):
    return a + b

add(2, 3)
