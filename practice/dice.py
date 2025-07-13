import mechanicalsoup
import time

url = "http://olympus.realpython.org/dice"

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get(url) # response object
    tag = page.soup.select("#result")[0]
    tag_time = page.soup.select("#time")[0]

    print(f"The result is {tag.text}, and quote at {tag_time.text}")
    
    if i < 3:
        print("waiting...")
        time.sleep(5)
