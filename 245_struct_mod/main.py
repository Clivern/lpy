# 245. struct
#
# struct packs values into bytes with a format string. < is little-endian, > is big, ! is
# network. Useful for binary files and sockets.
#
# Run: python 245_struct_mod/main.py

import struct
blob = struct.pack(">IHI", 1, 2, 3)
print(blob, struct.unpack(">IHI", blob))
print(struct.calcsize(">IHI"))
