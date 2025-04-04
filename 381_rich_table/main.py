# 381. rich Table
#
# Table() is a grid for terminals. add_column and add_row fill it. Console.print(table)
# renders. Markup in cells is optional.
#
# Run: python 381_rich_table/main.py

from rich.console import Console
from rich.table import Table
from io import StringIO
buf = StringIO()
t = Table(title="users")
t.add_column("name")
t.add_column("year")
t.add_row("Ada", "1815")
Console(file=buf, force_terminal=False, width=60).print(t)
print("Ada" in buf.getvalue() and "1815" in buf.getvalue())
