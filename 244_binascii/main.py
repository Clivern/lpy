# 244. binascii
#
# binascii is the low-level hex and hexlify layer. hexlify/unhexlify convert between bytes
# and hex. crc32 is a checksum, not a hash.
#
# Run: python 244_binascii/main.py

import binascii
print(binascii.hexlify(b"hi"))
print(binascii.unhexlify("6869"))
print(binascii.crc32(b"hello"))
