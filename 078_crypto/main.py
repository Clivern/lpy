# 078. cryptography and passlib
#
# Fernet encryption and password hashing.
#
# Run: python 078_crypto/main.py

# --- cryptography fernet ---
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"hello")
print(f.decrypt(token))

# --- passlib hash ---
from passlib.hash import pbkdf2_sha256
h = pbkdf2_sha256.hash("secret")
print(pbkdf2_sha256.verify("secret", h), pbkdf2_sha256.verify("no", h))
