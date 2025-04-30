# 014. Strings
#
# str is an immutable sequence of Unicode code points. Indexing and slicing copy; there is
# no item assignment. + concatenates, * repeats, join builds from parts. split, partition,
# strip, find, replace, case, startswith, and justify cover most text work.
#
# Run: python 014_strings/main.py

s = "Ada Lovelace"
print(s.upper(), s.lower(), s.title(), s[0], s[-1])
print(s.split(), "Ada" in s, s[::-1])
print("-".join(["a", "b", "c"]))
print("  hi  ".strip().replace("hi", "hello"))

csv = "a,b,c,d"
print(csv.split(","), csv.split(",", maxsplit=1), csv.rsplit(",", maxsplit=1))
print("  a   b\tc  ".split())
print("a/b/c.py".rsplit("/", maxsplit=1))
print("a\nb\r\nc\n".splitlines())
print("user@host".partition("@"), "a:b:c".rpartition(":"))

print("xxhelloxx".strip("x"), "  hi  ".lstrip(), "  hi  ".rstrip())
print("abracadabra".find("bra"), "abracadabra".rfind("bra"), "banana".count("ana"))
print("aa-aa-aa".replace("aa", "b", 1))
print("Ada3".isalpha(), "42".isdigit(), "A3".isalnum(), "name_1".isidentifier())
print("notes.tar.gz".endswith((".gz", ".zip")))
print("hi".center(6, "."), "42".zfill(5), "-42".zfill(5))
print("test_mod.py".removesuffix(".py"), "test_mod.py".removeprefix("test_"))

table = str.maketrans({"a": "4", "e": "3", "o": None})
print("adobe".translate(table))
print("a\tb\tc".expandtabs(4))
print("hello" " " "world")
print("{name} {year}".format_map({"name": "Ada", "year": 1815}))

try:
    s[0] = "p"
except TypeError as e:
    print(type(e).__name__)
