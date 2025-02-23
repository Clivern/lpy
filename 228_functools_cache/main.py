# 228. functools.cache
#
# cache is lru_cache(maxsize=None). It grows without bound. singledispatch lets you
# overload a function on the type of the first argument.
#
# Run: python 228_functools_cache/main.py

from functools import cache, singledispatch
@cache
def twice(n):
    return n * 2
print(twice(4))

@singledispatch
def dump(x):
    return str(x)

@dump.register
def _(x: int):
    return f"int:{x}"

print(dump(3), dump("a"))
