# 057. Tuples
#
# tuple is an immutable sequence. Parentheses are often optional. A one-element tuple
# needs a trailing comma. Tuples unpack on assignment.
#
# Run: python 057_tuples/main.py

point = (3, 4)
x, y = point
print(x, y, point[0])
alone = (1,)
print(alone, type(alone).__name__)
