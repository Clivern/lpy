# 343. numpy stats
#
# mean, sum, std, min, max take axis=. nanmean skips NaN. A 2d array with axis=0 reduces
# columns. dtype can overflow on sum of ints; pass dtype=float.
#
# Run: python 343_numpy_stats/main.py

import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
print(a.mean(), a.mean(axis=0), a.sum(axis=1))
print(np.nanmean([1.0, np.nan, 3.0]))
