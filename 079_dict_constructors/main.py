# 079. Dict constructors
#
# dict() copies a mapping. dict(a=1) uses keys that are identifiers. dict([("a", 1)])
# takes pairs. A dict display {k: v} is the usual literal.
#
# Run: python 079_dict_constructors/main.py

print(dict(name="Ada", year=1815))
print(dict([("a", 1), ("b", 2)]))
print(dict({"a": 1}, b=2))
print(dict())
