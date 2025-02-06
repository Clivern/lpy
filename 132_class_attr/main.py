# 132. Class attributes
#
# A name on the class is shared by all instances. Assignment on self shadows it for that
# instance. Mutable class attrs are a common trap.
#
# Run: python 132_class_attr/main.py

class Counter:
    created = 0

    def __init__(self):
        Counter.created += 1

Counter()
Counter()
print(Counter.created)
