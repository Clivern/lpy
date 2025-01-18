# 083. dict.clear
#
# clear() empties in place. Aliases see the empty dict. d = {} rebinds the name only.
# views such as d.keys() reflect clear immediately.
#
# Run: python 083_dict_clear/main.py

d = {"a": 1, "b": 2}
keys = d.keys()
alias = d
d.clear()
print(d, alias, list(keys))
