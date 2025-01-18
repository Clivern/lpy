# 064. set.update
#
# update adds each item from an iterable, in place. |= is the same. union (or |) returns a
# new set. A string updates character by character.
#
# Run: python 064_set_update/main.py

s = {1}
s.update([2, 3], {3, 4})
print(s)
print(s | {5, 6}, s)
s.update("ab")
print(s)
