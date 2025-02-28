# 243. base64
#
# base64 encodes bytes as ASCII. urlsafe_b64encode swaps +/ for -_. There is no encryption
# here: anyone can decode.
#
# Run: python 243_base64/main.py

import base64
print(base64.b64encode(b"hello"))
print(base64.b64decode("aGVsbG8="))
print(base64.urlsafe_b64encode(b"\xff\xfe"))
