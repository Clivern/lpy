# 393. Beautiful Soup navigate
#
# parent, parents, next_sibling, and descendants walk the tree. stripped_strings yields
# text bits. Replace_with edits in place.
#
# Run: python 393_bs4_navigate/main.py

from bs4 import BeautifulSoup
soup = BeautifulSoup("<ul><li>a</li><li>b</li></ul>", "html.parser")
li = soup.find("li")
print(li.parent.name, list(soup.stripped_strings))
