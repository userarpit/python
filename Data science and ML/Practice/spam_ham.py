import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)
import string
# import matplotlib.pyplot as plt

# load the dataset
try:
    df = pd.read_csv(
        "spam.csv",
        encoding="latin-1",
        header=0,
        names=["label", "message", "v1", "v2", "v3"],
    )
except:
    print("Error loading the dataset. Please check the file path and format.")
    exit()


# print("Original DataFrame")
df.drop(columns=["v1", "v2", "v3"], inplace=True)
# print(df.head())
# print(df.info())

# label count
# print(df["label"].value_counts())


# text preprocessing
def preprocess_text(text):
    # convert to lowercase
    text = text.lower()
    # remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    tokens = word_tokenize(text)
    # print(tokens)
    # remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)


# print(preprocess_text("This is a sample text for preprocessing."))
# apply text preprocessing
df["processed_messages"] = df["message"].apply(preprocess_text)
# print(df.head())

# split data into training and testing sets
X = df["processed_messages"]
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42
)

# print("Training set size:", len(X_train))
# print("Testing set size:", len(X_test))

# print train and test dataset
# print(X_train.tail())
# print(y_train)
# print(X_test)
# print(y_test)

# feature extraction (Vectorization)
# Convert text messages into numerical feature vectors.
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
# print(X_train_vectorized)
X_test_vectorized = vectorizer.transform(X_test)

# print vocabulary size
# print(vectorizer.get_feature_names_out())

# print(X_train_vectorized.toarray())

# train the multinomial Naive Bayes model
model = MultinomialNB()
# print(y_train)
model.fit(X_train_vectorized, y_train)

print("\nNaive Bayes Classifier trained successfully! for ham vs spam classification")

# make predictions on the test set
y_pred = model.predict(X_test_vectorized)

# evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="spam")
recall = recall_score(y_test, y_pred, pos_label="spam")
f1 = f1_score(y_test, y_pred, pos_label="spam")

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
print(f"F1 Score: {f1 * 100:.2f}%")


# test with new messages:
def predict_message(text):
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)
    # print(prediction)
    probability = model.predict_proba(vectorized_text)
    # print(probability)
    return prediction[0], probability[0]


print("\n--- Testing with New Messages ---")
test_message1 = "Congratulations! You've won a free iPhone. Click here to claim."
pred1, prob1 = predict_message(test_message1)
print(f"Message: '{test_message1}'")
print(f"Predicted as: {pred1}")
print(f"Probabilities (ham, spam): {prob1}")

test_message2 = "Hey, let's meet up for coffee tomorrow at 10 AM. Is that okay?"
pred2, prob2 = predict_message(test_message2)
print(f"\nMessage: '{test_message2}'")
print(f"Predicted as: {pred2}")
print(f"Probabilities (ham, spam): {prob2}")

# print(type(model.predict_proba(X_test_vectorized)))
# # print(y_pred)

# pred_df = pd.DataFrame(model.predict_proba(X_test_vectorized), columns=model.classes_, index=X_test.index)
# pred_df['message'] = df["message"]
# print(pred_df)

# print(df.iloc[2826,:])

message3 = "URGENT! Your account has been suspended. Verify at bit.ly/some_link NOW!"

pred3, prob3 = predict_message(message3)
print(f"\nMessage: '{message3}'")
print(f"Predicted as: {pred3}")
print(f"Probabilities (ham, spam): {prob3}")