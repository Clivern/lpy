# 114. Closures
#
# A nested function that refers to enclosing names keeps those bindings alive. Each
# factory call gets its own cells.
#
# Run: python 114_closures/main.py

def multiply_by(factor):
    def scale(n):
        return n * factor
    return scale

double = multiply_by(2)
print(double(5), multiply_by(10)(3))
