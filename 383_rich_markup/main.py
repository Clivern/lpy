# 383. rich markup
#
# [bold red]text[/] is markup. escape() protects user text. Theme maps names to styles.
# Markup is optional; you can print with style= instead.
#
# Run: python 383_rich_markup/main.py

from rich.markup import escape, render
from rich.text import Text
print(escape("[not a tag]"))
print(Text.from_markup("[bold]Ada[/]").plain)
