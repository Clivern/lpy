# 048. list.sort key
#
# key= is called once per item. Sort by length, then by the value itself with a tuple key.
# Timsort is stable: equal keys keep their previous order.
#
# Run: python 048_list_sort_key/main.py

words = ["pear", "Fig", "apple", "fig"]
words.sort(key=str.lower)
print(words)
words.sort(key=lambda w: (len(w), w.lower()))
print(words)
