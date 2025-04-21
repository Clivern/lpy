# 424. passlib hashing
#
# passlib.hash.pbkdf2_sha256.hash stores a password. verify checks it. Never store raw
# passwords. bcrypt is common; pbkdf2 ships without extra C deps.
#
# Run: python 424_passlib_hash/main.py

from passlib.hash import pbkdf2_sha256
h = pbkdf2_sha256.hash("secret")
print(pbkdf2_sha256.verify("secret", h), pbkdf2_sha256.verify("no", h))
