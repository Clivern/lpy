# 355. pandas apply
#
# apply runs a Python function along an axis. It is slower than vectorized ops. Use it
# when the logic does not map to ufuncs. assign adds columns.
#
# Run: python 355_pandas_apply/main.py

import pandas as pd
df = pd.DataFrame({"n": [1, 2, 3]})
print(df.assign(sq=lambda d: d["n"] ** 2))
print(df["n"].apply(lambda n: f"n={n}").tolist())
