# 357. pandas time series
#
# to_datetime parses dates. dt accessor extracts year, month, day. resample bins by
# frequency. A DatetimeIndex enables all of this.
#
# Run: python 357_pandas_time/main.py

import pandas as pd
s = pd.Series([1, 2, 3], index=pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]))
print(s.index.year.tolist())
print(s.resample("2D").sum().tolist())
