# 085. KeyError and tuple keys
#
# Keys must be hashable: str, int, tuple of hashables. A list is not. KeyError.args holds
# the missing key. A tuple key is a composite id.
#
# Run: python 085_dict_keyerror/main.py

d = {("Ada", 1815): "ok"}
print(d[("Ada", 1815)])
try:
    {[1]: "no"}
except TypeError as e:
    print(type(e).__name__)
try:
    d["missing"]
except KeyError as e:
    print(e.args)
