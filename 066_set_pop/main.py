# 066. set.pop and clear
#
# pop() removes an arbitrary item. Do not depend on the order. clear() empties in place.
# An empty pop raises KeyError.
#
# Run: python 066_set_pop/main.py

s = {1, 2}
print(s.pop() in {1, 2})
s.clear()
print(s)
try:
    s.pop()
except KeyError:
    print("empty")
