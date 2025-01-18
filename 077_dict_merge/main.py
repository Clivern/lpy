# 077. Dict merge with |
#
# | merges two dicts into a new one (3.9+). Right-hand keys win. |= updates in place.
# {**a, **b} is the older unpacking form.
#
# Run: python 077_dict_merge/main.py

a = {"x": 1, "y": 2}
b = {"y": 9, "z": 3}
print(a | b, a)
a |= {"z": 4}
print(a)
print({**{"a": 1}, **{"a": 2, "b": 3}})
print({**{"a": 1}, **{"b": 2}})
