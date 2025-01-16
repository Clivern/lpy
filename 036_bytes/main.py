# 036. Bytes and bytearray
#
# bytes is an immutable sequence of 0..255. decode turns bytes into str; encode goes the
# other way. bytearray is the mutable form.
#
# Run: python 036_bytes/main.py

b = "café".encode("utf-8")
print(b, list(b[:4]))
print(b.decode("utf-8"))
ba = bytearray(b)
ba[0] = 67
print(ba)
