# 012. bool is a subclass of int
#
# True is 1 and False is 0 in arithmetic. bool is a subclass of int. Prefer `if xs:` over
# `if len(xs) != 0`. Do not use `== True`.
#
# Run: python 012_bool_subclass/main.py

one = 1
print(True + True, False * 10, issubclass(bool, int))
print(True == one, True is not one)
print(bool([]), bool([0]), bool("0"))
