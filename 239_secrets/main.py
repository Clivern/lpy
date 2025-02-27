# 239. secrets
#
# secrets is for passwords, tokens, and urlsafe strings. It uses os.urandom, not the MT
# from random. token_hex and compare_digest are the usual pair.
#
# Run: python 239_secrets/main.py

import secrets
print(len(secrets.token_hex(16)))
print(secrets.compare_digest("ab", "ab"))
print(secrets.randbelow(10) < 10)
