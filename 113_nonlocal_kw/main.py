# 113. nonlocal
#
# nonlocal name rebinds a name in an enclosing (but not global) scope. Closures that
# accumulate state use it.
#
# Run: python 113_nonlocal_kw/main.py

def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

c = make_counter()
print(c(), c(), c())
