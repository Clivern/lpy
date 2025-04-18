# 415. tabulate
#
# tabulate(rows, headers=) formats a table as text, markdown, or grid. floatfmt controls
# precision. Good for CLI output without rich.
#
# Run: python 415_tabulate_table/main.py

from tabulate import tabulate
print(tabulate([["Ada", 1815], ["Alan", 1912]], headers=["name", "year"], tablefmt="github"))
