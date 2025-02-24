# 231. copy recap
#
# copy.copy and deepcopy live in copy. copyreg customizes pickle. For lists, xs[:] is a
# shallow copy; it is not enough when items are mutable.
#
# Run: python 231_copy_mod/main.py

import copy
class Node:
    def __init__(self, v, child=None):
        self.v = v
        self.child = child
n = Node(1, Node(2))
d = copy.deepcopy(n)
n.child.v = 9
print(d.child.v)
