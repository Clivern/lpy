# 026. center, ljust, rjust, zfill
#
# ljust, rjust, and center pad to a width. fillchar defaults to space. zfill pads with
# zeros on the left and keeps a sign. These return a new string.
#
# Run: python 026_str_justify/main.py

print("hi".ljust(6, "."), "hi".rjust(6, "."), "hi".center(6, "."))
print("42".zfill(5), "-42".zfill(5))
print("title".center(11, "-"))
