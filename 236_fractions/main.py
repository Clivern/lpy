# 236. fractions
#
# Fraction is a rational: exact numerator and denominator. limit_denominator approximates
# a float. Mixed with Decimal it stays exact until you convert.
#
# Run: python 236_fractions/main.py

from fractions import Fraction
print(Fraction(1, 3) + Fraction(1, 6))
print(Fraction(0.5), Fraction("0.5"))
print(Fraction(3.14159).limit_denominator(100))
