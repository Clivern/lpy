# 158. Abstract base classes
#
# ABC and @abstractmethod force subclasses to implement a method. Instantiating a class
# that left an abstract method raises TypeError.
#
# Run: python 158_abc/main.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self) -> float:
        return self.side ** 2

print(Square(3).area())
