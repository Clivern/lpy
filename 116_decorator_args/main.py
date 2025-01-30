# 116. Decorators with arguments
#
# @deco(x) is f = deco(x)(f). The outer function takes the arguments and returns the real
# decorator.
#
# Run: python 116_decorator_args/main.py

def repeat(times):
    def deco(fn):
        def wrapper(*args, **kwargs):
            return [fn(*args, **kwargs) for _ in range(times)]
        return wrapper
    return deco

@repeat(3)
def hi():
    return "hi"

print(hi())
