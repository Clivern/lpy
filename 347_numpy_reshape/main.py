# 347. numpy reshape
#
# reshape views when it can. -1 infers a dimension. ravel is flatten as a view if
# possible; flatten always copies. T transposes.
#
# Run: python 347_numpy_reshape/main.py

import numpy as np
a = np.arange(6)
print(a.reshape(2, 3))
print(a.reshape(2, 3).T.shape)
print(a.reshape(-1, 1).shape)
