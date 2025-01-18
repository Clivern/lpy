# 065. set.remove and discard
#
# remove raises KeyError if the item is missing. discard is silent. Use discard when
# absence is fine, remove when it is a bug.
#
# Run: python 065_set_remove_discard/main.py

s = {1, 2, 3}
s.discard(9)
s.remove(1)
print(s)
try:
    s.remove(9)
except KeyError:
    print("missing")
