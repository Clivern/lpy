# 138. Method resolution order
#
# The MRO is the C3 linearization of the class graph. Class.__mro__ lists it. super()
# follows that tuple, not "the parent" in the source.
#
# Run: python 138_mro/main.py

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print([c.__name__ for c in D.__mro__])
