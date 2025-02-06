# 131. self
#
# self is a convention, not a keyword. The first parameter of an instance method is the
# instance. Other names work; readers still expect self.
#
# Run: python 131_self/main.py

class Box:
    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

print(Box(9).get())
