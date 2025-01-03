# 006. int with a base
#
# int(s, base) parses a string. base 0 infers from 0b 0o 0x. bin, oct, and hex format.
# int("0x10", 0) works; int("0x10") does not.
#
# Run: python 006_int_bases/main.py

print(int("ff", 16), int("0xff", 0), int("1010", 2))
print(bin(10), oct(10), hex(10))
print(int("10"), int("10", 8))
