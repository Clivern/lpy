# 240. hashlib
#
# hashlib.md5/sha256/... hash bytes. update can be called in chunks. hexdigest is the
# usual print form. md5 is fast and not for security.
#
# Run: python 240_hashlib/main.py

import hashlib
h = hashlib.sha256(b"hello")
print(h.hexdigest()[:16])
print(hashlib.md5(b"hello").hexdigest())
