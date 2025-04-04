# 382. rich Progress
#
# Progress() draws bars. track() wraps an iterable. disable=True keeps tests quiet.
# transient=True clears the bar when done.
#
# Run: python 382_rich_progress/main.py

from rich.progress import track
n = 0
for _ in track(range(3), description="work", disable=True):
    n += 1
print(n)
