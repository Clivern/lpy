# 072. dict.setdefault
#
# setdefault(k, default) returns d[k] if present, otherwise inserts default and returns
# it. The default is evaluated even on a hit, so avoid a costly default.
#
# Run: python 072_dict_setdefault/main.py

d = {}
d.setdefault("names", []).append("Ada")
d.setdefault("names", []).append("Alan")
print(d)
print(d.setdefault("year", 1815), d)
