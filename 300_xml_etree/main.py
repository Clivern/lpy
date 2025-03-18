# 300. xml.etree
#
# ElementTree parses XML. find and findall take a limited XPath. Untrusted XML can explode
# an entity expander; this parser is not a full defense.
#
# Run: python 300_xml_etree/main.py

import xml.etree.ElementTree as ET
root = ET.fromstring("<doc><item id=\"1\">Ada</item></doc>")
el = root.find("item")
print(el.text, el.get("id"))
