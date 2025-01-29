# 111. LEGB scope
#
# Name lookup is Local, Enclosing, Global, Built-in. Assignment in a function makes a
# local name unless you declare global or nonlocal.
#
# Run: python 111_scope/main.py

x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()
    print(x)

outer()
print(x)
