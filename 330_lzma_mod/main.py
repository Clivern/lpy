# 330. lzma
#
# lzma compresses with XZ. compress/decompress work on bytes. Ratio is usually better than
# gzip and slower. tarfile.open mode='x:xz' uses it.
#
# Run: python 330_lzma_mod/main.py

import lzma
blob = lzma.compress(b"hello " * 50)
print(len(blob) < 80)
print(lzma.decompress(blob)[:5])
