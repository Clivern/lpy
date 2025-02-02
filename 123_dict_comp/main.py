# 123. Dict comprehensions
#
# {k: v for ...} builds a dict. Later keys overwrite earlier ones. Use it to invert a
# mapping or to pick a subset.
#
# Run: python 123_dict_comp/main.py

words = ["Ada", "Alan", "Alonzo"]
print({w[0]: w for w in words})
print({w: len(w) for w in words if w.startswith("Al")})
