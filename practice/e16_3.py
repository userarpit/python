import mechanicalsoup

browser = mechanicalsoup.Browser()
base_url = "http://olympus.realpython.org"
url = "http://olympus.realpython.org/login"

page = browser.get(url)
soup = page.soup
print(soup)

form = soup.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profile_page = browser.submit(form, page.url)
# print(profile_page.url)
profile_page_response = browser.get(profile_page.url)
profile_page_html = profile_page_response.soup
print(profile_page_html.title.text)

links = profile_page.soup.select("a")
for link in links:
    address = base_url + link["href"]
    text = link.text
    # print(f"{text} : {address}")

# print()

login_page = browser.get(url)
title = login_page.soup.title
print(f"Title : {title.text}")

form = soup.select("form")[0]
form.select("input")[0]["value"] = "wrong"
form.select("input")[1]["value"] = "password"

# submit the form
result = browser.submit(form, login_page.url)
result_html = result.soup
# if result_html.text.find("")
if result_html.text.find("Wrong username or password!") != -1:
    print("Login failed")
else:
    print("Login successful")