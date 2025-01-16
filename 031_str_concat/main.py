# 031. String concatenation
#
# + concatenates and * repeats. Adjacent literals merge at compile time. In a loop, join
# is faster than += because str is immutable and += copies.
#
# Run: python 031_str_concat/main.py

print("Ada" + " " + "Lovelace")
print("ab" * 3)
print("hello" " " "world")
parts = []
for w in ["a", "b", "c"]:
    parts.append(w)
print("-".join(parts))
