# 010. float.hex
#
# hex() is an exact hexadecimal representation. fromhex reverses it. Useful to serialize a
# float without decimal rounding.
#
# Run: python 010_float_hex/main.py

x = 0.1
print(x.hex())
print(float.fromhex(x.hex()) == x)
print(float.fromhex("0x1.0p0"))
