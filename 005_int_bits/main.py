# 005. Integer bit methods
#
# bit_length is the bits needed to represent the abs value. bit_count (3.10+) counts
# 1-bits. to_bytes and from_bytes convert with an endianness and a length.
#
# Run: python 005_int_bits/main.py

n = 255
print(n.bit_length(), n.bit_count())
print((0).bit_length(), (1).bit_length())
print((1024).to_bytes(2, "big"))
print(int.from_bytes(b"\x04\x00", "big"))
