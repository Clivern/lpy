# 118. Recursion
#
# A function may call itself. sys.getrecursionlimit caps the depth. Prefer iteration for
# linear work; recursion fits trees and divide-and-conquer.
#
# Run: python 118_recursion/main.py

def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)

print(fact(5), fact(0))
