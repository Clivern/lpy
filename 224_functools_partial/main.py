# 224. functools.partial
#
# partial(fn, *args, **kwargs) freezes some arguments and returns a new callable. Handy
# for callbacks that need extra context.
#
# Run: python 224_functools_partial/main.py

from functools import partial
def power(base, exp):
    return base ** exp
square = partial(power, exp=2)
print(square(5), partial(power, 2)(8))
