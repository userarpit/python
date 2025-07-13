from urllib.request import urlopen
import re

site = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(site)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# print(html)

for tag in ["Name: ", "Favorite Color: "]:
    tag_start = html.find(tag) + len(tag)
    tag_end = html[tag_start:].find("<")

    print(html[tag_start:tag_start + tag_end].strip(" \n"))

for pattern in ["Name: .*?[<\n]", "Favorite Color: .*?[ \n]"]:
    match_results = re.search(pattern, html, re.IGNORECASE)
    value = re.sub(".*: ", "", match_results.group())
    print(value.strip(" \n<"))