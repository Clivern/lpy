# 022. Case conversion
#
# upper, lower, title, capitalize, swapcase, and casefold change case. casefold is
# stronger than lower for caseless matching (German ß). title uppercases after non-
# letters.
#
# Run: python 022_str_case/main.py

s = "Ada lovelace"
print(s.upper(), s.lower())
print(s.title(), s.capitalize(), s.swapcase())
print("Straße".lower(), "Straße".casefold())
print("ß".casefold())
