# 391. Beautiful Soup parse
#
# BeautifulSoup(html, "html.parser") parses a document. find and find_all query tags.
# get_text() is visible text. html.parser needs no extra C deps.
#
# Run: python 391_bs4_parse/main.py

from bs4 import BeautifulSoup
soup = BeautifulSoup("<html><body><p class='x'>Ada</p></body></html>", "html.parser")
print(soup.find("p").text, soup.find("p")["class"])
