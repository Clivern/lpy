# 196. io.StringIO
#
# StringIO is an in-memory text file. Tests use it to capture print. getvalue() returns
# the full text. BytesIO is the binary twin.
#
# Run: python 196_io_stringio/main.py

from io import StringIO
import sys
buf = StringIO()
old = sys.stdout
sys.stdout = buf
print("captured")
sys.stdout = old
print(buf.getvalue().strip())
