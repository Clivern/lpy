# 011. Booleans and short circuit
#
# True and False are bool, a subclass of int. and/or return an operand, not necessarily
# True/False. Comparison chains work: 1 < x < 5.
#
# Run: python 011_bools/main.py

x = 3
print(True, False, True + True)
print(1 < x < 5)
print("a" or "b")
print("" or "b")
print(0 and "no")
