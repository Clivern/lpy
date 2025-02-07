# 137. super
#
# super() refers to the next class in the MRO. Call it from __init__ so parents
# initialize. Cooperative multiple inheritance depends on it.
#
# Run: python 137_super/main.py

class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.b = 2

print(B().a, B().b)
