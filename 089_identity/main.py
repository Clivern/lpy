# 089. Identity vs equality
#
# is asks whether two names refer to the same object. == asks whether the values compare
# equal. Small ints and interned strings may share identity.
#
# Run: python 089_identity/main.py

a = [1, 2]
b = a
c = [1, 2]
print(a is b, a is c, a == c)
print(id(a) == id(b))
