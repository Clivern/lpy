# 349. pandas Series
#
# Series is a 1d labeled array. index can be strings. values is the numpy array. NaN is
# the missing value. Alignment is by label, not position.
#
# Run: python 349_pandas_series/main.py

import pandas as pd
s = pd.Series([1, 2, 3], index=["a", "b", "c"])
print(s["b"], s.mean())
print(s + pd.Series({"b": 10, "c": 1, "d": 0}))
