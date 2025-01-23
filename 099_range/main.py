# 099. range
#
# range(stop) or range(start, stop, step) is a lazy sequence of ints. It is not a list
# until you materialize it. Negative step counts down.
#
# Run: python 099_range/main.py

print(list(range(4)))
print(list(range(2, 8, 2)))
print(list(range(5, 0, -1)))
print(len(range(1000)))
