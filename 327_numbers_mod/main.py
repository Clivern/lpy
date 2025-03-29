# 327. numbers ABCs
#
# numbers.Integral, Real, Complex form a numeric tower. isinstance(True, numbers.Integral)
# is True. Use these ABCs in APIs that accept any number-like.
#
# Run: python 327_numbers_mod/main.py

import numbers
print(isinstance(3, numbers.Integral), isinstance(1.2, numbers.Real))
print(isinstance(1+0j, numbers.Complex))
