# 312. enum.Flag
#
# Flag is a bitmask enum. | combines, in tests membership. IntFlag mixes with int. auto()
# assigns powers of two.
#
# Run: python 312_enum_flag/main.py

from enum import Flag, auto
class Perm(Flag):
    R = auto()
    W = auto()
    X = auto()
rw = Perm.R | Perm.W
print(Perm.R in rw, bool(rw & Perm.X), rw)
