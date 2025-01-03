# 003. Built-in types
#
# int, float, bool, str, bytes, list, tuple, set, and dict cover most day-one data.
# Everything is an object, including these values.
#
# Run: python 003_types/main.py

values = [1, 1.5, True, "hi", b"raw", [1], (1,), {1}, {"k": 1}]
for v in values:
    print(type(v).__name__, v)
print([type(v).__name__ for v in values])
