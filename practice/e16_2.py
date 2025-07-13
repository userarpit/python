from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

base_URL = "http://olympus.realpython.org"
address = base_URL + "/profiles"

page = urlopen(address)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


for a in soup.find_all("a"):
    link = base_URL + a["href"]

    each_site_page = urlopen(link)
    each_site_page_html = each_site_page.read().decode("utf-8")
    each_site_page_soup = BeautifulSoup(each_site_page_html, "html.parser")
    print(each_site_page_soup.get_text())
