# 027. str.join
#
# sep.join(iterable) glues strings. Every item must already be a str; join does not
# stringify. It is the usual way to build a string in a loop, rather than +=.
#
# Run: python 027_str_join/main.py

print(", ".join(["Ada", "Alan", "Alonzo"]))
print("".join(["a", "b", "c"]))
print("\n".join(["l1", "l2"]))
try:
    ",".join([1, 2])
except TypeError as e:
    print(type(e).__name__)
