# 063. pandas
#
# Series, DataFrame, loc/iloc, groupby, merge, missing data, apply, CSV, time, and sort.
#
# Run: python 063_pandas/main.py

# --- pandas series ---
import pandas as pd
s = pd.Series([1, 2, 3], index=["a", "b", "c"])
print(s["b"], s.mean())
print(s + pd.Series({"b": 10, "c": 1, "d": 0}))

# --- pandas frame ---
import pandas as pd
df = pd.DataFrame({"name": ["Ada", "Alan"], "year": [1815, 1912]})
print(df.shape, list(df.columns))
print(df.head(1))
print(df["year"].max())
print(df.dtypes.to_dict())

# --- pandas index ---
import pandas as pd
df = pd.DataFrame({"n": [10, 20, 30]}, index=["a", "b", "c"])
print(df.loc["b", "n"], df.iloc[0, 0])
print(df.loc[df["n"] > 15, "n"].tolist())

# --- pandas group ---
import pandas as pd
df = pd.DataFrame({"g": ["a", "a", "b"], "n": [1, 2, 3]})
print(df.groupby("g")["n"].sum())
print(df.groupby("g")["n"].transform("mean").tolist())

# --- pandas merge ---
import pandas as pd
left = pd.DataFrame({"id": [1, 2], "name": ["Ada", "Alan"]})
right = pd.DataFrame({"id": [1, 3], "city": ["London", "Paris"]})
print(left.merge(right, on="id", how="left"))

# --- pandas missing ---
import pandas as pd
import numpy as np
s = pd.Series([1.0, np.nan, 3.0])
print(s.isna().tolist())
print(s.fillna(0).tolist())
print(s.dropna().tolist())

# --- pandas apply ---
import pandas as pd
df = pd.DataFrame({"n": [1, 2, 3]})
print(df.assign(sq=lambda d: d["n"] ** 2))
print(df["n"].apply(lambda n: f"n={n}").tolist())

# --- pandas csv ---
import pandas as pd
from io import StringIO
text = "name,year\nAda,1815\nAlan,1912\n"
df = pd.read_csv(StringIO(text))
print(df.to_csv(index=False).strip())
print(df.year.dtype)

# --- pandas time ---
import pandas as pd
s = pd.Series([1, 2, 3], index=pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]))
print(s.index.year.tolist())
print(s.resample("2D").sum().tolist())

# --- pandas sort ---
import pandas as pd
df = pd.DataFrame({"g": ["b", "a", "a"], "n": [2, 3, 1]})
print(df.sort_values(["g", "n"]).to_dict("records"))
