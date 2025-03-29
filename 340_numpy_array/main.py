# 340. numpy arrays
#
# np.array builds an ndarray. shape, dtype, and ndim describe it. zeros, ones, and arange
# are the usual constructors. Indexing is richer than lists.
#
# Run: python 340_numpy_array/main.py

import numpy as np
a = np.array([1, 2, 3], dtype=np.int64)
print(a.shape, a.dtype, a.ndim)
print(np.zeros((2, 3)), np.arange(4))
print(a.dtype)
