# 126. yield from
#
# yield from iterable delegates to a sub-iterator. It forwards send and throw. Flattening
# nested generators is the common use.
#
# Run: python 126_yield_from/main.py

def chain(*iters):
    for it in iters:
        yield from it

print(list(chain(range(2), "ab", [9])))
