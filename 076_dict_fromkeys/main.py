# 076. dict.fromkeys
#
# fromkeys(keys, value=None) builds a dict with the same value for every key. The value is
# shared: fromkeys(keys, []) gives every key the same list.
#
# Run: python 076_dict_fromkeys/main.py

print(dict.fromkeys(["a", "b", "c"], 0))
shared = dict.fromkeys("ab", [])
shared["a"].append(1)
print(shared)
print({k: [] for k in "ab"})
