# 227. functools.wraps
#
# @wraps(fn) copies __name__, __doc__, and signature onto a wrapper. Without it,
# decorators hide the original function from help() and traces.
#
# Run: python 227_functools_wraps/main.py

from functools import wraps
def deco(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper

@deco
def greet():
    """say hi"""
    return "hi"

print(greet.__name__, greet.__doc__)
