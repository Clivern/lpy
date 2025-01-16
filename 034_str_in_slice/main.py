# 034. String membership and slices
#
# s in t searches for a substring. Slices copy; there is no mutable index assignment on
# str. step=-1 reverses. Indexing a str yields a one-character str, not a char type.
#
# Run: python 034_str_in_slice/main.py

s = "Python"
print("th" in s, "TH" in s)
print(s[1:4], s[::-1], s[::2])
print(s[0], type(s[0]).__name__, len(s[0]))
try:
    s[0] = "p"
except TypeError as e:
    print(type(e).__name__)
