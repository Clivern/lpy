# 073. dict.pop
#
# pop(k) removes a key and returns its value. pop(k, default) returns default if missing.
# Without a default, a miss is KeyError.
#
# Run: python 073_dict_pop/main.py

d = {"a": 1, "b": 2}
print(d.pop("a"), d)
print(d.pop("z", None))
try:
    d.pop("z")
except KeyError:
    print("missing")
