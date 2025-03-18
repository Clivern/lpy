# 298. codecs
#
# codecs.encode is the generic encoder. lookup finds a codec. errors='replace' inserts a
# fallback. Most code calls str.encode; codecs matters for custom encodings.
#
# Run: python 298_codecs/main.py

import codecs
print(codecs.encode("café", "utf-8"))
print(codecs.decode(b"\xff", "latin-1"))
print(codecs.lookup("utf-8").name)
