# 009. inf, nan, and isclose
#
# float("inf") and float("nan") exist. nan != nan. math.isnan and math.isinf test them.
# math.isclose compares with a tolerance; == does not.
#
# Run: python 009_float_specials/main.py

import math
print(float("inf"), math.isinf(1e309))
nan = float("nan")
print(nan == nan, math.isnan(nan))
print(math.isclose(0.1 + 0.2, 0.3))
