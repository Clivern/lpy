# 070. Beautiful Soup
#
# Parse HTML, CSS select, and tree navigation.
#
# Run: python 070_bs4/main.py

# --- bs4 parse ---
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html><body><p class='x'>Ada</p></body></html>", "html.parser")
print(soup.find("p").text, soup.find("p")["class"])

# --- bs4 select ---
from bs4 import BeautifulSoup
soup = BeautifulSoup("<div><a href='/x'>one</a><a href='/y'>two</a></div>", "html.parser")
print([a["href"] for a in soup.select("a")])
print(soup.select_one("a").text)

# --- bs4 navigate ---
from bs4 import BeautifulSoup
soup = BeautifulSoup("<ul><li>a</li><li>b</li></ul>", "html.parser")
li = soup.find("li")
print(li.parent.name, list(soup.stripped_strings))
