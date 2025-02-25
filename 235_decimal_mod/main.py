# 235. decimal
#
# Decimal is base-10 arithmetic with a settable precision. Use it for money. Construct
# from strings, not floats, or you import the binary error.
#
# Run: python 235_decimal_mod/main.py

from decimal import Decimal, getcontext
getcontext().prec = 6
print(Decimal("0.1") + Decimal("0.2"))
print(Decimal("1") / Decimal("7"))
