# 246. array
#
# array.array is a compact typed sequence of numbers. typecode 'i' is signed int, 'd' is
# double. It buffers better than a list when the type is uniform.
#
# Run: python 246_array_mod/main.py

from array import array
a = array("i", [1, 2, 3])
a.append(4)
print(a.tolist(), a.tobytes())
