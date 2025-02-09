# 197. io.BytesIO
#
# BytesIO is an in-memory binary file. Image libraries and zip writers accept a file
# object; BytesIO stands in without touching disk.
#
# Run: python 197_io_bytesio/main.py

from io import BytesIO
buf = BytesIO()
buf.write(b"hello")
print(buf.getvalue(), buf.tell())
buf.seek(0)
print(buf.read(2))
