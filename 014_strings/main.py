# 014. Strings
#
# str is an immutable sequence of Unicode code points. Concatenate with + or join. split,
# replace, strip, startswith, and in cover most text work.
#
# Run: python 014_strings/main.py

s = "Ada Lovelace"
print(s.upper(), s[0], s[-1])
print(s.split(), "Ada" in s)
print("-".join(["a", "b", "c"]))
print("  hi  ".strip().replace("hi", "hello"))
