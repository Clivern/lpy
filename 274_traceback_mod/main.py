# 274. traceback
#
# traceback.format_exc() is the text of the last exception. print_exception writes a
# stack. For logging, logger.exception is enough.
#
# Run: python 274_traceback_mod/main.py

import traceback
try:
    1 / 0
except ZeroDivisionError:
    text = traceback.format_exc()
print("ZeroDivisionError" in text)
