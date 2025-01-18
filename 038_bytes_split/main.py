# 038. bytes.split and find
#
# bytes has split, find, startswith, and replace, but they take bytes, not str. A str
# separator is a TypeError. decode first if you want text methods.
#
# Run: python 038_bytes_split/main.py

b = b"a,b,c"
print(b.split(b","), b.find(b"b"))
print(b.startswith(b"a"), b.replace(b",", b":"))
try:
    b.split(",")
except TypeError as e:
    print(type(e).__name__)
