# 004. Integers
#
# int is arbitrary precision. // is floor division. % is remainder. ** is power. 0b, 0o,
# 0x write binary, octal, and hex. int(s, base) parses a string. bit_length, bit_count,
# to_bytes, and from_bytes talk bits. as_integer_ratio is (n, 1).
#
# Run: python 004_integers/main.py

print(10 // 3, 10 % 3, 2 ** 8)
print(0b1010, 0o12, 0xA)
print(10**40)

print(int("ff", 16), int("0xff", 0), int("1010", 2))
print(bin(10), oct(10), hex(10))

n = 255
print(n.bit_length(), n.bit_count())
print((0).bit_length(), (1).bit_length())
print((1024).to_bytes(2, "big"))
print(int.from_bytes(b"\x04\x00", "big"))
print((6).as_integer_ratio())
