# 352. pandas groupby
#
# groupby(col).agg(...) splits, applies, and combines. size counts rows. transform
# broadcasts a group result back to row shape.
#
# Run: python 352_pandas_group/main.py

import pandas as pd
df = pd.DataFrame({"g": ["a", "a", "b"], "n": [1, 2, 3]})
print(df.groupby("g")["n"].sum())
print(df.groupby("g")["n"].transform("mean").tolist())
