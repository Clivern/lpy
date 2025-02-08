# 145. with
#
# with expr as name binds the result of __enter__. Several items can be comma-separated.
# The suite always ends with __exit__, even on error.
#
# Run: python 145_with_stmt/main.py

from io import StringIO
buf = StringIO()
with buf as f:
    f.write("hi")
print(buf.getvalue())
