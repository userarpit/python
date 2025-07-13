import requests
from bs4 import BeautifulSoup
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt

# scrape the quote
url = "https://quotes.toscrape.com"
page_url = "/"
quotes_data = []

while page_url:
    response = requests.get(url + page_url)

    soup = BeautifulSoup(response.content, "html.parser")
    quotes = soup.find_all("div", class_="quote")
    for quote in quotes:
        # print(quote)
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]
        # print(text)
        # print(author)

        quotes_data.append({"quote": text, "author": author, "tags": ", ".join(tags)})

        next_btn = soup.find("li", class_="next")
        # print(type(next_btn))
        page_url = next_btn.find("a")["href"] if next_btn else None
        # print("*" * 100)


# print(quotes_data)

# load the data in the data frames:
df = pd.DataFrame(quotes_data)

# clean up data
df["author"] = df["author"].str.strip()
df = df.drop_duplicates()

print(df)

# count quote per author
author_counts = df["author"].value_counts().reset_index()
author_counts.columns=['Author', 'Number of Quotes']


print(author_counts)
df.to_csv("all_quotes.csv", index=False)
# plot using matplotlib
plt.figure(figsize=(10, 6))
# plt.bar(df["author"], author_counts)
# author_counts.plot(kind="bar", color="skyblue")
# sns.set(style="whitegrid")
sns.set_style('whitegrid')
sns.barplot(data=author_counts, x="Author", y="Number of Quotes", palette="viridis")
# plt.xlabel("Author")
# plt.ylabel("Number of quote")
plt.title("Number of quote by Author")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
