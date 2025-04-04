# 384. rich Panel
#
# Panel wraps a renderable in a box. Rule is a horizontal line. Group stacks renderables.
# These are building blocks for CLI dashboards.
#
# Run: python 384_rich_panel/main.py

from rich.console import Console
from rich.panel import Panel
from io import StringIO
buf = StringIO()
Console(file=buf, force_terminal=False, width=40).print(Panel("hello", title="note"))
print("hello" in buf.getvalue())
