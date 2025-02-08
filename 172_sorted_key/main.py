# 172. sorted and key
#
# sorted returns a new list. list.sort sorts in place. key= extracts a comparison key.
# reverse=True flips order. Timsort is stable.
#
# Run: python 172_sorted_key/main.py

words = ["pear", "Fig", "apple"]
print(sorted(words))
print(sorted(words, key=str.lower))
print(sorted(words, key=len, reverse=True))
