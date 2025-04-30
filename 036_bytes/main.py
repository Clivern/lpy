# 036. Bytes and bytearray
#
# bytes is an immutable sequence of 0..255. decode turns bytes into str; encode goes the
# other way. bytearray is the mutable form. split, find, and replace take bytes, not str.
# hex and fromhex are the usual debug form.
#
# Run: python 036_bytes/main.py

b = "café".encode("utf-8")
print(b, list(b[:4]))
print(b.decode("utf-8"))
ba = bytearray(b)
ba[0] = 67
print(ba)

raw = bytes.fromhex("68 69")
print(raw, raw.hex(), raw.hex(" "))
print(bytes.fromhex("c3 a9").decode())

line = b"a,b,c"
print(line.split(b","), line.find(b"b"), line.replace(b",", b":"))
try:
    line.split(",")
except TypeError as e:
    print(type(e).__name__)
