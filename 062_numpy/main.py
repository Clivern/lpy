# 062. numpy
#
# ndarray, ops, slicing, stats, broadcasting, linalg, random, reshape, and where.
#
# Run: python 062_numpy/main.py

# --- numpy array ---
import numpy as np
a = np.array([1, 2, 3], dtype=np.int64)
print(a.shape, a.dtype, a.ndim)
print(np.zeros((2, 3)), np.arange(4))
print(a.dtype)

# --- numpy ops ---
import numpy as np
a = np.array([1.0, 2.0, 3.0])
print(a * 2, a + a, np.sqrt(a))
m = np.array([[1, 2], [3, 4]])
print(m @ np.array([1, 1]))

# --- numpy slice ---
import numpy as np
a = np.arange(8)
print(a[2:5], a[::2])
b = a[1:4]
b[0] = 99
print(a[1])
print(a[a > 3])

# --- numpy stats ---
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(a.mean(), a.mean(axis=0), a.sum(axis=1))
print(np.nanmean([1.0, np.nan, 3.0]))

# --- numpy broadcast ---
import numpy as np
col = np.arange(3).reshape(3, 1)
row = np.arange(4).reshape(1, 4)
print((col + row).shape)
print(col + row)

# --- numpy linalg ---
import numpy as np
A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])
x = np.linalg.solve(A, b)
print(np.allclose(A @ x, b), round(np.linalg.det(A), 3))

# --- numpy random ---
import numpy as np
rng = np.random.default_rng(0)
print(rng.integers(0, 10, size=3))
print(rng.normal(0, 1, size=2).shape)

# --- numpy reshape ---
import numpy as np
a = np.arange(6)
print(a.reshape(2, 3))
print(a.reshape(2, 3).T.shape)
print(a.reshape(-1, 1).shape)

# --- numpy where ---
import numpy as np
a = np.array([1, 2, 3, 4])
print(np.where(a % 2 == 0, a, 0))
print(np.clip(a, 2, 3), np.unique([1, 1, 2]))
