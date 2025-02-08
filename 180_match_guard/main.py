# 180. match guards
#
# case pattern if expr: only matches when the guard is true. The pattern binds first, then
# the guard runs. Overlapping cases rely on order.
#
# Run: python 180_match_guard/main.py

def grade(n):
    match n:
        case int() if n >= 90:
            return "A"
        case int() if n >= 70:
            return "B"
        case int():
            return "C"
        case _:
            return "?"

print(grade(95), grade(71), grade(10), grade("x"))
