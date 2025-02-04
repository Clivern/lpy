# 129. __init__
#
# __init__ initializes a new instance. self is the instance. It should not return a value.
# Work that belongs in a factory can stay out of init.
#
# Run: python 129_init/main.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Person("Ada", 36)
print(a.name, a.age)
