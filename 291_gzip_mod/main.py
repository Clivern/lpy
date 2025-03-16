# 291. gzip
#
# gzip.open compresses a file. compress/decompress work on bytes. ZIP and gzip are
# different formats. Lines can be read from a gzip text file.
#
# Run: python 291_gzip_mod/main.py

import gzip
blob = gzip.compress(b"hello " * 20)
print(len(blob) < 100)
print(gzip.decompress(blob)[:5])
