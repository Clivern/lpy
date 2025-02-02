# 124. Generator expressions
#
# (expr for x in it) is lazy. sum, any, and all can consume it without building a list. A
# genexp in a function call can drop the extra parens.
#
# Run: python 124_genexp/main.py

it = (n * n for n in range(5))
print(next(it), next(it))
print(sum(n * n for n in range(5)))
