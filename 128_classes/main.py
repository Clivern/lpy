# 128. Classes
#
# class names a type. Instances are created by calling the class. Attributes live on the
# instance dict unless you use slots.
#
# Run: python 128_classes/main.py

class Point:
    pass

p = Point()
p.x = 3
p.y = 4
print(p.x, p.y, type(p).__name__)
print(p.__dict__)
