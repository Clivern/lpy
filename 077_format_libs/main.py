# 077. tabulate and humanize
#
# Text tables and human-readable numbers and deltas.
#
# Run: python 077_format_libs/main.py

# --- tabulate table ---
from tabulate import tabulate
print(tabulate([["Ada", 1815], ["Alan", 1912]], headers=["name", "year"], tablefmt="github"))

# --- tabulate fmt ---
from tabulate import tabulate
print(tabulate([[1, 2], [3, 4]], tablefmt="plain", showindex=True))

# --- humanize num ---
import humanize
print(humanize.intword(1_200_000))
print(humanize.ordinal(3))
print(humanize.naturalsize(2048))

# --- humanize delta ---
import humanize
from datetime import timedelta
print(humanize.naturaldelta(timedelta(days=2, hours=3)))
print(humanize.precisedelta(timedelta(seconds=90), minimum_unit="seconds"))
