import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("spam.csv", encoding="latin-1")
# print(df.head())
df.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], inplace=True)
df = df.rename(columns={"v1": "label", "v2": "sms"})
print(df.head())

print(df.label.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    df["sms"], df["label"], test_size=0.3, random_state=42
)

# print(y_train)
# print(y_test)

count_vector = CountVectorizer(
    stop_words="english", lowercase=True, max_features=100
)

X_traing_data = count_vector.fit_transform(X_train)
X_testing_data = count_vector.fit_transform(X_test)

print(X_traing_data)
X_names = count_vector.get_feature_names_out()

X_training_data_df = pd.DataFrame(X_traing_data.toarray(), columns=X_names)
print(X_training_data_df)
X_training_data_df.to_csv("training_spam_matrix.csv")


from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_traing_data, y_train)
pred = nb.predict(X_testing_data)
print(pred.shape)

from sklearn.metrics import accuracy_score

print(accuracy_score(y_test, pred))

df = pd.DataFrame()
df['Test'] = X_test
df['actual'] = y_test
df['predict'] = pred
print(df)
df.to_csv("test_data_spam.csv")

# pred = nb.predict(X_testing_data)
