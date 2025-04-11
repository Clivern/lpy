# 392. Beautiful Soup CSS
#
# select() takes a CSS selector. select_one is the first match. attrs= on find is the
# older API. Navigating parents and siblings is the tree API.
#
# Run: python 392_bs4_select/main.py

from bs4 import BeautifulSoup
soup = BeautifulSoup("<div><a href='/x'>one</a><a href='/y'>two</a></div>", "html.parser")
print([a["href"] for a in soup.select("a")])
print(soup.select_one("a").text)
