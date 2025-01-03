# 007. as_integer_ratio and is_integer
#
# int.as_integer_ratio is (n, 1). float.as_integer_ratio is exact in binary, so 0.1 is a
# long pair. float.is_integer is True for 2.0, not 2.1.
#
# Run: python 007_int_ratio/main.py

print((6).as_integer_ratio())
print((2.0).is_integer(), (2.1).is_integer())
print((0.5).as_integer_ratio())
