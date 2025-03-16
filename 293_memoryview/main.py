# 293. memoryview
#
# memoryview is a view over a bytes-like object without copying. Slicing a view is cheap.
# tobytes() materializes. Binary protocols use it to cut packets.
#
# Run: python 293_memoryview/main.py

b = bytearray(b"abcdef")
v = memoryview(b)
print(bytes(v[1:4]))
v[0] = 65
print(b)
