# 416. tabulate formats
#
# tablefmt can be plain, simple, github, psql, or html. numalign and stralign set
# alignment. showindex adds a row number.
#
# Run: python 416_tabulate_fmt/main.py

from tabulate import tabulate
print(tabulate([[1, 2], [3, 4]], tablefmt="plain", showindex=True))
