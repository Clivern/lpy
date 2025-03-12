# 280. contextlib.suppress
#
# suppress(Exception) ignores those errors in a with block. closing(obj) calls obj.close()
# on the way out. Both keep try/except noise down.
#
# Run: python 280_suppress/main.py

from contextlib import suppress, closing
from io import StringIO
with suppress(FileNotFoundError):
    open("/no/such/file")
print("ok")
with closing(StringIO("x")) as f:
    print(f.read())
