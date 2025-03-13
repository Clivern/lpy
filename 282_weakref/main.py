# 282. weakref
#
# A weak reference does not keep the object alive. WeakValueDictionary maps to objects
# that can vanish. Caches use this to avoid leaks.
#
# Run: python 282_weakref/main.py

import weakref
class T:
    pass
t = T()
r = weakref.ref(t)
print(r() is t)
del t
print(r() is None)
