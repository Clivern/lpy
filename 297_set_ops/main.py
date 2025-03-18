# 297. Set methods
#
# add, discard, remove, and pop mutate. discard is silent when missing; remove raises.
# issubset and isdisjoint answer questions without allocating.
#
# Run: python 297_set_ops/main.py

s = {1, 2, 3}
s.add(4)
s.discard(9)
print(s.issubset({1, 2, 3, 4}), s.isdisjoint({9}))
s.remove(1)
print(s)
