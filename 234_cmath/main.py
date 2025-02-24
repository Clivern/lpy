# 234. cmath
#
# cmath is math for complex numbers. 1j is the imaginary unit. phase and polar convert to
# angle and length.
#
# Run: python 234_cmath/main.py

import cmath
z = 1 + 1j
print(z * z, abs(z), cmath.phase(z))
print(cmath.polar(z))
