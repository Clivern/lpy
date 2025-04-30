# 011. Booleans and short circuit
#
# True and False are bool, a subclass of int. True is 1 in arithmetic. and/or return an
# operand, not necessarily True/False. Comparison chains work: 1 < x < 5. Prefer `if xs:`
# over `if len(xs) != 0`. Compare with is for None, not for 1.
#
# Run: python 011_bools/main.py

x = 3
print(True, False, True + True)
print(1 < x < 5)
print("a" or "b")
print("" or "b")
print(0 and "no")

one = 1
print(True + True, False * 10, issubclass(bool, int))
print(True == one, True is not one)
print(bool([]), bool([0]), bool("0"))
