# 241. hmac
#
# HMAC signs bytes with a secret. compare_digest avoids timing leaks. hashlib supplies the
# inner hash. This is the stdlib MAC.
#
# Run: python 241_hmac/main.py

import hmac
import hashlib
sig = hmac.new(b"key", b"msg", hashlib.sha256).hexdigest()
print(len(sig), hmac.compare_digest(sig, sig))
