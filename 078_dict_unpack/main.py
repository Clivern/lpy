# 078. Dict unpacking in calls
#
# **d in a call fills keyword arguments. Duplicate keywords after unpacking are an error.
# In a display, {**a, **b} last key wins.
#
# Run: python 078_dict_unpack/main.py

def greet(name, year):
    return f"{name} {year}"
print(greet(**{"name": "Ada", "year": 1815}))
print({**{"a": 1, "b": 2}, "b": 3})
