# 166. Copying objects
#
# Assignment copies a reference. copy.copy is shallow: nested objects are shared.
# copy.deepcopy recurses. Immutable containers can look copied when they are not.
#
# Run: python 166_copy_obj/main.py

import copy
a = [[1], [2]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0].append(9)
print(a, b, c)
