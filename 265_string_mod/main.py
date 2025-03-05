# 265. string
#
# string.ascii_letters, digits, and punctuation are constants. Template substitutes $name.
# capwords is title-ish. str methods cover most other work.
#
# Run: python 265_string_mod/main.py

import string
print(string.ascii_lowercase[:5], string.digits)
print(string.Template("hi $name").substitute(name="Ada"))
print(string.capwords("ada lovelace"))
