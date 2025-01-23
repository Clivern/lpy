# 102. Functions
#
# def names a function. Parameters are local names. The last return value is what the
# caller receives. A missing return yields None.
#
# Run: python 102_functions/main.py

def add(a, b):
    return a + b

def greet(name):
    print(f"hi {name}")

print(add(2, 3))
greet("Ada")
print(greet("Alan"))
