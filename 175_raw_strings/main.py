# 175. Raw strings
#
# r"\n" is a two-character string, backslash and n. Regex and Windows paths use raw
# strings. A raw string cannot end with an odd number of backslashes.
#
# Run: python 175_raw_strings/main.py

print(r"\n", len(r"\n"))
print(r"C:\temp\x")
import re
print(re.findall(r"\d+", "a12b3"))
