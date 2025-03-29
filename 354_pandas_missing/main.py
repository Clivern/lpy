# 354. pandas missing data
#
# isna detects NA. fillna fills. dropna drops. None and np.nan become NA. Int64 dtype can
# hold NA; plain int64 cannot.
#
# Run: python 354_pandas_missing/main.py

import pandas as pd
import numpy as np
s = pd.Series([1.0, np.nan, 3.0])
print(s.isna().tolist())
print(s.fillna(0).tolist())
print(s.dropna().tolist())
