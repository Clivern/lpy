# 423. cryptography Fernet
#
# Fernet is symmetric encryption with HMAC. generate_key() makes a urlsafe key. Token
# includes a timestamp. This is not password hashing.
#
# Run: python 423_cryptography_fernet/main.py

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"hello")
print(f.decrypt(token))
