# 094. match and case
#
# match compares a subject against patterns. case _: is the wildcard. Capture names bind
# on a match. Python 3.10 added this.
#
# Run: python 094_match/main.py

def kind(x):
    match x:
        case 0:
            return "zero"
        case int() as n if n > 0:
            return "pos int"
        case str() as s:
            return f"str {s}"
        case _:
            return "other"

print(kind(0), kind(3), kind("hi"), kind(1.2))
