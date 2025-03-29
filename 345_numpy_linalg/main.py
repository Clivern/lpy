# 345. numpy.linalg
#
# linalg.inv, det, eig, and solve cover small dense linear algebra. solve(A, b) is more
# stable than inv(A) @ b. SVD is svd.
#
# Run: python 345_numpy_linalg/main.py

import numpy as np
A = np.array([[3.0, 1.0], [1.0, 2.0]])
b = np.array([9.0, 8.0])
x = np.linalg.solve(A, b)
print(np.allclose(A @ x, b), round(np.linalg.det(A), 3))
