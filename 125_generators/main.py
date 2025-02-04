# 125. Generators
#
# yield turns a function into a generator. Each next() runs to the next yield.
# StopIteration ends the loop. State lives between yields.
#
# Run: python 125_generators/main.py

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))
g = countdown(2)
print(next(g), next(g))
