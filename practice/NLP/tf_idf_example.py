from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "The dog barks loudly, and the fox runs away.",
    "A quick brown cat chases a mouse. did",
]


tfidf_vector = TfidfVectorizer(
    stop_words="english", min_df=1, lowercase=True
)
# print(count_vector)

tf_matrix = tfidf_vector.fit_transform(documents)
sklearn_vocabulary = tfidf_vector.get_feature_names_out()
# print(sklearn_vocabulary)
# print(tf_matrix.toarray())

sklearn_bow_df = pd.DataFrame(
    tf_matrix.toarray(),
    columns=sklearn_vocabulary,
    index=[f"Doc {i + 1}" for i in range(len(documents))],
)

print(sklearn_bow_df)
