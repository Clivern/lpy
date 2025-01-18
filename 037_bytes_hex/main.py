# 037. bytes.hex and fromhex
#
# hex() is a str of two digits per byte. fromhex parses spaces. This is the usual debug
# form, not encryption.
#
# Run: python 037_bytes_hex/main.py

b = bytes.fromhex("68 69")
print(b, b.hex(), b.hex(" "))
print(bytes.fromhex("c3 a9").decode())
