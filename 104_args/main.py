# 104. Positional arguments
#
# Callers fill parameters from left to right. The names in the def are local; the caller's
# names do not have to match.
#
# Run: python 104_args/main.py

def repeat(text, times):
    return text * times

print(repeat("ab", 3))
