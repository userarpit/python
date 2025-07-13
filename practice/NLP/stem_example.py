from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

pst = PorterStemmer()
lst = LancasterStemmer()


# words_to_stem = ["walk", "walks", "walking", "walked"]
words_to_stem = ["give", "gave", "giving", "given"]

for words in words_to_stem:
    print(words + " : " + pst.stem(words))

# Lemmatization

# from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer

word_lem = WordNetLemmatizer()

print(word_lem.lemmatize("giving", pos='n'))

