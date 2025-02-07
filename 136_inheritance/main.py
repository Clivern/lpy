# 136. Inheritance
#
# class Child(Parent) copies the parent's methods. Overriding replaces a name. isinstance
# and issubclass walk the hierarchy.
#
# Run: python 136_inheritance/main.py

class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "woof"

d = Dog()
print(d.speak(), isinstance(d, Animal), issubclass(Dog, Animal))
