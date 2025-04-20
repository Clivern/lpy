# 417. humanize
#
# intword, naturalsize, and ordinal turn numbers into English. naturaltime talks about
# datetimes. Activate a locale for other languages.
#
# Run: python 417_humanize_num/main.py

import humanize
print(humanize.intword(1_200_000))
print(humanize.ordinal(3))
print(humanize.naturalsize(2048))
