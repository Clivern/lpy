# 179. in
#
# x in seq scans a sequence. x in dict tests keys. x in set is average O(1). for uses in
# as syntax, not as a membership test.
#
# Run: python 179_in_op/main.py

print(3 in [1, 2, 3], "a" in "cat", "k" in {"k": 1})
print(2 not in {1, 3})
