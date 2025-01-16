# 035. F-strings
#
# f"{expr}" interpolates. Specs after : control width, precision, and type. {x=!r} prints
# the name and a repr. Debug with =.
#
# Run: python 035_fstrings/main.py

name = "Ada"
n = 3
print(f"{name} {n:02d}")
print(f"{n=}")
print(f"{1/3:.3f}")
