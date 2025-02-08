# 177. Encodings
#
# encode maps str to bytes; decode goes back. utf-8 is the default for most tools. errors=
# can be strict, replace, or ignore. latin-1 maps 0..255 one-to-one.
#
# Run: python 177_encoding/main.py

s = "café"
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8"))
print(b"\xff".decode("latin-1"))
