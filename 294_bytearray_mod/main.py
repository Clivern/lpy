# 294. bytearray methods
#
# bytearray is mutable bytes. extend, append, and slice assignment work. decode still
# needs a copy to str. Use it when you assemble a buffer in pieces.
#
# Run: python 294_bytearray_mod/main.py

ba = bytearray()
ba.extend(b"he")
ba.extend(b"llo")
print(ba.decode(), ba[0])
ba[0] = ord("H")
print(ba)
