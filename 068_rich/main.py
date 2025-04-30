# 068. rich and tqdm
#
# Console, Table, Progress, markup, Panel, and tqdm.
#
# Run: python 068_rich/main.py

# --- rich print ---
from rich.console import Console
from io import StringIO
buf = StringIO()
console = Console(file=buf, force_terminal=False, width=40)
console.print({"name": "Ada", "n": 1})
print("Ada" in buf.getvalue())
console.print([1, 2, 3])
print('1' in buf.getvalue())

# --- rich table ---
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

# --- rich progress ---
from rich.progress import track
n = 0
for _ in track(range(3), description="work", disable=True):
    n += 1
print(n)

# --- rich markup ---
from rich.markup import escape, render
from rich.text import Text
print(escape("[not a tag]"))
print(Text.from_markup("[bold]Ada[/]").plain)

# --- rich panel ---
from rich.console import Console
from rich.panel import Panel
from io import StringIO
buf = StringIO()
Console(file=buf, force_terminal=False, width=40).print(Panel("hello", title="note"))
print("hello" in buf.getvalue())

# --- tqdm bar ---
from tqdm import tqdm
total = 0
for n in tqdm(range(4), disable=True):
    total += n
print(total)
