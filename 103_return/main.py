# 103. return
#
# return exits immediately. Returning several values packs a tuple. An empty return is the
# same as return None.
#
# Run: python 103_return/main.py

def divmod_like(a, b):
    if b == 0:
        return None
    return a // b, a % b

print(divmod_like(7, 3))
print(divmod_like(7, 0))
