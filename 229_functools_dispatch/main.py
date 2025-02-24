# 229. singledispatchmethod
#
# singledispatchmethod is the method form. Register implementations per type. The first
# non-self argument is dispatched.
#
# Run: python 229_functools_dispatch/main.py

from functools import singledispatchmethod
class Printer:
    @singledispatchmethod
    def show(self, x):
        return f"obj:{x}"

    @show.register
    def _(self, x: int):
        return f"int:{x}"

p = Printer()
print(p.show(2), p.show("z"))
