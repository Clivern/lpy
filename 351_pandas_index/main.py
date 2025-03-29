# 351. pandas loc and iloc
#
# loc is label-based. iloc is position-based. df["col"] is a Series; df[["col"]] is a
# DataFrame. Chained assignment is a trap; use loc to write.
#
# Run: python 351_pandas_index/main.py

import pandas as pd
df = pd.DataFrame({"n": [10, 20, 30]}, index=["a", "b", "c"])
print(df.loc["b", "n"], df.iloc[0, 0])
print(df.loc[df["n"] > 15, "n"].tolist())
