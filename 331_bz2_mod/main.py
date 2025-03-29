# 331. bz2
#
# bz2 is bzip2 compression. Same compress/decompress API as gzip and lzma. Choose based on
# who consumes the file, not microbenchmarks in a lesson.
#
# Run: python 331_bz2_mod/main.py

import bz2
blob = bz2.compress(b"hello " * 50)
print(len(blob) < 80)
print(bz2.decompress(blob)[:5])
