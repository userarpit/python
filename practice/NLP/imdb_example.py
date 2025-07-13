import pandas as pd
import json
from textblob import TextBlob
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

df = pd.read_csv("imdb.csv")

# convert to lower
df["review"] = df["review"].str.lower()

# remove HTML tags
df["review"] = df["review"].str.replace(r"<.*?>", "", regex=True)

# remove email id
df["review"] = df["review"].str.replace(r"\(?https?://\S+", "", regex=True)

# remove punctuation
exclude = r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]"
df["review"] = df["review"].str.replace(exclude, "", regex=True)

print(df)

# remove chat words
# read slang json file and move to dictionary
try:
    with open("slang.json", "r", encoding="utf-8") as f:
        # json.load() reads from a file-like object and parses JSON data
        slang = json.load(f)
        # print(f"Successfully read JSON from '{filepath}' into a dictionary.")
except Exception as e:
    print(f"An unexpected error occurred while reading slang.json': {e}")


def expand_slang(text):
    words = text.split()
    expand_text = []
    for word in words:
        if word in slang:
            expand_text.append(slang[word])
        else:
            expand_text.append(word)
    return " ".join(expand_text)


df["review"] = df["review"].apply(expand_slang)

# text correction

for index in range(len(df["review"])):
    df.loc[index, "review"] = TextBlob(df.loc[index, "review"]).correct().string

# remove stopwords

stopwords_list = stopwords.words("english")


def remove_stopwords(text):
    words = text.split()
    expand_text = []
    for word in words:
        if word in stopwords_list:
            expand_text.append("")
        else:
            expand_text.append(word)
    return " ".join(expand_text)


# print(df)
df["review"] = df["review"].apply(remove_stopwords)
# print(df)

# print(list(df['review'][0].split()))

# Counter.

# print(word_tokenize(df['review'][0]))
print(word_tokenize("arpit khandelwal. lkasjd laknslk. lajsdf lkajdflk."))

print(list(nltk.trigrams('a b c d')))
print(list(nltk.ngrams('a b c d', 4)))


