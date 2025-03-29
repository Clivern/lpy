# 358. pandas sort
#
# sort_values orders by columns. sort_index orders by labels. na_position puts NA first or
# last. kind="stable" keeps equal rows in order.
#
# Run: python 358_pandas_sort/main.py

import pandas as pd
df = pd.DataFrame({"g": ["b", "a", "a"], "n": [2, 3, 1]})
print(df.sort_values(["g", "n"]).to_dict("records"))
