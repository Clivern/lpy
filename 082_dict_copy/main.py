# 082. dict.copy
#
# copy() is shallow: nested mutables are shared. dict(d) is the same. deepcopy copies
# nested dicts. Rebinding d["a"] = ... does not affect the copy; mutating d["a"].append
# does.
#
# Run: python 082_dict_copy/main.py

d = {"xs": [1, 2]}
c = d.copy()
c["xs"].append(3)
c["n"] = 0
print(d, c)
