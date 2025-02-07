# 135. property
#
# @property turns a method into an attribute. @x.setter adds write access. Use it to keep
# a computed field looking like data.
#
# Run: python 135_property/main.py

class Temp:
    def __init__(self, c):
        self._c = c

    @property
    def c(self):
        return self._c

    @property
    def f(self):
        return self._c * 9 / 5 + 32

t = Temp(100)
print(t.c, t.f)
