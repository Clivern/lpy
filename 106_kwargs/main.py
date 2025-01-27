# 106. Keyword arguments
#
# Callers can pass name=value. After the first keyword, the rest must be keywords.
# **kwargs in a def collects leftover keywords into a dict.
#
# Run: python 106_kwargs/main.py

def greet(name, greeting="hi"):
    return f"{greeting} {name}"

print(greet("Ada"))
print(greet(name="Alan", greeting="hello"))

def dump(**kwargs):
    return sorted(kwargs.items())

print(dump(a=1, b=2))
