# 342. numpy slicing
#
# Slices are views, not copies, unless you ask. Boolean masks pick rows. Fancy indexing
# with integer arrays copies. [:] still shares memory.
#
# Run: python 342_numpy_slice/main.py

import numpy as np
a = np.arange(8)
print(a[2:5], a[::2])
b = a[1:4]
b[0] = 99
print(a[1])
print(a[a > 3])
