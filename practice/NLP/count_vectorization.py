from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "The dog barks loudly, and the fox runs away.",
    "A quick brown cat chases a mouse.",
]

count_vector = CountVectorizer(stop_words="english", lowercase=True, token_pattern=r"\b[a-zA-Z]+\b")
# print(count_vector)

X = count_vector.fit_transform(documents)
sklearn_vocabulary = count_vector.get_feature_names_out()
print(sklearn_vocabulary)
print(X.toarray())

sklearn_bow_df = pd.DataFrame(
    X.toarray(),
    columns=sklearn_vocabulary,
    index=[f"Doc {i + 1}" for i in range(len(documents))],
)

print(sklearn_bow_df)