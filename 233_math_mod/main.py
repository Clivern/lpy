# 233. math
#
# math is C floats: sqrt, log, sin, pi, inf, nan, comb, factorial. It does not work on
# complexes; use cmath. Dist and hypot beat hand-rolled squares.
#
# Run: python 233_math_mod/main.py

import math
print(math.sqrt(16), math.hypot(3, 4), math.pi)
print(math.comb(5, 2), math.isclose(0.1 + 0.2, 0.3))
