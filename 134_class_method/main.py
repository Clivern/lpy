# 134. classmethod
#
# @classmethod receives the class as cls. Factories that return cls(...) honor subclasses.
# alternative constructors live here.
#
# Run: python 134_class_method/main.py

class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_pair(cls, first, last):
        return cls(f"{first} {last}")

print(Person.from_pair("Ada", "Lovelace").name)
