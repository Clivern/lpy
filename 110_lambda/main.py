# 110. lambda
#
# lambda params: expr is a tiny anonymous function. It is an expression, so it fits where
# def cannot. Keep it to one expression.
#
# Run: python 110_lambda/main.py

add = lambda a, b: a + b
print(add(2, 3))
print(sorted(["aa", "b", "ccc"], key=lambda s: len(s)))
