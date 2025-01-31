# 117. Nested functions
#
# A function defined inside another is local. It can close over enclosing names and is
# useful for small helpers that do not belong at module level.
#
# Run: python 117_nested/main.py

def sort_by_len(words):
    def key(w):
        return len(w), w
    return sorted(words, key=key)

print(sort_by_len(["pear", "fig", "apple"]))
