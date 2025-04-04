# 380. rich print
#
# rich.print understands [bold] markup and pretty-prints containers. Console() is the
# object API. Install rich to make tracebacks nicer too.
#
# Run: python 380_rich_print/main.py

from rich.console import Console
from io import StringIO
buf = StringIO()
console = Console(file=buf, force_terminal=False, width=40)
console.print({"name": "Ada", "n": 1})
print("Ada" in buf.getvalue())
