# 169. Chained comparisons
#
# 1 < x < 5 is (1 < x) and (x < 5), with x evaluated once. Mixing in is or == is allowed
# but easy to misread.
#
# Run: python 169_chaining/main.py

x = 3
print(1 < x < 5)
print(1 < x > 2)
print("a" <= "abc" <= "b")
