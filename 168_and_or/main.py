# 168. and, or, and not
#
# not always returns bool. and and or return the last evaluated operand. That is why `x or
# default` works, and why `x and x.method()` short-circuits.
#
# Run: python 168_and_or/main.py

print(not [])
print([] or "default")
print("hi" and "there")
print(0 or 2 or 3)
