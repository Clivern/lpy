# 092. elif chains
#
# elif is else-if. The first true branch runs and the rest are skipped. Order matters when
# ranges overlap.
#
# Run: python 092_elif/main.py

score = 76
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
