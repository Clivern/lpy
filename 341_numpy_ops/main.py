# 341. numpy operations
#
# Arithmetic is elementwise. @ is matrix multiply. Universal functions (sin, exp, sqrt)
# run in C. A Python for-loop over rows is usually the slow path.
#
# Run: python 341_numpy_ops/main.py

import numpy as np
a = np.array([1.0, 2.0, 3.0])
print(a * 2, a + a, np.sqrt(a))
m = np.array([[1, 2], [3, 4]])
print(m @ np.array([1, 1]))
