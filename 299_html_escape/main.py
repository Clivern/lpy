# 299. html
#
# html.escape turns & < > into entities. unescape reverses named and numeric entities.
# This is not a full HTML parser; use bs4 for documents.
#
# Run: python 299_html_escape/main.py

import html
print(html.escape("<a & b>"))
print(html.unescape("&amp; &lt; &#65;"))
