import mechanicalsoup as ms

browser = ms.Browser()
url = "http://olympus.realpython.org/login"

page = browser.get(url)
print(page)
print(page.soup)