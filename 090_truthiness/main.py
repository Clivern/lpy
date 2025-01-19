# 090. Truthiness
#
# bool(x) is False for None, False, 0, 0.0, empty sequences, and empty mappings.
# Everything else is True unless a type defines __bool__ or __len__.
#
# Run: python 090_truthiness/main.py

for v in (None, 0, 0.0, "", [], {}, set(), "x", [0]):
    print(repr(v), bool(v))
