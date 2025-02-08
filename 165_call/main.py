# 165. __call__
#
# obj() calls __call__. Instances that behave like functions are useful for callbacks that
# need state, without a nested def.
#
# Run: python 165_call/main.py

class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n

add3 = Adder(3)
print(add3(10), callable(add3))
