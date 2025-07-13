from urllib.request import urlopen
import re

url = "https://www.google.com"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)

start_index = html.find("<title>") + len("<title>")
# print(start_index)

end_index = html.find("</title>")

print(html[start_index:end_index])
print(re.findall("b.*?w ",html))