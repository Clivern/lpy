# 202. pickle
#
# pickle serializes Python objects to bytes. It is not secure: never unpickle untrusted
# data. json is the usual choice for interchange; pickle is for local caches.
#
# Run: python 202_pickle_mod/main.py

import pickle
obj = {"n": 3, "xs": [1, 2]}
blob = pickle.dumps(obj)
print(pickle.loads(blob))
