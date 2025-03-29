# 350. pandas DataFrame
#
# DataFrame is a table of Series. dict-of-lists construction is the usual start. head,
# dtypes, and shape inspect it. Each column is a Series.
#
# Run: python 350_pandas_frame/main.py

import pandas as pd
df = pd.DataFrame({"name": ["Ada", "Alan"], "year": [1815, 1912]})
print(df.shape, list(df.columns))
print(df.head(1))
print(df["year"].max())
print(df.dtypes.to_dict())
