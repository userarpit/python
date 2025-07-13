from bs4 import BeautifulSoup
from urllib.request import urlopen

site = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(site)
html = page.read().decode("utf-8")
# print(html)

soup = BeautifulSoup(html, "html.parser")
print(soup.get_text().replace("\n", ""))
image1, image2 = soup.find_all("img")
print(soup.title.string)
print(image1.name)
print(image1["src"])
print(image2["src"])