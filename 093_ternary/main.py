# 093. Conditional expressions
#
# x if cond else y picks a value. It is an expression, so it fits in an assignment or a
# return. Keep it short or use a full if.
#
# Run: python 093_ternary/main.py

n = 5
label = "pos" if n > 0 else "nonpos"
print(label, "even" if n % 2 == 0 else "odd")
