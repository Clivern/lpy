# 097. break and continue
#
# break leaves the nearest loop. continue skips the rest of the body and starts the next
# iteration.
#
# Run: python 097_break_continue/main.py

for n in range(8):
    if n % 2 == 0:
        continue
    if n > 5:
        break
    print(n)
