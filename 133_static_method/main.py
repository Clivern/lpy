# 133. staticmethod
#
# @staticmethod is a function on the class that does not receive self or cls. Use it for
# namespaced helpers that do not need instance data.
#
# Run: python 133_static_method/main.py

class Temp:
    @staticmethod
    def c_to_f(c):
        return c * 9 / 5 + 32

print(Temp.c_to_f(0), Temp().c_to_f(100))
