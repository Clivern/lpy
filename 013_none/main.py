# 013. None
#
# None is the missing value. Functions that omit return yield None. Compare with is, not
# ==. A name bound to None is still a name.
#
# Run: python 013_none/main.py

x = None
print(x is None)
print((lambda: None)() is None)
