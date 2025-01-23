# 098. else on loops
#
# for/else and while/else run the else suite when the loop was not ended by break. Useful
# for "search failed" after a scan.
#
# Run: python 098_else_loops/main.py

for n in [2, 4, 6]:
    if n % 2 == 1:
        print("odd")
        break
else:
    print("all even")
