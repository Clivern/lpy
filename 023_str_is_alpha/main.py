# 023. isalpha, isdigit, isalnum
#
# isalpha, isdigit, isalnum, isdecimal, and isnumeric test Unicode categories. isdigit is
# true for ²; isdecimal is the stricter 0-9 family. Empty strings are False.
#
# Run: python 023_str_is_alpha/main.py

print("Ada".isalpha(), "Ada3".isalpha())
print("42".isdigit(), "42".isdecimal(), "²".isdigit(), "²".isdecimal())
print("A3".isalnum(), "".isalpha())
print("Ⅳ".isnumeric(), "Ⅳ".isdigit())
